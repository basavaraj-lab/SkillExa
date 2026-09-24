/**
 * SkillExa API Client
 * Connects the React Native frontend to the Python FastAPI Backend.
 * Supports configurable LAN IP for Android/iOS Expo devices on Wi-Fi.
 */

import { useEffect, useState } from 'react';
import { Platform } from 'react-native';

// Priority: 1. Custom runtime configured IP -> 2. EXPO_PUBLIC_API_URL env -> 3. Platform default
let customBaseUrl: string | null = null;

export const setCustomApiBaseUrl = (url: string) => {
  customBaseUrl = url.trim().replace(/\/+$/, '');
};

export const getCustomApiBaseUrl = (): string | null => customBaseUrl;

export const getApiBaseUrl = (): string => {
  if (customBaseUrl) return `${customBaseUrl}/api`;
  if (process.env.EXPO_PUBLIC_API_URL) {
    return `${process.env.EXPO_PUBLIC_API_URL.replace(/\/+$/, '')}/api`;
  }
  return Platform.select({
    android: 'http://10.0.2.2:8000/api', // Android Emulator default
    ios: 'http://localhost:8000/api',     // iOS Simulator default
    default: 'http://localhost:8000/api', // Web browser default
  });
};

let authToken: string | null = null;

export const setAuthToken = (token: string | null) => {
  authToken = token;
};

export const getAuthToken = () => authToken;

async function request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<{ success: boolean; data?: T; message?: string; code?: string; isOffline?: boolean }> {
  const url = `${getApiBaseUrl()}${endpoint}`;
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string>),
  };

  if (authToken) {
    headers['Authorization'] = `Bearer ${authToken}`;
  }

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 6000); // 6s timeout

    const response = await fetch(url, {
      ...options,
      headers,
      signal: controller.signal,
    });
    clearTimeout(timeoutId);

    const data = await response.json();
    return data;
  } catch (error: any) {
    return {
      success: false,
      isOffline: true,
      message: error.name === 'AbortError'
        ? 'Backend request timed out. Check if backend is running on the specified IP & Port.'
        : (error.message || 'Cannot reach FastAPI backend server. Ensure PC and Phone are on the same Wi-Fi.'),
      code: 'NETWORK_ERROR',
    };
  }
}

export const ApiClient = {
  // 0. Health & Real Full-Stack Database Test
  checkHealth: async (): Promise<{ connected: boolean; message: string; raw?: any }> => {
    try {
      const url = `${getApiBaseUrl()}/health`;
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 3500);

      const res = await fetch(url, { signal: controller.signal });
      clearTimeout(timeoutId);

      if (res.ok) {
        const json = await res.json();
        return { connected: true, message: json.message || 'SkillExa backend is running', raw: json };
      }
      return { connected: false, message: `Backend responded with HTTP ${res.status}` };
    } catch (e: any) {
      return {
        connected: false,
        message: e.message === 'Network request failed'
          ? 'Network request failed. Ensure backend is running and phone is on the same Wi-Fi.'
          : (e.message || 'Backend Offline'),
      };
    }
  },

  testFullStack: async (): Promise<{
    success: boolean;
    backendOnline: boolean;
    databaseConnected: boolean;
    details: any;
    error?: string;
  }> => {
    try {
      const url = `${getApiBaseUrl()}/health/fullstack`;
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 4000);

      const res = await fetch(url, { signal: controller.signal });
      clearTimeout(timeoutId);

      if (res.ok) {
        const data = await res.json();
        return {
          success: data.status === 'ok',
          backendOnline: true,
          databaseConnected: data.database?.status === 'connected',
          details: data,
        };
      }
      return {
        success: false,
        backendOnline: false,
        databaseConnected: false,
        details: null,
        error: `HTTP ${res.status}: Backend returned an unexpected response.`,
      };
    } catch (e: any) {
      return {
        success: false,
        backendOnline: false,
        databaseConnected: false,
        details: null,
        error: e.message || 'Could not connect to FastAPI server. Verify your IPv4 address and port 8000.',
      };
    }
  },

  // 1. Authentication
  login: (email: string, password: string) =>
    request<any>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    }),

  registerStudent: (payload: any) =>
    request<any>('/auth/register/student', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  registerFaculty: (payload: any) =>
    request<any>('/auth/register/faculty', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  getCurrentUser: () => request<any>('/auth/me'),

  // 2. Student & College Workspace
  getMyCollegeWorkspace: () => request<any>('/student/my-college'),

  followFaculty: (facultyId: string) =>
    request<any>(`/student/faculty/${facultyId}/follow`, {
      method: 'POST',
    }),

  unfollowFaculty: (facultyId: string) =>
    request<any>(`/student/faculty/${facultyId}/follow`, {
      method: 'DELETE',
    }),

  getFollowing: () => request<any[]>('/student/following'),

  getStudentStats: () => request<any>('/student/stats'),

  // 3. Community Feed
  getCommunityContent: (params: { category?: string; contentType?: string; search?: string; page?: number; limit?: number }) => {
    const query = new URLSearchParams();
    if (params.category) query.append('category', params.category);
    if (params.contentType) query.append('content_type', params.contentType);
    if (params.search) query.append('search', params.search);
    if (params.page) query.append('page', params.page.toString());
    if (params.limit) query.append('limit', params.limit.toString());
    return request<any>(`/community/content?${query.toString()}`);
  },

  // 4. Notes & PDFs
  getNotes: (subject?: string, topic?: string) => {
    const query = new URLSearchParams();
    if (subject) query.append('subject', subject);
    if (topic) query.append('topic', topic);
    return request<any[]>(`/notes?${query.toString()}`);
  },

  createFacultyNote: (payload: any) =>
    request<any>('/faculty/notes', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  // 5. Quizzes & Assessments
  startQuizAttempt: (quizId: string) =>
    request<any>(`/quizzes/${quizId}/start`, {
      method: 'POST',
    }),

  submitQuiz: (payload: { attempt_id: string; time_taken_seconds: number; answers: Record<string, number | null> }) =>
    request<any>('/quizzes/submit', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  getQuizHistory: () => request<any[]>('/quizzes/history'),

  getQuestions: (params: { section?: string; subject?: string; topic?: string; subtopic?: string; language?: string; difficulty?: string }) => {
    const query = new URLSearchParams();
    if (params.section) query.append('section', params.section);
    if (params.subject) query.append('subject', params.subject);
    if (params.topic) query.append('topic', params.topic);
    if (params.subtopic) query.append('subtopic', params.subtopic);
    if (params.language) query.append('language', params.language);
    if (params.difficulty) query.append('difficulty', params.difficulty);
    return request<any[]>(`/questions?${query.toString()}`);
  },

  // 6. Coding Execution Sandbox
  executeCode: (language: string, code: string, customInput?: string) =>
    request<any>('/coding/execute', {
      method: 'POST',
      body: JSON.stringify({ language, code, custom_input: customInput }),
    }),

  submitCode: (problemId: string, language: string, code: string) =>
    request<any>('/coding/submit', {
      method: 'POST',
      body: JSON.stringify({ problem_id: problemId, language, code }),
    }),

  getCodingProblems: (language?: string, topic?: string) => {
    const query = new URLSearchParams();
    if (language) query.append('language', language);
    if (topic) query.append('topic', topic);
    return request<any[]>(`/coding/problems?${query.toString()}`);
  },

  // 7. Interviews & Viva
  getInterviews: () => request<any[]>('/interviews'),

  scheduleInterview: (payload: any) =>
    request<any>('/interviews', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  evaluateInterview: (interviewId: string, payload: any) =>
    request<any>(`/interviews/${interviewId}/evaluate`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  getVideoRoomStatus: (roomId: string) => request<any>(`/interviews/rooms/${roomId}`),

  // 8. Notifications
  getNotifications: () => request<any[]>('/notifications'),

  markNotificationRead: (id: string) =>
    request<any>(`/notifications/${id}/read`, {
      method: 'POST',
    }),

  markAllNotificationsRead: () =>
    request<any>('/notifications/read-all', {
      method: 'POST',
    }),

  // 9. Topics & Learning Curriculum (Backend-verified)
  getTopics: (language: string = 'python') => request<any>(`/topics?language=${language}`),
  getTopicDetails: (topicId: number, language: string = 'python') =>
    request<any>(`/topics/${topicId}/details?language=${language}`),
  completeTopic: (topicId: number, score: number = 100, language: string = 'python') =>
    request<any>(`/topics/${topicId}/complete?score=${score}&language=${language}`, {
      method: 'POST',
    }),

  // 10. DSA Practice & Problem Solving Module
  getDsaProblems: (params?: { search?: string; category?: string; difficulty?: string; language?: string; solved_status?: string }) => {
    const query = new URLSearchParams();
    if (params?.search) query.append('search', params.search);
    if (params?.category) query.append('category', params.category);
    if (params?.difficulty) query.append('difficulty', params.difficulty);
    if (params?.language) query.append('language', params.language);
    if (params?.solved_status) query.append('solved_status', params.solved_status);
    return request<any[]>(`/coding/problems?${query.toString()}`);
  },

  getDsaProblemById: (id: string) => request<any>(`/coding/problems/${id}`),

  executeDsaCode: (language: string, code: string, customInput?: string) =>
    request<any>('/coding/execute', {
      method: 'POST',
      body: JSON.stringify({ language, code, custom_input: customInput }),
    }),

  submitDsaCode: (problemId: string, language: string, code: string) =>
    request<any>('/coding/submit', {
      method: 'POST',
      body: JSON.stringify({ problem_id: problemId, language, code }),
    }),

  getDsaProgress: () => request<any>('/coding/progress'),
};

/**
 * Hook to monitor backend connection status
 */
export function useBackendStatus() {
  const [isConnected, setIsConnected] = useState<boolean | null>(null);
  const [message, setMessage] = useState<string>('Checking backend...');
  const [isChecking, setIsChecking] = useState<boolean>(false);

  const check = async () => {
    setIsChecking(true);
    const res = await ApiClient.checkHealth();
    setIsConnected(res.connected);
    setMessage(res.message);
    setIsChecking(false);
  };

  useEffect(() => {
    check();
  }, []);

  return { isConnected, message, isChecking, refresh: check, apiUrl: getApiBaseUrl() };
}
