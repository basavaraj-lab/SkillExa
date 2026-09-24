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

// Initial Announcements Seed
let announcementsList: CollegeAnnouncement[] = [
  {
    id: 'ann-1',
    collegeId: 'clg-kvg',
    title: '📢 Tomorrow\'s Embedded Systems Quiz at 10:00 AM',
    content: 'All 3rd Year ECE Section A students are required to attempt the Unit 3 ARM Cortex-M Quiz on SkillExa. Duration is 15 minutes with negative marking.',
    target: {
      targetType: 'SECTION',
      collegeId: 'clg-kvg',
      department: 'ECE',
      academicYear: '3rd Year',
      section: 'A',
    },
    facultyId: 'fac-101',
    facultyName: 'Dr. Kusumadhara S',
    facultyDept: 'ECE Department',
    priority: 'HIGH',
    isPinned: true,
    createdAt: 'Today, 09:30 AM',
  },
  {
    id: 'ann-2',
    collegeId: 'clg-kvg',
    title: '📄 VLSI Design Lab Manual & Theory Notes Released',
    content: 'The complete CMOS stick diagrams & layout rules notes have been published in your Faculty Notes section.',
    target: {
      targetType: 'YEAR',
      collegeId: 'clg-kvg',
      department: 'ECE',
      academicYear: '3rd Year',
    },
    facultyId: 'fac-101',
    facultyName: 'Dr. Kusumadhara S',
    facultyDept: 'ECE Department',
    priority: 'NORMAL',
    isPinned: false,
    createdAt: 'Yesterday, 04:15 PM',
  },
  {
    id: 'ann-3',
    collegeId: 'clg-kvg',
    title: '💼 Campus Placement Technical Screening Schedule',
    content: 'All final and pre-final year engineering students must complete their SkillExa AI Mock Interview & DSA milestones by Friday.',
    target: {
      targetType: 'ENTIRE_COLLEGE',
      collegeId: 'clg-kvg',
    },
    facultyId: 'fac-103',
    facultyName: 'Dr. Suresh Gowda',
    facultyDept: 'Placement Cell & CSE',
    priority: 'URGENT',
    isPinned: true,
    createdAt: 'Aug 14, 2026',
  },
];

// Initial In-App Notifications
let notificationsList: CollegeNotification[] = [
  {
    id: 'notif-1',
    studentId: 'std-101',
    collegeId: 'clg-kvg',
    title: '🔔 New Quiz Available',
    message: 'Dr. Kusumadhara S assigned "ARM Cortex-M Architecture Assessment".',
    type: 'QUIZ',
    actionRoute: '/quizzpage',
    actionParams: {
      topic: 'Microcontrollers',
      subject: 'Embedded Systems',
      section: 'engineering',
    },
    isRead: false,
    createdAt: '10 mins ago',
  },
  {
    id: 'notif-2',
    studentId: 'std-101',
    collegeId: 'clg-kvg',
    title: '🔔 New Faculty Notes Published',
    message: 'New verified notes on "ARM Cortex-M Hardware & Memory Mapped I/O".',
    type: 'NOTE',
    actionRoute: '/topic-learning',
    actionParams: {
      topic: 'Microcontrollers',
      subject: 'Embedded Systems',
      section: 'engineering',
    },
    isRead: false,
    createdAt: '1 hour ago',
  },
  {
    id: 'notif-3',
    studentId: 'std-101',
    collegeId: 'clg-kvg',
    title: '📢 Urgent Department Announcement',
    message: 'Embedded Systems Quiz scheduled for tomorrow at 10:00 AM.',
    type: 'ANNOUNCEMENT',
    actionRoute: '/my-college',
    isRead: true,
    createdAt: '3 hours ago',
  },
  {
    id: 'notif-4',
    studentId: 'std-101',
    collegeId: 'clg-kvg',
    title: '🎥 New Lecture Video',
    message: 'Dr. Kusumadhara S uploaded "ARM Cortex-M GPIO & BSRR Register Explained".',
    type: 'VIDEO',
    actionRoute: '/topic-learning',
    actionParams: {
      topic: 'Microcontrollers',
      subject: 'Embedded Systems',
      section: 'engineering',
    },
    isRead: true,
    createdAt: '1 day ago',
  },
];

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
    if (!studentId) return [...notificationsList];
    return notificationsList.filter((n) => n.studentId === studentId || n.studentId === 'all');
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

  dispatchNotification(notif: Omit<CollegeNotification, 'id' | 'createdAt' | 'isRead'>) {
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
