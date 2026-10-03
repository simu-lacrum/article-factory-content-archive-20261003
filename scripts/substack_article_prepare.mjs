import { readFile } from "node:fs/promises";

const escapeHtml = (text) =>
  text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

const inlineMarkdown = (text) => {
  let html = escapeHtml(text);
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
  html = html.replace(
    /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
    '<a href="$2">$1</a>',
  );
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, "<em>$1</em>");
  return html;
};

const bodyMarkdownToHtml = (markdown) => {
  const text = markdown
    .replace(/^\uFEFF/, "")
    .replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "")
    .replace(/<!--[\s\S]*?-->/g, "")
    .replace(/^!\[[^\]]*\]\([^\r\n]+\)\s*$/gm, "");

  const output = [];
  let paragraph = [];
  let listType = null;
  let listItems = [];

  const flushParagraph = () => {
    if (paragraph.length) {
      output.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
      paragraph = [];
    }
  };

  const flushList = () => {
    if (listType) {
      const items = listItems
        .map((item) => `<li>${inlineMarkdown(item)}</li>`)
        .join("");
      output.push(`<${listType}>${items}</${listType}>`);
      listType = null;
      listItems = [];
    }
  };

  for (const line of text.split(/\r?\n/)) {
    if (!line.trim()) {
      flushParagraph();
      flushList();
      continue;
    }

    const heading = line.match(/^(#{1,6})\s+(.+)$/);
    if (heading) {
      flushParagraph();
      flushList();
      const level = heading[1].length;
      output.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
      continue;
    }

    const quote = line.match(/^>\s?(.*)$/);
    if (quote) {
      flushParagraph();
      flushList();
      output.push(`<blockquote><p>${inlineMarkdown(quote[1])}</p></blockquote>`);
      continue;
    }

    const unordered = line.match(/^[-*]\s+(.+)$/);
    if (unordered) {
      flushParagraph();
      if (listType && listType !== "ul") flushList();
      listType = "ul";
      listItems.push(unordered[1]);
      continue;
    }

    const ordered = line.match(/^\d+\.\s+(.+)$/);
    if (ordered) {
      flushParagraph();
      if (listType && listType !== "ol") flushList();
      listType = "ol";
      listItems.push(ordered[1]);
      continue;
    }

    flushList();
    paragraph.push(line.trim());
  }

  flushParagraph();
  flushList();
  return output.join("");
};

const parseArticle = (markdown) => {
  const match = markdown.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
  const frontMatter = match ? match[1] : "";
  const readField = (name) => {
    const field = frontMatter.match(
      new RegExp(`^${name}:\\s*[\\\"']?(.+?)[\\\"']?\\s*$`, "m"),
    );
    return field ? field[1].replace(/[\"']$/, "") : "";
  };

  let body = markdown
    .replace(/^\uFEFF/, "")
    .replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "")
    .replace(/<!--[\s\S]*?-->/g, "")
    .replace(/^!\[[^\]]*\]\([^\r\n]+\)\s*$/gm, "");
  const h1Match = body.match(/^#\s+(.+)$/m);
  const h1 = h1Match ? h1Match[1].trim() : readField("title");
  if (h1Match) body = body.replace(/^#\s+.+\r?\n?/m, "");

  return {
    h1,
    seoTitle: readField("seo_title") || readField("title"),
    description: readField("description"),
    html: bodyMarkdownToHtml(`---\nx: y\n---\n${body}`),
  };
};

export const loadPreparedArticles = async (manifestPath) => {
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  return Promise.all(
    manifest.articles.map(async (article) => ({
      ...article,
      ...parseArticle(await readFile(article.file, "utf8")),
    })),
  );
};

export const withImage = (html, imageUrl, altText) =>
  html.replace(
    "<h2>",
    `<figure><img src="${imageUrl}" alt="${altText}" /></figure><h2>`,
  );

export const htmlToPlainText = (html) =>
  html
    .replace(/<li>/g, "• ")
    .replace(/<\/li>/g, "\n")
    .replace(/<\/p>|<\/h[1-6]>|<\/blockquote>|<\/figure>/g, "\n\n")
    .replace(/<[^>]+>/g, "")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">");
