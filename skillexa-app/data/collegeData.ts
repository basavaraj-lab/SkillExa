export interface Department {
  code: string;
  name: string;
  years: string[];
  sections: string[];
}

export interface College {
  id: string;
  name: string;
  code: string;
  location: string;
  logoText?: string;
  departments: Department[];
}

export type TargetAudienceType =
  | 'ENTIRE_COLLEGE'
  | 'DEPARTMENT'
  | 'YEAR'
  | 'SECTION'
  | 'SELECTED_STUDENTS';

export interface TargetAudience {
  targetType: TargetAudienceType;
  collegeId: string;
  collegeName?: string;
  department?: string;
  academicYear?: string;
  section?: string;
  studentIds?: string[];
}

export interface FacultyMember {
  id: string;
  name: string;
  email: string;
  collegeId: string;
  collegeName: string;
  department: string;
  designation: string;
  subjectsTaught: string[];
  officeRoom?: string;
  avatarLetter?: string;
  verificationStatus: 'APPROVED' | 'PENDING' | 'REJECTED';
  joinedDate: string;
}

export interface CollegeAnnouncement {
  id: string;
  collegeId: string;
  title: string;
  content: string;
  target: TargetAudience;
  facultyId: string;
  facultyName: string;
  facultyDept: string;
  priority: 'NORMAL' | 'HIGH' | 'URGENT';
  isPinned?: boolean;
  createdAt: string;
}

export interface CollegeNotification {
  id: string;
  studentId: string;
  collegeId: string;
  title: string;
  message: string;
  type: 'NOTE' | 'QUIZ' | 'VIDEO' | 'ASSIGNMENT' | 'INTERVIEW' | 'ANNOUNCEMENT';
  actionRoute: string;
  actionParams?: Record<string, string>;
  isRead: boolean;
  createdAt: string;
}

export const COLLEGES_LIST: College[] = [
  {
    id: 'clg-kvg',
    name: 'KVG College of Engineering',
    code: 'KVGCE',
    location: 'Sullia, Karnataka',
    logoText: 'KVG',
    departments: [
      {
        code: 'ECE',
        name: 'Electronics & Communication Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B', 'C'],
      },
      {
        code: 'CSE',
        name: 'Computer Science & Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B', 'C'],
      },
      {
        code: 'AIML',
        name: 'Artificial Intelligence & Machine Learning',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B'],
      },
      {
        code: 'MECH',
        name: 'Mechanical Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B'],
      },
    ],
  },
  {
    id: 'clg-bms',
    name: 'BMS College of Engineering',
    code: 'BMSCE',
    location: 'Basavanagudi, Bengaluru',
    logoText: 'BMS',
    departments: [
      {
        code: 'ECE',
        name: 'Electronics & Communication Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B', 'C'],
      },
      {
        code: 'CSE',
        name: 'Computer Science & Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B', 'C', 'D'],
      },
      {
        code: 'ISE',
        name: 'Information Science & Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B'],
      },
    ],
  },
  {
    id: 'clg-rvce',
    name: 'RV College of Engineering',
    code: 'RVCE',
    location: 'Mysuru Road, Bengaluru',
    logoText: 'RV',
    departments: [
      {
        code: 'ECE',
        name: 'Electronics & Communication Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B', 'C'],
      },
      {
        code: 'CSE',
        name: 'Computer Science & Engineering',
        years: ['1st Year', '2nd Year', '3rd Year', '4th Year'],
        sections: ['A', 'B', 'C'],
      },
    ],
  },
];

export const FACULTY_DIRECTORY_SEED: FacultyMember[] = [
  {
    id: 'fac-101',
    name: 'Dr. Kusumadhara S',
    email: 'kusumadhara.s@kvgce.edu.in',
    collegeId: 'clg-kvg',
    collegeName: 'KVG College of Engineering',
    department: 'ECE',
    designation: 'Associate Professor & HOD in-charge',
    subjectsTaught: ['Embedded Systems', 'Microcontrollers', 'VLSI Design'],
    officeRoom: 'EC-304, Academic Block 2',
    avatarLetter: 'K',
    verificationStatus: 'APPROVED',
    joinedDate: '2019-08-01',
  },
  {
    id: 'fac-102',
    name: 'Prof. Ananya Sen',
    email: 'ananya.sen@kvgce.edu.in',
    collegeId: 'clg-kvg',
    collegeName: 'KVG College of Engineering',
    department: 'ECE',
    designation: 'Assistant Professor',
    subjectsTaught: ['Digital Electronics', 'Signals & Systems', 'Communication Systems'],
    officeRoom: 'EC-208, Academic Block 2',
    avatarLetter: 'A',
    verificationStatus: 'APPROVED',
    joinedDate: '2021-03-15',
  },
  {
    id: 'fac-103',
    name: 'Dr. Suresh Gowda',
    email: 'suresh.gowda@kvgce.edu.in',
    collegeId: 'clg-kvg',
    collegeName: 'KVG College of Engineering',
    department: 'CSE',
    designation: 'Professor',
    subjectsTaught: ['Data Structures & Algorithms', 'Python Programming', 'Operating Systems'],
    officeRoom: 'CS-402, IT Tower',
    avatarLetter: 'S',
    verificationStatus: 'APPROVED',
    joinedDate: '2017-06-20',
  },
  {
    id: 'fac-201',
    name: 'Dr. Priya Sharma',
    email: 'priya.sharma@bmsce.ac.in',
    collegeId: 'clg-bms',
    collegeName: 'BMS College of Engineering',
    department: 'ECE',
    designation: 'Professor & Head',
    subjectsTaught: ['Analog Circuits', 'Digital Signal Processing'],
    officeRoom: 'ECE Block 4th Floor',
    avatarLetter: 'P',
    verificationStatus: 'APPROVED',
    joinedDate: '2016-01-10',
  },
];
