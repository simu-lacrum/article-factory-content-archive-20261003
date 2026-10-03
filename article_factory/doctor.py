from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .settings import DEFAULT_DB


def run_quiet(command: list[str], timeout: int = 5) -> tuple[bool, str]:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
        ok = result.returncode == 0
        output = (result.stdout or result.stderr or "").strip()
        return ok, output
    except Exception as exc:
        return False, str(exc)


def doctor(root: Path) -> dict[str, Any]:
    db_path = root / DEFAULT_DB
    python_ok = True
    pypdf_ok = importlib.util.find_spec("pypdf") is not None
    docker_path = shutil.which("docker")
    docker_ok = False
    docker_message = "docker not found"
    if docker_path:
        docker_ok, docker_message = run_quiet(["docker", "version", "--format", "{{.Server.Version}}"])
    ollama_path = shutil.which("ollama")
    ollama_ok = False
    ollama_message = "ollama not found"
    if ollama_path:
        ollama_ok, ollama_message = run_quiet(["ollama", "list"])
    return {
        "root": str(root.resolve()),
        "database_exists": db_path.exists(),
        "database_path": str(db_path.resolve()),
        "python": python_ok,
        "pypdf_installed": pypdf_ok,
        "docker_found": bool(docker_path),
        "docker_daemon_ok": docker_ok,
        "docker_message": docker_message,
        "ollama_found": bool(ollama_path),
        "ollama_ok": ollama_ok,
        "ollama_message": ollama_message,
        "openai_api_key_set": bool(os.getenv("OPENAI_API_KEY")),
        "external_llm_required": False,
        "codex_first_workflow": True,
        "free_fallback_generation_available": False,
        "article_writer": "Codex",
        "no_api_brief_generation_available": True,
    }
