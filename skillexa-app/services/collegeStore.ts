import { UserProfile } from '../components/auth-context';
import {
  College,
  CollegeAnnouncement,
  CollegeNotification,
  COLLEGES_LIST,
  FacultyMember,
  FACULTY_DIRECTORY_SEED,
  TargetAudience,
} from '../data/collegeData';

// Initial Announcements Seed (Synchronized with Backend)
let announcementsList: CollegeAnnouncement[] = [
  {
    id: '38690bc1-9633-434b-8174-9eefbdbb835b',
    collegeId: 'clg-kvg',
    title: '📢 aptitude test on 31/10/2026 at 3:30AM',
    content: 'everyone should attend the aptitude without fail',
    target: {
      targetType: 'ENTIRE_COLLEGE',
      collegeId: 'clg-kvg',
      department: 'ECE',
    },
    facultyId: '6b8409c4-36db-4085-9f6d-fd0a8f323ba2',
    facultyName: 'Dr. Ramesh Kumar',
    facultyDept: 'ECE Department',
    priority: 'HIGH',
    isPinned: true,
    createdAt: '2026-10-30',
  },
];

// Notifications List (dynamic, synchronized with backend)
let notificationsList: CollegeNotification[] = [];

let facultyMembersList: FacultyMember[] = [...FACULTY_DIRECTORY_SEED];

type Listener = () => void;
const listeners: Set<Listener> = new Set();
function notify() {
  listeners.forEach((l) => l());
}

export const CollegeStore = {
  // Colleges
  getColleges(): College[] {
    return COLLEGES_LIST;
  },

  getCollegeById(id: string): College | undefined {
    return COLLEGES_LIST.find((c) => c.id === id);
  },

  // Faculty Directory
  getFacultyMembers(collegeId?: string, department?: string): FacultyMember[] {
    return facultyMembersList.filter((f) => {
      if (collegeId && f.collegeId !== collegeId) return false;
      if (department && f.department.toLowerCase() !== department.toLowerCase()) return false;
      return true;
    });
  },

  addFacultyMember(member: Omit<FacultyMember, 'id' | 'joinedDate'>) {
    const newMember: FacultyMember = {
      ...member,
      id: `fac-${Date.now()}`,
      joinedDate: new Date().toISOString().split('T')[0],
    };
    facultyMembersList.unshift(newMember);
    notify();
    return newMember;
  },

  updateFacultyVerification(facultyId: string, status: 'APPROVED' | 'PENDING' | 'REJECTED') {
    facultyMembersList = facultyMembersList.map((f) => (f.id === facultyId ? { ...f, verificationStatus: status } : f));
    notify();
  },

  // Target Matching Algorithm
  isTargetMatchingStudent(target: TargetAudience, student: UserProfile): boolean {
    if (!student || !target) return false;

    // 1. College must match strictly
    if (target.collegeId && target.collegeId !== student.collegeId) {
      return false;
    }

    // 2. Evaluate target audience level
    switch (target.targetType) {
      case 'ENTIRE_COLLEGE':
        return true;

      case 'DEPARTMENT':
        return (
          !target.department ||
          target.department.toLowerCase() === student.department?.toLowerCase()
        );

      case 'YEAR':
        return (
          (!target.department || target.department.toLowerCase() === student.department?.toLowerCase()) &&
          (!target.academicYear || target.academicYear.toLowerCase() === student.academicYear?.toLowerCase())
        );

      case 'SECTION':
        return (
          (!target.department || target.department.toLowerCase() === student.department?.toLowerCase()) &&
          (!target.academicYear || target.academicYear.toLowerCase() === student.academicYear?.toLowerCase()) &&
          (!target.section || target.section.toLowerCase() === student.section?.toLowerCase())
        );

      case 'SELECTED_STUDENTS':
        return (
          !target.studentIds ||
          target.studentIds.length === 0 ||
          (student.id ? target.studentIds.includes(student.id) : true)
        );

      default:
        return true;
    }
  },

  // Announcements
  getAnnouncements(student?: UserProfile): CollegeAnnouncement[] {
    if (!student) return [...announcementsList];
    return announcementsList.filter((ann) => this.isTargetMatchingStudent(ann.target, student));
  },

  addAnnouncement(ann: Omit<CollegeAnnouncement, 'id' | 'createdAt'>): CollegeAnnouncement {
    const newAnn: CollegeAnnouncement = {
      ...ann,
      id: `ann-${Date.now()}`,
      createdAt: 'Just now',
    };
    announcementsList.unshift(newAnn);

    // Auto-dispatch notification to target students
    this.dispatchNotification({
      studentId: 'std-101',
      collegeId: ann.collegeId,
      title: '📢 New College Announcement',
      message: `${ann.facultyName}: "${ann.title}"`,
      type: 'ANNOUNCEMENT',
      actionRoute: '/my-college',
    });

    notify();
    return newAnn;
  },

  deleteAnnouncement(id: string) {
    announcementsList = announcementsList.filter((a) => a.id !== id);
    notify();
  },

  // Notifications
  getNotifications(studentId?: string): CollegeNotification[] {
    const list = !studentId
      ? notificationsList
      : notificationsList.filter((n) => n.studentId === studentId || n.studentId === 'all');
    const seen = new Set<string>();
    const deduped: CollegeNotification[] = [];
    for (const n of list) {
      const key = `${(n.title || '').trim()}::${(n.message || '').trim()}`;
      if (!seen.has(key)) {
        seen.add(key);
        deduped.push(n);
      }
    }
    return deduped;
  },

  getUnreadCount(studentId?: string): number {
    return this.getNotifications(studentId).filter((n) => !n.isRead).length;
  },

  markAsRead(notificationId: string) {
    notificationsList = notificationsList.map((n) => (n.id === notificationId ? { ...n, isRead: true } : n));
    notify();
  },

  markAllAsRead(studentId?: string) {
    notificationsList = notificationsList.map((n) => {
      if (!studentId || n.studentId === studentId || n.studentId === 'all') {
        return { ...n, isRead: true };
      }
      return n;
    });
    notify();
  },

  deleteNotification(notificationId: string) {
    notificationsList = notificationsList.filter((n) => n.id !== notificationId);
    notify();
  },

  dispatchNotification(notif: Omit<CollegeNotification, 'id' | 'createdAt' | 'isRead'>) {
    // Avoid duplicate notifications with identical title and message
    const isDuplicate = notificationsList.some(
      (n) => (n.title || '').trim() === (notif.title || '').trim() && (n.message || '').trim() === (notif.message || '').trim()
    );
    if (isDuplicate) return;

    const newNotif: CollegeNotification = {
      ...notif,
      id: `notif-${Date.now()}-${Math.random().toString(36).substring(2, 5)}`,
      isRead: false,
      createdAt: 'Just now',
    };
    notificationsList.unshift(newNotif);
    notify();
  },

  subscribe(listener: Listener) {
    listeners.add(listener);
    return () => {
      listeners.delete(listener);
    };
  },
};
