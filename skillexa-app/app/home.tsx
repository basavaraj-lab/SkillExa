import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React from 'react';
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
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';

export default function HomeScreen() {
  const { profile } = useAuth();
  const userName = profile?.name || 'Scholar';

  const weeklyDays = [
    { day: 'Mon', count: 18, isToday: false },
    { day: 'Tue', count: 24, isToday: false },
    { day: 'Wed', count: 12, isToday: false },
    { day: 'Thu', count: 30, isToday: false },
    { day: 'Fri', count: 22, isToday: false },
    { day: 'Sat', count: 35, isToday: true },
    { day: 'Sun', count: 0, isToday: false },
  ];

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader />

      <ScrollView
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Welcome Greeting */}
        <View style={styles.greetingHeader}>
          <Text style={styles.greetingTitle}>Good morning, {userName} 👋</Text>
          <Text style={styles.greetingSubtitle}>Let&apos;s build your skills today.</Text>
        </View>

        {/* 1. Today's Goal Card */}
        <View style={styles.goalCard}>
          <View style={styles.goalTopRow}>
            <View style={styles.goalIconBox}>
              <Feather name="target" size={18} color={Palette.primary} />
            </View>
            <View style={styles.goalTitleCol}>
              <Text style={styles.goalLabel}>TODAY&apos;S GOAL</Text>
              <Text style={styles.goalTitle}>Complete 20 practice questions</Text>
            </View>
            <Text style={styles.goalPercent}>60%</Text>
          </View>

          <View style={styles.goalProgressWrapper}>
            <ProgressBar progress={0.6} color={Palette.primary} />
            <Text style={styles.goalProgressDetail}>12 of 20 solved</Text>
          </View>

          <TouchableOpacity
            style={styles.primaryBtn}
            onPress={() => router.push('/quizzpage' as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.primaryBtnText}>Continue Practice</Text>
            <Feather name="arrow-right" size={16} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* 🏫 MY COLLEGE WORKSPACE HERO CARD */}
        <TouchableOpacity
          style={styles.collegeHeroCard}
          onPress={() => router.push('/my-college' as any)}
          activeOpacity={0.85}
        >
          <View style={styles.collegeHeroTop}>
            <View style={styles.collegeIconBox}>
              <Feather name="book-open" size={22} color={Palette.primary} />
            </View>
            <View style={{ flex: 1 }}>
              <View style={styles.collegeTagRow}>
                <View style={styles.collegePill}>
                  <Text style={styles.collegePillText}>🏫 MY COLLEGE</Text>
                </View>
                <View style={styles.notifPill}>
                  <Text style={styles.notifPillText}>3 New Updates</Text>
                </View>
              </View>
              <Text style={styles.collegeTitle}>{profile.collegeName || 'KVG College of Engineering'}</Text>
              <Text style={styles.collegeSub}>
                {profile.department || 'ECE'} • {profile.academicYear || '3rd Year'} Sec {profile.section || 'A'}
              </Text>
            </View>
          </View>

          <View style={styles.collegeHeroFooter}>
            <Text style={styles.collegeActionText}>Open College Workspace (Notices, Notes, Quizzes)</Text>
            <Feather name="arrow-right" size={15} color={Palette.primary} />
          </View>
        </TouchableOpacity>

        {/* 2. Continue Learning Carousel */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Continue Learning</Text>
          <Text style={styles.sectionSubtitle}>Jump back into your active tracks</Text>
        </View>

        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.horizontalScroll}
        >
          {/* Card 1: DSA */}
          <View style={styles.continueCard}>
            <View style={styles.trackBadge}>
              <Text style={styles.trackBadgeText}>DSA</Text>
            </View>
            <Text style={styles.continueModuleTitle}>Arrays & Memory</Text>
            <Text style={styles.continueProgressText}>65% complete</Text>
            <View style={styles.continueProgressBar}>
              <ProgressBar progress={0.65} color={Palette.primary} />
            </View>
            <TouchableOpacity
              style={styles.continueBtn}
              onPress={() => router.push('/dsa-practice' as any)}
            >
              <Text style={styles.continueBtnText}>Continue</Text>
              <Feather name="play" size={12} color={Palette.primary} />
            </TouchableOpacity>
          </View>

          {/* Card 2: English */}
          <View style={styles.continueCard}>
            <View style={[styles.trackBadge, { backgroundColor: Palette.warningLight }]}>
              <Text style={[styles.trackBadgeText, { color: Palette.warning }]}>ENGLISH</Text>
            </View>
            <Text style={styles.continueModuleTitle}>Tenses & Rules</Text>
            <Text style={styles.continueProgressText}>40% complete</Text>
            <View style={styles.continueProgressBar}>
              <ProgressBar progress={0.4} color={Palette.warning} />
            </View>
            <TouchableOpacity
              style={styles.continueBtn}
              onPress={() => router.push('/english' as any)}
            >
              <Text style={styles.continueBtnText}>Continue</Text>
              <Feather name="play" size={12} color={Palette.primary} />
            </TouchableOpacity>
          </View>

          {/* Card 3: Quantitative Math */}
          <View style={styles.continueCard}>
            <View style={[styles.trackBadge, { backgroundColor: Palette.successLight }]}>
              <Text style={[styles.trackBadgeText, { color: Palette.success }]}>MATH</Text>
            </View>
            <Text style={styles.continueModuleTitle}>Percentage & Profit</Text>
            <Text style={styles.continueProgressText}>50% complete</Text>
            <View style={styles.continueProgressBar}>
              <ProgressBar progress={0.5} color={Palette.success} />
            </View>
            <TouchableOpacity
              style={styles.continueBtn}
              onPress={() => router.push('/mathematics' as any)}
            >
              <Text style={styles.continueBtnText}>Continue</Text>
              <Feather name="play" size={12} color={Palette.primary} />
            </TouchableOpacity>
          </View>
        </ScrollView>

        {/* 3. Choose Your Path */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Choose Your Path</Text>
          <Text style={styles.sectionSubtitle}>Select your main academic track</Text>
        </View>

        <View style={styles.pathsContainer}>
          {/* Engineering Path Card */}
          <TouchableOpacity
            style={styles.pathLargeCard}
            onPress={() => router.push('/engineering' as any)}
            activeOpacity={0.88}
          >
            <View style={styles.pathIconHeader}>
              <View style={styles.pathIconCircle}>
                <Feather name="cpu" size={24} color={Palette.primary} />
              </View>
              <View style={styles.pathBadge}>
                <Text style={styles.pathBadgeText}>5 Modules</Text>
              </View>
            </View>
            <Text style={styles.pathLargeTitle}>Engineering Learning</Text>
            <Text style={styles.pathLargeDesc}>
              Coding • DSA • Resume • Interview • Placement Ready
            </Text>
            <View style={styles.pathCardFooter}>
              <Text style={styles.pathExploreText}>Explore Engineering</Text>
              <Feather name="arrow-right" size={16} color={Palette.primary} />
            </View>
          </TouchableOpacity>

          {/* Competitive Exams Path Card */}
          <TouchableOpacity
            style={styles.pathLargeCard}
            onPress={() => router.push('/competitive' as any)}
            activeOpacity={0.88}
          >
            <View style={styles.pathIconHeader}>
              <View style={[styles.pathIconCircle, { backgroundColor: Palette.warningLight }]}>
                <Feather name="award" size={24} color={Palette.warning} />
              </View>
              <View style={[styles.pathBadge, { backgroundColor: Palette.warningLight }]}>
                <Text style={[styles.pathBadgeText, { color: Palette.warning }]}>6 Subjects</Text>
              </View>
            </View>
            <Text style={styles.pathLargeTitle}>Competitive Exams</Text>
            <Text style={styles.pathLargeDesc}>
              Aptitude • Reasoning • English • GK • Science • Fitness
            </Text>
            <View style={styles.pathCardFooter}>
              <Text style={[styles.pathExploreText, { color: Palette.warning }]}>Explore Competitive</Text>
              <Feather name="arrow-right" size={16} color={Palette.warning} />
            </View>
          </TouchableOpacity>
        </View>

        {/* 4. Quick Practice Actions */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Quick Practice</Text>
          <Text style={styles.sectionSubtitle}>Jump into targeted drills</Text>
        </View>

        <View style={styles.quickGrid}>
          <TouchableOpacity
            style={styles.quickCard}
            onPress={() => router.push('/coding-problems' as any)}
            activeOpacity={0.7}
          >
            <View style={styles.quickIconCircle}>
              <Feather name="terminal" size={18} color={Palette.primary} />
            </View>
            <Text style={styles.quickLabel}>Coding</Text>
            <Text style={styles.quickMeta}>250+ Problems</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.quickCard}
            onPress={() => router.push('/dsa-practice' as any)}
            activeOpacity={0.7}
          >
            <View style={[styles.quickIconCircle, { backgroundColor: Palette.successLight }]}>
              <Feather name="code" size={18} color={Palette.success} />
            </View>
            <Text style={styles.quickLabel}>DSA Roadmap</Text>
            <Text style={styles.quickMeta}>12 Topics</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.quickCard}
            onPress={() => router.push('/quizzpage' as any)}
            activeOpacity={0.7}
          >
            <View style={[styles.quickIconCircle, { backgroundColor: Palette.warningLight }]}>
              <Feather name="edit-3" size={18} color={Palette.warning} />
            </View>
            <Text style={styles.quickLabel}>Topic Quiz</Text>
            <Text style={styles.quickMeta}>Timed Drills</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.quickCard}
            onPress={() => router.push('/mock-interviews' as any)}
            activeOpacity={0.7}
          >
            <View style={[styles.quickIconCircle, { backgroundColor: Palette.aiPurpleLight }]}>
              <Feather name="message-square" size={18} color={Palette.aiPurple} />
            </View>
            <Text style={styles.quickLabel}>AI Interview</Text>
            <Text style={styles.quickMeta}>Voice & Tech</Text>
          </TouchableOpacity>
        </View>

        {/* 5. Weekly Activity Chart */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Weekly Progress</Text>
          <Text style={styles.sectionSubtitle}>110 questions solved this week</Text>
        </View>

        <View style={styles.weeklyCard}>
          <View style={styles.chartBarsRow}>
            {weeklyDays.map((d, i) => {
              const max = 35;
              const barHeight = Math.max((d.count / max) * 70, 8);
              return (
                <View key={i} style={styles.chartCol}>
                  <Text style={styles.barCount}>{d.count > 0 ? d.count : ''}</Text>
                  <View style={styles.barTrack}>
                    <View
                      style={[
                        styles.barFill,
                        { height: barHeight },
                        d.isToday && styles.barFillToday,
                      ]}
                    />
                  </View>
                  <Text style={[styles.barDayLabel, d.isToday && styles.barDayToday]}>
                    {d.day}
                  </Text>
                </View>
              );
            })}
          </View>
        </View>

        {/* 6. Recommended For You */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Recommended for You</Text>
          <Text style={styles.sectionSubtitle}>Based on your recent performance</Text>
        </View>

        <View style={styles.recommendCard}>
          <View style={styles.recommendHeader}>
            <View style={styles.recommendIconBox}>
              <Feather name="trending-up" size={18} color={Palette.primary} />
            </View>
            <View style={styles.recommendInfo}>
              <Text style={styles.recommendTitle}>Practice Percentage — Medium</Text>
              <Text style={styles.recommendStats}>Your current accuracy: 54%</Text>
            </View>
          </View>
          <Text style={styles.recommendDesc}>
            Boosting your accuracy in Quantitative Aptitude by 15% unlocks placement level evaluations.
          </Text>
          <TouchableOpacity
            style={styles.recommendBtn}
            onPress={() => router.push('/mathematics' as any)}
          >
            <Text style={styles.recommendBtnText}>Practice Now</Text>
            <Feather name="arrow-right" size={14} color="#FFFFFF" />
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.background,
  },
  scrollContent: {
    paddingHorizontal: 16,
    paddingTop: 16,
    paddingBottom: 40,
  },
  greetingHeader: {
    marginBottom: 20,
  },
  greetingTitle: {
    fontSize: 22,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  greetingSubtitle: {
    fontSize: 14,
    color: Palette.textSecondary,
    marginTop: 3,
  },
  goalCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  goalTopRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  goalIconBox: {
    width: 36,
    height: 36,
    borderRadius: 10,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 12,
  },
  goalTitleCol: {
    flex: 1,
  },
  goalLabel: {
    fontSize: 11,
    fontWeight: '800',
    color: Palette.primary,
    letterSpacing: 0.8,
  },
  goalTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
    marginTop: 2,
  },
  goalPercent: {
    fontSize: 16,
    fontWeight: '800',
    color: Palette.primary,
  },
  goalProgressWrapper: {
    marginBottom: 16,
  },
  goalProgressDetail: {
    fontSize: 12,
    color: Palette.textSecondary,
    marginTop: 6,
  },
  primaryBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    ...Shadows.button,
  },
  primaryBtnText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '700',
  },
  sectionHeaderRow: {
    marginBottom: 12,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  sectionSubtitle: {
    fontSize: 12,
    color: Palette.textSecondary,
    marginTop: 2,
  },
  horizontalScroll: {
    gap: 12,
    paddingBottom: 4,
    marginBottom: 24,
  },
  continueCard: {
    width: 200,
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  trackBadge: {
    alignSelf: 'flex-start',
    backgroundColor: Palette.primaryLight,
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    marginBottom: 10,
  },
  trackBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: Palette.primary,
    letterSpacing: 0.6,
  },
  continueModuleTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
    marginBottom: 6,
  },
  continueProgressText: {
    fontSize: 12,
    color: Palette.textSecondary,
    marginBottom: 8,
  },
  continueProgressBar: {
    marginBottom: 12,
  },
  continueBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    paddingVertical: 8,
    borderRadius: 8,
    backgroundColor: Palette.primaryLight,
  },
  continueBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.primary,
  },
  pathsContainer: {
    gap: 12,
    marginBottom: 24,
  },
  pathLargeCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  pathIconHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  pathIconCircle: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
  },
  pathBadge: {
    backgroundColor: Palette.primaryLight,
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 8,
  },
  pathBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: Palette.primary,
  },
  pathLargeTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: Palette.textTitle,
    marginBottom: 4,
  },
  pathLargeDesc: {
    fontSize: 13,
    color: Palette.textSecondary,
    lineHeight: 18,
    marginBottom: 14,
  },
  pathCardFooter: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  pathExploreText: {
    fontSize: 13,
    fontWeight: '700',
    color: Palette.primary,
  },
  quickGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    gap: 10,
    marginBottom: 24,
  },
  quickCard: {
    width: '48%',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  quickIconCircle: {
    width: 36,
    height: 36,
    borderRadius: 10,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 8,
  },
  quickLabel: {
    fontSize: 14,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  quickMeta: {
    fontSize: 11,
    color: Palette.textSecondary,
    marginTop: 2,
  },
  weeklyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  chartBarsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    height: 110,
    paddingTop: 10,
  },
  chartCol: {
    alignItems: 'center',
    flex: 1,
  },
  barCount: {
    fontSize: 10,
    fontWeight: '700',
    color: Palette.textSecondary,
    marginBottom: 4,
  },
  barTrack: {
    width: 14,
    height: 70,
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: 7,
    justifyContent: 'flex-end',
    overflow: 'hidden',
  },
  barFill: {
    width: '100%',
    backgroundColor: Palette.primaryBorder,
    borderRadius: 7,
  },
  barFillToday: {
    backgroundColor: Palette.primary,
  },
  barDayLabel: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.textSecondary,
    marginTop: 6,
  },
  barDayToday: {
    color: Palette.primary,
    fontWeight: '800',
  },
  recommendCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  recommendHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  recommendIconBox: {
    width: 36,
    height: 36,
    borderRadius: 10,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 12,
  },
  recommendInfo: {
    flex: 1,
  },
  recommendTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  recommendStats: {
    fontSize: 12,
    color: Palette.primary,
    fontWeight: '600',
    marginTop: 1,
  },
  recommendDesc: {
    fontSize: 13,
    color: Palette.textBody,
    lineHeight: 19,
    marginBottom: 14,
  },
  recommendBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 10,
    paddingHorizontal: 16,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
  },
  recommendBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
  collegeHeroCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.primary,
    marginBottom: 20,
    ...Shadows.card,
  },
  collegeHeroTop: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 12,
  },
  collegeIconBox: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
  },
  collegeTagRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 3,
  },
  collegePill: {
    backgroundColor: Palette.primaryLight,
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
  },
  collegePillText: {
    fontSize: 9.5,
    fontWeight: '800',
    color: Palette.primary,
    letterSpacing: 0.6,
  },
  notifPill: {
    backgroundColor: Palette.dangerLight,
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
  },
  notifPillText: {
    fontSize: 9.5,
    fontWeight: '800',
    color: Palette.danger,
  },
  collegeTitle: {
    fontSize: 15.5,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  collegeSub: {
    fontSize: 12,
    color: Palette.primary,
    fontWeight: '700',
    marginTop: 1,
  },
  collegeHeroFooter: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: Palette.borderSubtle,
  },
  collegeActionText: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.textTitle,
  },
});
