const fs = require("fs");
const path = require("path");

const articlePath =
  "C:/Users/User/Desktop/articles/output/articles/20260723-174302/01-kak-ustanovit-chity-dlya-cs2.md";
const sourcePath =
  "C:/Users/User/Desktop/articles/knowledge/agent_memory/sources/mrkhertz-medium/how-to-install-cs2-cheats-hacks-for-free-9e187ffde710.md";

const raw = fs.readFileSync(articlePath, "utf8");
const sourceRaw = fs.readFileSync(sourcePath, "utf8");

function stripDoc(text) {
  return text
    .replace(/^---[\s\S]*?\n---\s*\n/, "")
    .replace(/<!--[\s\S]*?-->/g, " ")
    .replace(/!\[[^\]]*\]\([^)]*\)/g, " ")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/https?:\/\/\S+/g, " ");
}

function words(text) {
  return (
    stripDoc(text)
      .toLowerCase()
      .match(/[\p{L}\p{N}]+(?:[-'][\p{L}\p{N}]+)*/gu) || []
  );
}

function grams(tokens, size) {
  const result = new Set();
  for (let index = 0; index <= tokens.length - size; index += 1) {
    result.add(tokens.slice(index, index + size).join(" "));
  }
  return result;
}

function shared(left, right, size) {
  const leftGrams = grams(left, size);
  const rightGrams = grams(right, size);
  return [...leftGrams].filter((value) => rightGrams.has(value));
}

function walk(directory, output = []) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const filePath = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      walk(filePath, output);
    } else if (
      entry.isFile() &&
      filePath.endsWith(".md") &&
      path.resolve(filePath) !== path.resolve(articlePath)
    ) {
      output.push(filePath);
    }
  }
  return output;
}

const articleWords = words(raw);
const sourceWords = words(
  sourceRaw.split("Markdown Content:").slice(1).join("Markdown Content:"),
);

const frontMatter = raw.match(/^---\s*\n([\s\S]*?)\n---\s*\n/);
const metadata = {};
for (const line of (frontMatter ? frontMatter[1] : "").split(/\r?\n/)) {
  const match = line.match(/^([^:]+):\s*"?(.*?)"?\s*$/);
  if (match) {
    metadata[match[1].trim()] = match[2].replace(/^"|"$/g, "");
  }
}

const body = stripDoc(raw).toLowerCase();
const exactKeyword = "как установить читы для cs2";
const exactUses = body.split(exactKeyword).length - 1;

const stopWords = new Set(
  "и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли если уже или ни быть был него до вас нибудь опять уж вам ведь там потом себя ничего ей может они тут где есть надо ней для мы тебя их чем была сам чтоб без будто чего раз тоже себе под будет ж тогда кто этот того потому этого какой совсем ним здесь этом один почти мой тем чтобы нее сейчас были куда зачем сказать всех никогда сегодня можно при наконец два об другой хоть после над больше тот через эти нас про всего них какая много разве три эту моя впрочем хорошо свою этой перед иногда лучше чуть том нельзя такой им более всегда конечно всю между".split(
    " ",
  ),
);

const wordCounts = {};
for (const word of articleWords) {
  if (!stopWords.has(word) && word.length > 2) {
    wordCounts[word] = (wordCounts[word] || 0) + 1;
  }
}

const topWords = Object.entries(wordCounts)
  .sort((left, right) => right[1] - left[1])
  .slice(0, 15)
  .map(([word, count]) => ({
    word,
    count,
    pct: Number(((100 * count) / articleWords.length).toFixed(2)),
  }));

const corpus = [
  ...walk(
    "C:/Users/User/Desktop/articles/knowledge/agent_memory/sources",
  ),
  ...walk("C:/Users/User/Desktop/articles/output/articles"),
];

const articleFiveGrams = grams(articleWords, 5);
const localMatches = [];
for (const filePath of corpus) {
  const localGrams = grams(words(fs.readFileSync(filePath, "utf8")), 5);
  const hits = [...articleFiveGrams].filter((value) =>
    localGrams.has(value),
  );
  if (hits.length) {
    localMatches.push({
      file: filePath.replace(/\\/g, "/"),
      count: hits.length,
      samples: hits.slice(0, 5),
    });
  }
}

const sourceOverlap = {};
for (const size of [4, 5, 6, 8, 10]) {
  const hits = shared(articleWords, sourceWords, size);
  sourceOverlap[size] = {
    count: hits.length,
    samples: hits.slice(0, 10),
  };
}

const faqBody = raw.split(/^## Частые вопросы\s*$/m)[1] || "";

console.log(
  JSON.stringify(
    {
      words_excluding_frontmatter_and_image_notes: articleWords.length,
      title_chars: (metadata.title || "").length,
      description_chars: (metadata.description || "").length,
      primary_keyword_exact_uses: exactUses,
      primary_keyword_word_density_pct: Number(
        ((100 * 4 * exactUses) / articleWords.length).toFixed(2),
      ),
      cluster_links: (
        raw.match(/https:\/\/cluster\.center\/en\/cs2/g) || []
      ).length,
      image_slots: (raw.match(/<!-- IMAGE_SLOT_/g) || []).length,
      h2_count: (raw.match(/^##\s+/gm) || []).length,
      faq_questions: (faqBody.match(/^###\s+/gm) || []).length,
      source_overlap: sourceOverlap,
      local_5gram_files_with_matches: localMatches,
      top_content_words: topWords,
    },
    null,
    2,
  ),
);
