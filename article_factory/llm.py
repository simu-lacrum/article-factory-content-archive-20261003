from __future__ import annotations

import json
import os
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass
class LlmResult:
    text: str
    provider: str
    model: str | None
    error: str | None = None


def call_llm(provider: str, prompt: str, model: str | None = None) -> LlmResult:
    provider = provider.lower()
    if provider in {"none", "off", "prompt"}:
        return LlmResult(text="", provider="none", model=model)
    if provider == "ollama":
        return call_ollama(prompt, model or os.getenv("OLLAMA_MODEL", "llama3.1:8b"))
    if provider == "openai":
        return call_openai(prompt, model or os.getenv("OPENAI_MODEL", "gpt-4.1-mini"))
    return LlmResult(text="", provider=provider, model=model, error=f"Unknown LLM provider: {provider}")


def post_json(url: str, payload: dict, headers: dict[str, str] | None = None, timeout: int = 180) -> dict:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", **(headers or {})},
        method="POST",
    )
    with urlopen(req, timeout=timeout) as response:
        raw = response.read().decode("utf-8", errors="replace")
    return json.loads(raw)


def call_ollama(prompt: str, model: str) -> LlmResult:
    try:
        payload = {"model": model, "prompt": prompt, "stream": False}
        data = post_json("http://127.0.0.1:11434/api/generate", payload, timeout=300)
        return LlmResult(text=data.get("response", ""), provider="ollama", model=model)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        return LlmResult(text="", provider="ollama", model=model, error=str(exc))


def call_openai(prompt: str, model: str) -> LlmResult:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return LlmResult(text="", provider="openai", model=model, error="OPENAI_API_KEY is not set")
    try:
        payload = {
            "model": model,
            "input": prompt,
            "temperature": 0.7,
        }
        data = post_json(
            "https://api.openai.com/v1/responses",
            payload,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=300,
        )
        text = data.get("output_text")
        if text is None:
            parts: list[str] = []
            for item in data.get("output", []):
                for content in item.get("content", []):
                    if content.get("type") in {"output_text", "text"} and content.get("text"):
                        parts.append(content["text"])
            text = "\n".join(parts)
        return LlmResult(text=text or "", provider="openai", model=model)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        return LlmResult(text="", provider="openai", model=model, error=str(exc))
