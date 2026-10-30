import { Platform } from 'react-native';

const STORAGE_KEY_DSA = 'skillexa_user_solved_dsa_problems';
const STORAGE_KEY_CODING = 'skillexa_user_solved_coding_topics';

// Fallback in-memory sets for non-web environments
const memoryDsa = new Set<string>();
const memoryCoding = new Set<string>();

export const ProgressStorage = {
  getSolvedDsaProblems(): string[] {
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        const raw = window.localStorage.getItem(STORAGE_KEY_DSA);
        if (raw) {
          const parsed = JSON.parse(raw);
          if (Array.isArray(parsed)) return parsed;
        }
      } catch (e) {
        console.warn('Failed to read solved DSA problems:', e);
      }
    }
    return Array.from(memoryDsa);
  },

  addSolvedDsaProblem(problemId: string): void {
    if (!problemId) return;
    memoryDsa.add(problemId);

    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        const current = ProgressStorage.getSolvedDsaProblems();
        if (!current.includes(problemId)) {
          current.push(problemId);
          window.localStorage.setItem(STORAGE_KEY_DSA, JSON.stringify(current));
        }
      } catch (e) {
        console.warn('Failed to save solved DSA problem:', e);
      }
    }
  },

  getSolvedCodingTopics(): string[] {
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        const raw = window.localStorage.getItem(STORAGE_KEY_CODING);
        if (raw) {
          const parsed = JSON.parse(raw);
          if (Array.isArray(parsed)) return parsed;
        }
      } catch (e) {
        console.warn('Failed to read solved coding topics:', e);
      }
    }
    return Array.from(memoryCoding);
  },

  addSolvedCodingTopic(topicId: string): void {
    if (!topicId) return;
    memoryCoding.add(topicId);

    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        const current = ProgressStorage.getSolvedCodingTopics();
        if (!current.includes(topicId)) {
          current.push(topicId);
          window.localStorage.setItem(STORAGE_KEY_CODING, JSON.stringify(current));
        }
      } catch (e) {
        console.warn('Failed to save solved coding topic:', e);
      }
    }
  },

  resetAllProgress(): void {
    memoryDsa.clear();
    memoryCoding.clear();
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        window.localStorage.removeItem(STORAGE_KEY_DSA);
        window.localStorage.removeItem(STORAGE_KEY_CODING);
      } catch (e) {}
    }
  },
};

