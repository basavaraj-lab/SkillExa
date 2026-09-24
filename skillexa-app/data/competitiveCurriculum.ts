import { TopicCurriculum } from './curriculumSchema';

export const COMPETITIVE_SUBJECTS_LIST = [
  'Quantitative Aptitude',
  'Logical Reasoning',
  'English Language',
  'General Science',
  'General Awareness',
  'Current Affairs',
];

export const ENGLISH_TOPICS_LIST = [
  'Grammar & Parts of Speech',
  'Tenses & Verb Forms',
  'Articles & Determiners',
  'Prepositions & Phrasal Verbs',
  'Subject-Verb Agreement',
  'Active & Passive Voice',
  'Direct & Indirect Speech',
  'Error Detection',
  'Sentence Improvement',
  'Vocabulary & Root Words',
  'Synonyms & Antonyms',
  'Idioms & Phrases',
  'One Word Substitution',
  'Reading Comprehension',
  'Para Jumbles',
  'Cloze Test',
];

export const COMPETITIVE_CURRICULUM: Record<string, TopicCurriculum> = {
  // English -> Tenses
  'English Language - Tenses & Verb Forms': {
    id: 'comp-eng-tenses',
    section: 'competitive',
    category: 'english',
    subject: 'English Language',
    topic: 'Tenses & Verb Forms',
    subtopic: 'Sequence of Tenses & Conditionals',
    badge: 'ENGLISH GRAMMAR',
    overview: 'Master the 12 tense forms, conditional structures, past anteriority, and time markers tested in competitive examinations.',
    theory: 'Tenses locate events in time and denote their completeness. Crucial rules include Past Anteriority (the earlier of two past events requires Past Perfect "had + V3"), Third Conditional ("If + had + V3 ..., would have + V3"), and habitual/universal truths in Simple Present.',
    importantConcepts: [
      'Proximity Rule in Correlatives: In "Neither...nor", "Either...or", verb agrees with the closer subject.',
      'Universal Truths: Scientific facts never change tense even when reporting verb is in the past.',
      'Since vs For: "Since" denotes a specific point in time; "For" denotes a period of duration.',
      'Stativity: Verbs of perception and cognition (know, understand, smell, believe) do not take continuous forms.',
    ],
    rules: [
      'If + Simple Present -> Future Simple (First Conditional)',
      'If + Simple Past -> would + V1 (Second Conditional)',
      'If + Past Perfect (had + V3) -> would have + V3 (Third Conditional)',
    ],
    tipsTricks: [
      'When you spot "By the time + Past Simple", the companion clause MUST use "Past Perfect (had + V3)".',
      '"No sooner...than" and "Hardly/Scarcely...when" invert auxiliary verbs (e.g., "Hardly had I arrived when...").',
    ],
    examples: [
      {
        title: 'Past Anteriority Correction',
        example: 'Incorrect: The thief escaped before the police arrived.\nCorrect:   The thief had escaped before the police arrived.',
        explanation: 'Thief escaping occurred prior to police arrival; earlier action requires Past Perfect.',
      },
    ],
    examPoints: [
      'Spotting Error questions in SSC CGL and IBPS PO frequently conceal subject-verb agreement errors across long intervening phrases.',
    ],
    commonMistakes: [
      'Using present perfect with specific past time indicators (e.g., "I have passed the exam in 2021" is incorrect; use "I passed").',
    ],
    pyqs: [
      {
        id: 'pyq-comp-eng-1',
        exam: 'SSC CGL',
        year: '2024',
        difficulty: 'Medium',
        question: 'Neither the principal nor the lecturers ______ present at the auditorium when the ceremony commenced.',
        options: ['was', 'were', 'is', 'has been'],
        correct: 'were',
        explanation: 'Verb agrees with nearest subject ("lecturers" -> plural "were").',
      },
    ],
    questions: [
      {
        id: 'q-eng-tenses-1',
        section: 'competitive',
        category: 'english',
        subject: 'English Language',
        topic: 'Tenses & Verb Forms',
        subtopic: 'Conditionals',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'If she ______ the warning signals, she would have avoided the dangerous route.',
        options: ['had observed', 'observed', 'has observed', 'would observe'],
        correctAnswer: 0,
        explanation: 'Third conditional requires "had + past participle" in the if-clause.',
        marks: 2,
        negativeMarks: 0.5,
      },
      {
        id: 'q-eng-tenses-2',
        section: 'competitive',
        category: 'english',
        subject: 'English Language',
        topic: 'Tenses & Verb Forms',
        subtopic: 'Subject-Verb Concord',
        difficulty: 'easy',
        questionType: 'mcq',
        question: 'Every student and teacher ______ expected to submit their security clearance by Monday.',
        options: ['is', 'are', 'were', 'have been'],
        correctAnswer: 0,
        explanation: 'Nouns qualified by "Each" or "Every" take singular verbs.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  },

  // English -> Articles
  'English Language - Articles & Determiners': {
    id: 'comp-eng-articles',
    section: 'competitive',
    category: 'english',
    subject: 'English Language',
    topic: 'Articles & Determiners',
    subtopic: 'Definite & Indefinite Rules',
    badge: 'ENGLISH GRAMMAR',
    overview: 'Master the rules of A, An, The, Zero Article, and determiners like Few, A Few, The Few, Little, A Little, The Little.',
    theory: 'Articles define a noun as specific or unspecific. "A/An" are indefinite articles (used with singular countable nouns based on initial vowel SOUND, not spelling). "The" is the definite article used for specific references, unique celestial bodies, rivers, oceans, and superlatives.',
    importantConcepts: [
      'Vowel Sound vs Letter: "A university" (consonant "yu" sound), "An hour" (silent h, vowel sound).',
      'Definite Article "The": Used before superlatives ("the best"), musical instruments ("play the guitar"), rivers ("the Ganges"), and mountain ranges ("the Himalayas").',
      'Zero Article: No article before proper nouns, abstract nouns in general sense, languages, games, and meals.',
      'Few vs Little: "Few" is used with countable nouns; "Little" is used with uncountable nouns.',
    ],
    rules: [
      'Few / Little = Almost none (Negative meaning)',
      'A Few / A Little = Some / at least a small amount (Positive meaning)',
      'The Few / The Little = The specific remaining quantity',
    ],
    tipsTricks: [
      'Words starting with "Eu" or "U" sounding like "You" take "A" (A European, A Union, A Unique opportunity).',
      'Words with silent "H" take "An" (An honest man, An heir, An honorary degree).',
    ],
    examples: [
      {
        title: 'Determiner Nuance in Context',
        example: 'Sentence: A little knowledge is a dangerous thing.\nExplanation: "A little" indicates a small existing amount, whereas "little" would mean virtually no knowledge.',
        explanation: 'Context determines whether negative (little) or positive (a little) determiner is required.',
      },
    ],
    examPoints: [
      'SSC exams frequently test omission of articles before school/college/hospital when visited for primary purpose.',
    ],
    commonMistakes: [
      'Using "an" before "European" or "university" simply because they start with vowels E and U.',
    ],
    pyqs: [
      {
        id: 'pyq-comp-art-1',
        exam: 'SSC CGL',
        year: '2023',
        difficulty: 'Easy',
        question: 'He is ______ honorary secretary of our cooperative housing society.',
        options: ['an', 'a', 'the', 'no article'],
        correct: 'an',
        explanation: '"Honorary" begins with a silent "h" producing an initial vowel sound, requiring "an".',
      },
    ],
    questions: [
      {
        id: 'q-eng-art-1',
        section: 'competitive',
        category: 'english',
        subject: 'English Language',
        topic: 'Articles & Determiners',
        subtopic: 'Indefinite Articles',
        difficulty: 'easy',
        questionType: 'mcq',
        question: 'Copper is ______ useful metal.',
        options: ['a', 'an', 'the', 'no article'],
        correctAnswer: 0,
        explanation: '"Useful" starts with the consonant sound "yu", so indefinite article "a" is required.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  },

  // Quant -> Profit & Loss
  'Quantitative Aptitude - Percentage & Profit/Loss': {
    id: 'comp-quant-profit',
    section: 'competitive',
    category: 'aptitude',
    subject: 'Quantitative Aptitude',
    topic: 'Percentage & Profit/Loss',
    subtopic: 'Markup & Successive Discounts',
    badge: 'ARITHMETIC APTITUDE',
    overview: 'Master fractions, successive changes, profit margins, cost price calculations, markups, and dishonest dealer problems.',
    theory: 'Profit and loss calculations govern transactions involving Cost Price (CP), Selling Price (SP), Marked Price (MP), and Discount. Profit = SP - CP (when SP > CP). Profit% and Loss% are always computed on CP.',
    importantConcepts: [
      'Fraction Equivalents: 1/6 = 16.66%, 1/7 = 14.28%, 1/8 = 12.5%, 1/9 = 11.11%, 1/11 = 9.09%, 1/12 = 8.33%.',
      'Successive Percentage Formula: (a + b + (ab/100))%.',
      'Marked Price Relation: MP / CP = (100 + Profit%) / (100 - Discount%).',
      'Dishonest Dealer Formula: Gain% = (Error / (True Value - Error)) * 100%.',
    ],
    formulas: [
      'Profit % = (Profit / CP) * 100',
      'Loss % = (Loss / CP) * 100',
      'Equivalent Discount = d1 + d2 - (d1 * d2)/100',
      'Overall Loss when 2 items sold at same SP with x% gain and x% loss = (x/10)^2 %',
    ],
    tipsTricks: [
      'If price rises by R%, consumption reduction to keep expenditure constant = [R / (100 + R)] * 100%.',
    ],
    examples: [
      {
        title: 'Equivalent Discount Calculation',
        example: 'Find equivalent discount for 30% and 20% successive discounts.\nNet Discount = 30 + 20 - (30*20)/100 = 50 - 6 = 44%.',
        explanation: 'A single 44% discount equals two successive discounts of 30% and 20%.',
      },
    ],
    examPoints: [
      'Dishonest seller using false weights is asked in almost every shift of SSC CGL.',
    ],
    commonMistakes: [
      'Adding successive discounts linearly (30% + 20% = 50% is wrong; it is 44%).',
    ],
    pyqs: [
      {
        id: 'pyq-comp-quant-1',
        exam: 'SSC CGL',
        year: '2024',
        difficulty: 'Medium',
        question: 'A shopkeeper marks an item 40% above CP and offers 25% discount. His profit percentage is:',
        options: ['5%', '10%', '12%', '15%'],
        correct: '5%',
        explanation: 'CP=100 -> MP=140 -> SP=140*0.75=105 -> Profit = 5%.',
      },
    ],
    questions: [
      {
        id: 'q-quant-pl-1',
        section: 'competitive',
        category: 'aptitude',
        subject: 'Quantitative Aptitude',
        topic: 'Percentage & Profit/Loss',
        subtopic: 'Markup',
        difficulty: 'medium',
        questionType: 'mcq',
        question: 'If the cost price is 80% of the selling price, what is the profit percentage?',
        options: ['25%', '20%', '16.66%', '30%'],
        correctAnswer: 0,
        explanation: 'Let SP = 100, then CP = 80. Profit = 20. Profit% = (20/80) * 100 = 25%.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  },
};

export function getCompetitiveTopic(subject: string, topic: string): TopicCurriculum {
  const key = `${subject} - ${topic}`;
  if (COMPETITIVE_CURRICULUM[key]) return COMPETITIVE_CURRICULUM[key];

  const foundKey = Object.keys(COMPETITIVE_CURRICULUM).find(
    (k) =>
      k.toLowerCase().includes(topic.toLowerCase()) ||
      topic.toLowerCase().includes(k.toLowerCase())
  );
  if (foundKey && COMPETITIVE_CURRICULUM[foundKey]) return COMPETITIVE_CURRICULUM[foundKey];

  return {
    id: `comp-${topic.toLowerCase().replace(/[^a-z0-9]/g, '-')}`,
    section: 'competitive',
    category: 'aptitude',
    subject,
    topic,
    badge: 'COMPETITIVE CURRICULUM',
    overview: `Master comprehensive concepts, formulas, shortcuts, and previous year patterns for ${topic} in ${subject}.`,
    theory: `${topic} is a high-yield section in competitive examinations. Achieving high speed and accuracy requires systematic rule understanding and daily practice.`,
    importantConcepts: [
      `Core definitions, identities, and structural rules of ${topic}.`,
      `Shortcuts and elimination strategies for high speed.`,
      `Handling tricky trap conditions and edge cases.`,
    ],
    tipsTricks: [
      'Eliminate extreme options immediately by verifying parity and dimensional magnitude.',
    ],
    examples: [
      {
        title: `Standard Solved Pattern in ${topic}`,
        example: `Step-by-step resolution illustrating foundational rules.`,
        explanation: `Demonstrates high-accuracy problem decomposition.`,
      },
    ],
    examPoints: [
      `High-weightage topic across SSC, Banking, Railways, and State PSC tests.`,
    ],
    commonMistakes: [
      `Rushing through calculations without verifying problem constraints.`,
    ],
    pyqs: [
      {
        id: `pyq-comp-${topic.toLowerCase().replace(/[^a-z0-9]/g, '-')}`,
        exam: 'SSC / Banking Examination',
        year: '2024',
        difficulty: 'Medium',
        question: `Which strategy yields optimal results when tackling complex ${topic} problems?`,
        options: ['Identify core principles and use option elimination', 'Blind guessing', 'Skip all steps', 'Arbitrary estimation'],
        correct: 'Identify core principles and use option elimination',
        explanation: 'Systematic deduction paired with option elimination maximizes speed and accuracy.',
      },
    ],
    questions: [
      {
        id: `q-comp-${topic.toLowerCase().replace(/[^a-z0-9]/g, '-')}-1`,
        section: 'competitive',
        category: 'aptitude',
        subject,
        topic,
        difficulty: 'medium',
        questionType: 'mcq',
        question: `In competitive exams, what is the primary benefit of mastering shortcuts in ${topic}?`,
        options: [
          'Reduces time per question while maintaining high accuracy',
          'Eliminates need for concept understanding',
          'Guarantees zero negative marking blindly',
          'None of the above',
        ],
        correctAnswer: 0,
        explanation: 'Shortcuts free up vital exam time for multi-step reasoning problems.',
        marks: 2,
        negativeMarks: 0.5,
      },
    ],
  };
}
