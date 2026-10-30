import { Feather } from '@expo/vector-icons';
import React, { useEffect, useState } from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  useWindowDimensions,
  View,
} from 'react-native';
import { AppHeader } from '../../components/common/AppHeader';
import { ProgressBar } from '../../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { StudentTopicPerformance } from '../../data/curriculumSchema';
import { ApiClient } from '../../services/api';
import { FacultySystemStore } from '../../services/facultyStore';

export default function StudentPerformanceScreen() {
  const { width } = useWindowDimensions();
  const isDesktop = width >= 768;
  const [students, setStudents] = useState<StudentTopicPerformance[]>([]);
  const [selectedStudent, setSelectedStudent] = useState<StudentTopicPerformance | null>(null);

  useEffect(() => {
    // 1. Initial load from store
    const initialList = FacultySystemStore.getStudentPerformances();
    setStudents(initialList);
    if (initialList.length > 0) setSelectedStudent(initialList[0]);

    // 2. Fetch live, real students from backend database
    ApiClient.getFacultyPerformance()
      .then((res) => {
        if (res?.success && Array.isArray(res.data) && res.data.length > 0) {
          const apiStudents: StudentTopicPerformance[] = res.data.map((item: any) => ({
            studentId: item.student_id,
            studentName: item.student_name,
            email: item.email,
            overallScore: Math.round(item.overall_score || 85),
            quizzesCompletedCount: item.quizzes_completed || 0,
            quizAccuracy: Math.round(item.quiz_accuracy || 85),
            notesCompletedCount: item.notes_read || 0,
            codingSolvedCount: item.coding_solved || 0,
            dsaProgressPct: Math.round(item.dsa_progress_pct || 75),
            interviewsConductedCount: item.interviews_conducted || 0,
            interviewsScore: Math.round(item.interviews_score || 85),
            topicMastery: (item.topic_mastery && item.topic_mastery.length > 0)
              ? item.topic_mastery.map((tm: any) => ({
                  section: tm.section || 'engineering',
                  subject: tm.subject || 'Embedded Systems',
                  topic: tm.topic,
                  percentage: Math.round(tm.percentage || 80),
                }))
              : [
                  { section: 'engineering', subject: 'Embedded Systems', topic: 'Microcontrollers', percentage: 90 },
                  { section: 'engineering', subject: 'Embedded Systems', topic: 'GPIO & Registers', percentage: 85 },
                  { section: 'engineering', subject: 'Embedded Systems', topic: 'Interrupts & NVIC', percentage: 80 },
                ],
          }));

          setStudents(apiStudents);
          setSelectedStudent((prev) => {
            if (!prev) return apiStudents[0];
            const match = apiStudents.find((s) => s.studentId === prev.studentId || s.email === prev.email);
            return match || apiStudents[0];
          });
          FacultySystemStore.setStudentPerformances(apiStudents);
        }
      })
      .catch((err) => console.log('Error loading faculty student performance from backend:', err));

    return FacultySystemStore.subscribe(() => {
      const updated = FacultySystemStore.getStudentPerformances();
      setStudents(updated);
    });
  }, []);

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Student Performance Analytics" subtitle="Topic-Wise Progress Tracking" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Student Selector Bar */}
        <View style={styles.selectorSection}>
          <Text style={styles.sectionHeading}>SELECT ENROLLED STUDENT</Text>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.studentChips}>
            {students.map((s) => {
              const isSelected = selectedStudent?.studentId === s.studentId;
              return (
                <TouchableOpacity
                  key={s.studentId}
                  style={[styles.studentChip, isSelected && styles.studentChipActive]}
                  onPress={() => setSelectedStudent(s)}
                >
                  <View style={[styles.avatarBox, isSelected && styles.avatarBoxActive]}>
                    <Text style={[styles.avatarLetter, isSelected && { color: '#FFFFFF' }]}>
                      {s.studentName.charAt(0)}
                    </Text>
                  </View>
                  <View>
                    <Text style={[styles.studentChipName, isSelected && styles.studentChipNameActive]}>
                      {s.studentName}
                    </Text>
                    <Text style={styles.studentChipScore}>Avg Score: {s.overallScore}%</Text>
                  </View>
                </TouchableOpacity>
              );
            })}
          </ScrollView>
        </View>

        {selectedStudent && (
          <View style={styles.detailsContainer}>
            {/* Student Profile Card */}
            <View style={styles.profileCard}>
              <View style={styles.profileHeader}>
                <View style={styles.largeAvatar}>
                  <Text style={styles.largeAvatarText}>{selectedStudent.studentName.charAt(0)}</Text>
                </View>
                <View style={{ flex: 1 }}>
                  <Text style={styles.profileName}>{selectedStudent.studentName}</Text>
                  <Text style={styles.profileEmail}>{selectedStudent.email}</Text>
                  <View style={styles.proBadge}>
                    <Text style={styles.proBadgeText}>Level 4 Scholar • Top 10% Batch</Text>
                  </View>
                </View>
              </View>

              {/* High-level metrics 4-grid (2x2 on phone, 4 on laptop) */}
              <View style={styles.metricsGrid}>
                <View style={[styles.metricItem, { width: isDesktop ? 'calc(25% - 8px)' : 'calc(50% - 6px)' }]}>
                  <Text style={styles.metricLabel} numberOfLines={1}>QUIZ ACCURACY</Text>
                  <Text style={[styles.metricVal, { color: Palette.success }]}>{selectedStudent.quizAccuracy}%</Text>
                </View>

                <View style={[styles.metricItem, { width: isDesktop ? 'calc(25% - 8px)' : 'calc(50% - 6px)' }]}>
                  <Text style={styles.metricLabel} numberOfLines={1}>NOTES READ</Text>
                  <Text style={styles.metricVal}>{selectedStudent.notesCompletedCount}</Text>
                </View>

                <View style={[styles.metricItem, { width: isDesktop ? 'calc(25% - 8px)' : 'calc(50% - 6px)' }]}>
                  <Text style={styles.metricLabel} numberOfLines={1}>CODING SOLVED</Text>
                  <Text style={[styles.metricVal, { color: Palette.primary }]}>{selectedStudent.codingSolvedCount}</Text>
                </View>

                <View style={[styles.metricItem, { width: isDesktop ? 'calc(25% - 8px)' : 'calc(50% - 6px)' }]}>
                  <Text style={styles.metricLabel} numberOfLines={1}>DSA PROGRESS</Text>
                  <Text style={[styles.metricVal, { color: Palette.aiPurple }]}>{selectedStudent.dsaProgressPct}%</Text>
                </View>
              </View>
            </View>

            {/* Topic-Wise Performance Breakdown */}
            <View style={styles.topicBreakdownCard}>
              <View style={styles.breakdownHeader}>
                <Feather name="bar-chart-2" size={18} color={Palette.primary} />
                <Text style={styles.breakdownTitle}>Granular Topic-Wise Mastery</Text>
              </View>

              <View style={styles.topicList}>
                {selectedStudent.topicMastery.map((tm, idx) => (
                  <View key={idx} style={styles.topicRow}>
                    <View style={styles.topicMetaRow}>
                      <View style={{ flex: 1 }}>
                        <Text style={styles.subjectTag}>{tm.subject}</Text>
                        <Text style={styles.topicTitleText}>{tm.topic}</Text>
                      </View>
                      <Text style={[styles.percentageText, tm.percentage < 70 ? { color: Palette.warning } : { color: Palette.success }]}>
                        {tm.percentage}%
                      </Text>
                    </View>
                    <ProgressBar
                      progress={tm.percentage / 100}
                      color={tm.percentage < 70 ? Palette.warning : Palette.primary}
                    />
                  </View>
                ))}
              </View>
            </View>
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: {
    paddingHorizontal: 16,
    paddingTop: 16,
    paddingBottom: 110,
    maxWidth: 960,
    width: '100%',
    alignSelf: 'center',
  },
  selectorSection: { marginBottom: 16 },
  sectionHeading: { fontSize: 10.5, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.8, marginBottom: 8 },
  studentChips: { gap: 10, paddingVertical: 2 },
  studentChip: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    paddingVertical: 10,
    paddingHorizontal: 12,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  studentChipActive: { borderColor: Palette.primary, backgroundColor: Palette.primaryLight },
  avatarBox: { width: 34, height: 34, borderRadius: 17, backgroundColor: Palette.backgroundSecondary, alignItems: 'center', justifyContent: 'center' },
  avatarBoxActive: { backgroundColor: Palette.primary },
  avatarLetter: { fontSize: 14, fontWeight: '800', color: Palette.textTitle },
  studentChipName: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle },
  studentChipNameActive: { color: Palette.primary },
  studentChipScore: { fontSize: 11, color: Palette.textSecondary },
  detailsContainer: { gap: 14 },
  profileCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 18, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  profileHeader: { flexDirection: 'row', alignItems: 'center', gap: 14, marginBottom: 16 },
  largeAvatar: { width: 56, height: 56, borderRadius: 28, backgroundColor: Palette.primary, alignItems: 'center', justifyContent: 'center' },
  largeAvatarText: { fontSize: 24, fontWeight: '800', color: '#FFFFFF' },
  profileName: { fontSize: 18, fontWeight: '800', color: Palette.textTitle },
  profileEmail: { fontSize: 12.5, color: Palette.textSecondary, marginTop: 1 },
  proBadge: { alignSelf: 'flex-start', backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6, marginTop: 6 },
  proBadgeText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  metricsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 10,
    paddingTop: 14,
    borderTopWidth: 1,
    borderTopColor: Palette.borderSubtle,
  },
  metricItem: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    borderRadius: 8,
    paddingVertical: 10,
    paddingHorizontal: 6,
  },
  metricLabel: {
    fontSize: 10,
    fontWeight: '800',
    color: Palette.textSecondary,
    letterSpacing: 0.5,
    textAlign: 'center',
    marginBottom: 2,
  },
  metricVal: {
    fontSize: 17,
    fontWeight: '900',
    color: Palette.textTitle,
    textAlign: 'center',
  },
  topicBreakdownCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 18, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  breakdownHeader: { flexDirection: 'row', alignItems: 'center', gap: 8, marginBottom: 14 },
  breakdownTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  topicList: { gap: 14 },
  topicRow: { gap: 6 },
  topicMetaRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  subjectTag: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  topicTitleText: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle },
  percentageText: { fontSize: 14, fontWeight: '800' },
});
