import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  Alert,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { NotificationBellButton } from '../components/CollegeNotificationsModal';
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';
import { CollegeAnnouncement, FacultyMember } from '../data/collegeData';
import {
  CommunityContentItem,
  CommunityContentType,
  FacultyInterview,
  FacultyNote,
  FacultyQuiz,
  FacultyVideo,
} from '../data/curriculumSchema';
import { CollegeStore } from '../services/collegeStore';
import { FacultySystemStore } from '../services/facultyStore';

export default function MyCollegeScreen() {
  const { profile } = useAuth();
  // Main Tab Switcher: 'my-college' vs 'community'
  const [mainScope, setMainScope] = useState<'my-college' | 'community'>('my-college');

  // Sub-tabs for My College
  const [activeTab, setActiveTab] = useState<'workspace' | 'faculty' | 'performance'>('workspace');

  // State for My College
  const [announcements, setAnnouncements] = useState<CollegeAnnouncement[]>([]);
  const [facultyMembers, setFacultyMembers] = useState<FacultyMember[]>([]);
  const [facultyNotes, setFacultyNotes] = useState<FacultyNote[]>([]);
  const [facultyVideos, setFacultyVideos] = useState<FacultyVideo[]>([]);
  const [facultyQuizzes, setFacultyQuizzes] = useState<FacultyQuiz[]>([]);
  const [interviews, setInterviews] = useState<FacultyInterview[]>([]);

  // State & Filters for SkillExa Community
  const [communityItems, setCommunityItems] = useState<CommunityContentItem[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<'all' | 'engineering' | 'competitive' | 'programming' | 'dsa'>('all');
  const [selectedContentType, setSelectedContentType] = useState<CommunityContentType>('all');
  const [selectedSubject, setSelectedSubject] = useState<string>('all');
  const [selectedLanguage, setSelectedLanguage] = useState<string>('all');

  useEffect(() => {
    // Load targeted content for this student
    const loadContent = () => {
      // My College items (only targeted to this student's college)
      setAnnouncements(CollegeStore.getAnnouncements(profile));
      setFacultyMembers(CollegeStore.getFacultyMembers(profile.collegeId, profile.department));
      setFacultyNotes(FacultySystemStore.getNotes().filter((n) => n.visibility !== 'community'));
      setFacultyVideos(FacultySystemStore.getVideos().filter((v) => v.visibility !== 'community'));
      setFacultyQuizzes(FacultySystemStore.getQuizzes().filter((q) => q.visibility !== 'community'));
      setInterviews(FacultySystemStore.getInterviews());

      // Community items (public across all colleges from verified educators)
      setCommunityItems(
        FacultySystemStore.getCommunityContent({
          searchQuery,
          category: selectedCategory,
          contentType: selectedContentType,
          subject: selectedSubject === 'all' ? undefined : selectedSubject,
          language: selectedLanguage === 'all' ? undefined : selectedLanguage,
        })
      );
    };

    loadContent();
    const unsub1 = CollegeStore.subscribe(loadContent);
    const unsub2 = FacultySystemStore.subscribe(loadContent);
    return () => {
      unsub1();
      unsub2();
    };
  }, [profile, searchQuery, selectedCategory, selectedContentType, selectedSubject, selectedLanguage]);

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        title={mainScope === 'my-college' ? 'My College' : 'SkillExa Community'}
        subtitle={mainScope === 'my-college' ? profile.collegeName || 'KVG College of Engineering' : 'Discover Public Educator Content'}
        rightAction={<NotificationBellButton />}
      />

      {/* 🌍 MAIN TOP-LEVEL SCOPE SWITCHER: 🏫 My College vs 🌍 SkillExa Community */}
      <View style={styles.scopeSwitcherContainer}>
        <TouchableOpacity
          style={[styles.scopeBtn, mainScope === 'my-college' && styles.scopeBtnActive]}
          onPress={() => setMainScope('my-college')}
          activeOpacity={0.85}
        >
          <Feather
            name="home"
            size={15}
            color={mainScope === 'my-college' ? Palette.primary : Palette.textSecondary}
          />
          <Text
            style={[
              styles.scopeBtnText,
              mainScope === 'my-college' && styles.scopeBtnTextActive,
            ]}
          >
            🏫 My College
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.scopeBtn, mainScope === 'community' && styles.scopeBtnCommunityActive]}
          onPress={() => setMainScope('community')}
          activeOpacity={0.85}
        >
          <Feather
            name="globe"
            size={15}
            color={mainScope === 'community' ? Palette.aiPurple : Palette.textSecondary}
          />
          <Text
            style={[
              styles.scopeBtnText,
              mainScope === 'community' && styles.scopeBtnTextCommunityActive,
            ]}
          >
            🌍 Community
          </Text>
          <View style={styles.newPill}>
            <Text style={styles.newPillText}>DISCOVER</Text>
          </View>
        </TouchableOpacity>
      </View>

      {/* ========================================================================= */}
      {/* 🏫 MY COLLEGE VIEW                                                         */}
      {/* ========================================================================= */}
      {mainScope === 'my-college' && (
        <>
          {/* College Identity Banner */}
          <View style={styles.identityCard}>
            <View style={styles.identityTop}>
              <View style={styles.collegeIconBox}>
                <Feather name="book-open" size={24} color={Palette.primary} />
              </View>
              <View style={{ flex: 1 }}>
                <View style={styles.badgeRow}>
                  <View style={styles.verifiedBadge}>
                    <Feather name="check-circle" size={11} color={Palette.success} />
                    <Text style={styles.verifiedText}>OFFICIAL WORKSPACE</Text>
                  </View>
                  <Text style={styles.batchTag}>Batch 2024-2028</Text>
                </View>

                <Text style={styles.collegeName}>{profile.collegeName || 'KVG College of Engineering'}</Text>
                <Text style={styles.classDetails}>
                  {profile.department || 'ECE'} Department • {profile.academicYear || '3rd Year'} • Section {profile.section || 'A'}
                </Text>
              </View>
            </View>
          </View>

          {/* Navigation Sub-Tabs */}
          <View style={styles.tabsRow}>
            <TouchableOpacity
              style={[styles.tabItem, activeTab === 'workspace' && styles.tabItemActive]}
              onPress={() => setActiveTab('workspace')}
            >
              <Feather name="grid" size={14} color={activeTab === 'workspace' ? Palette.primary : Palette.textSecondary} />
              <Text style={[styles.tabItemText, activeTab === 'workspace' && styles.tabItemTextActive]}>
                Workspace
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.tabItem, activeTab === 'faculty' && styles.tabItemActive]}
              onPress={() => setActiveTab('faculty')}
            >
              <Feather name="users" size={14} color={activeTab === 'faculty' ? Palette.primary : Palette.textSecondary} />
              <Text style={[styles.tabItemText, activeTab === 'faculty' && styles.tabItemTextActive]}>
                Faculty ({facultyMembers.length})
              </Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={[styles.tabItem, activeTab === 'performance' && styles.tabItemActive]}
              onPress={() => setActiveTab('performance')}
            >
              <Feather name="award" size={14} color={activeTab === 'performance' ? Palette.primary : Palette.textSecondary} />
              <Text style={[styles.tabItemText, activeTab === 'performance' && styles.tabItemTextActive]}>
                My Standing
              </Text>
            </TouchableOpacity>
          </View>

          <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
            {activeTab === 'workspace' && (
              <View style={styles.workspaceContainer}>
                {/* 1. 📢 ANNOUNCEMENTS FEED */}
                <View style={styles.sectionHeaderRow}>
                  <View style={styles.sectionTitleRow}>
                    <Feather name="volume-2" size={18} color={Palette.primary} />
                    <Text style={styles.sectionTitle}>Department Announcements</Text>
                  </View>
                  <Text style={styles.sectionCount}>{announcements.length} Notices</Text>
                </View>

                <View style={styles.announcementsList}>
                  {announcements.map((ann) => (
                    <View
                      key={ann.id}
                      style={[
                        styles.announcementCard,
                        ann.priority === 'HIGH' || ann.priority === 'URGENT' ? styles.announcementCardUrgent : null,
                      ]}
                    >
                      <View style={styles.annTopRow}>
                        <View style={styles.annBadge}>
                          <Text style={styles.annBadgeText}>
                            {ann.priority === 'URGENT' ? '🚨 URGENT' : ann.isPinned ? '📌 PINNED' : '📢 NOTICE'}
                          </Text>
                        </View>
                        <Text style={styles.annDate}>{ann.createdAt}</Text>
                      </View>

                      <Text style={styles.annTitle}>{ann.title}</Text>
                      <Text style={styles.annContent}>{ann.content}</Text>
                      <Text style={styles.annAuthor}>By {ann.facultyName} • {ann.facultyDept}</Text>
                    </View>
                  ))}
                </View>

                {/* 2. 📝 ACTIVE FACULTY QUIZZES */}
                <View style={[styles.sectionHeaderRow, { marginTop: 20 }]}>
                  <View style={styles.sectionTitleRow}>
                    <Feather name="check-circle" size={18} color={Palette.success} />
                    <Text style={styles.sectionTitle}>Active Faculty Quizzes</Text>
                  </View>
                </View>

                <View style={styles.cardsGrid}>
                  {facultyQuizzes.map((q) => (
                    <View key={q.id} style={styles.quizCard}>
                      <View style={styles.quizTop}>
                        <View style={styles.tag}>
                          <Text style={styles.tagText}>{q.subject} • {q.topic}</Text>
                        </View>
                        <Text style={styles.quizMeta}>{q.durationMinutes} Mins • {q.totalMarks} Marks</Text>
                      </View>

                      <Text style={styles.quizTitle}>{q.quizName}</Text>
                      <Text style={styles.quizDesc}>{q.description}</Text>

                      <TouchableOpacity
                        style={styles.startQuizBtn}
                        onPress={() =>
                          router.push({
                            pathname: '/quizzpage',
                            params: {
                              topic: q.topic,
                              subject: q.subject,
                              section: q.section,
                            },
                          })
                        }
                        activeOpacity={0.85}
                      >
                        <Text style={styles.startQuizBtnText}>Start Quiz Assessment</Text>
                        <Feather name="arrow-right" size={14} color="#FFFFFF" />
                      </TouchableOpacity>
                    </View>
                  ))}
                </View>

                {/* 3. 📚 FACULTY NOTES & PDFS */}
                <View style={[styles.sectionHeaderRow, { marginTop: 20 }]}>
                  <View style={styles.sectionTitleRow}>
                    <Feather name="file-text" size={18} color={Palette.primary} />
                    <Text style={styles.sectionTitle}>Faculty Notes & PDF Guides</Text>
                  </View>
                </View>

                <View style={styles.notesGrid}>
                  {facultyNotes.map((fn) => (
                    <TouchableOpacity
                      key={fn.id}
                      style={styles.noteCard}
                      onPress={() =>
                        router.push({
                          pathname: '/topic-learning',
                          params: {
                            topic: fn.topic,
                            subject: fn.subject,
                            section: fn.section,
                          },
                        })
                      }
                      activeOpacity={0.8}
                    >
                      <View style={styles.noteCardTop}>
                        <View style={styles.noteTag}>
                          <Text style={styles.noteTagText}>📚 {fn.subject}</Text>
                        </View>
                        <Text style={styles.noteDate}>Verified</Text>
                      </View>

                      <Text style={styles.noteTitle}>{fn.title}</Text>
                      <Text style={styles.noteIntro} numberOfLines={2}>{fn.introduction || fn.theory}</Text>

                      <View style={styles.noteFooter}>
                        <Text style={styles.noteAuthorText}>By {fn.facultyName}</Text>
                        <Feather name="arrow-right" size={14} color={Palette.primary} />
                      </View>
                    </TouchableOpacity>
                  ))}
                </View>

                {/* 4. 🎥 FACULTY VIDEO LECTURES */}
                <View style={[styles.sectionHeaderRow, { marginTop: 20 }]}>
                  <View style={styles.sectionTitleRow}>
                    <Feather name="film" size={18} color={Palette.aiPurple} />
                    <Text style={styles.sectionTitle}>Department Video Lectures</Text>
                  </View>
                </View>

                <View style={styles.videosGrid}>
                  {facultyVideos.map((v) => (
                    <View key={v.id} style={styles.videoCard}>
                      <View style={styles.videoHeader}>
                        <View style={styles.vBadge}>
                          <Text style={styles.vBadgeText}>🎥 {v.duration || '18 mins'}</Text>
                        </View>
                        <Text style={styles.vAuthor}>By {v.facultyName}</Text>
                      </View>

                      <Text style={styles.vTitle}>{v.title}</Text>
                      <Text style={styles.vDesc} numberOfLines={2}>{v.description}</Text>

                      <TouchableOpacity
                        style={styles.watchLectureBtn}
                        onPress={() => Alert.alert('Streaming Lecture', `Playing video: ${v.title}`)}
                      >
                        <Feather name="play" size={14} color="#FFFFFF" />
                        <Text style={styles.watchLectureText}>Watch Lecture Video</Text>
                      </TouchableOpacity>
                    </View>
                  ))}
                </View>

                {/* 5. 🎤 INTERVIEW INVITATIONS */}
                <View style={[styles.sectionHeaderRow, { marginTop: 20 }]}>
                  <View style={styles.sectionTitleRow}>
                    <Feather name="video" size={18} color={Palette.danger} />
                    <Text style={styles.sectionTitle}>Viva & Placement Interviews</Text>
                  </View>
                </View>

                <View style={styles.interviewsGrid}>
                  {interviews.map((item) => (
                    <View key={item.id} style={styles.interviewCard}>
                      <View style={styles.intTop}>
                        <Text style={styles.intType}>{item.interviewType}</Text>
                        <View style={styles.statusPill}>
                          <Text style={styles.statusText}>{item.status}</Text>
                        </View>
                      </View>

                      <Text style={styles.intRole}>{item.subjectOrRole}</Text>
                      <Text style={styles.intSchedule}>🕒 {item.scheduledTime} • Examiner: {item.facultyName}</Text>

                      <TouchableOpacity
                        style={styles.joinCallBtn}
                        onPress={() =>
                          router.push({
                            pathname: '/faculty/live-interview',
                            params: {
                              studentName: profile.name,
                              role: item.subjectOrRole,
                              interviewType: item.interviewType,
                            },
                          })
                        }
                      >
                        <Feather name="video" size={14} color="#FFFFFF" />
                        <Text style={styles.joinCallText}>Join Live Video Interview</Text>
                      </TouchableOpacity>
                    </View>
                  ))}
                </View>
              </View>
            )}

            {/* FACULTY DIRECTORY TAB */}
            {activeTab === 'faculty' && (
              <View style={styles.facultyTabContainer}>
                <View style={styles.dirBanner}>
                  <Text style={styles.dirBannerTitle}>Department Faculty Directory</Text>
                  <Text style={styles.dirBannerDesc}>
                    Contact verified educators in the {profile.department || 'ECE'} Department for academic queries and mentoring.
                  </Text>
                </View>

                <View style={styles.facultyList}>
                  {facultyMembers.map((fac) => (
                    <View key={fac.id} style={styles.facCard}>
                      <View style={styles.facHeader}>
                        <View style={styles.facAvatar}>
                          <Text style={styles.facAvatarLetter}>{fac.avatarLetter || fac.name.charAt(0)}</Text>
                        </View>

                        <View style={{ flex: 1 }}>
                          <Text style={styles.facName}>{fac.name}</Text>
                          <Text style={styles.facDesignation}>{fac.designation}</Text>
                          <Text style={styles.facDept}>{fac.collegeName} • {fac.department} Dept</Text>
                        </View>
                      </View>

                      {/* Subjects */}
                      <View style={styles.subjectsBox}>
                        <Text style={styles.subjectsLabel}>SUBJECTS TAUGHT:</Text>
                        <View style={styles.subjectChipsRow}>
                          {fac.subjectsTaught.map((sub, i) => (
                            <View key={i} style={styles.subjectChip}>
                              <Text style={styles.subjectChipText}>{sub}</Text>
                            </View>
                          ))}
                        </View>
                      </View>

                      {fac.officeRoom && (
                        <Text style={styles.officeText}>📍 Office: {fac.officeRoom}</Text>
                      )}

                      <TouchableOpacity
                        style={styles.askDoubtBtn}
                        onPress={() => Alert.alert('Ask Doubt', `Message channel opened with ${fac.name}.`)}
                      >
                        <Feather name="message-square" size={14} color={Palette.primary} />
                        <Text style={styles.askDoubtText}>Ask Question / Academic Query</Text>
                      </TouchableOpacity>
                    </View>
                  ))}
                </View>
              </View>
            )}

            {/* PERFORMANCE & CLASS STANDING TAB */}
            {activeTab === 'performance' && (
              <View style={styles.perfTabContainer}>
                <View style={styles.standingCard}>
                  <View style={styles.rankBadge}>
                    <Feather name="award" size={20} color={Palette.warning} />
                    <Text style={styles.rankNum}>#4</Text>
                  </View>
                  <View style={{ flex: 1 }}>
                    <Text style={styles.standingTitle}>Section A Class Standing</Text>
                    <Text style={styles.standingSubtitle}>Top 8% in ECE 3rd Year • KVGCE</Text>
                  </View>
                </View>

                <View style={styles.statsRowGrid}>
                  <View style={styles.pStatBox}>
                    <Text style={styles.pStatVal}>86%</Text>
                    <Text style={styles.pStatLabel}>Quiz Accuracy</Text>
                  </View>
                  <View style={styles.pStatBox}>
                    <Text style={[styles.pStatVal, { color: Palette.success }]}>18</Text>
                    <Text style={styles.pStatLabel}>Notes Read</Text>
                  </View>
                  <View style={styles.pStatBox}>
                    <Text style={[styles.pStatVal, { color: Palette.aiPurple }]}>45</Text>
                    <Text style={styles.pStatLabel}>Coding Solved</Text>
                  </View>
                </View>

                {/* Topic Progress */}
                <View style={styles.topicCard}>
                  <Text style={styles.topicCardTitle}>Department Curriculum Progress</Text>

                  <View style={styles.progressItem}>
                    <View style={styles.pMetaRow}>
                      <Text style={styles.pSubj}>Embedded Systems • Microcontrollers</Text>
                      <Text style={styles.pPct}>74%</Text>
                    </View>
                    <ProgressBar progress={0.74} color={Palette.primary} />
                  </View>

                  <View style={styles.progressItem}>
                    <View style={styles.pMetaRow}>
                      <Text style={styles.pSubj}>Programming in C • Pointers & Memory</Text>
                      <Text style={styles.pPct}>62%</Text>
                    </View>
                    <ProgressBar progress={0.62} color={Palette.warning} />
                  </View>

                  <View style={styles.progressItem}>
                    <View style={styles.pMetaRow}>
                      <Text style={styles.pSubj}>Python Programming • Lists & Data Structures</Text>
                      <Text style={styles.pPct}>85%</Text>
                    </View>
                    <ProgressBar progress={0.85} color={Palette.success} />
                  </View>
                </View>
              </View>
            )}
          </ScrollView>
        </>
      )}

      {/* ========================================================================= */}
      {/* 🌍 SKILLEXA COMMUNITY VIEW                                                */}
      {/* ========================================================================= */}
      {mainScope === 'community' && (
        <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
          {/* Community Header Banner */}
          <View style={styles.communityHeroBanner}>
            <View style={styles.commHeroTop}>
              <View style={styles.commHeroIcon}>
                <Feather name="globe" size={24} color={Palette.aiPurple} />
              </View>
              <View style={{ flex: 1 }}>
                <View style={styles.verifiedRow}>
                  <Feather name="check-circle" size={12} color={Palette.success} />
                  <Text style={styles.commVerifiedText}>VERIFIED INTER-COLLEGE NETWORK</Text>
                </View>
                <Text style={styles.commHeroTitle}>SkillExa Community Faculty Content</Text>
                <Text style={styles.commHeroSubtitle}>
                  Explore topic-specific notes, quizzes, and videos published by verified professors across top institutions (RVCE, BMSCE, NITK, IIT, DIT).
                </Text>
              </View>
            </View>
          </View>

          {/* Search Box */}
          <View style={styles.commSearchBox}>
            <Feather name="search" size={16} color={Palette.textSecondary} />
            <TextInput
              style={styles.commSearchInput}
              placeholder="Search topic, subject, faculty or college..."
              placeholderTextColor={Palette.textMuted}
              value={searchQuery}
              onChangeText={setSearchQuery}
            />
            {searchQuery ? (
              <TouchableOpacity onPress={() => setSearchQuery('')}>
                <Feather name="x" size={16} color={Palette.textMuted} />
              </TouchableOpacity>
            ) : null}
          </View>

          {/* 1. Category Filter Chips */}
          <View style={styles.filterSection}>
            <Text style={styles.filterSectionTitle}>LEARNING TRACK</Text>
            <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipsScroll}>
              {[
                { id: 'all', label: 'All Tracks' },
                { id: 'engineering', label: '⚙️ Engineering' },
                { id: 'competitive', label: '🎯 Competitive Exams' },
                { id: 'programming', label: '💻 Programming' },
                { id: 'dsa', label: '🌳 DSA Mastery' },
              ].map((c) => (
                <TouchableOpacity
                  key={c.id}
                  style={[styles.filterChip, selectedCategory === c.id && styles.filterChipActive]}
                  onPress={() => setSelectedCategory(c.id as any)}
                >
                  <Text style={[styles.filterChipText, selectedCategory === c.id && styles.filterChipTextActive]}>
                    {c.label}
                  </Text>
                </TouchableOpacity>
              ))}
            </ScrollView>
          </View>

          {/* 2. Content Type Filter Chips */}
          <View style={[styles.filterSection, { marginTop: 10 }]}>
            <Text style={styles.filterSectionTitle}>CONTENT TYPE</Text>
            <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipsScroll}>
              {[
                { id: 'all', label: 'All Types' },
                { id: 'notes', label: '📚 Topic Notes' },
                { id: 'pdf', label: '📄 PDF Guides' },
                { id: 'quiz', label: '📝 Quizzes' },
                { id: 'video', label: '🎥 Video Lectures' },
              ].map((t) => (
                <TouchableOpacity
                  key={t.id}
                  style={[styles.filterChip, selectedContentType === t.id && styles.filterChipActive]}
                  onPress={() => setSelectedContentType(t.id as any)}
                >
                  <Text style={[styles.filterChipText, selectedContentType === t.id && styles.filterChipTextActive]}>
                    {t.label}
                  </Text>
                </TouchableOpacity>
              ))}
            </ScrollView>
          </View>

          {/* Community Content Count */}
          <View style={styles.commResultsHeader}>
            <Text style={styles.commResultsTitle}>
              Discoverable Community Content ({communityItems.length})
            </Text>
            <Text style={styles.commResultsSub}>Verified Educator Publications</Text>
          </View>

          {/* 🌍 Community Cards List */}
          <View style={styles.communityCardsList}>
            {communityItems.map((item) => (
              <View key={item.id} style={styles.commCard}>
                {/* Header with Type & Date */}
                <View style={styles.commCardHeader}>
                  <View style={styles.commTypeBadge}>
                    <Text style={styles.commTypeBadgeText}>
                      {item.type === 'note' && '📚 NOTES'}
                      {item.type === 'pdf' && '📄 PDF GUIDE'}
                      {item.type === 'quiz' && '📝 QUIZ ASSESSMENT'}
                      {item.type === 'video' && '🎥 VIDEO LECTURE'}
                    </Text>
                  </View>

                  <Text style={styles.commDateText}>📅 {item.publishedDate}</Text>
                </View>

                {/* 📚 Content Title */}
                <Text style={styles.commTitle}>{item.title}</Text>

                {/* 📖 Subject & 📌 Topic */}
                <View style={styles.commMetaRow}>
                  <View style={styles.commSubjectTag}>
                    <Text style={styles.commSubjectTagText}>📖 {item.subject}</Text>
                  </View>
                  <View style={styles.commTopicTag}>
                    <Text style={styles.commTopicTagText}>📌 {item.topic}</Text>
                  </View>
                </View>

                {/* Summary / Highlights */}
                {item.summary ? (
                  <Text style={styles.commSummary} numberOfLines={2}>
                    {item.summary}
                  </Text>
                ) : null}

                {/* 👨‍🏫 Faculty Name, ✓ Verified Badge, 🏫 College Name */}
                <View style={styles.commAuthorBox}>
                  <View style={styles.commAuthorAvatar}>
                    <Text style={styles.commAvatarLetter}>{item.facultyName.charAt(0)}</Text>
                  </View>
                  <View style={{ flex: 1 }}>
                    <View style={styles.commFacultyNameRow}>
                      <Text style={styles.commFacultyName}>👨‍🏫 {item.facultyName}</Text>
                      {item.isVerified && (
                        <View style={styles.commVerifiedPill}>
                          <Feather name="check" size={10} color={Palette.success} />
                          <Text style={styles.commVerifiedPillText}>Verified</Text>
                        </View>
                      )}
                    </View>
                    <Text style={styles.commCollegeName}>🏫 {item.collegeName}</Text>
                  </View>
                </View>

                {/* [View] Action Button */}
                <TouchableOpacity
                  style={styles.commViewBtn}
                  onPress={() => {
                    if (item.type === 'quiz') {
                      router.push({
                        pathname: '/quizzpage',
                        params: {
                          topic: item.targetParams.topic,
                          subject: item.targetParams.subject,
                          section: item.targetParams.section,
                        },
                      });
                    } else {
                      router.push({
                        pathname: '/topic-learning',
                        params: {
                          topic: item.targetParams.topic,
                          subject: item.targetParams.subject,
                          section: item.targetParams.section,
                        },
                      });
                    }
                  }}
                  activeOpacity={0.85}
                >
                  <Text style={styles.commViewBtnText}>
                    {item.type === 'quiz' ? 'Start Community Quiz' : item.type === 'video' ? 'Watch Lecture' : 'View Notes & Theory'}
                  </Text>
                  <Feather name="arrow-right" size={15} color="#FFFFFF" />
                </TouchableOpacity>
              </View>
            ))}

            {communityItems.length === 0 && (
              <View style={styles.emptyCommBox}>
                <Feather name="inbox" size={32} color={Palette.textMuted} />
                <Text style={styles.emptyCommTitle}>No Community Content Found</Text>
                <Text style={styles.emptyCommSubtitle}>
                  Try adjusting your search query or filter tags to discover other educator materials.
                </Text>
              </View>
            )}
          </View>
        </ScrollView>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },

  // Top-level Scope Switcher (My College vs Community)
  scopeSwitcherContainer: {
    flexDirection: 'row',
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: Palette.border,
    gap: 10,
  },
  scopeBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 10,
    borderRadius: Radii.button,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  scopeBtnActive: {
    backgroundColor: Palette.primaryLight,
    borderColor: Palette.primary,
  },
  scopeBtnCommunityActive: {
    backgroundColor: Palette.aiPurpleLight,
    borderColor: Palette.aiPurple,
  },
  scopeBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: Palette.textSecondary,
  },
  scopeBtnTextActive: {
    color: Palette.primary,
    fontWeight: '800',
  },
  scopeBtnTextCommunityActive: {
    color: Palette.aiPurple,
    fontWeight: '800',
  },
  newPill: {
    backgroundColor: Palette.aiPurple,
    paddingHorizontal: 5,
    paddingVertical: 1.5,
    borderRadius: 4,
  },
  newPillText: {
    fontSize: 8.5,
    fontWeight: '900',
    color: '#FFFFFF',
    letterSpacing: 0.5,
  },

  identityCard: {
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 16,
    paddingVertical: 14,
    borderBottomWidth: 1,
    borderBottomColor: Palette.border,
  },
  identityTop: { flexDirection: 'row', alignItems: 'center', gap: 12 },
  collegeIconBox: {
    width: 46,
    height: 46,
    borderRadius: 14,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
  },
  badgeRow: { flexDirection: 'row', alignItems: 'center', gap: 8, marginBottom: 2 },
  verifiedBadge: { flexDirection: 'row', alignItems: 'center', gap: 4, backgroundColor: Palette.successLight, paddingHorizontal: 6, paddingVertical: 2, borderRadius: 4 },
  verifiedText: { fontSize: 9.5, fontWeight: '800', color: Palette.success, letterSpacing: 0.6 },
  batchTag: { fontSize: 10.5, color: Palette.textSecondary, fontWeight: '600' },
  collegeName: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  classDetails: { fontSize: 12, color: Palette.primary, fontWeight: '700', marginTop: 2 },
  tabsRow: {
    flexDirection: 'row',
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: Palette.border,
  },
  tabItem: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    paddingVertical: 11,
  },
  tabItemActive: { borderBottomWidth: 2, borderBottomColor: Palette.primary },
  tabItemText: { fontSize: 12.5, fontWeight: '600', color: Palette.textSecondary },
  tabItemTextActive: { color: Palette.primary, fontWeight: '700' },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  workspaceContainer: { gap: 14 },
  sectionHeaderRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  sectionTitleRow: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  sectionTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  sectionCount: { fontSize: 11.5, color: Palette.textSecondary, fontWeight: '600' },
  announcementsList: { gap: 10 },
  announcementCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  announcementCardUrgent: {
    borderColor: Palette.dangerBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.danger,
  },
  annTopRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  annBadge: { backgroundColor: Palette.primaryLight, paddingHorizontal: 6, paddingVertical: 2, borderRadius: 4 },
  annBadgeText: { fontSize: 10, fontWeight: '800', color: Palette.primary },
  annDate: { fontSize: 11, color: Palette.textMuted },
  annTitle: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  annContent: { fontSize: 12.5, color: Palette.textBody, lineHeight: 18, marginBottom: 8 },
  annAuthor: { fontSize: 11, color: Palette.textSecondary, fontStyle: 'italic' },
  cardsGrid: { gap: 10 },
  quizCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  quizTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  tag: { backgroundColor: Palette.successLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  tagText: { fontSize: 10.5, fontWeight: '700', color: Palette.success },
  quizMeta: { fontSize: 11, color: Palette.textSecondary },
  quizTitle: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 2 },
  quizDesc: { fontSize: 12, color: Palette.textSecondary, marginBottom: 10 },
  startQuizBtn: { backgroundColor: Palette.success, borderRadius: Radii.button, paddingVertical: 10, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6 },
  startQuizBtnText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },
  notesGrid: { gap: 10 },
  noteCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  noteCardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  noteTag: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  noteTagText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  noteDate: { fontSize: 11, color: Palette.success, fontWeight: '700' },
  noteTitle: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  noteIntro: { fontSize: 12.5, color: Palette.textSecondary, lineHeight: 17, marginBottom: 8 },
  noteFooter: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingTop: 6, borderTopWidth: 1, borderTopColor: Palette.borderSubtle },
  noteAuthorText: { fontSize: 11, color: Palette.textMuted },
  videosGrid: { gap: 10 },
  videoCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  videoHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  vBadge: { backgroundColor: Palette.aiPurpleLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  vBadgeText: { fontSize: 10.5, fontWeight: '800', color: Palette.aiPurple },
  vAuthor: { fontSize: 11, color: Palette.textSecondary },
  vTitle: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  vDesc: { fontSize: 12, color: Palette.textSecondary, marginBottom: 10 },
  watchLectureBtn: { backgroundColor: Palette.aiPurple, borderRadius: Radii.button, paddingVertical: 10, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6 },
  watchLectureText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },
  interviewsGrid: { gap: 10 },
  interviewCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  intTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 },
  intType: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle },
  statusPill: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  statusText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  intRole: { fontSize: 12.5, color: Palette.textSecondary, marginBottom: 4 },
  intSchedule: { fontSize: 11.5, color: Palette.textMuted, marginBottom: 10 },
  joinCallBtn: { backgroundColor: Palette.danger, borderRadius: Radii.button, paddingVertical: 10, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6 },
  joinCallText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },
  facultyTabContainer: { gap: 12 },
  dirBanner: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, marginBottom: 4 },
  dirBannerTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginBottom: 2 },
  dirBannerDesc: { fontSize: 12, color: Palette.textSecondary, lineHeight: 16 },
  facultyList: { gap: 10 },
  facCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 16, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  facHeader: { flexDirection: 'row', gap: 12, marginBottom: 12 },
  facAvatar: { width: 44, height: 44, borderRadius: 22, backgroundColor: Palette.primary, alignItems: 'center', justifyContent: 'center' },
  facAvatarLetter: { fontSize: 18, fontWeight: '800', color: '#FFFFFF' },
  facName: { fontSize: 15.5, fontWeight: '800', color: Palette.textTitle },
  facDesignation: { fontSize: 12, color: Palette.primary, fontWeight: '700', marginTop: 1 },
  facDept: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 1 },
  subjectsBox: { backgroundColor: Palette.backgroundSecondary, padding: 10, borderRadius: 8, marginBottom: 8 },
  subjectsLabel: { fontSize: 9.5, fontWeight: '800', color: Palette.textSecondary, letterSpacing: 0.6, marginBottom: 6 },
  subjectChipsRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 6 },
  subjectChip: { backgroundColor: '#FFFFFF', paddingHorizontal: 8, paddingVertical: 3, borderRadius: 4, borderWidth: 1, borderColor: Palette.border },
  subjectChipText: { fontSize: 11, fontWeight: '600', color: Palette.textTitle },
  officeText: { fontSize: 11.5, color: Palette.textSecondary, marginBottom: 10 },
  askDoubtBtn: { backgroundColor: Palette.primaryLight, borderRadius: Radii.button, paddingVertical: 10, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6 },
  askDoubtText: { color: Palette.primary, fontSize: 12.5, fontWeight: '700' },
  perfTabContainer: { gap: 12 },
  standingCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 16, borderWidth: 1, borderColor: Palette.border, flexDirection: 'row', alignItems: 'center', gap: 14, ...Shadows.card },
  rankBadge: { width: 48, height: 48, borderRadius: 24, backgroundColor: Palette.warningLight, alignItems: 'center', justifyContent: 'center' },
  rankNum: { fontSize: 11, fontWeight: '900', color: Palette.warning, marginTop: -2 },
  standingTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  standingSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 1 },
  statsRowGrid: { flexDirection: 'row', gap: 10 },
  pStatBox: { flex: 1, backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 12, alignItems: 'center', borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  pStatVal: { fontSize: 18, fontWeight: '900', color: Palette.primary },
  pStatLabel: { fontSize: 10.5, color: Palette.textSecondary, fontWeight: '600', marginTop: 2 },
  topicCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 16, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  topicCardTitle: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  progressItem: { marginBottom: 12 },
  pMetaRow: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 4 },
  pSubj: { fontSize: 12, fontWeight: '700', color: Palette.textTitle },
  pPct: { fontSize: 12, fontWeight: '800', color: Palette.primary },

  // =========================================================================
  // COMMUNITY STYLES
  // =========================================================================
  communityHeroBanner: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.aiPurple,
    marginBottom: 14,
    ...Shadows.card,
  },
  commHeroTop: { flexDirection: 'row', alignItems: 'flex-start', gap: 12 },
  commHeroIcon: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: Palette.aiPurpleLight,
    alignItems: 'center',
    justifyContent: 'center',
  },
  verifiedRow: { flexDirection: 'row', alignItems: 'center', gap: 4, marginBottom: 3 },
  commVerifiedText: { fontSize: 9.5, fontWeight: '800', color: Palette.success, letterSpacing: 0.6 },
  commHeroTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginBottom: 3 },
  commHeroSubtitle: { fontSize: 11.5, color: Palette.textSecondary, lineHeight: 16 },
  commSearchBox: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.input,
    paddingHorizontal: 12,
    borderWidth: 1,
    borderColor: Palette.border,
    gap: 8,
    marginBottom: 14,
    ...Shadows.card,
  },
  commSearchInput: { flex: 1, paddingVertical: 10, fontSize: 13, color: Palette.textTitle },
  filterSection: { marginBottom: 4 },
  filterSectionTitle: { fontSize: 9.5, fontWeight: '800', color: Palette.textSecondary, letterSpacing: 0.6, marginBottom: 6 },
  chipsScroll: { gap: 6, paddingBottom: 6 },
  filterChip: {
    paddingHorizontal: 11,
    paddingVertical: 6,
    borderRadius: Radii.pill,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  filterChipActive: {
    backgroundColor: Palette.aiPurple,
    borderColor: Palette.aiPurple,
  },
  filterChipText: { fontSize: 11.5, fontWeight: '600', color: Palette.textBody },
  filterChipTextActive: { color: '#FFFFFF', fontWeight: '700' },
  commResultsHeader: { marginVertical: 10 },
  commResultsTitle: { fontSize: 15.5, fontWeight: '800', color: Palette.textTitle },
  commResultsSub: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 1 },
  communityCardsList: { gap: 12 },
  commCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  commCardHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  commTypeBadge: { backgroundColor: Palette.aiPurpleLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  commTypeBadgeText: { fontSize: 10, fontWeight: '800', color: Palette.aiPurple, letterSpacing: 0.5 },
  commDateText: { fontSize: 11, color: Palette.textMuted },
  commTitle: { fontSize: 15.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 8, lineHeight: 21 },
  commMetaRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 6, marginBottom: 8 },
  commSubjectTag: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 4 },
  commSubjectTagText: { fontSize: 11, fontWeight: '700', color: Palette.primary },
  commTopicTag: { backgroundColor: Palette.backgroundSecondary, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 4, borderWidth: 1, borderColor: Palette.borderSubtle },
  commTopicTagText: { fontSize: 11, fontWeight: '600', color: Palette.textTitle },
  commSummary: { fontSize: 12.5, color: Palette.textSecondary, lineHeight: 18, marginBottom: 10 },
  commAuthorBox: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    backgroundColor: Palette.backgroundSecondary,
    padding: 10,
    borderRadius: 8,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: Palette.borderSubtle,
  },
  commAuthorAvatar: { width: 34, height: 34, borderRadius: 17, backgroundColor: Palette.aiPurple, alignItems: 'center', justifyContent: 'center' },
  commAvatarLetter: { fontSize: 14, fontWeight: '800', color: '#FFFFFF' },
  commFacultyNameRow: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  commFacultyName: { fontSize: 12.5, fontWeight: '800', color: Palette.textTitle },
  commVerifiedPill: { flexDirection: 'row', alignItems: 'center', gap: 2, backgroundColor: Palette.successLight, paddingHorizontal: 4, paddingVertical: 1, borderRadius: 4 },
  commVerifiedPillText: { fontSize: 8.5, fontWeight: '800', color: Palette.success },
  commCollegeName: { fontSize: 11, color: Palette.textSecondary, marginTop: 1 },
  commViewBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.button,
    paddingVertical: 10,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    ...Shadows.button,
  },
  commViewBtnText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },
  emptyCommBox: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 30, alignItems: 'center', justifyContent: 'center', borderWidth: 1, borderColor: Palette.border, marginTop: 10 },
  emptyCommTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginTop: 8 },
  emptyCommSubtitle: { fontSize: 12, color: Palette.textSecondary, textAlign: 'center', marginTop: 4, lineHeight: 17 },
});
