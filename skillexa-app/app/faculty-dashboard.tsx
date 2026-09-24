import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
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
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';
import { FacultySystemStore } from '../services/facultyStore';

export default function FacultyDashboardScreen() {
  const { profile } = useAuth();
  const [stats, setStats] = useState(FacultySystemStore.getStats());

  useEffect(() => {
    const unsub = FacultySystemStore.subscribe(() => {
      setStats(FacultySystemStore.getStats());
    });
    return unsub;
  }, []);

  const menuModules = [
    {
      id: 'announcements',
      title: 'College Announcements',
      desc: 'Publish departmental notices and alerts to targeted classes',
      icon: 'volume-2',
      color: Palette.primary,
      route: '/faculty/announcements',
      count: 'Direct Notices',
    },
    {
      id: 'students',
      title: 'My Students',
      desc: 'View enrolled class roster, batch progress & metrics',
      icon: 'users',
      color: Palette.success,
      route: '/faculty/students',
      count: `${stats.totalStudents} Students`,
    },
    {
      id: 'notes',
      title: 'Faculty Notes',
      desc: 'Create, draft, and publish rich topic notes to students',
      icon: 'file-text',
      color: Palette.primary,
      route: '/faculty/notes',
      count: `${stats.notesPublished} Published`,
    },
    {
      id: 'create-quiz',
      title: 'Create Quiz',
      desc: 'Author multi-question quizzes with time & negative marking',
      icon: 'plus-circle',
      color: Palette.success,
      route: '/faculty/create-quiz',
      count: `${stats.quizzesCreated} Quizzes`,
    },
    {
      id: 'question-bank',
      title: 'Question Bank',
      desc: 'Filterable repository of MCQs, Numerical & Coding questions',
      icon: 'database',
      color: Palette.warning,
      route: '/faculty/question-bank',
      count: '50+ Questions',
    },
    {
      id: 'assignments',
      title: 'Assignments & Grading',
      desc: 'Assign quizzes to classes and view detailed submissions',
      icon: 'check-square',
      color: Palette.aiPurple,
      route: '/faculty/assignments',
      count: 'Active Batches',
    },
    {
      id: 'interview',
      title: 'Take Interview',
      desc: 'Schedule custom viva & placement interviews with students',
      icon: 'message-square',
      color: Palette.primary,
      route: '/faculty/interview',
      count: `${stats.pendingEvaluations} Pending`,
    },
    {
      id: 'live-interview',
      title: 'Live Video Interview Room',
      desc: 'Real-time WebRTC-ready video interview call with timer & rubric',
      icon: 'video',
      color: Palette.danger,
      route: '/faculty/live-interview',
      count: 'Live Room Ready',
    },
    {
      id: 'performance',
      title: 'Student Performance Analytics',
      desc: 'Inspect individual student progress and topic-wise mastery',
      icon: 'trending-up',
      color: Palette.success,
      route: '/faculty/performance',
      count: `${stats.totalStudents} Enrolled`,
    },
    {
      id: 'videos',
      title: 'Faculty Videos',
      desc: 'Attach video lectures to specific curriculum topics',
      icon: 'film',
      color: Palette.aiPurple,
      route: '/faculty/videos',
      count: 'Lectures',
    },
  ];

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        title="Faculty Portal"
        subtitle={profile.collegeName || 'KVG College of Engineering'}
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* College & Faculty Verification Hero */}
        <View style={styles.heroCard}>
          <View style={styles.heroTop}>
            <View style={styles.heroIconBox}>
              <Feather name="award" size={24} color={Palette.aiPurple} />
            </View>
            <View style={{ flex: 1 }}>
              <View style={styles.badgeRow}>
                <View style={styles.badge}>
                  <Text style={styles.badgeText}>AUTHORIZED FACULTY</Text>
                </View>
                <View style={styles.statusPill}>
                  <Feather name="check" size={10} color={Palette.success} />
                  <Text style={styles.statusText}>VERIFIED</Text>
                </View>
              </View>

              <Text style={styles.heroTitle}>{profile.name || 'Dr. Kusumadhara S'}</Text>
              <Text style={styles.heroSubtitle}>
                {profile.facultyDesignation || 'Associate Professor'} • {profile.department || 'ECE'} Department
              </Text>
              <Text style={styles.collegeSubtext}>{profile.collegeName || 'KVG College of Engineering'}</Text>
            </View>
          </View>
        </View>

        {/* Real-time Stats Grid */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Dashboard Statistics</Text>
          <Text style={styles.sectionSubtitle}>Real-time department student & content metrics</Text>
        </View>

        <View style={styles.statsGrid}>
          <View style={styles.statCard}>
            <Text style={styles.statVal}>{stats.totalStudents}</Text>
            <Text style={styles.statLabel}>Enrolled Students</Text>
          </View>

          <View style={styles.statCard}>
            <Text style={[styles.statVal, { color: Palette.success }]}>{stats.notesPublished}</Text>
            <Text style={styles.statLabel}>Notes Published</Text>
          </View>

          <View style={styles.statCard}>
            <Text style={[styles.statVal, { color: Palette.warning }]}>{stats.quizzesCreated}</Text>
            <Text style={styles.statLabel}>Quizzes Created</Text>
          </View>

          <View style={styles.statCard}>
            <Text style={[styles.statVal, { color: Palette.aiPurple }]}>{stats.interviewsConducted}</Text>
            <Text style={styles.statLabel}>Interviews Done</Text>
          </View>

          <View style={styles.statCard}>
            <Text style={[styles.statVal, { color: Palette.danger }]}>{stats.pendingEvaluations}</Text>
            <Text style={styles.statLabel}>Pending Reviews</Text>
          </View>

          <View style={styles.statCard}>
            <Text style={[styles.statVal, { color: Palette.primary }]}>{stats.averageStudentScore}%</Text>
            <Text style={styles.statLabel}>Class Avg Score</Text>
          </View>
        </View>

        {/* 10 Core Faculty Modules */}
        <View style={[styles.sectionHeaderRow, { marginTop: 10 }]}>
          <Text style={styles.sectionTitle}>Faculty Management Modules</Text>
          <Text style={styles.sectionSubtitle}>Select an option to manage college learning materials</Text>
        </View>

        <View style={styles.modulesGrid}>
          {menuModules.map((mod) => (
            <TouchableOpacity
              key={mod.id}
              style={styles.modCard}
              onPress={() => router.push(mod.route as any)}
              activeOpacity={0.8}
            >
              <View style={styles.modCardTop}>
                <View style={[styles.modIconBox, { backgroundColor: `${mod.color}15` }]}>
                  <Feather name={mod.icon as any} size={20} color={mod.color} />
                </View>
                <View style={styles.countBadge}>
                  <Text style={[styles.countBadgeText, { color: mod.color }]}>{mod.count}</Text>
                </View>
              </View>

              <Text style={styles.modTitle}>{mod.title}</Text>
              <Text style={styles.modDesc}>{mod.desc}</Text>

              <View style={styles.modFooter}>
                <Text style={[styles.openLinkText, { color: mod.color }]}>Open Management</Text>
                <Feather name="arrow-right" size={14} color={mod.color} />
              </View>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  heroCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.aiPurple,
    marginBottom: 20,
    ...Shadows.card,
  },
  heroTop: { flexDirection: 'row', alignItems: 'flex-start', gap: 12 },
  heroIconBox: { width: 44, height: 44, borderRadius: 12, backgroundColor: Palette.aiPurpleLight, alignItems: 'center', justifyContent: 'center' },
  badgeRow: { flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 4 },
  badge: { backgroundColor: Palette.aiPurpleLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  badgeText: { fontSize: 10, fontWeight: '800', color: Palette.aiPurple, letterSpacing: 0.6 },
  statusPill: { flexDirection: 'row', alignItems: 'center', gap: 4, backgroundColor: Palette.successLight, paddingHorizontal: 6, paddingVertical: 3, borderRadius: 6 },
  statusText: { fontSize: 9.5, fontWeight: '800', color: Palette.success },
  heroTitle: { fontSize: 17.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 2 },
  heroSubtitle: { fontSize: 13, color: Palette.primary, fontWeight: '700' },
  collegeSubtext: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  sectionHeaderRow: { marginBottom: 12 },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  statsGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 10, marginBottom: 20 },
  statCard: {
    width: '31%',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    paddingVertical: 14,
    paddingHorizontal: 8,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    ...Shadows.card,
  },
  statVal: { fontSize: 18, fontWeight: '900', color: Palette.primary },
  statLabel: { fontSize: 10.5, color: Palette.textSecondary, fontWeight: '600', marginTop: 2, textAlign: 'center' },
  modulesGrid: { gap: 12 },
  modCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  modCardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  modIconBox: { width: 38, height: 38, borderRadius: 10, alignItems: 'center', justifyContent: 'center' },
  countBadge: { backgroundColor: Palette.backgroundSecondary, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  countBadgeText: { fontSize: 11, fontWeight: '700' },
  modTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  modDesc: { fontSize: 12.5, color: Palette.textSecondary, lineHeight: 18, marginBottom: 12 },
  modFooter: { flexDirection: 'row', alignItems: 'center', gap: 6, paddingTop: 8, borderTopWidth: 1, borderTopColor: Palette.borderSubtle },
  openLinkText: { fontSize: 12.5, fontWeight: '700' },
});
