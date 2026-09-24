import { Feather } from '@expo/vector-icons';
import React, { useEffect, useState } from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../../components/common/AppHeader';
import { ProgressBar } from '../../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { StudentTopicPerformance } from '../../data/curriculumSchema';
import { FacultySystemStore } from '../../services/facultyStore';

export default function StudentPerformanceScreen() {
  const [students, setStudents] = useState<StudentTopicPerformance[]>([]);
  const [selectedStudent, setSelectedStudent] = useState<StudentTopicPerformance | null>(null);

  useEffect(() => {
    const list = FacultySystemStore.getStudentPerformances();
    setStudents(list);
    if (list.length > 0) setSelectedStudent(list[0]);
    return FacultySystemStore.subscribe(() => {
      const updated = FacultySystemStore.getStudentPerformances();
      setStudents(updated);
      if (updated.length > 0 && !selectedStudent) setSelectedStudent(updated[0]);
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

              {/* High-level metrics 4-grid */}
              <View style={styles.metricsGrid}>
                <View style={styles.metricItem}>
                  <Text style={styles.metricLabel}>QUIZ ACCURACY</Text>
                  <Text style={[styles.metricVal, { color: Palette.success }]}>{selectedStudent.quizAccuracy}%</Text>
                </View>

                <View style={styles.metricItem}>
                  <Text style={styles.metricLabel}>NOTES READ</Text>
                  <Text style={styles.metricVal}>{selectedStudent.notesCompletedCount}</Text>
                </View>

                <View style={styles.metricItem}>
                  <Text style={styles.metricLabel}>CODING SOLVED</Text>
                  <Text style={[styles.metricVal, { color: Palette.primary }]}>{selectedStudent.codingSolvedCount}</Text>
                </View>

                <View style={styles.metricItem}>
                  <Text style={styles.metricLabel}>DSA PROGRESS</Text>
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
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
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
  metricsGrid: { flexDirection: 'row', justifyContent: 'space-between', paddingTop: 14, borderTopWidth: 1, borderTopColor: Palette.borderSubtle },
  metricItem: { alignItems: 'center' },
  metricLabel: { fontSize: 9.5, fontWeight: '800', color: Palette.textSecondary, letterSpacing: 0.6 },
  metricVal: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
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
