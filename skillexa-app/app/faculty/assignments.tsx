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
import { Palette, Radii, Shadows } from '../../constants/theme';
import { FacultyQuiz, StudentQuizSubmission } from '../../data/curriculumSchema';
import { FacultySystemStore } from '../../services/facultyStore';

export default function AssignmentsScreen() {
  const [quizzes, setQuizzes] = useState<FacultyQuiz[]>([]);
  const [submissions, setSubmissions] = useState<StudentQuizSubmission[]>([]);

  useEffect(() => {
    setQuizzes(FacultySystemStore.getQuizzes());
    setSubmissions(FacultySystemStore.getSubmissions());
    return FacultySystemStore.subscribe(() => {
      setQuizzes(FacultySystemStore.getQuizzes());
      setSubmissions(FacultySystemStore.getSubmissions());
    });
  }, []);

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Assignments & Grading" subtitle="Manage Assigned Quizzes & Results" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Banner */}
        <View style={styles.banner}>
          <Feather name="check-square" size={22} color={Palette.aiPurple} />
          <View style={{ flex: 1 }}>
            <Text style={styles.bannerTitle}>Class Assignments & Live Submissions</Text>
            <Text style={styles.bannerDesc}>Track student submissions, accuracy rates, and time taken per assessment.</Text>
          </View>
        </View>

        {/* 1. Active Assigned Quizzes */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Active Assigned Quizzes ({quizzes.length})</Text>
        </View>

        <View style={styles.quizzesList}>
          {quizzes.map((q) => (
            <View key={q.id} style={styles.quizCard}>
              <View style={styles.quizTop}>
                <View style={styles.badge}>
                  <Text style={styles.badgeText}>{q.subject} • {q.topic}</Text>
                </View>
                <Text style={styles.durationText}>{q.durationMinutes} Mins • {q.totalMarks} Marks</Text>
              </View>

              <Text style={styles.quizTitle}>{q.quizName}</Text>
              <Text style={styles.quizDesc}>{q.description}</Text>

              <View style={styles.classesRow}>
                <Feather name="users" size={13} color={Palette.textSecondary} />
                <Text style={styles.classesText}>
                  Assigned to: {(q.assignedClasses || ['All Students']).join(', ')}
                </Text>
              </View>
            </View>
          ))}
        </View>

        {/* 2. Student Submissions Feed */}
        <View style={[styles.sectionHeaderRow, { marginTop: 18 }]}>
          <Text style={styles.sectionTitle}>Recent Student Submissions ({submissions.length})</Text>
          <Text style={styles.sectionSubtitle}>Real-time auto-graded results</Text>
        </View>

        <View style={styles.submissionsList}>
          {submissions.map((sub) => (
            <View key={sub.id} style={styles.submissionCard}>
              <View style={styles.subCardTop}>
                <View style={styles.studentInfoCol}>
                  <Text style={styles.studentName}>{sub.studentName}</Text>
                  <Text style={styles.subMetaText}>{sub.quizTitle} • {sub.submittedAt}</Text>
                </View>
                <View style={styles.scoreCircle}>
                  <Text style={styles.scoreNum}>{sub.score}</Text>
                  <Text style={styles.scoreDen}>/{sub.totalMarks}</Text>
                </View>
              </View>

              <View style={styles.subStatsRow}>
                <View style={styles.subStatItem}>
                  <Text style={styles.subStatLabel}>ACCURACY</Text>
                  <Text style={[styles.subStatVal, { color: Palette.success }]}>{sub.accuracy}%</Text>
                </View>
                <View style={styles.subStatItem}>
                  <Text style={styles.subStatLabel}>CORRECT</Text>
                  <Text style={styles.subStatVal}>{sub.correctAnswersCount}</Text>
                </View>
                <View style={styles.subStatItem}>
                  <Text style={styles.subStatLabel}>WRONG</Text>
                  <Text style={[styles.subStatVal, { color: Palette.danger }]}>{sub.wrongAnswersCount}</Text>
                </View>
                <View style={styles.subStatItem}>
                  <Text style={styles.subStatLabel}>TIME</Text>
                  <Text style={styles.subStatVal}>{sub.timeSpent}</Text>
                </View>
              </View>
            </View>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  banner: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.aiPurple,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 18,
    ...Shadows.card,
  },
  bannerTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  bannerDesc: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  sectionHeaderRow: { marginBottom: 10 },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  quizzesList: { gap: 10, marginBottom: 10 },
  quizCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  quizTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  badge: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  badgeText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  durationText: { fontSize: 11.5, color: Palette.textSecondary, fontWeight: '600' },
  quizTitle: { fontSize: 15, fontWeight: '700', color: Palette.textTitle, marginBottom: 2 },
  quizDesc: { fontSize: 12, color: Palette.textSecondary, marginBottom: 8 },
  classesRow: { flexDirection: 'row', alignItems: 'center', gap: 6, paddingTop: 6, borderTopWidth: 1, borderTopColor: Palette.borderSubtle },
  classesText: { fontSize: 11.5, color: Palette.textSecondary },
  submissionsList: { gap: 10 },
  submissionCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  subCardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 },
  studentInfoCol: { flex: 1 },
  studentName: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  subMetaText: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 2 },
  scoreCircle: { width: 44, height: 44, borderRadius: 22, backgroundColor: Palette.primaryLight, alignItems: 'center', justifyContent: 'center' },
  scoreNum: { fontSize: 15, fontWeight: '900', color: Palette.primary },
  scoreDen: { fontSize: 9, fontWeight: '700', color: Palette.primary },
  subStatsRow: { flexDirection: 'row', justifyContent: 'space-around', paddingTop: 8, borderTopWidth: 1, borderTopColor: Palette.borderSubtle },
  subStatItem: { alignItems: 'center' },
  subStatLabel: { fontSize: 9.5, fontWeight: '800', color: Palette.textSecondary, letterSpacing: 0.6 },
  subStatVal: { fontSize: 13, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
});
