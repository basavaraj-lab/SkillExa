import { Feather, Ionicons } from '@expo/vector-icons';
import React, { useEffect, useMemo, useState } from 'react';
import {
  Alert,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  useWindowDimensions,
  View,
} from 'react-native';
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';

// ==========================================
// CONSTANTS & ATS DICTIONARIES
// ==========================================

const WIZARD_STEPS = [
  { id: 1, label: 'Personal', icon: 'user' },
  { id: 2, label: 'Education', icon: 'book' },
  { id: 3, label: 'Skills', icon: 'code' },
  { id: 4, label: 'Projects', icon: 'folder' },
  { id: 5, label: 'Experience', icon: 'briefcase' },
  { id: 6, label: 'Certs & Honors', icon: 'award' },
];

const TARGET_ROLES = [
  'Full Stack Developer',
  'Software Engineer (SDE)',
  'Frontend Developer',
  'Backend Developer',
  'Data Science & AI',
  'Cloud & DevOps',
  'Mobile App Developer',
  'Cybersecurity & Systems',
] as const;

type TargetRoleType = (typeof TARGET_ROLES)[number];

const ROLE_KEYWORDS: Record<TargetRoleType, string[]> = {
  'Full Stack Developer': [
    'react',
    'node.js',
    'typescript',
    'javascript',
    'sql',
    'rest api',
    'docker',
    'git',
    'mongodb',
    'html5',
    'css',
    'express',
    'postgresql',
    'full-stack',
    'microservices',
    'redux',
  ],
  'Software Engineer (SDE)': [
    'python',
    'java',
    'c++',
    'data structures',
    'algorithms',
    'git',
    'linux',
    'sql',
    'oop',
    'system design',
    'problem solving',
    'unit testing',
    'concurrency',
    'multithreading',
  ],
  'Frontend Developer': [
    'react',
    'javascript',
    'typescript',
    'css',
    'html5',
    'responsive design',
    'ui/ux',
    'redux',
    'tailwind',
    'expo',
    'next.js',
    'web performance',
    'dom',
    'rest api',
  ],
  'Backend Developer': [
    'python',
    'java',
    'node.js',
    'sql',
    'postgresql',
    'rest api',
    'microservices',
    'docker',
    'redis',
    'aws',
    'database design',
    'express',
    'fastapi',
    'orm',
    'scalability',
  ],
  'Data Science & AI': [
    'python',
    'machine learning',
    'tensorflow',
    'pytorch',
    'pandas',
    'numpy',
    'sql',
    'data analysis',
    'deep learning',
    'statistics',
    'scikit-learn',
    'nlp',
    'data visualization',
    'jupyter',
  ],
  'Cloud & DevOps': [
    'aws',
    'docker',
    'kubernetes',
    'linux',
    'ci/cd',
    'terraform',
    'git',
    'bash',
    'monitoring',
    'cloud architecture',
    'ansible',
    'jenkins',
    'security',
    'networking',
  ],
  'Mobile App Developer': [
    'react native',
    'android',
    'ios',
    'flutter',
    'typescript',
    'javascript',
    'expo',
    'mobile ui',
    'redux',
    'rest api',
    'gradle',
    'xcode',
    'app store',
  ],
  'Cybersecurity & Systems': [
    'linux',
    'network security',
    'cryptography',
    'penetration testing',
    'firewall',
    'owasp',
    'vulnerability',
    'wireshark',
    'bash',
    'python',
    'siem',
    'incident response',
  ],
};

const ACTION_VERBS = [
  'engineered',
  'architected',
  'developed',
  'built',
  'optimized',
  'implemented',
  'designed',
  'created',
  'deployed',
  'managed',
  'led',
  'spearheaded',
  'automated',
  'collaborated',
  'resolved',
  'integrated',
  'streamlined',
  'scaled',
  'delivered',
  'accelerated',
  'refactored',
  'orchestrated',
  'formulated',
  'mentored',
  'standardized',
  'reduced',
  'increased',
  'maintained',
];

const SAMPLE_TECH_RESUME = `Ganesh Sharan
Software Engineer & Full Stack Developer
ganesh@skillexa.edu | +91 98765 43210 | Karnataka, India
github.com/ganesh-code | linkedin.com/in/ganesh-tech

PROFESSIONAL SUMMARY
Results-driven Computer Science Engineer with expertise in building scalable web applications and distributed architectures. Proven track record in optimizing backend microservices and modern frontend interfaces.

EDUCATION
B.Tech in Computer Science and Engineering
KVG College of Engineering, Sullia (2022 - 2026)
CGPA: 8.85 / 10

TECHNICAL SKILLS
Languages: Java, Python, TypeScript, JavaScript, SQL, C++
Frameworks: React, React Native, Node.js, Express, Next.js, FastAPI
Databases: PostgreSQL, MongoDB, Redis, MySQL
Cloud & Tools: Docker, AWS, Git, CI/CD, Postman, Linux, REST API
Core: Data Structures, Algorithms, System Design, OOP, DBMS

KEY PROJECTS
SkillExa - Career & Placement Learning Platform
• Engineered an interactive learning platform with online coding compilers, achieving 28% faster problem load times and zero-downtime test suite executions.
• Implemented role-based authentication and secure session tokens handling 1,500+ active student users.

Distributed Task Queue & Worker Service
• Architected a fault-tolerant asynchronous job runner in Python and Redis handling 2,000+ requests/sec with automated heartbeat recovery.
• Reduced background task latency by 45ms and improved server throughput by 30%.

EXPERIENCE
Software Engineering Intern - NextGen Solutions Lab (June 2025 - August 2025)
• Developed automated REST API test harnesses that increased unit test coverage by 35%.
• Optimized SQL query execution plans across 50,000+ database records, saving 18% query runtime.

CERTIFICATIONS
• AWS Certified Cloud Practitioner
• Meta Front-End Developer Professional Certificate`;

const SAMPLE_FRESHER_RESUME = `Priya Sharma
Computer Science Graduate | Aspiring Software Developer
priya.sharma@example.com | +91 98123 45678 | Bangalore, India
github.com/priya-dev | linkedin.com/in/priya-sharma

PROFESSIONAL SUMMARY
Enthusiastic Computer Science undergraduate eager to apply strong foundation in data structures, algorithms, and Java/Python development to solve real-world problems.

EDUCATION
B.E. in Information Science and Engineering
VTU University (2021 - 2025) | CGPA: 8.2 / 10

TECHNICAL SKILLS
Programming: Python, Java, C++, SQL
Web Technologies: HTML, CSS, JavaScript, React basics
Developer Tools: Git, GitHub, VS Code, Linux
Key Courses: Data Structures, Algorithms, Operating Systems, Database Management Systems

ACADEMIC PROJECTS
Smart Campus Event Portal
• Developed full-stack event registration portal using React and Python backend.
• Handled registrations for 800+ attendees across 12 college symposiums.

Algorithm Visualizer
• Built interactive visualizer for sorting and graph pathfinding algorithms with real-time step explanations.
• Received Best Academic Project award among 60 student teams.

ACHIEVEMENTS & CERTIFICATIONS
• 1st Place - Inter-College Hackathon 2024
• HackerRank 5-Star Problem Solving Badge`;

// ==========================================
// MAIN COMPONENT
// ==========================================

export default function ResumeBuilderPage() {
  const { profile } = useAuth();
  const { width } = useWindowDimensions();
  const isDesktop = width >= 768;

  // Mode: 'wizard' (Form Editor) | 'preview' (A4 Document Canvas) | 'ats' (ATS Verification Studio)
  const [activeMode, setActiveMode] = useState<'wizard' | 'preview' | 'ats'>('wizard');
  const [currentStep, setCurrentStep] = useState(1);
  const [template, setTemplate] = useState<'modern' | 'classic' | 'minimal'>('modern');

  // ATS State
  const [atsSource, setAtsSource] = useState<'created' | 'upload' | 'paste'>('created');
  const [targetRole, setTargetRole] = useState<TargetRoleType>('Full Stack Developer');
  const [uploadedFileName, setUploadedFileName] = useState<string>('');
  const [uploadedFileSize, setUploadedFileSize] = useState<string>('');
  const [uploadedText, setUploadedText] = useState<string>('');
  const [pastedText, setPastedText] = useState<string>('');
  const [jobDescription, setJobDescription] = useState<string>('');
  const [showJdMatcher, setShowJdMatcher] = useState<boolean>(false);

  // Resume Builder Data State
  const [personal, setPersonal] = useState({
    fullName: profile?.name || 'Ganesh Sharan',
    title: 'Computer Science Engineer | Full Stack Developer',
    email: profile?.email || 'ganesh@skillexa.edu',
    phone: profile?.phone || '+91 98765 43210',
    location: 'Karnataka, India',
    github: 'github.com/ganesh-code',
    linkedin: 'linkedin.com/in/ganesh-tech',
    portfolio: 'ganeshsharan.dev',
    summary:
      'High-performing Computer Science Engineer with strong hands-on expertise in full-stack architecture, scalable microservices, and database optimization. Dedicated to developing maintainable code and solving complex algorithmic problems.',
  });

  const [educationList, setEducationList] = useState([
    {
      id: 'edu-1',
      degree: `B.Tech in ${profile?.department || 'Computer Science & Engineering'}`,
      institution: profile?.collegeName || 'KVG College of Engineering, Sullia',
      score: 'CGPA: 8.85 / 10',
      year: '2022 - 2026',
    },
    {
      id: 'edu-2',
      degree: 'Pre-University / 12th Standard (Science PCMB)',
      institution: 'Karnataka State Pre-University Board',
      score: 'Percentage: 92.4%',
      year: '2020 - 2022',
    },
  ]);

  const [skills, setSkills] = useState({
    languages: 'Java, Python, C++, TypeScript, SQL, JavaScript',
    frameworks: 'React, React Native, Node.js, Express, Expo, Next.js, FastAPI',
    tools: 'Git, GitHub, Docker, AWS, Postman, Linux, VS Code, CI/CD',
    databases: 'PostgreSQL, MySQL, MongoDB, Redis',
    core: 'Data Structures, Algorithms, OOP, Operating Systems, DBMS, System Design',
  });

  const [projectsList, setProjectsList] = useState([
    {
      id: 'proj-1',
      title: 'SkillExa - Smart Career & Placement Platform',
      tech: 'React Native, FastAPI, TypeScript, SQLite, Docker',
      desc: 'Engineered an interactive student learning and placement platform with online coding compilers, achieving 28% faster problem load times and zero-downtime test suite executions for 1,500+ active users.',
    },
    {
      id: 'proj-2',
      title: 'Distributed Asynchronous Task Queue & Worker',
      tech: 'Python, Redis, Docker, REST API, Celery',
      desc: 'Architected a fault-tolerant async job runner handling 2,000+ requests/sec with automated heartbeat checks, saving 45ms latency and delivering 99.8% uptime reliability.',
    },
  ]);

  const [hasExperience, setHasExperience] = useState(true);
  const [experienceList, setExperienceList] = useState([
    {
      id: 'exp-1',
      role: 'Software Development Engineering Intern',
      company: 'NextGen Solutions Lab',
      duration: 'June 2025 - August 2025',
      desc: 'Optimized SQL query performance across 50,000+ database records, reduced REST API response latency by 35ms, and built 15+ reusable responsive UI components.',
    },
  ]);

  const [certificationsList, setCertificationsList] = useState([
    { id: 'cert-1', title: 'AWS Certified Cloud Practitioner (Amazon Web Services, 2025)' },
    { id: 'cert-2', title: 'Meta Certified React Native Specialist (Coursera Verified)' },
    { id: 'cert-3', title: '1st Place Finalist - Smart India Hackathon Regional Finals' },
  ]);

  // Inject web print CSS once
  useEffect(() => {
    if (Platform.OS === 'web' && typeof document !== 'undefined') {
      if (!document.getElementById('resume-print-style')) {
        const style = document.createElement('style');
        style.id = 'resume-print-style';
        style.innerHTML = `
          @media print {
            body * { visibility: hidden !important; }
            #resume-a4-canvas, #resume-a4-canvas * { visibility: visible !important; }
            #resume-a4-canvas {
              position: absolute !important;
              left: 0 !important;
              top: 0 !important;
              width: 100% !important;
              margin: 0 !important;
              padding: 24px !important;
              box-shadow: none !important;
              border: none !important;
            }
          }
        `;
        document.head.appendChild(style);
      }
    }
  }, []);

  // Autofill from user profile
  const handleAutofill = () => {
    if (profile) {
      setPersonal((prev) => ({
        ...prev,
        fullName: profile.name || prev.fullName,
        email: profile.email || prev.email,
        phone: profile.phone || prev.phone,
      }));
      setEducationList((prev) =>
        prev.map((e, idx) =>
          idx === 0
            ? {
                ...e,
                institution: profile.collegeName || e.institution,
                degree: profile.department ? `B.Tech in ${profile.department}` : e.degree,
              }
            : e
        )
      );
      Alert.alert('Autofill Successful', 'Student profile details applied directly to your resume.');
    } else {
      Alert.alert('Profile Loaded', 'Applied student account details to personal information.');
    }
  };

  // Compile active resume text representation
  const compiledResumeText = useMemo(() => {
    const parts = [
      personal.fullName,
      personal.title,
      personal.summary,
      personal.email,
      personal.phone,
      personal.location,
      personal.github,
      personal.linkedin,
      personal.portfolio,
      ...educationList.map((e) => `${e.degree} ${e.institution} ${e.score} ${e.year}`),
      skills.languages,
      skills.frameworks,
      skills.tools,
      skills.databases,
      skills.core,
      ...projectsList.map((p) => `${p.title} ${p.tech} ${p.desc}`),
      ...(hasExperience ? experienceList.map((e) => `${e.role} ${e.company} ${e.duration} ${e.desc}`) : []),
      ...certificationsList.map((c) => c.title),
    ];
    return parts.filter(Boolean).join('\n');
  }, [personal, educationList, skills, projectsList, hasExperience, experienceList, certificationsList]);

  // Active text evaluated by ATS
  const activeAtsText = useMemo(() => {
    if (atsSource === 'upload') {
      return uploadedText || compiledResumeText;
    }
    if (atsSource === 'paste') {
      return pastedText || compiledResumeText;
    }
    return compiledResumeText;
  }, [atsSource, uploadedText, pastedText, compiledResumeText]);

  // ATS Verification Calculation Engine
  const atsReport = useMemo(() => {
    const rawText = activeAtsText;
    const lower = rawText.toLowerCase();
    const wordList = rawText.trim() ? rawText.trim().split(/\s+/) : [];
    const wordCount = wordList.length;

    // 1. Contact Verification (10 pts)
    const hasEmail = lower.includes('@') && lower.includes('.');
    const hasPhone = (lower.match(/\+?\d[\d\s-]{7,}\d/) !== null) || lower.includes('phone') || lower.includes('+91');
    const hasLinks = lower.includes('github') || lower.includes('linkedin') || lower.includes('.com') || lower.includes('.dev');
    const hasLocation =
      lower.includes('india') ||
      lower.includes('karnataka') ||
      lower.includes('bangalore') ||
      lower.includes('sullia') ||
      personal.location.length > 3;

    let contactScore = 0;
    if (hasEmail) contactScore += 2.5;
    if (hasPhone) contactScore += 2.5;
    if (hasLinks) contactScore += 3;
    if (hasLocation) contactScore += 2;
    contactScore = Math.round(contactScore);

    // 2. Standard ATS Structure (15 pts)
    const hasSummary = lower.includes('summary') || lower.includes('objective') || lower.includes('profile');
    const hasEdu = lower.includes('education') || lower.includes('degree') || lower.includes('b.tech') || lower.includes('college');
    const hasSkillsSec = lower.includes('skill') || lower.includes('technical') || lower.includes('languages');
    const hasProjectsSec = lower.includes('project');
    const hasExpOrCert = lower.includes('experience') || lower.includes('intern') || lower.includes('certif') || lower.includes('award');

    let structureScore = 0;
    if (hasSummary) structureScore += 3;
    if (hasEdu) structureScore += 3;
    if (hasSkillsSec) structureScore += 3;
    if (hasProjectsSec) structureScore += 3;
    if (hasExpOrCert) structureScore += 3;

    // 3. Action Verbs Check (15 pts)
    const matchedVerbs = ACTION_VERBS.filter((v) => lower.includes(v));
    const verbScore = Math.min(15, matchedVerbs.length * 3);

    // 4. Quantifiable Impact & Metrics (20 pts)
    const metricMatches = (
      lower.match(/\d+(\.\d+)?%|\b\d{2,}\+\b|\b\d+\s*(ms|sec|seconds|users|records|requests|qps|endpoints|students)\b|\b\d+x\b|(?:\$|₹)\s*\d+/g) || []
    ).length;
    let metricScore = 0;
    if (metricMatches >= 3) metricScore = 20;
    else if (metricMatches === 2) metricScore = 14;
    else if (metricMatches === 1) metricScore = 7;
    else metricScore = 0;

    // 5. Target Role Keywords Match (30 pts)
    const roleKeywords = ROLE_KEYWORDS[targetRole] || ROLE_KEYWORDS['Full Stack Developer'];
    const matchedKeywords = roleKeywords.filter((k) => lower.includes(k.toLowerCase()));
    const missingKeywords = roleKeywords.filter((k) => !lower.includes(k.toLowerCase()));
    const keywordMatchRatio = matchedKeywords.length / Math.min(roleKeywords.length, 11);
    const keywordScore = Math.min(30, Math.round(keywordMatchRatio * 30));

    // 6. Length & Density Balance (10 pts)
    let densityScore = 10;
    if (wordCount < 150) densityScore = 2;
    else if (wordCount < 280) densityScore = 6;
    else if (wordCount > 1200) densityScore = 4;

    // Overall ATS Total Score
    const totalScore = Math.min(100, contactScore + structureScore + verbScore + metricScore + keywordScore + densityScore);

    // Job Description Matcher (Optional)
    let jdScore: number | null = null;
    let jdMatchedWords: string[] = [];
    if (jobDescription.trim().length > 20) {
      const jdWords = Array.from(
        new Set(
          (jobDescription.toLowerCase().match(/[a-z+#.]{3,}/g) || []).filter(
            (w) =>
              ![
                'and',
                'the',
                'with',
                'for',
                'you',
                'are',
                'will',
                'have',
                'our',
                'team',
                'role',
                'must',
                'years',
                'work',
                'experience',
              ].includes(w)
          )
        )
      );
      if (jdWords.length > 0) {
        jdMatchedWords = jdWords.filter((w) => lower.includes(w));
        jdScore = Math.min(100, Math.round((jdMatchedWords.length / Math.min(jdWords.length, 25)) * 100));
      }
    }

    // Determine Tier & Status
    let grade = 'A+';
    let statusText = 'Elite ATS Match (Ready for Top Tech)';
    let statusColor = '#10B981';
    let statusBg = '#ECFDF5';

    if (totalScore >= 85) {
      grade = 'A+';
      statusText = 'Top Tier: Passes 98%+ Automated ATS Filters';
      statusColor = '#10B981';
      statusBg = '#ECFDF5';
    } else if (totalScore >= 72) {
      grade = 'A';
      statusText = 'Competitive: High Probability of Recruiter Review';
      statusColor = '#2563EB';
      statusBg = '#EFF6FF';
    } else if (totalScore >= 55) {
      grade = 'B';
      statusText = 'Moderate Risk: Add Missing Keywords & Metrics';
      statusColor = '#F59E0B';
      statusBg = '#FFFBEB';
    } else {
      grade = 'C';
      statusText = 'High Rejection Risk: Structural & Keyword Deficits';
      statusColor = '#EF4444';
      statusBg = '#FEF2F2';
    }

    // Diagnostics / Fix-It Checklist
    const diagnostics = [
      {
        id: 'contact',
        passed: contactScore >= 9,
        title: 'Contact Information & Web Presence',
        detail: contactScore >= 9 ? 'Email, phone number, and online tech links detected' : 'Ensure email, phone, and GitHub/LinkedIn are included',
      },
      {
        id: 'structure',
        passed: structureScore >= 12,
        title: 'Standard ATS Section Architecture',
        detail: structureScore >= 12 ? 'Clear headers for Education, Skills, Projects, and Experience' : 'Missing standard section headings',
      },
      {
        id: 'keywords',
        passed: keywordScore >= 22,
        title: `Role Keywords for ${targetRole}`,
        detail: `${matchedKeywords.length} of ${roleKeywords.length} target keywords verified`,
      },
      {
        id: 'metrics',
        passed: metricScore >= 14,
        title: 'Measurable Outcomes & Quantifiable Metrics',
        detail:
          metricScore >= 14
            ? `Found ${metricMatches} numerical metrics (%, ms, latencies, or scale)`
            : 'Add at least 2 measurable metrics (e.g. "improved speed by 25%")',
      },
      {
        id: 'verbs',
        passed: verbScore >= 12,
        title: 'Action Verbs & Power Phrasing',
        detail: `Found ${matchedVerbs.length} high-impact technical action verbs`,
      },
      {
        id: 'density',
        passed: densityScore === 10,
        title: 'Document Word Count & Density',
        detail: `${wordCount} words (${wordCount >= 350 && wordCount <= 850 ? 'Ideal 1-page length' : 'Adjust density to 350–800 words'})`,
      },
    ];

    return {
      totalScore,
      grade,
      statusText,
      statusColor,
      statusBg,
      contactScore,
      structureScore,
      verbScore,
      metricScore,
      keywordScore,
      densityScore,
      wordCount,
      matchedVerbs,
      matchedKeywords,
      missingKeywords,
      metricMatches,
      diagnostics,
      jdScore,
      jdMatchedWordsCount: jdMatchedWords.length,
    };
  }, [activeAtsText, targetRole, personal.location, jobDescription]);

  // Open file picker on web
  const openFilePicker = () => {
    if (Platform.OS === 'web' && typeof document !== 'undefined') {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.pdf,.txt,.doc,.docx,.md';
      input.onchange = (e: any) => {
        const file = e.target?.files?.[0];
        if (!file) return;

        setUploadedFileName(file.name);
        setUploadedFileSize(`${(file.size / 1024).toFixed(1)} KB`);

        const reader = new FileReader();
        if (file.name.endsWith('.txt') || file.name.endsWith('.md')) {
          reader.onload = (event: any) => {
            const txt = event.target?.result as string;
            setUploadedText(txt);
            setAtsSource('upload');
            setActiveMode('ats');
          };
          reader.readAsText(file);
        } else {
          // PDF or binary file: read and extract text stream
          reader.onload = (event: any) => {
            const buffer = event.target?.result as ArrayBuffer;
            let extracted = '';
            if (buffer) {
              const uint8 = new Uint8Array(buffer);
              let raw = '';
              const len = Math.min(uint8.length, 600000);
              for (let i = 0; i < len; i++) {
                raw += String.fromCharCode(uint8[i]);
              }
              const textBlocks: string[] = [];
              const btRegex = /BT[\s\S]*?ET/g;
              let match;
              while ((match = btRegex.exec(raw)) !== null) {
                const block = match[0];
                const tjRegex = /\((.*?)\)\s*Tj/g;
                let tjMatch;
                while ((tjMatch = tjRegex.exec(block)) !== null) {
                  textBlocks.push(tjMatch[1]);
                }
                const bracketRegex = /\[(.*?)\]\s*TJ/g;
                let bMatch;
                while ((bMatch = bracketRegex.exec(block)) !== null) {
                  const inner = bMatch[1].replace(/\((.*?)\)/g, '$1 ');
                  textBlocks.push(inner);
                }
              }
              if (textBlocks.length > 5) {
                extracted = textBlocks.join(' ');
              } else {
                const words = raw.match(/[A-Za-z0-9+#.\-@]{3,}/g) || [];
                extracted = words.join(' ');
              }
            }
            setUploadedText(extracted || 'Parsed text from uploaded PDF resume.');
            setAtsSource('upload');
            setActiveMode('ats');
          };
          reader.readAsArrayBuffer(file);
        }
      };
      input.click();
    } else {
      Alert.alert('Upload Resume', 'Please switch to the "Paste Resume Text" tab to paste your resume content.');
    }
  };

  // 1-Click add missing keyword to resume
  const handleAddKeywordToSkills = (keyword: string) => {
    if (skills.tools.toLowerCase().includes(keyword.toLowerCase())) {
      Alert.alert('Already Present', `"${keyword}" is already in your skills.`);
      return;
    }
    setSkills((prev) => ({
      ...prev,
      tools: prev.tools ? `${prev.tools}, ${keyword}` : keyword,
    }));
    Alert.alert('Keyword Added!', `Added "${keyword}" to your skills! Your ATS score has been boosted.`);
  };

  // Print or download PDF
  const handlePrintPdf = () => {
    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      window.print();
    } else {
      Alert.alert('Print / Download PDF', 'Your ATS-compliant PDF resume has been compiled successfully!');
    }
  };

  // Copy plain ATS text
  const handleCopyCleanText = () => {
    if (Platform.OS === 'web' && typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(compiledResumeText);
      Alert.alert('Copied to Clipboard', 'Clean plain-text resume copied successfully for easy pasting.');
    } else {
      Alert.alert('Resume Exported', 'Clean text generated successfully.');
    }
  };

  // Dynamic Item Helpers
  const addProject = () => {
    const newId = `proj-${projectsList.length + 1}`;
    setProjectsList([
      ...projectsList,
      {
        id: newId,
        title: 'New Featured Project',
        tech: 'React, Node.js, SQL',
        desc: 'Engineered a full-stack solution improving system throughput by 20% and reducing latency by 30ms.',
      },
    ]);
  };

  const removeProject = (id: string) => {
    if (projectsList.length <= 1) {
      Alert.alert('Required', 'Keep at least one project on your resume.');
      return;
    }
    setProjectsList(projectsList.filter((p) => p.id !== id));
  };

  const addExperience = () => {
    const newId = `exp-${experienceList.length + 1}`;
    setExperienceList([
      ...experienceList,
      {
        id: newId,
        role: 'Software Development Intern',
        company: 'Innovate Tech Labs',
        duration: 'Jan 2025 - May 2025',
        desc: 'Collaborated with engineering team to deploy CI/CD pipelines, increasing deployment frequency by 40%.',
      },
    ]);
  };

  const removeExperience = (id: string) => {
    setExperienceList(experienceList.filter((e) => e.id !== id));
  };

  const addEducation = () => {
    const newId = `edu-${educationList.length + 1}`;
    setEducationList([
      ...educationList,
      {
        id: newId,
        degree: 'Secondary School Certificate (10th Standard)',
        institution: 'State Board of Education',
        score: 'Percentage: 94.0%',
        year: '2020',
      },
    ]);
  };

  const removeEducation = (id: string) => {
    if (educationList.length <= 1) {
      Alert.alert('Required', 'Keep at least one education entry on your resume.');
      return;
    }
    setEducationList(educationList.filter((e) => e.id !== id));
  };

  const addCertification = () => {
    const newId = `cert-${certificationsList.length + 1}`;
    setCertificationsList([
      ...certificationsList,
      { id: newId, title: 'Google Professional Cloud Developer (Coursera)' },
    ]);
  };

  const removeCertification = (id: string) => {
    setCertificationsList(certificationsList.filter((c) => c.id !== id));
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        title="Resume Builder & ATS Studio"
        subtitle={
          activeMode === 'wizard'
            ? `Step ${currentStep} of 6: ${WIZARD_STEPS[currentStep - 1]?.label || 'Details'}`
            : activeMode === 'preview'
            ? 'Live ATS Resume Canvas & PDF Export'
            : `Automated ATS Audit Engine (${atsReport.totalScore}% Score)`
        }
      />

      {/* Primary Mode Switcher Tab Bar */}
      <View style={[styles.modeTabContainer, isDesktop && styles.modeTabContainerDesktop]}>
        <TouchableOpacity
          style={[styles.modeTab, activeMode === 'wizard' && styles.modeTabActive]}
          onPress={() => setActiveMode('wizard')}
          activeOpacity={0.8}
        >
          <Feather name="edit-3" size={15} color={activeMode === 'wizard' ? Palette.primary : Palette.textSecondary} />
          <Text style={[styles.modeTabText, activeMode === 'wizard' && styles.modeTabTextActive]}>
            Form Editor
          </Text>
          <View style={styles.stepCountBadge}>
            <Text style={styles.stepCountBadgeText}>{currentStep}/6</Text>
          </View>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.modeTab, activeMode === 'preview' && styles.modeTabActive]}
          onPress={() => setActiveMode('preview')}
          activeOpacity={0.8}
        >
          <Feather name="file-text" size={15} color={activeMode === 'preview' ? Palette.primary : Palette.textSecondary} />
          <Text style={[styles.modeTabText, activeMode === 'preview' && styles.modeTabTextActive]}>
            Document Preview
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.modeTab, activeMode === 'ats' && styles.modeTabActiveAts]}
          onPress={() => setActiveMode('ats')}
          activeOpacity={0.8}
        >
          <Ionicons
            name="shield-checkmark"
            size={16}
            color={activeMode === 'ats' ? '#10B981' : Palette.textSecondary}
          />
          <Text style={[styles.modeTabText, activeMode === 'ats' && styles.modeTabTextActiveAts]}>
            ATS Verification
          </Text>
          <View
            style={[
              styles.atsScoreBadgeMini,
              {
                backgroundColor:
                  atsReport.totalScore >= 85 ? '#10B981' : atsReport.totalScore >= 70 ? '#2563EB' : '#F59E0B',
              },
            ]}
          >
            <Text style={styles.atsScoreBadgeMiniText}>{atsReport.totalScore}%</Text>
          </View>
        </TouchableOpacity>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        <View style={[styles.container, isDesktop && styles.containerDesktop]}>
          {/* ============================================================== */}
          {/* MODE 1: FORM WIZARD (ACCURATE BUILDER)                         */}
          {/* ============================================================== */}
          {activeMode === 'wizard' && (
            <>
              {/* Wizard Top Step Pills & Autofill Bar */}
              <View style={styles.wizardTopRow}>
                <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.stepScroll}>
                  {WIZARD_STEPS.map((step) => {
                    const isCompleted = step.id < currentStep;
                    const isCurrent = step.id === currentStep;
                    return (
                      <TouchableOpacity
                        key={step.id}
                        style={[
                          styles.stepPill,
                          isCurrent && styles.stepPillCurrent,
                          isCompleted && styles.stepPillCompleted,
                        ]}
                        onPress={() => setCurrentStep(step.id)}
                        activeOpacity={0.7}
                      >
                        <Text
                          style={[
                            styles.stepNumText,
                            isCurrent && styles.stepNumTextCurrent,
                            isCompleted && styles.stepNumTextCompleted,
                          ]}
                        >
                          {isCompleted ? '✓' : step.id}
                        </Text>
                        <Text style={[styles.stepLabelText, isCurrent && styles.stepLabelTextCurrent]}>
                          {step.label}
                        </Text>
                      </TouchableOpacity>
                    );
                  })}
                </ScrollView>

                <TouchableOpacity style={styles.autofillBtn} onPress={handleAutofill} activeOpacity={0.7}>
                  <Feather name="zap" size={13} color="#0284C7" />
                  <Text style={styles.autofillText}>Autofill Profile</Text>
                </TouchableOpacity>
              </View>

              {/* Step 1: Personal & Professional Summary */}
              {currentStep === 1 && (
                <View style={styles.formCard}>
                  <View style={styles.formHeaderRow}>
                    <View style={styles.stepBadge}>
                      <Text style={styles.stepBadgeText}>1</Text>
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.formSectionTitle}>Personal & Contact Details</Text>
                      <Text style={styles.formSectionSub}>
                        Accurate headers ensure ATS spiders extract contact info and portfolio URLs reliably.
                      </Text>
                    </View>
                  </View>

                  <Text style={styles.inputLabel}>FULL NAME *</Text>
                  <TextInput
                    style={styles.input}
                    value={personal.fullName}
                    placeholder="e.g. Ganesh Sharan"
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setPersonal({ ...personal, fullName: t })}
                  />

                  <Text style={styles.inputLabel}>PROFESSIONAL HEADLINE *</Text>
                  <TextInput
                    style={styles.input}
                    value={personal.title}
                    placeholder="e.g. Computer Science Engineer | Full Stack Developer"
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setPersonal({ ...personal, title: t })}
                  />

                  <View style={styles.inputRow}>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.inputLabel}>EMAIL ADDRESS *</Text>
                      <TextInput
                        style={styles.input}
                        value={personal.email}
                        keyboardType="email-address"
                        placeholder="student@example.edu"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) => setPersonal({ ...personal, email: t })}
                      />
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.inputLabel}>PHONE NUMBER *</Text>
                      <TextInput
                        style={styles.input}
                        value={personal.phone}
                        keyboardType="phone-pad"
                        placeholder="+91 98765 43210"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) => setPersonal({ ...personal, phone: t })}
                      />
                    </View>
                  </View>

                  <View style={styles.inputRow}>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.inputLabel}>CURRENT LOCATION (CITY, STATE) *</Text>
                      <TextInput
                        style={styles.input}
                        value={personal.location}
                        placeholder="e.g. Sullia, Karnataka"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) => setPersonal({ ...personal, location: t })}
                      />
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.inputLabel}>PORTFOLIO / WEBSITE</Text>
                      <TextInput
                        style={styles.input}
                        value={personal.portfolio}
                        placeholder="e.g. ganesh.dev"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) => setPersonal({ ...personal, portfolio: t })}
                      />
                    </View>
                  </View>

                  <View style={styles.inputRow}>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.inputLabel}>GITHUB REPOSITORY</Text>
                      <TextInput
                        style={styles.input}
                        value={personal.github}
                        placeholder="github.com/username"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) => setPersonal({ ...personal, github: t })}
                      />
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.inputLabel}>LINKEDIN PROFILE</Text>
                      <TextInput
                        style={styles.input}
                        value={personal.linkedin}
                        placeholder="linkedin.com/in/username"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) => setPersonal({ ...personal, linkedin: t })}
                      />
                    </View>
                  </View>

                  <View style={{ marginTop: 14 }}>
                    <View style={styles.labelWithQuickFill}>
                      <Text style={styles.inputLabel}>PROFESSIONAL SUMMARY / OBJECTIVE</Text>
                      <Text style={styles.labelSubText}>ATS scanners reward targeted summaries.</Text>
                    </View>
                    <TextInput
                      style={[styles.input, styles.textArea]}
                      multiline
                      value={personal.summary}
                      placeholder="Brief 2-3 sentence overview of your technical focus and strengths..."
                      placeholderTextColor="#94A3B8"
                      onChangeText={(t) => setPersonal({ ...personal, summary: t })}
                    />
                  </View>
                </View>
              )}

              {/* Step 2: Academic Credentials */}
              {currentStep === 2 && (
                <View style={styles.formCard}>
                  <View style={styles.formHeaderRow}>
                    <View style={styles.stepBadge}>
                      <Text style={styles.stepBadgeText}>2</Text>
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.formSectionTitle}>Academic Credentials</Text>
                      <Text style={styles.formSectionSub}>
                        List college degrees, universities, GPAs, and pre-university credentials.
                      </Text>
                    </View>
                  </View>

                  {educationList.map((edu, index) => (
                    <View key={edu.id} style={[styles.innerCard, index > 0 && { marginTop: 14 }]}>
                      <View style={styles.innerCardHeader}>
                        <Text style={styles.innerCardHeading}>Education #{index + 1}</Text>
                        {educationList.length > 1 && (
                          <TouchableOpacity onPress={() => removeEducation(edu.id)} style={styles.deleteBtn}>
                            <Feather name="trash-2" size={14} color="#EF4444" />
                            <Text style={styles.deleteBtnText}>Remove</Text>
                          </TouchableOpacity>
                        )}
                      </View>

                      <Text style={styles.inputLabel}>DEGREE / PROGRAM *</Text>
                      <TextInput
                        style={styles.input}
                        value={edu.degree}
                        placeholder="e.g. B.Tech in Computer Science and Engineering"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) =>
                          setEducationList(
                            educationList.map((item) => (item.id === edu.id ? { ...item, degree: t } : item))
                          )
                        }
                      />

                      <Text style={styles.inputLabel}>COLLEGE / UNIVERSITY *</Text>
                      <TextInput
                        style={styles.input}
                        value={edu.institution}
                        placeholder="e.g. KVG College of Engineering, Sullia"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) =>
                          setEducationList(
                            educationList.map((item) => (item.id === edu.id ? { ...item, institution: t } : item))
                          )
                        }
                      />

                      <View style={styles.inputRow}>
                        <View style={{ flex: 1 }}>
                          <Text style={styles.inputLabel}>SCORE (CGPA / %)</Text>
                          <TextInput
                            style={styles.input}
                            value={edu.score}
                            placeholder="e.g. CGPA: 8.85 / 10"
                            placeholderTextColor="#94A3B8"
                            onChangeText={(t) =>
                              setEducationList(
                                educationList.map((item) => (item.id === edu.id ? { ...item, score: t } : item))
                              )
                            }
                          />
                        </View>
                        <View style={{ flex: 1 }}>
                          <Text style={styles.inputLabel}>TIMELINE / GRAD YEAR</Text>
                          <TextInput
                            style={styles.input}
                            value={edu.year}
                            placeholder="e.g. 2022 - 2026"
                            placeholderTextColor="#94A3B8"
                            onChangeText={(t) =>
                              setEducationList(
                                educationList.map((item) => (item.id === edu.id ? { ...item, year: t } : item))
                              )
                            }
                          />
                        </View>
                      </View>
                    </View>
                  ))}

                  <TouchableOpacity style={styles.addSectionBtn} onPress={addEducation} activeOpacity={0.7}>
                    <Feather name="plus-circle" size={15} color="#2563EB" />
                    <Text style={styles.addSectionBtnText}>+ Add Another Degree / School</Text>
                  </TouchableOpacity>
                </View>
              )}

              {/* Step 3: Technical Skills Matrix */}
              {currentStep === 3 && (
                <View style={styles.formCard}>
                  <View style={styles.formHeaderRow}>
                    <View style={styles.stepBadge}>
                      <Text style={styles.stepBadgeText}>3</Text>
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.formSectionTitle}>Technical Skills & Competencies</Text>
                      <Text style={styles.formSectionSub}>
                        Categorize skills cleanly so ATS keyword scanners extract hard skills effortlessly.
                      </Text>
                    </View>
                  </View>

                  <Text style={styles.inputLabel}>PROGRAMMING LANGUAGES *</Text>
                  <TextInput
                    style={styles.input}
                    value={skills.languages}
                    placeholder="e.g. Java, Python, C++, TypeScript, SQL, JavaScript"
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setSkills({ ...skills, languages: t })}
                  />

                  <Text style={styles.inputLabel}>FRAMEWORKS & LIBRARIES *</Text>
                  <TextInput
                    style={styles.input}
                    value={skills.frameworks}
                    placeholder="e.g. React, React Native, Node.js, Express, Next.js, FastAPI"
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setSkills({ ...skills, frameworks: t })}
                  />

                  <Text style={styles.inputLabel}>DEVELOPER TOOLS & CLOUD</Text>
                  <TextInput
                    style={styles.input}
                    value={skills.tools}
                    placeholder="e.g. Git, GitHub, Docker, AWS, Postman, Linux, CI/CD"
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setSkills({ ...skills, tools: t })}
                  />

                  <Text style={styles.inputLabel}>DATABASES & ORMS</Text>
                  <TextInput
                    style={styles.input}
                    value={skills.databases}
                    placeholder="e.g. PostgreSQL, MySQL, MongoDB, Redis, SQLite"
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setSkills({ ...skills, databases: t })}
                  />

                  <Text style={styles.inputLabel}>CORE COMPUTER SCIENCE CONCEPTS</Text>
                  <TextInput
                    style={styles.input}
                    value={skills.core}
                    placeholder="e.g. Data Structures, Algorithms, OOP, Operating Systems, DBMS, System Design"
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setSkills({ ...skills, core: t })}
                  />

                  {/* ATS Recommended Skill Chips for Target Role */}
                  <View style={styles.quickKeywordBox}>
                    <Text style={styles.quickKeywordTitle}>
                      💡 Recommended Keywords for {targetRole} (Tap to insert):
                    </Text>
                    <View style={styles.chipsWrap}>
                      {(ROLE_KEYWORDS[targetRole] || []).slice(0, 8).map((k) => (
                        <TouchableOpacity
                          key={k}
                          style={styles.quickKeywordChip}
                          onPress={() => handleAddKeywordToSkills(k)}
                        >
                          <Text style={styles.quickKeywordChipText}>+ {k}</Text>
                        </TouchableOpacity>
                      ))}
                    </View>
                  </View>
                </View>
              )}

              {/* Step 4: Key Projects */}
              {currentStep === 4 && (
                <View style={styles.formCard}>
                  <View style={styles.formHeaderRow}>
                    <View style={styles.stepBadge}>
                      <Text style={styles.stepBadgeText}>4</Text>
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.formSectionTitle}>Featured Technical Projects</Text>
                      <Text style={styles.formSectionSub}>
                        ATS Rule: Start each bullet with an active verb (Engineered, Developed) and include measurable metrics (%, ms, users).
                      </Text>
                    </View>
                  </View>

                  {projectsList.map((proj, index) => (
                    <View key={proj.id} style={[styles.innerCard, index > 0 && { marginTop: 14 }]}>
                      <View style={styles.innerCardHeader}>
                        <Text style={styles.innerCardHeading}>Project #{index + 1}</Text>
                        {projectsList.length > 1 && (
                          <TouchableOpacity onPress={() => removeProject(proj.id)} style={styles.deleteBtn}>
                            <Feather name="trash-2" size={14} color="#EF4444" />
                            <Text style={styles.deleteBtnText}>Remove</Text>
                          </TouchableOpacity>
                        )}
                      </View>

                      <Text style={styles.inputLabel}>PROJECT TITLE *</Text>
                      <TextInput
                        style={styles.input}
                        value={proj.title}
                        placeholder="e.g. SkillExa - Career & Placement Platform"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) =>
                          setProjectsList(
                            projectsList.map((p) => (p.id === proj.id ? { ...p, title: t } : p))
                          )
                        }
                      />

                      <Text style={styles.inputLabel}>TECH STACK USED *</Text>
                      <TextInput
                        style={styles.input}
                        value={proj.tech}
                        placeholder="e.g. React Native, FastAPI, TypeScript, SQLite, Docker"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) =>
                          setProjectsList(
                            projectsList.map((p) => (p.id === proj.id ? { ...p, tech: t } : p))
                          )
                        }
                      />

                      <Text style={styles.inputLabel}>ACCOMPLISHMENTS & QUANTIFIABLE METRICS *</Text>
                      <TextInput
                        style={[styles.input, styles.textArea]}
                        multiline
                        value={proj.desc}
                        placeholder="e.g. Engineered full-stack solution achieving 28% faster problem load times and zero downtime for 1,500+ users."
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) =>
                          setProjectsList(
                            projectsList.map((p) => (p.id === proj.id ? { ...p, desc: t } : p))
                          )
                        }
                      />
                    </View>
                  ))}

                  <TouchableOpacity style={styles.addSectionBtn} onPress={addProject} activeOpacity={0.7}>
                    <Feather name="plus-circle" size={15} color="#2563EB" />
                    <Text style={styles.addSectionBtnText}>+ Add Another Project</Text>
                  </TouchableOpacity>
                </View>
              )}

              {/* Step 5: Professional Experience / Internships */}
              {currentStep === 5 && (
                <View style={styles.formCard}>
                  <View style={styles.formHeaderRow}>
                    <View style={styles.stepBadge}>
                      <Text style={styles.stepBadgeText}>5</Text>
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.formSectionTitle}>Internships & Experience</Text>
                      <Text style={styles.formSectionSub}>
                        Highlight internships, open-source contributions, or campus leadership.
                      </Text>
                    </View>
                  </View>

                  {/* Experience Toggle */}
                  <View style={styles.toggleRow}>
                    <TouchableOpacity
                      style={[styles.toggleBtn, hasExperience && styles.toggleBtnActive]}
                      onPress={() => setHasExperience(true)}
                    >
                      <Text style={[styles.toggleBtnText, hasExperience && styles.toggleBtnTextActive]}>
                        ✓ Include Internships / Work Experience
                      </Text>
                    </TouchableOpacity>

                    <TouchableOpacity
                      style={[styles.toggleBtn, !hasExperience && styles.toggleBtnActive]}
                      onPress={() => setHasExperience(false)}
                    >
                      <Text style={[styles.toggleBtnText, !hasExperience && styles.toggleBtnTextActive]}>
                        Fresher (Focus on Projects & Academics)
                      </Text>
                    </TouchableOpacity>
                  </View>

                  {hasExperience && (
                    <>
                      {experienceList.map((exp, index) => (
                        <View key={exp.id} style={[styles.innerCard, index > 0 && { marginTop: 14 }]}>
                          <View style={styles.innerCardHeader}>
                            <Text style={styles.innerCardHeading}>Experience #{index + 1}</Text>
                            {experienceList.length > 1 && (
                              <TouchableOpacity onPress={() => removeExperience(exp.id)} style={styles.deleteBtn}>
                                <Feather name="trash-2" size={14} color="#EF4444" />
                                <Text style={styles.deleteBtnText}>Remove</Text>
                              </TouchableOpacity>
                            )}
                          </View>

                          <Text style={styles.inputLabel}>JOB TITLE / ROLE *</Text>
                          <TextInput
                            style={styles.input}
                            value={exp.role}
                            placeholder="e.g. Software Development Intern"
                            placeholderTextColor="#94A3B8"
                            onChangeText={(t) =>
                              setExperienceList(
                                experienceList.map((e) => (e.id === exp.id ? { ...e, role: t } : e))
                              )
                            }
                          />

                          <Text style={styles.inputLabel}>COMPANY / ORGANIZATION *</Text>
                          <TextInput
                            style={styles.input}
                            value={exp.company}
                            placeholder="e.g. NextGen Solutions Lab"
                            placeholderTextColor="#94A3B8"
                            onChangeText={(t) =>
                              setExperienceList(
                                experienceList.map((e) => (e.id === exp.id ? { ...e, company: t } : e))
                              )
                            }
                          />

                          <Text style={styles.inputLabel}>TIMELINE / DATES</Text>
                          <TextInput
                            style={styles.input}
                            value={exp.duration}
                            placeholder="e.g. June 2025 - August 2025"
                            placeholderTextColor="#94A3B8"
                            onChangeText={(t) =>
                              setExperienceList(
                                experienceList.map((e) => (e.id === exp.id ? { ...e, duration: t } : e))
                              )
                            }
                          />

                          <Text style={styles.inputLabel}>KEY RESPONSIBILITIES & MEASURABLE OUTCOMES</Text>
                          <TextInput
                            style={[styles.input, styles.textArea]}
                            multiline
                            value={exp.desc}
                            placeholder="e.g. Optimized SQL queries across 50,000+ records, reduced API latency by 35ms, and built reusable UI tokens."
                            placeholderTextColor="#94A3B8"
                            onChangeText={(t) =>
                              setExperienceList(
                                experienceList.map((e) => (e.id === exp.id ? { ...e, desc: t } : e))
                              )
                            }
                          />
                        </View>
                      ))}

                      <TouchableOpacity style={styles.addSectionBtn} onPress={addExperience} activeOpacity={0.7}>
                        <Feather name="plus-circle" size={15} color="#2563EB" />
                        <Text style={styles.addSectionBtnText}>+ Add Another Experience</Text>
                      </TouchableOpacity>
                    </>
                  )}
                </View>
              )}

              {/* Step 6: Certifications & Honors + Completion Callout */}
              {currentStep === 6 && (
                <View style={styles.formCard}>
                  <View style={styles.formHeaderRow}>
                    <View style={styles.stepBadge}>
                      <Text style={styles.stepBadgeText}>6</Text>
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.formSectionTitle}>Certifications & Honors</Text>
                      <Text style={styles.formSectionSub}>
                        Industry credentials and competitive hackathon honors validate your candidate profile.
                      </Text>
                    </View>
                  </View>

                  {certificationsList.map((cert, index) => (
                    <View key={cert.id} style={[styles.innerCard, index > 0 && { marginTop: 12 }]}>
                      <View style={styles.innerCardHeader}>
                        <Text style={styles.innerCardHeading}>Credential #{index + 1}</Text>
                        {certificationsList.length > 1 && (
                          <TouchableOpacity onPress={() => removeCertification(cert.id)} style={styles.deleteBtn}>
                            <Feather name="trash-2" size={14} color="#EF4444" />
                            <Text style={styles.deleteBtnText}>Remove</Text>
                          </TouchableOpacity>
                        )}
                      </View>

                      <Text style={styles.inputLabel}>CERTIFICATION NAME / AWARD</Text>
                      <TextInput
                        style={styles.input}
                        value={cert.title}
                        placeholder="e.g. AWS Certified Cloud Practitioner"
                        placeholderTextColor="#94A3B8"
                        onChangeText={(t) =>
                          setCertificationsList(
                            certificationsList.map((c) => (c.id === cert.id ? { ...c, title: t } : c))
                          )
                        }
                      />
                    </View>
                  ))}

                  <TouchableOpacity style={styles.addSectionBtn} onPress={addCertification} activeOpacity={0.7}>
                    <Feather name="plus-circle" size={15} color="#2563EB" />
                    <Text style={styles.addSectionBtnText}>+ Add Another Certification</Text>
                  </TouchableOpacity>

                  {/* Completion Action Card */}
                  <View style={styles.completionCard}>
                    <View style={styles.completionIconCircle}>
                      <Ionicons name="checkmark-done" size={24} color="#10B981" />
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.completionHeading}>🎉 Resume Completed Neatly!</Text>
                      <Text style={styles.completionSub}>
                        All 6 core sections have been populated. Run the automated ATS audit or preview the document canvas.
                      </Text>
                    </View>
                  </View>

                  <View style={styles.completionButtonsRow}>
                    <TouchableOpacity
                      style={styles.completionVerifyBtn}
                      onPress={() => {
                        setAtsSource('created');
                        setActiveMode('ats');
                      }}
                      activeOpacity={0.85}
                    >
                      <Ionicons name="shield-checkmark" size={17} color="#FFFFFF" />
                      <Text style={styles.completionVerifyBtnText}>Audit ATS Score ({atsReport.totalScore}%)</Text>
                    </TouchableOpacity>

                    <TouchableOpacity
                      style={styles.completionPreviewBtn}
                      onPress={() => setActiveMode('preview')}
                      activeOpacity={0.85}
                    >
                      <Feather name="eye" size={17} color="#2563EB" />
                      <Text style={styles.completionPreviewBtnText}>Preview & Print PDF</Text>
                    </TouchableOpacity>
                  </View>
                </View>
              )}

              {/* Wizard Bottom Nav Buttons */}
              <View style={styles.wizardNavRow}>
                {currentStep > 1 && (
                  <TouchableOpacity
                    style={styles.prevBtn}
                    onPress={() => setCurrentStep(currentStep - 1)}
                    activeOpacity={0.8}
                  >
                    <Feather name="arrow-left" size={16} color={Palette.textTitle} />
                    <Text style={styles.prevBtnText}>Previous</Text>
                  </TouchableOpacity>
                )}

                {currentStep < 6 ? (
                  <TouchableOpacity
                    style={styles.nextBtn}
                    onPress={() => setCurrentStep(currentStep + 1)}
                    activeOpacity={0.85}
                  >
                    <Text style={styles.nextBtnText}>Continue to Step {currentStep + 1}</Text>
                    <Feather name="arrow-right" size={16} color="#FFFFFF" />
                  </TouchableOpacity>
                ) : (
                  <TouchableOpacity
                    style={[styles.nextBtn, { backgroundColor: '#10B981' }]}
                    onPress={() => {
                      setAtsSource('created');
                      setActiveMode('ats');
                    }}
                    activeOpacity={0.85}
                  >
                    <Text style={styles.nextBtnText}>Verify ATS Score ({atsReport.totalScore}%)</Text>
                    <Ionicons name="shield-checkmark" size={16} color="#FFFFFF" />
                  </TouchableOpacity>
                )}
              </View>
            </>
          )}

          {/* ============================================================== */}
          {/* MODE 2: LIVE A4 DOCUMENT PREVIEW & PDF EXPORT                  */}
          {/* ============================================================== */}
          {activeMode === 'preview' && (
            <View style={styles.previewContainer}>
              {/* Toolbar */}
              <View style={styles.previewToolbar}>
                <View style={styles.templateOptions}>
                  <Text style={styles.toolbarLabel}>Style:</Text>
                  {(['modern', 'classic', 'minimal'] as const).map((t) => (
                    <TouchableOpacity
                      key={t}
                      style={[styles.templateBtn, template === t && styles.templateBtnActive]}
                      onPress={() => setTemplate(t)}
                    >
                      <Text style={[styles.templateBtnText, template === t && styles.templateBtnTextActive]}>
                        {t === 'modern' ? 'Modern Tech' : t === 'classic' ? 'Harvard Classic' : 'Minimalist'}
                      </Text>
                    </TouchableOpacity>
                  ))}
                </View>

                <View style={styles.toolbarActions}>
                  <TouchableOpacity
                    style={styles.verifyAtsBtn}
                    onPress={() => {
                      setAtsSource('created');
                      setActiveMode('ats');
                    }}
                    activeOpacity={0.8}
                  >
                    <Ionicons name="shield-checkmark" size={16} color="#10B981" />
                    <Text style={styles.verifyAtsBtnText}>ATS Score: {atsReport.totalScore}%</Text>
                  </TouchableOpacity>

                  <TouchableOpacity style={styles.copyTextBtn} onPress={handleCopyCleanText} activeOpacity={0.8}>
                    <Feather name="copy" size={15} color="#475569" />
                    <Text style={styles.copyTextBtnText}>Copy Text</Text>
                  </TouchableOpacity>

                  <TouchableOpacity style={styles.downloadPrimaryBtn} onPress={handlePrintPdf} activeOpacity={0.85}>
                    <Feather name="download" size={16} color="#FFFFFF" />
                    <Text style={styles.downloadPrimaryBtnText}>Print / Save PDF</Text>
                  </TouchableOpacity>
                </View>
              </View>

              {/* A4 Paper Document Canvas */}
              <View
                nativeID="resume-a4-canvas"
                style={[
                  styles.a4Canvas,
                  template === 'classic' && styles.canvasClassic,
                  template === 'minimal' && styles.canvasMinimal,
                ]}
              >
                {/* Header */}
                <View style={styles.docHeader}>
                  <Text style={[styles.docName, template === 'classic' && { fontFamily: 'serif' }]}>
                    {personal.fullName}
                  </Text>
                  <Text style={styles.docTitle}>{personal.title}</Text>
                  <Text style={styles.docContactLine}>
                    {personal.email}  |  {personal.phone}  |  {personal.location}
                  </Text>
                  <Text style={styles.docLinksLine}>
                    {personal.github}  •  {personal.linkedin}
                    {personal.portfolio ? `  •  ${personal.portfolio}` : ''}
                  </Text>
                </View>

                {personal.summary ? (
                  <View style={styles.docSummaryBox}>
                    <Text style={styles.docSummaryText}>{personal.summary}</Text>
                  </View>
                ) : null}

                <View style={[styles.docHr, template === 'modern' && { backgroundColor: Palette.primary }]} />

                {/* Education */}
                <View style={styles.docSection}>
                  <Text style={[styles.docSectionTitle, template === 'modern' && { color: Palette.primary }]}>
                    EDUCATION
                  </Text>
                  {educationList.map((edu) => (
                    <View key={edu.id} style={{ marginBottom: 6 }}>
                      <View style={styles.docRowBetween}>
                        <Text style={styles.docItemTitle}>{edu.degree}</Text>
                        <Text style={styles.docItemDate}>{edu.year}</Text>
                      </View>
                      <Text style={styles.docItemSub}>
                        {edu.institution}  —  <Text style={{ fontWeight: '700' }}>{edu.score}</Text>
                      </Text>
                    </View>
                  ))}
                </View>

                {/* Technical Skills */}
                <View style={styles.docSection}>
                  <Text style={[styles.docSectionTitle, template === 'modern' && { color: Palette.primary }]}>
                    TECHNICAL SKILLS
                  </Text>
                  <Text style={styles.docSkillLine}>
                    <Text style={styles.docSkillCategory}>Languages: </Text>
                    {skills.languages}
                  </Text>
                  <Text style={styles.docSkillLine}>
                    <Text style={styles.docSkillCategory}>Frameworks & Libraries: </Text>
                    {skills.frameworks}
                  </Text>
                  <Text style={styles.docSkillLine}>
                    <Text style={styles.docSkillCategory}>Developer Tools & Cloud: </Text>
                    {skills.tools}
                  </Text>
                  {skills.databases ? (
                    <Text style={styles.docSkillLine}>
                      <Text style={styles.docSkillCategory}>Databases: </Text>
                      {skills.databases}
                    </Text>
                  ) : null}
                  {skills.core ? (
                    <Text style={styles.docSkillLine}>
                      <Text style={styles.docSkillCategory}>Core Concepts: </Text>
                      {skills.core}
                    </Text>
                  ) : null}
                </View>

                {/* Projects */}
                <View style={styles.docSection}>
                  <Text style={[styles.docSectionTitle, template === 'modern' && { color: Palette.primary }]}>
                    KEY PROJECTS
                  </Text>
                  {projectsList.map((proj, idx) => (
                    <View key={proj.id} style={[styles.docProjectBlock, idx > 0 && { marginTop: 8 }]}>
                      <Text style={styles.docItemTitle}>
                        {proj.title}  <Text style={styles.docTechBracket}>[{proj.tech}]</Text>
                      </Text>
                      <Text style={styles.docBullet}>• {proj.desc}</Text>
                    </View>
                  ))}
                </View>

                {/* Experience */}
                {hasExperience && experienceList.length > 0 ? (
                  <View style={styles.docSection}>
                    <Text style={[styles.docSectionTitle, template === 'modern' && { color: Palette.primary }]}>
                      EXPERIENCE & INTERNSHIPS
                    </Text>
                    {experienceList.map((exp) => (
                      <View key={exp.id} style={{ marginBottom: 6 }}>
                        <View style={styles.docRowBetween}>
                          <Text style={styles.docItemTitle}>
                            {exp.role}  |  {exp.company}
                          </Text>
                          <Text style={styles.docItemDate}>{exp.duration}</Text>
                        </View>
                        <Text style={styles.docBullet}>• {exp.desc}</Text>
                      </View>
                    ))}
                  </View>
                ) : null}

                {/* Certifications & Honors */}
                {certificationsList.length > 0 ? (
                  <View style={styles.docSection}>
                    <Text style={[styles.docSectionTitle, template === 'modern' && { color: Palette.primary }]}>
                      CERTIFICATIONS & HONORS
                    </Text>
                    {certificationsList.map((cert) => (
                      <Text key={cert.id} style={styles.docBullet}>
                        • {cert.title}
                      </Text>
                    ))}
                  </View>
                ) : null}
              </View>
            </View>
          )}

          {/* ============================================================== */}
          {/* MODE 3: ATS VERIFICATION STUDIO (UPLOAD + VERIFY)              */}
          {/* ============================================================== */}
          {activeMode === 'ats' && (
            <View style={styles.atsContainer}>
              {/* Resume Source Selector */}
              <View style={styles.atsSourceTabsWrap}>
                <TouchableOpacity
                  style={[styles.atsSourceTab, atsSource === 'created' && styles.atsSourceTabActive]}
                  onPress={() => setAtsSource('created')}
                  activeOpacity={0.8}
                >
                  <Ionicons
                    name="document-text"
                    size={16}
                    color={atsSource === 'created' ? Palette.primary : Palette.textSecondary}
                  />
                  <Text style={[styles.atsSourceTabText, atsSource === 'created' && styles.atsSourceTabTextActive]}>
                    Created Resume (Builder Data)
                  </Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={[styles.atsSourceTab, atsSource === 'upload' && styles.atsSourceTabActive]}
                  onPress={() => {
                    setAtsSource('upload');
                    if (!uploadedFileName) openFilePicker();
                  }}
                  activeOpacity={0.8}
                >
                  <Feather
                    name="upload-cloud"
                    size={16}
                    color={atsSource === 'upload' ? Palette.primary : Palette.textSecondary}
                  />
                  <Text style={[styles.atsSourceTabText, atsSource === 'upload' && styles.atsSourceTabTextActive]}>
                    Upload Resume File
                  </Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={[styles.atsSourceTab, atsSource === 'paste' && styles.atsSourceTabActive]}
                  onPress={() => setAtsSource('paste')}
                  activeOpacity={0.8}
                >
                  <Feather
                    name="clipboard"
                    size={16}
                    color={atsSource === 'paste' ? Palette.primary : Palette.textSecondary}
                  />
                  <Text style={[styles.atsSourceTabText, atsSource === 'paste' && styles.atsSourceTabTextActive]}>
                    Paste Resume Text
                  </Text>
                </TouchableOpacity>
              </View>

              {/* Source 2: File Upload Dropzone */}
              {atsSource === 'upload' && (
                <View style={styles.uploadCard}>
                  <TouchableOpacity style={styles.dropzone} onPress={openFilePicker} activeOpacity={0.8}>
                    <View style={styles.dropzoneIconWrap}>
                      <Feather name="upload-cloud" size={28} color="#2563EB" />
                    </View>
                    <Text style={styles.dropzoneTitle}>
                      {uploadedFileName ? `Loaded: ${uploadedFileName}` : 'Click to Upload Resume (.pdf, .txt, .docx)'}
                    </Text>
                    <Text style={styles.dropzoneSub}>
                      {uploadedFileName
                        ? `File Size: ${uploadedFileSize} • Successfully extracted ${atsReport.wordCount} words`
                        : 'Accurately parses applicant tracking system keywords and formatting.'}
                    </Text>

                    <View style={styles.dropzoneActionBtn}>
                      <Feather name="folder" size={14} color="#FFFFFF" />
                      <Text style={styles.dropzoneActionBtnText}>
                        {uploadedFileName ? 'Choose Different File' : 'Browse Files'}
                      </Text>
                    </View>
                  </TouchableOpacity>
                </View>
              )}

              {/* Source 3: Paste Text Input */}
              {atsSource === 'paste' && (
                <View style={styles.pasteCard}>
                  <View style={styles.pasteTopRow}>
                    <Text style={styles.pasteTitle}>Paste Raw Resume Text</Text>
                    <View style={styles.sampleBtnsRow}>
                      <TouchableOpacity
                        style={styles.samplePill}
                        onPress={() => setPastedText(SAMPLE_TECH_RESUME)}
                      >
                        <Text style={styles.samplePillText}>Tech Sample</Text>
                      </TouchableOpacity>
                      <TouchableOpacity
                        style={styles.samplePill}
                        onPress={() => setPastedText(SAMPLE_FRESHER_RESUME)}
                      >
                        <Text style={styles.samplePillText}>Fresher Sample</Text>
                      </TouchableOpacity>
                      {pastedText.length > 0 && (
                        <TouchableOpacity style={styles.samplePillClear} onPress={() => setPastedText('')}>
                          <Text style={styles.samplePillClearText}>Clear</Text>
                        </TouchableOpacity>
                      )}
                    </View>
                  </View>
                  <TextInput
                    style={[styles.input, styles.pasteArea]}
                    multiline
                    value={pastedText}
                    placeholder="Paste the full text of your resume here (from PDF, Word, or LinkedIn)..."
                    placeholderTextColor="#94A3B8"
                    onChangeText={(t) => setPastedText(t)}
                  />
                  <Text style={styles.pasteWordCount}>{atsReport.wordCount} words analyzed in real-time</Text>
                </View>
              )}

              {/* ATS Score Hero Banner */}
              <View style={styles.atsHeroCard}>
                <View style={styles.atsScoreCircleWrap}>
                  <View
                    style={[
                      styles.atsScoreCircle,
                      { borderColor: atsReport.statusColor },
                    ]}
                  >
                    <Text style={[styles.atsScoreLargeText, { color: atsReport.statusColor }]}>
                      {atsReport.totalScore}
                    </Text>
                    <Text style={styles.atsScoreOutOf}>/ 100</Text>
                  </View>
                </View>

                <View style={styles.atsHeroInfoCol}>
                  <View style={styles.atsBadgeRow}>
                    <View style={[styles.atsStatusPill, { backgroundColor: atsReport.statusColor }]}>
                      <Text style={styles.atsStatusPillText}>Grade {atsReport.grade}</Text>
                    </View>
                    <View style={[styles.atsSourceIndicatorPill, { backgroundColor: atsReport.statusBg }]}>
                      <Text style={[styles.atsSourceIndicatorText, { color: atsReport.statusColor }]}>
                        Source: {atsSource === 'created' ? 'Created Resume' : atsSource === 'upload' ? 'Uploaded File' : 'Pasted Text'}
                      </Text>
                    </View>
                  </View>

                  <Text style={styles.atsHeroTitle}>{atsReport.statusText}</Text>
                  <Text style={styles.atsHeroSub}>
                    Evaluates candidate contact reachability, standard section hierarchy, target role keyword density,
                    quantifiable metrics, and action verb frequency.
                  </Text>
                </View>
              </View>

              {/* Target Role Selector */}
              <View style={styles.targetRoleCard}>
                <View style={styles.roleHeaderRow}>
                  <Text style={styles.targetRoleLabel}>Target Job Role:</Text>
                  <Text style={styles.roleSubNote}>Matching against {ROLE_KEYWORDS[targetRole]?.length || 0} essential tech keywords</Text>
                </View>
                <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.roleChipsScroll}>
                  {TARGET_ROLES.map((role) => {
                    const isSelected = targetRole === role;
                    return (
                      <TouchableOpacity
                        key={role}
                        style={[styles.roleChip, isSelected && styles.roleChipSelected]}
                        onPress={() => setTargetRole(role)}
                        activeOpacity={0.7}
                      >
                        <Text style={[styles.roleChipText, isSelected && styles.roleChipTextSelected]}>
                          {role}
                        </Text>
                      </TouchableOpacity>
                    );
                  })}
                </ScrollView>
              </View>

              {/* Optional Job Description Matcher Accordion */}
              <View style={styles.jdCard}>
                <TouchableOpacity
                  style={styles.jdToggleHeader}
                  onPress={() => setShowJdMatcher(!showJdMatcher)}
                  activeOpacity={0.8}
                >
                  <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                    <Feather name="crosshair" size={16} color="#2563EB" />
                    <Text style={styles.jdToggleTitle}>Target Job Description (JD) Keyword Matcher</Text>
                  </View>
                  <Feather name={showJdMatcher ? 'chevron-up' : 'chevron-down'} size={18} color="#64748B" />
                </TouchableOpacity>

                {showJdMatcher && (
                  <View style={styles.jdBody}>
                    <Text style={styles.jdSub}>
                      Paste a specific job opening description from LinkedIn or Indeed to calculate a direct match percentage:
                    </Text>
                    <TextInput
                      style={[styles.input, styles.jdInputArea]}
                      multiline
                      value={jobDescription}
                      placeholder="Paste job description requirements & responsibilities..."
                      placeholderTextColor="#94A3B8"
                      onChangeText={(t) => setJobDescription(t)}
                    />
                    {atsReport.jdScore !== null && (
                      <View style={styles.jdScoreBox}>
                        <Ionicons name="sparkles" size={16} color="#2563EB" />
                        <Text style={styles.jdScoreText}>
                          Tailored JD Match: <Text style={{ fontWeight: '800' }}>{atsReport.jdScore}%</Text> (Found{' '}
                          {atsReport.jdMatchedWordsCount} job keywords)
                        </Text>
                      </View>
                    )}
                  </View>
                )}
              </View>

              {/* 6-Pillar Detailed Score Breakdown */}
              <View style={styles.breakdownGrid}>
                {/* 1. Contact Info */}
                <View style={styles.breakdownCard}>
                  <View style={styles.breakdownCardTop}>
                    <Text style={styles.breakdownCardTitle}>1. Contact & Socials</Text>
                    <Text style={styles.breakdownCardScore}>{atsReport.contactScore} / 10</Text>
                  </View>
                  <Text style={styles.breakdownCardSub}>
                    {atsReport.contactScore >= 8
                      ? '✅ Email, phone, location & verified links parsed'
                      : '⚠️ Missing professional links or email'}
                  </Text>
                </View>

                {/* 2. Standard Structure */}
                <View style={styles.breakdownCard}>
                  <View style={styles.breakdownCardTop}>
                    <Text style={styles.breakdownCardTitle}>2. ATS Structure</Text>
                    <Text style={styles.breakdownCardScore}>{atsReport.structureScore} / 15</Text>
                  </View>
                  <Text style={styles.breakdownCardSub}>
                    {atsReport.structureScore >= 12
                      ? '✅ Education, Skills, Projects, and Experience valid'
                      : '⚠️ Include standard clear section headers'}
                  </Text>
                </View>

                {/* 3. Role Keywords */}
                <View style={styles.breakdownCard}>
                  <View style={styles.breakdownCardTop}>
                    <Text style={styles.breakdownCardTitle}>3. Role Keywords</Text>
                    <Text style={styles.breakdownCardScore}>{atsReport.keywordScore} / 30</Text>
                  </View>
                  <Text style={styles.breakdownCardSub}>
                    Matched {atsReport.matchedKeywords.length} of {ROLE_KEYWORDS[targetRole]?.length || 0} target role keywords.
                  </Text>
                </View>

                {/* 4. Quantifiable Metrics */}
                <View style={styles.breakdownCard}>
                  <View style={styles.breakdownCardTop}>
                    <Text style={styles.breakdownCardTitle}>4. Quantified Metrics</Text>
                    <Text style={styles.breakdownCardScore}>{atsReport.metricScore} / 20</Text>
                  </View>
                  <Text style={styles.breakdownCardSub}>
                    {atsReport.metricMatches >= 2
                      ? `✅ Found ${atsReport.metricMatches} numerical metrics (%, latency, throughput)`
                      : '⚠️ Add numbers or percentages (e.g., "reduced latency by 25%")'}
                  </Text>
                </View>

                {/* 5. Action Verbs */}
                <View style={styles.breakdownCard}>
                  <View style={styles.breakdownCardTop}>
                    <Text style={styles.breakdownCardTitle}>5. Action Verbs</Text>
                    <Text style={styles.breakdownCardScore}>{atsReport.verbScore} / 15</Text>
                  </View>
                  <Text style={styles.breakdownCardSub}>
                    Found {atsReport.matchedVerbs.length} high-impact technical verbs ({atsReport.matchedVerbs.slice(0, 3).join(', ')}...).
                  </Text>
                </View>

                {/* 6. Density Balance */}
                <View style={styles.breakdownCard}>
                  <View style={styles.breakdownCardTop}>
                    <Text style={styles.breakdownCardTitle}>6. Word Density</Text>
                    <Text style={styles.breakdownCardScore}>{atsReport.densityScore} / 10</Text>
                  </View>
                  <Text style={styles.breakdownCardSub}>
                    {atsReport.wordCount} words ({atsReport.densityScore === 10 ? 'Ideal 1-page density' : 'Keep between 350-800 words'}).
                  </Text>
                </View>
              </View>

              {/* Matched vs Missing Role Keywords */}
              <View style={styles.keywordsCard}>
                <View style={styles.keywordsCardTop}>
                  <Text style={styles.keywordsCardTitle}>
                    Technical Keyword Matrix ({atsReport.keywordScore} / 30 pts)
                  </Text>
                  <Text style={styles.keywordsRoleBadge}>{targetRole}</Text>
                </View>

                <Text style={styles.keywordGroupHeader}>✅ Matched in Resume ({atsReport.matchedKeywords.length}):</Text>
                <View style={styles.chipsWrap}>
                  {atsReport.matchedKeywords.length > 0 ? (
                    atsReport.matchedKeywords.map((k) => (
                      <View key={k} style={styles.matchedChip}>
                        <Text style={styles.matchedChipText}>✓ {k}</Text>
                      </View>
                    ))
                  ) : (
                    <Text style={styles.emptyNote}>No role-specific keywords detected yet.</Text>
                  )}
                </View>

                {atsReport.missingKeywords.length > 0 && (
                  <>
                    <View style={styles.missingHeaderRow}>
                      <Text style={[styles.keywordGroupHeader, { marginTop: 14 }]}>
                        💡 Recommended Missing Keywords (Tap to Add):
                      </Text>
                      <Text style={styles.missingHint}>Tap keyword to add to skills</Text>
                    </View>
                    <View style={styles.chipsWrap}>
                      {atsReport.missingKeywords.map((k) => (
                        <TouchableOpacity
                          key={k}
                          style={styles.missingChip}
                          onPress={() => handleAddKeywordToSkills(k)}
                          activeOpacity={0.7}
                        >
                          <Text style={styles.missingChipText}>+ {k}</Text>
                        </TouchableOpacity>
                      ))}
                    </View>
                  </>
                )}
              </View>

              {/* Automated Fix-It Checklist */}
              <View style={styles.diagnosticsCard}>
                <Text style={styles.diagnosticsTitle}>📋 Automated ATS Fix-It Diagnostics</Text>
                {atsReport.diagnostics.map((diag) => (
                  <View key={diag.id} style={styles.diagItem}>
                    <View
                      style={[
                        styles.diagIconWrap,
                        diag.passed ? styles.diagIconPassed : styles.diagIconWarning,
                      ]}
                    >
                      <Feather
                        name={diag.passed ? 'check' : 'alert-circle'}
                        size={14}
                        color={diag.passed ? '#10B981' : '#F59E0B'}
                      />
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.diagItemTitle}>{diag.title}</Text>
                      <Text style={styles.diagItemSub}>{diag.detail}</Text>
                    </View>
                  </View>
                ))}
              </View>

              {/* Recruiter Strategy Advice */}
              <View style={styles.adviceCard}>
                <Text style={styles.adviceTitle}>🎯 Recruiter Strategies for 98%+ Pass Rate</Text>
                <View style={styles.adviceRow}>
                  <Feather name="check-circle" size={15} color="#10B981" />
                  <Text style={styles.adviceText}>
                    Use the Google X-Y-Z formula for bullets: &quot;Accomplished [X], as measured by [Y], by doing [Z]&quot;.
                  </Text>
                </View>
                <View style={styles.adviceRow}>
                  <Feather name="check-circle" size={15} color="#10B981" />
                  <Text style={styles.adviceText}>
                    Avoid tables, complex multi-column layouts, and images which confuse Workday, Taleo, and Greenhouse parsers.
                  </Text>
                </View>
                <View style={styles.adviceRow}>
                  <Feather name="check-circle" size={15} color="#10B981" />
                  <Text style={styles.adviceText}>
                    Export as a clean PDF or plain text to guarantee that character encoding remains pristine across all systems.
                  </Text>
                </View>
              </View>
            </View>
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// ==========================================
// STYLES
// ==========================================

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: '#F8FAFC' },
  scrollContent: { paddingHorizontal: 16, paddingTop: 14, paddingBottom: 60 },
  container: { width: '100%' },
  containerDesktop: { maxWidth: 1040, alignSelf: 'center' },

  // Mode Switcher Tab Bar
  modeTabContainer: {
    flexDirection: 'row',
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
    paddingHorizontal: 16,
    paddingVertical: 8,
    gap: 8,
    zIndex: 10,
  },
  modeTabContainerDesktop: {
    maxWidth: 1040,
    width: '100%',
    alignSelf: 'center',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    marginTop: 10,
    marginBottom: 6,
  },
  modeTab: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 10,
    borderRadius: 10,
    backgroundColor: '#F8FAFC',
    gap: 6,
  },
  modeTabActive: {
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
  },
  modeTabActiveAts: {
    backgroundColor: '#ECFDF5',
    borderWidth: 1,
    borderColor: '#A7F3D0',
  },
  modeTabText: {
    fontSize: 13,
    fontWeight: '600',
    color: Palette.textSecondary,
  },
  modeTabTextActive: {
    color: Palette.primary,
    fontWeight: '700',
  },
  modeTabTextActiveAts: {
    color: '#059669',
    fontWeight: '700',
  },
  stepCountBadge: {
    backgroundColor: '#DBEAFE',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 8,
  },
  stepCountBadgeText: {
    fontSize: 10,
    fontWeight: '700',
    color: '#1D4ED8',
  },
  atsScoreBadgeMini: {
    backgroundColor: '#10B981',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 8,
  },
  atsScoreBadgeMiniText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#FFFFFF',
  },

  // Wizard Top Bar
  wizardTopRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 14,
    gap: 10,
  },
  stepScroll: {
    flexDirection: 'row',
    gap: 8,
    paddingRight: 8,
  },
  stepPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
    gap: 6,
  },
  stepPillCurrent: {
    backgroundColor: '#2563EB',
    borderColor: '#2563EB',
  },
  stepPillCompleted: {
    backgroundColor: '#F0FDF4',
    borderColor: '#BBF7D0',
  },
  stepNumText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#64748B',
  },
  stepNumTextCurrent: {
    color: '#FFFFFF',
  },
  stepNumTextCompleted: {
    color: '#16A34A',
  },
  stepLabelText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#334155',
  },
  stepLabelTextCurrent: {
    color: '#FFFFFF',
  },
  autofillBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F0F9FF',
    borderWidth: 1,
    borderColor: '#BAE6FD',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 20,
    gap: 4,
  },
  autofillText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#0284C7',
  },

  // Form Card
  formCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 20,
    marginBottom: 16,
    ...Shadows.card,
  },
  formHeaderRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 12,
    marginBottom: 16,
  },
  stepBadge: {
    width: 28,
    height: 28,
    borderRadius: 14,
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    alignItems: 'center',
    justifyContent: 'center',
  },
  stepBadgeText: {
    fontSize: 13,
    fontWeight: '800',
    color: '#2563EB',
  },
  formSectionTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  formSectionSub: {
    fontSize: 13,
    color: Palette.textSecondary,
    marginTop: 2,
    lineHeight: 18,
  },
  inputLabel: {
    fontSize: 11,
    fontWeight: '800',
    color: '#475569',
    letterSpacing: 0.5,
    marginTop: 12,
    marginBottom: 5,
  },
  labelWithQuickFill: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  labelSubText: {
    fontSize: 11,
    color: '#64748B',
  },
  input: {
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 10,
    paddingHorizontal: 14,
    paddingVertical: 10,
    fontSize: 14,
    color: Palette.textTitle,
  },
  textArea: {
    minHeight: 74,
    textAlignVertical: 'top',
    paddingTop: 10,
  },
  inputRow: {
    flexDirection: 'row',
    gap: 12,
  },

  // Inner Nested Cards (Projects, Education, Experience)
  innerCard: {
    backgroundColor: '#F8FAFC',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 14,
  },
  innerCardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  innerCardHeading: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1E293B',
  },
  deleteBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingHorizontal: 8,
    paddingVertical: 3,
    backgroundColor: '#FEF2F2',
    borderRadius: 6,
  },
  deleteBtnText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#EF4444',
  },
  addSectionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    borderStyle: 'dashed',
    borderRadius: 10,
    paddingVertical: 11,
    marginTop: 14,
    gap: 6,
  },
  addSectionBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#2563EB',
  },

  // Toggle Row
  toggleRow: {
    flexDirection: 'row',
    gap: 8,
    marginBottom: 14,
  },
  toggleBtn: {
    flex: 1,
    paddingVertical: 8,
    paddingHorizontal: 10,
    borderRadius: 8,
    backgroundColor: '#F1F5F9',
    alignItems: 'center',
  },
  toggleBtnActive: {
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
  },
  toggleBtnText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
  },
  toggleBtnTextActive: {
    color: '#2563EB',
    fontWeight: '700',
  },

  // Quick Keywords Box
  quickKeywordBox: {
    marginTop: 16,
    padding: 12,
    backgroundColor: '#F0FDF4',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#BBF7D0',
  },
  quickKeywordTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: '#166534',
    marginBottom: 8,
  },
  quickKeywordChip: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#86EFAC',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 14,
  },
  quickKeywordChipText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#15803D',
  },

  // Completion Callout
  completionCard: {
    flexDirection: 'row',
    backgroundColor: '#ECFDF5',
    borderWidth: 1,
    borderColor: '#A7F3D0',
    borderRadius: 12,
    padding: 14,
    marginTop: 16,
    gap: 12,
    alignItems: 'center',
  },
  completionIconCircle: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#D1FAE5',
    alignItems: 'center',
    justifyContent: 'center',
  },
  completionHeading: {
    fontSize: 15,
    fontWeight: '800',
    color: '#065F46',
  },
  completionSub: {
    fontSize: 12,
    color: '#047857',
    marginTop: 2,
    lineHeight: 16,
  },
  completionButtonsRow: {
    flexDirection: 'row',
    gap: 10,
    marginTop: 14,
  },
  completionVerifyBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#10B981',
    paddingVertical: 12,
    borderRadius: 10,
    gap: 6,
    ...Shadows.button,
  },
  completionVerifyBtnText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  completionPreviewBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    paddingVertical: 12,
    borderRadius: 10,
    gap: 6,
  },
  completionPreviewBtnText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#2563EB',
  },

  // Wizard Bottom Navigation
  wizardNavRow: {
    flexDirection: 'row',
    gap: 12,
    marginTop: 4,
    marginBottom: 40,
  },
  prevBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderRadius: 12,
    gap: 6,
  },
  prevBtnText: {
    fontSize: 14,
    fontWeight: '600',
    color: Palette.textTitle,
  },
  nextBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: Palette.primary,
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 12,
    gap: 8,
    ...Shadows.button,
  },
  nextBtnText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#FFFFFF',
  },

  // ==========================================
  // DOCUMENT PREVIEW STYLES
  // ==========================================
  previewContainer: {
    marginBottom: 50,
  },
  previewToolbar: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 12,
    marginBottom: 16,
    flexDirection: 'row',
    flexWrap: 'wrap',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 10,
  },
  templateOptions: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  toolbarLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: '#64748B',
    marginRight: 4,
  },
  templateBtn: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 8,
    backgroundColor: '#F1F5F9',
  },
  templateBtnActive: {
    backgroundColor: '#2563EB',
  },
  templateBtnText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
  },
  templateBtnTextActive: {
    color: '#FFFFFF',
  },
  toolbarActions: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  verifyAtsBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#ECFDF5',
    borderWidth: 1,
    borderColor: '#A7F3D0',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 8,
    gap: 5,
  },
  verifyAtsBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#059669',
  },
  copyTextBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 8,
    gap: 5,
  },
  copyTextBtnText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
  },
  downloadPrimaryBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.primary,
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 8,
    gap: 6,
    ...Shadows.button,
  },
  downloadPrimaryBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#FFFFFF',
  },

  // A4 Document Canvas
  a4Canvas: {
    backgroundColor: '#FFFFFF',
    borderRadius: 8,
    padding: 34,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Shadows.card,
    minHeight: 880,
  },
  canvasClassic: {
    borderColor: '#CBD5E1',
  },
  canvasMinimal: {
    borderColor: '#94A3B8',
  },
  docHeader: {
    alignItems: 'center',
    marginBottom: 10,
  },
  docName: {
    fontSize: 24,
    fontWeight: '800',
    color: '#0F172A',
    letterSpacing: 0.5,
  },
  docTitle: {
    fontSize: 13,
    fontWeight: '600',
    color: '#475569',
    marginTop: 2,
  },
  docContactLine: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 4,
  },
  docLinksLine: {
    fontSize: 12,
    color: '#2563EB',
    marginTop: 2,
    fontWeight: '600',
  },
  docSummaryBox: {
    marginTop: 8,
    marginBottom: 6,
  },
  docSummaryText: {
    fontSize: 12,
    color: '#334155',
    lineHeight: 17,
    textAlign: 'center',
  },
  docHr: {
    height: 2,
    backgroundColor: '#0F172A',
    marginVertical: 12,
  },
  docSection: {
    marginBottom: 14,
  },
  docSectionTitle: {
    fontSize: 13,
    fontWeight: '800',
    color: '#0F172A',
    letterSpacing: 0.8,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
    paddingBottom: 4,
    marginBottom: 8,
  },
  docRowBetween: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  docItemTitle: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1E293B',
  },
  docItemDate: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
  },
  docItemSub: {
    fontSize: 12,
    color: '#475569',
    marginTop: 1,
  },
  docSkillLine: {
    fontSize: 12,
    color: '#334155',
    lineHeight: 18,
    marginBottom: 3,
  },
  docSkillCategory: {
    fontWeight: '700',
    color: '#0F172A',
  },
  docProjectBlock: {
    marginBottom: 6,
  },
  docTechBracket: {
    fontSize: 11,
    fontWeight: '600',
    color: '#2563EB',
  },
  docBullet: {
    fontSize: 12,
    color: '#334155',
    lineHeight: 17,
    marginTop: 2,
  },

  // ==========================================
  // ATS VERIFICATION STUDIO STYLES
  // ==========================================
  atsContainer: {
    marginBottom: 50,
  },
  atsSourceTabsWrap: {
    flexDirection: 'row',
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 4,
    marginBottom: 14,
    gap: 4,
  },
  atsSourceTab: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 9,
    borderRadius: 8,
    gap: 6,
  },
  atsSourceTabActive: {
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
  },
  atsSourceTabText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
  },
  atsSourceTabTextActive: {
    color: '#2563EB',
    fontWeight: '700',
  },

  // Upload Card
  uploadCard: {
    marginBottom: 14,
  },
  dropzone: {
    backgroundColor: '#FFFFFF',
    borderWidth: 2,
    borderColor: '#BFDBFE',
    borderStyle: 'dashed',
    borderRadius: 16,
    padding: 24,
    alignItems: 'center',
    justifyContent: 'center',
  },
  dropzoneIconWrap: {
    width: 54,
    height: 54,
    borderRadius: 27,
    backgroundColor: '#EFF6FF',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 10,
  },
  dropzoneTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: '#1E293B',
    textAlign: 'center',
  },
  dropzoneSub: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 4,
    textAlign: 'center',
  },
  dropzoneActionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#2563EB',
    paddingHorizontal: 16,
    paddingVertical: 9,
    borderRadius: 10,
    marginTop: 14,
    gap: 6,
  },
  dropzoneActionBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#FFFFFF',
  },

  // Paste Card
  pasteCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 16,
    marginBottom: 14,
  },
  pasteTopRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  pasteTitle: {
    fontSize: 14,
    fontWeight: '700',
    color: '#1E293B',
  },
  sampleBtnsRow: {
    flexDirection: 'row',
    gap: 6,
  },
  samplePill: {
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  samplePillText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#2563EB',
  },
  samplePillClear: {
    backgroundColor: '#FEF2F2',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  samplePillClearText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#EF4444',
  },
  pasteArea: {
    minHeight: 120,
    textAlignVertical: 'top',
  },
  pasteWordCount: {
    fontSize: 11,
    color: '#64748B',
    marginTop: 6,
    textAlign: 'right',
  },

  // ATS Hero Card
  atsHeroCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 18,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 22,
    marginBottom: 14,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 20,
    ...Shadows.card,
  },
  atsScoreCircleWrap: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  atsScoreCircle: {
    width: 106,
    height: 106,
    borderRadius: 53,
    borderWidth: 6,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFFFFF',
  },
  atsScoreLargeText: {
    fontSize: 34,
    fontWeight: '900',
    lineHeight: 38,
  },
  atsScoreOutOf: {
    fontSize: 12,
    fontWeight: '700',
    color: '#64748B',
    marginTop: -2,
  },
  atsHeroInfoCol: {
    flex: 1,
  },
  atsBadgeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 6,
    flexWrap: 'wrap',
  },
  atsStatusPill: {
    paddingHorizontal: 10,
    paddingVertical: 3,
    borderRadius: 12,
  },
  atsStatusPillText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#FFFFFF',
    letterSpacing: 0.3,
  },
  atsSourceIndicatorPill: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 10,
  },
  atsSourceIndicatorText: {
    fontSize: 11,
    fontWeight: '700',
  },
  atsHeroTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: '#0F172A',
    lineHeight: 22,
  },
  atsHeroSub: {
    fontSize: 12,
    color: Palette.textSecondary,
    marginTop: 4,
    lineHeight: 17,
  },

  // Target Role Selector Card
  targetRoleCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 14,
    marginBottom: 14,
  },
  roleHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  targetRoleLabel: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1E293B',
  },
  roleSubNote: {
    fontSize: 11,
    color: '#64748B',
  },
  roleChipsScroll: {
    flexDirection: 'row',
    gap: 8,
  },
  roleChip: {
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
  },
  roleChipSelected: {
    backgroundColor: '#2563EB',
    borderColor: '#2563EB',
  },
  roleChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
  },
  roleChipTextSelected: {
    color: '#FFFFFF',
    fontWeight: '700',
  },

  // Job Description Matcher Card
  jdCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    marginBottom: 14,
    overflow: 'hidden',
  },
  jdToggleHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 14,
    backgroundColor: '#F8FAFC',
  },
  jdToggleTitle: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1E293B',
  },
  jdBody: {
    padding: 14,
    borderTopWidth: 1,
    borderTopColor: '#E2E8F0',
  },
  jdSub: {
    fontSize: 12,
    color: '#64748B',
    marginBottom: 8,
  },
  jdInputArea: {
    minHeight: 80,
    textAlignVertical: 'top',
  },
  jdScoreBox: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    borderRadius: 8,
    padding: 10,
    marginTop: 10,
    gap: 8,
  },
  jdScoreText: {
    fontSize: 12,
    color: '#1E3A8A',
  },

  // 6-Pillar Breakdown Grid
  breakdownGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
    marginBottom: 14,
  },
  breakdownCard: {
    flex: 1,
    minWidth: 155,
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 12,
  },
  breakdownCardTop: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 4,
  },
  breakdownCardTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: '#1E293B',
  },
  breakdownCardScore: {
    fontSize: 12,
    fontWeight: '800',
    color: '#2563EB',
  },
  breakdownCardSub: {
    fontSize: 11,
    color: '#64748B',
    lineHeight: 15,
  },

  // Keywords Analysis Card
  keywordsCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 16,
    marginBottom: 14,
  },
  keywordsCardTop: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  keywordsCardTitle: {
    fontSize: 14,
    fontWeight: '800',
    color: '#0F172A',
  },
  keywordsRoleBadge: {
    fontSize: 11,
    fontWeight: '700',
    color: '#2563EB',
    backgroundColor: '#EFF6FF',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
  },
  keywordGroupHeader: {
    fontSize: 12,
    fontWeight: '700',
    color: '#334155',
    marginBottom: 6,
  },
  missingHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  missingHint: {
    fontSize: 11,
    color: '#64748B',
    marginTop: 12,
  },
  chipsWrap: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
  },
  matchedChip: {
    backgroundColor: '#F0FDF4',
    borderWidth: 1,
    borderColor: '#86EFAC',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  matchedChipText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#15803D',
  },
  missingChip: {
    backgroundColor: '#FFFBEB',
    borderWidth: 1,
    borderColor: '#FDE68A',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  missingChipText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#B45309',
  },
  emptyNote: {
    fontSize: 12,
    color: '#94A3B8',
    fontStyle: 'italic',
  },

  // Diagnostics Checklist Card
  diagnosticsCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 16,
    marginBottom: 14,
  },
  diagnosticsTitle: {
    fontSize: 14,
    fontWeight: '800',
    color: '#0F172A',
    marginBottom: 12,
  },
  diagItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 10,
    marginBottom: 10,
  },
  diagIconWrap: {
    width: 22,
    height: 22,
    borderRadius: 11,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 1,
  },
  diagIconPassed: {
    backgroundColor: '#DCFCE7',
  },
  diagIconWarning: {
    backgroundColor: '#FEF3C7',
  },
  diagItemTitle: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1E293B',
  },
  diagItemSub: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 1,
  },

  // Advice Card
  adviceCard: {
    backgroundColor: '#F8FAFC',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 16,
  },
  adviceTitle: {
    fontSize: 13,
    fontWeight: '800',
    color: '#0F172A',
    marginBottom: 8,
  },
  adviceRow: {
    flexDirection: 'row',
    gap: 8,
    marginTop: 6,
    alignItems: 'flex-start',
  },
  adviceText: {
    flex: 1,
    fontSize: 12,
    color: '#475569',
    lineHeight: 17,
  },
});
