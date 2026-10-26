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
  if (Platform.OS === 'web' && typeof window !== 'undefined' && window.location?.hostname) {
    const host = window.location.hostname;
    const protocol = window.location.protocol || 'http:';
    return `${protocol}//${host}:8000/api`;
  }
  return Platform.select({
    android: 'http://10.0.2.2:8000/api', // Android Emulator default
    ios: 'http://localhost:8000/api',     // iOS Simulator default
    default: 'http://localhost:8000/api', // Web browser default
  });
};

let authToken: string | null = null;

// Initialize token from localStorage if in web environment
if (typeof window !== 'undefined' && window.localStorage) {
  try {
    const stored = window.localStorage.getItem('skillexa_jwt_token');
    if (stored && stored !== 'null' && stored !== 'undefined') {
      authToken = stored;
    }
  } catch (e) {}
}

export const setAuthToken = (token: string | null) => {
  authToken = token;
  if (typeof window !== 'undefined' && window.localStorage) {
    try {
      if (token) {
        window.localStorage.setItem('skillexa_jwt_token', token);
      } else {
        window.localStorage.removeItem('skillexa_jwt_token');
      }
    } catch (e) {}
  }
};

export const getAuthToken = () => authToken;

export function parseJwtRole(token: string | null): string | null {
  if (!token) return null;
  try {
    const parts = token.split('.');
    if (parts.length === 3) {
      const base64 = parts[1].replace(/-/g, '+').replace(/_/g, '/');
      const g = globalThis as any;
      let json = '';
      if (typeof g.atob === 'function') {
        json = g.atob(base64);
      } else if (g.Buffer) {
        json = g.Buffer.from(base64, 'base64').toString('utf8');
      }
      if (json) {
        return JSON.parse(json).role?.toLowerCase() || null;
      }
    }
  } catch (e) {}
  return null;
}

export const ensureAuthToken = async (
  forceRefresh = false,
  targetRole?: 'STUDENT' | 'FACULTY'
): Promise<string | null> => {
  if (!forceRefresh && authToken) {
    if (targetRole) {
      const currentRole = parseJwtRole(authToken);
      const isMatch = targetRole === 'FACULTY'
        ? (currentRole === 'faculty' || currentRole === 'admin')
        : (currentRole === 'student');
      if (isMatch) return authToken;
    } else {
      return authToken;
    }
  }

  if (!forceRefresh && typeof window !== 'undefined' && window.localStorage) {
    try {
      const saved = window.localStorage.getItem('skillexa_jwt_token');
      if (saved && saved !== 'null' && saved !== 'undefined') {
        if (targetRole) {
          const savedRole = parseJwtRole(saved);
          const isMatch = targetRole === 'FACULTY'
            ? (savedRole === 'faculty' || savedRole === 'admin')
            : (savedRole === 'student');
          if (isMatch) {
            authToken = saved;
            return saved;
          }
        } else {
          authToken = saved;
          return saved;
        }
      }
    } catch (e) {}
  }

  // Clear invalid or stale token before requesting a fresh one
  setAuthToken(null);

  // Determine active profile from storage
  let activeEmail: string | null = null;
  let activeRole: 'STUDENT' | 'FACULTY' | null = null;

  if (typeof window !== 'undefined' && window.localStorage) {
    try {
      const savedProfile = window.localStorage.getItem('skillexa_user_profile');
      if (savedProfile) {
        const p = JSON.parse(savedProfile);
        activeEmail = p.email || null;
        activeRole = p.role === 'FACULTY' || p.role === 'ADMIN' ? 'FACULTY' : 'STUDENT';
      }
    } catch (e) {}
  }

  // If targetRole is specified and matches the logged-in user, or no targetRole specified
  const shouldAuthenticateActiveUser =
    activeEmail && (!targetRole || targetRole === activeRole);

  if (shouldAuthenticateActiveUser && activeEmail) {
    try {
      const url = `${getApiBaseUrl()}/auth/google-login`;
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: activeEmail, role: activeRole?.toLowerCase() }),
      });
      if (res.ok) {
        const data = await res.json();
        if (data?.data?.access_token) {
          setAuthToken(data.data.access_token);
          return data.data.access_token;
        }
      }
    } catch (e) {
      console.warn('Session sync with user email failed, falling back:', e);
    }
  }

  // Fallback demo credentials if no authenticated session exists
  const effectiveRole = targetRole || activeRole || 'STUDENT';
  const email = effectiveRole === 'FACULTY' ? 'dr.ramesh@kvgce.edu.in' : 'ganesh@kvgce.edu.in';
  const password = effectiveRole === 'FACULTY' ? 'faculty123' : 'student123';

  // Acquire active session from backend
  try {
    const url = `${getApiBaseUrl()}/auth/login`;
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });
    if (res.ok) {
      const data = await res.json();
      if (data?.data?.access_token) {
        setAuthToken(data.data.access_token);
        return data.data.access_token;
      }
    } else {
      console.warn('Auto-authentication responded with status:', res.status);
    }
  } catch (e) {
    console.warn('Auto-authentication failed:', e);
  }
  return null;
};

async function request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<{ success: boolean; data?: T; message?: string; code?: string; isOffline?: boolean }> {
  // Ensure authenticated token for non-auth endpoints
  if (!authToken && !endpoint.includes('/auth/login') && !endpoint.includes('/health')) {
    await ensureAuthToken();
  }

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
    const timeoutId = setTimeout(() => controller.abort(), 30000); // 30s timeout for deep evaluations

    let response = await fetch(url, {
      ...options,
      headers,
      signal: controller.signal,
    });
    clearTimeout(timeoutId);

    // If unauthorized, clear token, attempt one re-login refresh and retry request
    if (response.status === 401 && !endpoint.includes('/auth/login')) {
      const refreshedToken = await ensureAuthToken(true);
      if (refreshedToken) {
        headers['Authorization'] = `Bearer ${refreshedToken}`;
        response = await fetch(url, {
          ...options,
          headers,
        });
      }
    }

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
  ensureAuthToken: (forceRefresh = false, targetRole?: 'STUDENT' | 'FACULTY') =>
    ensureAuthToken(forceRefresh, targetRole),
  ensureFacultyToken: (forceRefresh = false) => ensureAuthToken(forceRefresh, 'FACULTY'),
  ensureStudentToken: (forceRefresh = false) => ensureAuthToken(forceRefresh, 'STUDENT'),

  login: async (email: string, password: string) => {
    const res = await request<any>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    if (res.success && res.data?.access_token) {
      setAuthToken(res.data.access_token);
    }
    return res;
  },

  googleLogin: async (payload: {
    email: string;
    name?: string;
    role?: string;
    avatar?: string;
    google_uid?: string;
  }) => {
    const res = await request<any>('/auth/google-login', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
    if (res.success && res.data?.access_token) {
      setAuthToken(res.data.access_token);
    }
    return res;
  },

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

  // 7. AI Mock Interview Module
  startAIInterview: (payload: {
    interview_category: string;
    job_role: string;
    subject: string;
    programming_language?: string;
    difficulty: string;
    experience_level: string;
    total_questions: number;
    interview_mode: string;
    preferred_language?: string;
    duration_minutes?: number;
  }) =>
    request<any>('/ai-interview/start', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  getAIInterviewState: (interviewId: string) =>
    request<any>(`/ai-interview/${interviewId}`),

  submitAIAnswer: (
    interviewId: string,
    payload: {
      question_id: string;
      answer_text: string;
      answer_mode: string;
      speech_metrics?: any;
    }
  ) =>
    request<any>(`/ai-interview/${interviewId}/answer`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  getNextAIQuestion: (interviewId: string) =>
    request<any>(`/ai-interview/${interviewId}/next-question`, {
      method: 'POST',
    }),

  finishAIInterview: (interviewId: string) =>
    request<any>(`/ai-interview/${interviewId}/finish`, {
      method: 'POST',
    }),

  getAIInterviewReport: (interviewId: string) =>
    request<any>(`/ai-interview/${interviewId}/report`),

  getAIInterviewHistory: (page = 1, limit = 20) =>
    request<any>(`/ai-interview/history?page=${page}&limit=${limit}`),

  synthesizeTTS: (text: string, voice = 'alloy', language = 'en') =>
    request<any>('/ai-interview/tts', {
      method: 'POST',
      body: JSON.stringify({ text, voice, language }),
    }),

  getQuestionBank: (params?: { category?: string; subject?: string; difficulty?: string }) => {
    const query = new URLSearchParams();
    if (params?.category) query.append('category', params.category);
    if (params?.subject) query.append('subject', params.subject);
    if (params?.difficulty) query.append('difficulty', params.difficulty);
    return request<any[]>(`/ai-interview/questions?${query.toString()}`);
  },

  // =========================================================
  // SkillExa Live Interview (Human-to-Human Video Conferencing)
  // =========================================================
  createLiveInterviewBooking: async (payload: {
    student_id: string;
    interview_category: string;
    subject: string;
    scheduled_at: string;
    duration_minutes?: number;
    instructions?: string;
    preparation_materials?: string;
  }) => {
    await ensureAuthToken(false, 'FACULTY');
    return request<any>('/live-interview/bookings', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  getLiveInterviewBookings: (statusFilter?: string) => {
    const q = statusFilter ? `?status=${encodeURIComponent(statusFilter)}` : '';
    return request<any[]>(`/live-interview/bookings${q}`);
  },

  getLiveInterviewBookingDetails: (bookingId: string) =>
    request<any>(`/live-interview/bookings/${bookingId}`),

  confirmLiveInterviewBooking: (bookingId: string) =>
    request<any>(`/live-interview/bookings/${bookingId}/confirm`, {
      method: 'POST',
    }),

  cancelLiveInterviewBooking: (bookingId: string) =>
    request<any>(`/live-interview/bookings/${bookingId}/cancel`, {
      method: 'POST',
    }),

  rescheduleLiveInterviewBooking: (
    bookingId: string,
    payload: { scheduled_at: string; duration_minutes?: number }
  ) =>
    request<any>(`/live-interview/bookings/${bookingId}/reschedule`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  validateLiveInterviewRoom: (roomCode: string) =>
    request<any>(`/live-interview/validate-room/${encodeURIComponent(roomCode.trim())}`),

  prepareLiveInterviewRoom: (bookingId: string) =>
    request<any>(`/live-interview/bookings/${bookingId}/room`, {
      method: 'POST',
    }),

  joinLiveInterviewRoom: (roomId: string) =>
    request<any>(`/live-interview/rooms/${roomId}/join`, {
      method: 'POST',
    }),

  admitStudentToLiveInterview: (roomId: string) =>
    request<any>(`/live-interview/rooms/${roomId}/admit`, {
      method: 'POST',
    }),

  endLiveInterviewRoomForAll: (roomId: string) =>
    request<any>(`/live-interview/rooms/${roomId}/end`, {
      method: 'POST',
    }),

  leaveLiveInterviewRoom: (roomId: string) =>
    request<any>(`/live-interview/rooms/${roomId}/leave`, {
      method: 'POST',
    }),

  getLiveInterviewRoom: (roomId: string) =>
    request<any>(`/live-interview/rooms/${roomId}`),

  getLiveMeetingMessages: (roomId: string) =>
    request<any[]>(`/live-interview/rooms/${roomId}/messages`),

  sendLiveMeetingMessage: (roomId: string, message: string) =>
    request<any>(`/live-interview/rooms/${roomId}/messages`, {
      method: 'POST',
      body: JSON.stringify({ message }),
    }),

  submitLiveInterviewFeedback: (
    bookingId: string,
    payload: {
      technical_score: number;
      communication_feedback: string;
      problem_solving_feedback: string;
      strengths?: string[];
      areas_for_improvement?: string[];
      teacher_comments?: string;
      recommended_topics?: string[];
    }
  ) =>
    request<any>(`/live-interview/bookings/${bookingId}/feedback`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),

  getLiveInterviewFeedback: (bookingId: string) =>
    request<any>(`/live-interview/bookings/${bookingId}/feedback`),

  getDepartmentStudents: async () => {
    await ensureAuthToken(false, 'FACULTY');
    return request<any[]>('/faculty/students');
  },

  // Aptitude Test APIs
  getAptitudeCategories: async () => {
    return request<{
      categories: Record<string, string[]>;
      difficulties: string[];
      test_presets: Record<string, any>;
    }>('/aptitude/categories');
  },

  createAptitudeTestAttempt: async (payload: {
    category: string;
    topic?: string;
    difficulty?: string;
    question_count?: number;
    test_mode?: string;
    duration_minutes?: number;
  }) => {
    await ensureAuthToken(false, 'STUDENT');
    return request<{
      attempt_id: string;
      category: string;
      topic: string;
      difficulty: string;
      test_mode: string;
      question_count: number;
      duration_minutes: number;
      started_at: string;
      status: string;
      saved_responses: Record<string, string>;
      questions: Array<{
        id: string;
        order_index: number;
        question_text: string;
        options: Array<{ id: string; text: string }>;
        category: string;
        topic: string;
        difficulty: string;
        marks: number;
        negative_marks: number;
      }>;
    }>('/aptitude/attempts', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  getAptitudeTestAttempt: async (attemptId: string) => {
    await ensureAuthToken(false, 'STUDENT');
    return request<any>(`/aptitude/attempts/${attemptId}`);
  },

  saveAptitudeResponse: async (
    attemptId: string,
    payload: {
      question_id: string;
      selected_option: string;
      time_spent_seconds?: number;
    }
  ) => {
    await ensureAuthToken(false, 'STUDENT');
    return request<any>(`/aptitude/attempts/${attemptId}/save-response`, {
      method: 'PUT',
      body: JSON.stringify(payload),
    });
  },

  submitAptitudeTest: async (
    attemptId: string,
    payload: {
      responses: Record<string, string>;
      time_spent_seconds: number;
    }
  ) => {
    await ensureAuthToken(false, 'STUDENT');
    return request<any>(`/aptitude/attempts/${attemptId}/submit`, {
      method: 'POST',
      body: JSON.stringify(payload),
    });
  },

  getAptitudeHistory: async () => {
    await ensureAuthToken(false, 'STUDENT');
    return request<any[]>('/aptitude/history');
  },
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
