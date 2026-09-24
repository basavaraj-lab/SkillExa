const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "../data/topicCatalogData.ts");
let code = fs.readFileSync(filePath, "utf8");

// Parse file using Function engine
const executableCode = code
  .replace(/export interface[\s\S]*?\n\n/g, "")
  .replace(/export const ([A-Z0-9_]+): TopicItem\[\] =/g, "var $1 =")
  .replace(/export const PYTHON_FUNDAMENTALS_17_TOPICS = PYTHON_ALL_67_TOPICS;/g, "");

const fn = new Function(executableCode + "; return { PYTHON_ALL_67_TOPICS, C_ALL_54_TOPICS, CPP_ALL_73_TOPICS, JAVA_ALL_120_TOPICS, JS_ALL_108_TOPICS };");
const datasets = fn();

const progOptionsMap = {
  "PYTHON": ["print", "input", "len", "def"],
  "C": ["printf", "scanf", "main", "include"],
  "CPP": ["cout", "cin", "endl", "main"],
  "JAVA": ["System.out.println", "Scanner", "public", "class"],
  "JS": ["console.log", "let", "const", "function"]
};

function padQuestionsForTopic(topic, langKey) {
  const langUpper = langKey.upper ? langKey.upper() : langKey.toUpperCase();
  const test = topic.skillExaTest || [];
  const tTitle = topic.title || `Topic ${topic.id}`;
  const tCat = topic.category || "Fundamentals";
  const optsPool = progOptionsMap[langUpper] || progOptionsMap["PYTHON"];

  const padTemplates = [
    {
      question: `What is the primary role of '${tTitle}' in ${langUpper} programming?`,
      options: [
        `A core programming concept in ${tCat} for ${tTitle}`,
        "An unused CSS styling directive",
        "A hardware driver protocol only used in firmware",
        "A database table locking rule"
      ],
      answer: `A core programming concept in ${tCat} for ${tTitle}`
    },
    {
      question: `Which standard keyword or construct is fundamental to '${tTitle}' in ${langUpper}?`,
      options: [
        optsPool[0],
        "Direct raw disk sector formatting",
        "Unbounded buffer overflow execution",
        "Operating system power cycle reset"
      ],
      answer: optsPool[0]
    },
    {
      question: `What is the recommended best practice when working with '${tTitle}' in ${langUpper}?`,
      options: [
        `Write structured, maintainable code following ${langUpper} clean code standards`,
        "Hardcode magic numbers without comments or error checks",
        "Ignore compiler warnings and memory safety guidelines",
        "Bypass function scope and use global state everywhere"
      ],
      answer: `Write structured, maintainable code following ${langUpper} clean code standards`
    },
    {
      question: `What potential error or bug can happen if '${tTitle}' is implemented incorrectly?`,
      options: [
        `Syntax or runtime execution errors in ${langUpper}`,
        "Physical GPU fan speed reduction",
        "Static HTML layout shift",
        "Automatic database deletion"
      ],
      answer: `Syntax or runtime execution errors in ${langUpper}`
    },
    {
      question: `How does mastering '${tTitle}' benefit software development in ${langUpper}?`,
      options: [
        "Improves program modularity, execution safety, and readability",
        "Slows down program compilation by 10x",
        "Prevents the program from running on modern operating systems",
        "Removes the need for variable type definitions"
      ],
      answer: "Improves program modularity, execution safety, and readability"
    }
  ];

  while (test.length < 5) {
    const idx = test.length + 1;
    const tpl = padTemplates[(idx - 1) % padTemplates.length];
    const ansVal = tpl.answer;
    const opts = tpl.options;
    const correctIdx = opts.indexOf(ansVal) !== -1 ? opts.indexOf(ansVal) : 0;
    test.push({
      id: idx,
      question: tpl.question,
      options: opts,
      correct_answer: correctIdx,
      answer: ansVal
    });
  }

  // Ensure options pills exist
  if (!topic.progOptions || topic.progOptions.length === 0) {
    topic.progOptions = optsPool;
  }
  if (!topic.fillOptions || topic.fillOptions.length === 0) {
    topic.fillOptions = optsPool;
  }

  topic.skillExaTest = test;
  return topic;
}

const langMapping = {
  PYTHON_ALL_67_TOPICS: "PYTHON",
  C_ALL_54_TOPICS: "C",
  CPP_ALL_73_TOPICS: "CPP",
  JAVA_ALL_120_TOPICS: "JAVA",
  JS_ALL_108_TOPICS: "JS"
};

Object.keys(datasets).forEach(varName => {
  const langKey = langMapping[varName];
  datasets[varName] = datasets[varName].map(t => padQuestionsForTopic(t, langKey));
});

// Re-serialize back into topicCatalogData.ts format
let newFileContent = `export interface QuizQuestion {
  id: number;
  question: string;
  options: string[];
  correct_answer: number;
  answer: string;
}

export interface TopicItem {
  id: number;
  title: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  duration: string;
  category: string;
  status: 'IN_PROGRESS' | 'COMPLETED' | 'LOCKED';
  completeness: number;
  isUnlocked: boolean;
  concept?: string;
  syntax?: string;
  exampleCode?: string;
  exampleOutput?: string;
  explanation?: string[];
  starterCode?: string;
  progOptions?: string[];
  fillQuestion?: string;
  fillOptions?: string[];
  fillAnswers?: string[];
  skillExaTest?: QuizQuestion[];
}

export const PYTHON_ALL_67_TOPICS: TopicItem[] = ${JSON.stringify(datasets.PYTHON_ALL_67_TOPICS, null, 2)};

export const C_ALL_54_TOPICS: TopicItem[] = ${JSON.stringify(datasets.C_ALL_54_TOPICS, null, 2)};

export const CPP_ALL_73_TOPICS: TopicItem[] = ${JSON.stringify(datasets.CPP_ALL_73_TOPICS, null, 2)};

export const JAVA_ALL_120_TOPICS: TopicItem[] = ${JSON.stringify(datasets.JAVA_ALL_120_TOPICS, null, 2)};

export const JS_ALL_108_TOPICS: TopicItem[] = ${JSON.stringify(datasets.JS_ALL_108_TOPICS, null, 2)};

export const PYTHON_FUNDAMENTALS_17_TOPICS = PYTHON_ALL_67_TOPICS;
`;

fs.writeFileSync(filePath, newFileContent, "utf8");
console.log("Successfully updated topicCatalogData.ts with 5 questions per topic for all 422 topics!");
