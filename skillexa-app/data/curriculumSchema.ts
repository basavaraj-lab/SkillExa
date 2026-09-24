export type SectionType = 'engineering' | 'competitive';

export type CategoryType =
  | 'subjects'
  | 'programming'
  | 'dsa'
  | 'placement'
  | 'aptitude'
  | 'reasoning'
  | 'english'
  | 'gk'
  | 'science';

export type LanguageType =
  | 'c'
  | 'cpp'
  | 'java'
  | 'python'
  | 'javascript'
  | 'html-css'
  | 'react-native';

export type DifficultyType = 'easy' | 'medium' | 'hard';

export type QuestionType =
  | 'mcq'
  | 'multiple_correct'
  | 'true_false'
  | 'fill_blank'
  | 'numerical'
  | 'coding';

export interface QuestionMetadata {
  id: string;
  section: SectionType;
  category: CategoryType;
  subject: string;
  topic: string;
  subtopic?: string;
  language?: LanguageType;
  difficulty: DifficultyType;
  questionType: QuestionType;
  question: string;
  options?: string[];
  correctAnswer: number | string | boolean | string[];
  explanation: string;
  marks?: number;
  negativeMarks?: number;
  isFacultyCreated?: boolean;
  facultyName?: string;
}

export interface SolvedExample {
  title: string;
  example: string;
  explanation: string;
}

export interface PYQEntry {
  id: string;
  exam: string;
  year: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  question: string;
  options: string[];
  correct: string;
  explanation: string;
}

export interface TopicCurriculum {
  id: string;
  section: SectionType;
  category: CategoryType;
  subject: string;
  topic: string;
  subtopic?: string;
  language?: LanguageType;
  badge: string;
  overview: string;
  theory: string;
  importantConcepts: string[];
  formulas?: string[];
  rules?: string[];
  tipsTricks: string[];
  examples: SolvedExample[];
  examPoints: string[];
  commonMistakes: string[];
  interviewQuestions?: string[];
  pyqs: PYQEntry[];
  questions: QuestionMetadata[];
}

export type ContentVisibility = 'college' | 'community';

export interface FacultyNote {
  id: string;
  section: SectionType;
  category?: CategoryType;
  subject: string;
  topic: string;
  subtopic?: string;
  language?: LanguageType;
  title: string;
  introduction: string;
  theory: string;
  importantConcepts: string[];
  formulas?: string[];
  rules?: string[];
  examples: SolvedExample[];
  importantPoints: string[];
  commonMistakes: string[];
  quickRevision: string;
  pdfUrl?: string;
  videoUrl?: string;
  facultyName: string;
  facultyDesignation?: string;
  facultyDepartment?: string;
  collegeId?: string;
  collegeName?: string;
  isVerifiedFaculty?: boolean;
  visibility?: ContentVisibility;
  published: boolean;
  createdAt: string;
}

export interface FacultyVideo {
  id: string;
  section: SectionType;
  category?: CategoryType;
  subject: string;
  topic: string;
  subtopic?: string;
  language?: LanguageType;
  title: string;
  videoUrl: string;
  description: string;
  thumbnail?: string;
  duration?: string;
  facultyName: string;
  facultyDesignation?: string;
  facultyDepartment?: string;
  collegeId?: string;
  collegeName?: string;
  isVerifiedFaculty?: boolean;
  visibility?: ContentVisibility;
  published: boolean;
  createdAt: string;
}

export interface FacultyQuiz {
  id: string;
  section: SectionType;
  category?: CategoryType;
  subject: string;
  topic: string;
  subtopic?: string;
  language?: LanguageType;
  quizName: string;
  description: string;
  durationMinutes: number;
  difficulty: DifficultyType;
  totalMarks: number;
  negativeMarks: number;
  passingScore: number;
  questions: QuestionMetadata[];
  published: boolean;
  assignedClasses?: string[];
  startDate?: string;
  endDate?: string;
  facultyName: string;
  facultyDesignation?: string;
  facultyDepartment?: string;
  collegeId?: string;
  collegeName?: string;
  isVerifiedFaculty?: boolean;
  visibility?: ContentVisibility;
  createdAt: string;
}

export type CommunityContentType = 'all' | 'notes' | 'pdf' | 'quiz' | 'video' | 'coding';

export interface CommunityContentItem {
  id: string;
  type: 'note' | 'pdf' | 'quiz' | 'video' | 'coding';
  title: string;
  facultyName: string;
  facultyDesignation?: string;
  collegeName: string;
  collegeId?: string;
  isVerified: boolean;
  section: SectionType;
  category: CategoryType | 'programming' | 'dsa';
  subject: string;
  topic: string;
  subtopic?: string;
  language?: LanguageType;
  publishedDate: string;
  summary?: string;
  duration?: string;
  questionsCount?: number;
  rating?: number;
  viewsCount?: number;
  targetParams: {
    section: SectionType;
    subject: string;
    topic: string;
    subtopic?: string;
    language?: LanguageType;
    quizId?: string;
    noteId?: string;
    videoId?: string;
  };
}

export interface CommunityFilterOptions {
  searchQuery?: string;
  section?: 'all' | 'engineering' | 'competitive';
  category?: 'all' | 'engineering' | 'competitive' | 'programming' | 'dsa';
  contentType?: CommunityContentType;
  subject?: string;
  topic?: string;
  language?: string;
}

export interface StudentQuizSubmission {
  id: string;
  quizId: string;
  quizTitle: string;
  studentId: string;
  studentName: string;
  subject: string;
  topic: string;
  score: number;
  totalMarks: number;
  accuracy: number;
  correctAnswersCount: number;
  wrongAnswersCount: number;
  skippedCount: number;
  timeSpent: string;
  submittedAt: string;
}

export interface FacultyInterview {
  id: string;
  studentId: string;
  studentName: string;
  interviewType:
    | 'HR Interview'
    | 'Technical Interview'
    | 'Coding Interview'
    | 'Engineering Viva'
    | 'Project Viva'
    | 'Placement Interview'
    | 'Custom Interview';
  subjectOrRole: string;
  difficulty: DifficultyType;
  scheduledTime: string;
  status: 'Scheduled' | 'Live' | 'Completed' | 'Pending Evaluation';
  questions: string[];
  studentAnswers?: string[];
  scores?: {
    technical: number;
    communication: number;
    confidence: number;
    problemSolving: number;
    overall: number;
  };
  feedback?: {
    strengths: string[];
    weaknesses: string[];
    suggestions: string[];
    overallSummary: string;
  };
  facultyName: string;
  createdAt: string;
}

export interface StudentTopicPerformance {
  studentId: string;
  studentName: string;
  avatar?: string;
  email: string;
  overallScore: number;
  quizzesCompletedCount?: number;
  quizAccuracy: number;
  notesCompletedCount: number;
  codingSolvedCount: number;
  dsaProgressPct: number;
  interviewsConductedCount?: number;
  interviewsScore: number;
  topicMastery: {
    section: SectionType;
    subject: string;
    topic: string;
    percentage: number;
  }[];
}
