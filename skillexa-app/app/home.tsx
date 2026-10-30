import { Feather, Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ImageBackground,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  useWindowDimensions,
  View,
} from 'react-native';
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';
import { ApiClient } from '../services/api';

interface WeeklyDayItem {
  day: string;
  date: string;
  count: number;
  isToday: boolean;
  isFuture: boolean;
}

interface StudentWeeklyStats {
  total_solved_this_week: number;
  today_solved: number;
  today_goal: number;
  today_progress_pct: number;
  daily_breakdown: WeeklyDayItem[];
  streak_days?: number;
}

const getInitialWeeklyDays = (): WeeklyDayItem[] => {
  const dayNames = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  const today = new Date();
  const currentDayIdx = (today.getDay() + 6) % 7;
  return dayNames.map((d, i) => ({
    day: d,
    date: '',
    count: 0,
    isToday: i === currentDayIdx,
    isFuture: i > currentDayIdx,
  }));
};

const getGreeting = () => {
  const hour = new Date().getHours();
  if (hour >= 5 && hour < 12) return 'Good morning';
  if (hour >= 12 && hour < 17) return 'Good afternoon';
  return 'Good evening';
};

export default function HomeScreen() {
  const { profile } = useAuth();
  const userName = profile?.name && profile.name.toLowerCase() !== 'faculty' ? profile.name : 'Ganesh Sharan';
  const greeting = getGreeting();
  const { width } = useWindowDimensions();
  const isDesktop = width >= 768;

  const [weeklyStats, setWeeklyStats] = useState<StudentWeeklyStats | null>(null);
  const [weeklyDays, setWeeklyDays] = useState<WeeklyDayItem[]>(getInitialWeeklyDays);

  useEffect(() => {
    if (
      profile?.role === 'FACULTY' ||
      profile?.role === 'ADMIN' ||
      profile?.email?.includes('faculty') ||
      profile?.email === 'dr.ramesh@kvgce.edu.in'
    ) {
      router.replace('/faculty-dashboard' as any);
      return;
    }

    ApiClient.getStudentStats()
      .then((res) => {
        if (res?.success && res.data?.weekly_progress) {
          const wp = res.data.weekly_progress;
          setWeeklyStats({
            total_solved_this_week: wp.total_solved_this_week ?? 0,
            today_solved: wp.today_solved ?? 0,
            today_goal: wp.today_goal ?? 20,
            today_progress_pct: wp.today_progress_pct ?? 0,
            daily_breakdown: wp.daily_breakdown ?? [],
            streak_days: wp.streak_days,
          });

          if (Array.isArray(wp.daily_breakdown) && wp.daily_breakdown.length === 7) {
            setWeeklyDays(
              wp.daily_breakdown.map((d: any) => ({
                day: d.day,
                date: d.date,
                count: d.count ?? 0,
                isToday: Boolean(d.is_today),
                isFuture: Boolean(d.is_future),
              }))
            );
          }
        }
      })
      .catch(() => {});
  }, [profile?.role, profile?.email]);

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader />

      <ScrollView
        contentContainerStyle={[styles.scrollContent, isDesktop && styles.scrollContentDesktop]}
        showsVerticalScrollIndicator={false}
      >
        <View style={[styles.container, isDesktop && styles.containerDesktop]}>
          {/* 1. Dynamic Greeting Card (Morning / Afternoon / Evening) */}
          <View style={[styles.greetingCard, isDesktop && styles.greetingCardDesktop]}>
            <Text style={[styles.greetingTitle, isDesktop && styles.greetingTitleDesktop]}>
              {greeting}, {userName}
            </Text>
            <Text style={[styles.greetingSub, isDesktop && styles.greetingSubDesktop]}>
              Small steps today, big dreams tomorrow 🚀
            </Text>
          </View>

          {/* 2. Choose Your Path Section */}
          <View style={styles.sectionHeader}>
            <Text style={[styles.sectionTitle, isDesktop && styles.sectionTitleDesktop]}>
              Choose Your Path
            </Text>
            <Text style={[styles.sectionSub, isDesktop && styles.sectionSubDesktop]}>
              Pick your goal and start learning
            </Text>
          </View>

          <View style={[styles.pathCardsRow, isDesktop && styles.pathCardsRowDesktop]}>
            {/* Engineering Learning Card */}
            <TouchableOpacity
              style={[styles.engPathCard, isDesktop && styles.engPathCardDesktop]}
              onPress={() => router.push('/engineering' as any)}
              activeOpacity={0.85}
            >
              <View style={styles.pathCardTop}>
                <View style={[styles.engIconBox, isDesktop && styles.engIconBoxDesktop]}>
                  <Feather name="cpu" size={isDesktop ? 22 : 18} color="#0284C7" />
                </View>
                <Text style={[styles.pathCardTitle, isDesktop && styles.pathCardTitleDesktop]}>
                  Engineering{'\n'}Learning
                </Text>
                <Feather name="chevron-right" size={isDesktop ? 18 : 14} color="#94A3B8" style={styles.pathChevron} />
              </View>
              <View style={[styles.pathSubWrapper, isDesktop && styles.pathSubWrapperDesktop]}>
                <Text style={[styles.pathSubtext, isDesktop && styles.pathSubtextDesktop]}>Coding  •  DSA  •  Resume</Text>
                <Text style={[styles.pathSubtext, isDesktop && styles.pathSubtextDesktop]}>AI Interview  •  Placement Prep</Text>
              </View>
            </TouchableOpacity>

            {/* Competitive Exams Card */}
            <TouchableOpacity
              style={[styles.compPathCard, isDesktop && styles.compPathCardDesktop]}
              onPress={() => router.push('/competitive' as any)}
              activeOpacity={0.85}
            >
              <View style={styles.pathCardTop}>
                <View style={[styles.compIconBox, isDesktop && styles.compIconBoxDesktop]}>
                  <Feather name="target" size={isDesktop ? 22 : 18} color="#EA580C" />
                </View>
                <Text style={[styles.pathCardTitle, isDesktop && styles.pathCardTitleDesktop]}>
                  Competitive{'\n'}Exams
                </Text>
                <Feather name="chevron-right" size={isDesktop ? 18 : 14} color="#94A3B8" style={styles.pathChevron} />
              </View>
              <View style={[styles.pathSubWrapper, isDesktop && styles.pathSubWrapperDesktop]}>
                <Text style={[styles.pathSubtext, isDesktop && styles.pathSubtextDesktop]}>Aptitude  •  Reasoning  •</Text>
                <Text style={[styles.pathSubtext, isDesktop && styles.pathSubtextDesktop]}>English  •  GK  •  Science</Text>
                <Text style={[styles.pathSubtext, isDesktop && styles.pathSubtextDesktop]}>Fitness</Text>
              </View>
            </TouchableOpacity>
          </View>

          {/* 3. College Workspace Banner */}
          <TouchableOpacity
            style={[styles.collegeBanner, isDesktop && styles.collegeBannerDesktop]}
            onPress={() => router.push('/my-college' as any)}
            activeOpacity={0.88}
          >
            <View style={[styles.collegeBannerContent, isDesktop && styles.collegeBannerContentDesktop]}>
              <View style={styles.collegeLeft}>
                <View style={[styles.collegeCapBox, isDesktop && styles.collegeCapBoxDesktop]}>
                  <Ionicons name="school" size={isDesktop ? 22 : 18} color="#0284C7" />
                </View>
                <View style={styles.collegeTextCol}>
                  <Text style={[styles.collegeBannerTitle, isDesktop && styles.collegeBannerTitleDesktop]}>
                    College Workspace
                  </Text>
                  <Text style={[styles.collegeBannerSub, isDesktop && styles.collegeBannerSubDesktop]} numberOfLines={1}>
                    {profile?.collegeName || 'KVG College of Engineering, Sullia'}
                  </Text>
                </View>
              </View>

              <View style={[styles.openWorkspaceBtn, isDesktop && styles.openWorkspaceBtnDesktop]}>
                <Text style={[styles.openWorkspaceText, isDesktop && styles.openWorkspaceTextDesktop]}>
                  Open Workspace →
                </Text>
              </View>
            </View>
          </TouchableOpacity>

          {/* 4. Quick Practice Section */}
          <View style={styles.quickPracticeHeader}>
            <View>
              <Text style={[styles.sectionTitle, isDesktop && styles.sectionTitleDesktop]}>Quick Practice</Text>
              <Text style={[styles.sectionSub, isDesktop && styles.sectionSubDesktop]}>Jump into your favourite topics</Text>
            </View>
            <TouchableOpacity
              onPress={() => router.push('/coding-problems' as any)}
              activeOpacity={0.7}
            >
              <Text style={[styles.exploreAllText, isDesktop && styles.exploreAllTextDesktop]}>Explore All →</Text>
            </TouchableOpacity>
          </View>

          <View style={[styles.quickGrid, isDesktop && styles.quickGridDesktop]}>
            {/* Coding */}
            <TouchableOpacity
              style={[styles.quickCard, isDesktop && styles.quickCardDesktop]}
              onPress={() => router.push('/coding-problems' as any)}
              activeOpacity={0.8}
            >
              <View style={[styles.quickIconBox, isDesktop && styles.quickIconBoxDesktop, { backgroundColor: '#E0F2FE' }]}>
                <Feather name="code" size={isDesktop ? 20 : 16} color="#0284C7" />
              </View>
              <Text style={[styles.quickTitle, isDesktop && styles.quickTitleDesktop]}>Coding</Text>
              <Text style={[styles.quickSub, isDesktop && styles.quickSubDesktop]}>26+ Problems</Text>
            </TouchableOpacity>

            {/* DSA Roadmap */}
            <TouchableOpacity
              style={[styles.quickCard, isDesktop && styles.quickCardDesktop]}
              onPress={() => router.push('/dsa-practice' as any)}
              activeOpacity={0.8}
            >
              <View style={[styles.quickIconBox, isDesktop && styles.quickIconBoxDesktop, { backgroundColor: '#DCFCE7' }]}>
                <Feather name="git-branch" size={isDesktop ? 20 : 16} color="#10B981" />
              </View>
              <Text style={[styles.quickTitle, isDesktop && styles.quickTitleDesktop]}>DSA Roadmap</Text>
              <Text style={[styles.quickSub, isDesktop && styles.quickSubDesktop]}>12 Topics</Text>
            </TouchableOpacity>

            {/* Topic Quiz */}
            <TouchableOpacity
              style={[styles.quickCard, isDesktop && styles.quickCardDesktop]}
              onPress={() => router.push('/quizzpage' as any)}
              activeOpacity={0.8}
            >
              <View style={[styles.quickIconBox, isDesktop && styles.quickIconBoxDesktop, { backgroundColor: '#F3E8FF' }]}>
                <Feather name="file-text" size={isDesktop ? 20 : 16} color="#8B5CF6" />
              </View>
              <Text style={[styles.quickTitle, isDesktop && styles.quickTitleDesktop]}>Topic Quiz</Text>
              <Text style={[styles.quickSub, isDesktop && styles.quickSubDesktop]}>12 Topics</Text>
            </TouchableOpacity>

            {/* AI Interview */}
            <TouchableOpacity
              style={[styles.quickCard, isDesktop && styles.quickCardDesktop]}
              onPress={() => router.push('/mock-interviews' as any)}
              activeOpacity={0.8}
            >
              <View style={[styles.quickIconBox, isDesktop && styles.quickIconBoxDesktop, { backgroundColor: '#FCE7F3' }]}>
                <Feather name="cpu" size={isDesktop ? 20 : 16} color="#EC4899" />
              </View>
              <Text style={[styles.quickTitle, isDesktop && styles.quickTitleDesktop]}>AI Interview</Text>
              <Text style={[styles.quickSub, isDesktop && styles.quickSubDesktop, { color: '#0284C7', fontWeight: '700' }]}>
                Practice Now
              </Text>
            </TouchableOpacity>
          </View>

          {/* 5. Live Interview Card */}
          <TouchableOpacity
            style={[styles.actionCardLive, isDesktop && styles.actionCardLiveDesktop]}
            onPress={() => router.push('/live-interview' as any)}
            activeOpacity={0.85}
          >
            <View style={[styles.actionIconCircleRed, isDesktop && styles.actionIconCircleRedDesktop]}>
              <Feather name="video" size={isDesktop ? 20 : 17} color="#E11D48" />
            </View>
            <View style={styles.actionTextCol}>
              <View style={styles.actionTitleRow}>
                <Text style={[styles.actionTitle, isDesktop && styles.actionTitleDesktop]}>Live Interview</Text>
                <View style={styles.liveTag}>
                  <Text style={styles.liveTagText}>LIVE</Text>
                </View>
              </View>
              <Text style={[styles.actionSub, isDesktop && styles.actionSubDesktop]}>
                1-on-1 video calls with expert mentors & placement guidance
              </Text>
            </View>
            <Feather name="chevron-right" size={isDesktop ? 18 : 16} color="#94A3B8" />
          </TouchableOpacity>

          {/* 6. Govt Jobs & Exam Notifications Card */}
          <TouchableOpacity
            style={[styles.actionCardJobs, isDesktop && styles.actionCardJobsDesktop]}
            onPress={() => router.push('/govt-jobs' as any)}
            activeOpacity={0.85}
          >
            <View style={[styles.actionIconCircleBlue, isDesktop && styles.actionIconCircleBlueDesktop]}>
              <Feather name="bell" size={isDesktop ? 20 : 17} color="#0284C7" />
            </View>
            <View style={styles.actionTextCol}>
              <Text style={[styles.actionTitle, isDesktop && styles.actionTitleDesktop]}>
                Govt Jobs & Exam Notifications
              </Text>
              <Text style={[styles.actionSub, isDesktop && styles.actionSubDesktop]}>
                Latest updates for all government jobs, exams & results
              </Text>
            </View>
            <Feather name="chevron-right" size={isDesktop ? 18 : 16} color="#94A3B8" />
          </TouchableOpacity>

          {/* 7. Weekly Progress */}
          <View style={[styles.weeklyCard, isDesktop && styles.weeklyCardDesktop]}>
            <Text style={[styles.weeklyTitle, isDesktop && styles.weeklyTitleDesktop]}>Weekly Progress</Text>
            <Text style={[styles.weeklySub, isDesktop && styles.weeklySubDesktop]}>
              {weeklyStats?.total_solved_this_week || 0} questions solved this week
            </Text>

            <View style={[styles.barChartRow, isDesktop && styles.barChartRowDesktop]}>
              {weeklyDays.map((item, idx) => (
                <View key={idx} style={styles.barCol}>
                  <View style={[styles.barTrack, isDesktop && styles.barTrackDesktop]}>
                    <View
                      style={[
                        styles.barFill,
                        item.isToday ? styles.barFillToday : undefined,
                        { height: `${Math.min(100, Math.max(12, item.count * 16))}%` },
                      ]}
                    />
                  </View>
                  <Text style={[styles.barDayLabel, isDesktop && styles.barDayLabelDesktop, item.isToday && styles.barDayToday]}>
                    {item.day}
                  </Text>
                </View>
              ))}
            </View>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  scrollContent: {
    paddingHorizontal: 12,
    paddingTop: 10,
    paddingBottom: 95, // Leaves clean clearance for the bottom navigation
  },
  scrollContentDesktop: {
    paddingHorizontal: 24,
    paddingTop: 18,
    paddingBottom: 110,
  },
  container: {
    width: '100%',
  },
  containerDesktop: {
    maxWidth: 1240,
    alignSelf: 'center',
  },

  // 1. Dynamic Greeting Card
  greetingCard: {
    backgroundColor: '#F0F7FF',
    borderRadius: 14,
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderWidth: 1,
    borderColor: '#D8EAFF',
    marginBottom: 16,
  },
  greetingCardDesktop: {
    borderRadius: 18,
    paddingHorizontal: 24,
    paddingVertical: 18,
    marginBottom: 24,
  },
  greetingTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: '#0F172A',
    marginBottom: 3,
  },
  greetingTitleDesktop: {
    fontSize: 22,
    marginBottom: 5,
  },
  greetingSub: {
    fontSize: 12,
    color: '#475569',
    fontWeight: '500',
  },
  greetingSubDesktop: {
    fontSize: 14,
  },

  // Section Headers
  sectionHeader: {
    marginBottom: 10,
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
  },
  sectionTitleDesktop: {
    fontSize: 19,
  },
  sectionSub: {
    fontSize: 11.5,
    color: '#64748B',
    marginTop: 2,
  },
  sectionSubDesktop: {
    fontSize: 13.5,
  },

  // 2. Choose Your Path
  pathCardsRow: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 16,
  },
  pathCardsRowDesktop: {
    gap: 16,
    marginBottom: 24,
  },
  engPathCard: {
    flex: 1,
    backgroundColor: '#F0F8FF',
    borderRadius: 14,
    padding: 11,
    borderWidth: 1,
    borderColor: '#D0E7FF',
    justifyContent: 'space-between',
    minHeight: 125,
  },
  engPathCardDesktop: {
    borderRadius: 18,
    padding: 18,
    minHeight: 150,
  },
  compPathCard: {
    flex: 1,
    backgroundColor: '#FFF8F0',
    borderRadius: 14,
    padding: 11,
    borderWidth: 1,
    borderColor: '#FED7AA',
    justifyContent: 'space-between',
    minHeight: 125,
  },
  compPathCardDesktop: {
    borderRadius: 18,
    padding: 18,
    minHeight: 150,
  },
  pathCardTop: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'space-between',
  },
  engIconBox: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#E0F2FE',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 6,
  },
  engIconBoxDesktop: {
    width: 44,
    height: 44,
    borderRadius: 12,
    marginRight: 10,
  },
  compIconBox: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#FFEDD5',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 6,
  },
  compIconBoxDesktop: {
    width: 44,
    height: 44,
    borderRadius: 12,
    marginRight: 10,
  },
  pathCardTitle: {
    flex: 1,
    fontSize: 12.5,
    fontWeight: '800',
    color: '#0F172A',
    lineHeight: 16,
  },
  pathCardTitleDesktop: {
    fontSize: 16,
    lineHeight: 22,
  },
  pathChevron: {
    marginTop: 2,
  },
  pathSubWrapper: {
    marginTop: 10,
  },
  pathSubWrapperDesktop: {
    marginTop: 14,
  },
  pathSubtext: {
    fontSize: 9.5,
    color: '#64748B',
    lineHeight: 14,
  },
  pathSubtextDesktop: {
    fontSize: 12,
    lineHeight: 18,
  },

  // 3. College Workspace Banner (Transparent Background)
  collegeBanner: {
    backgroundColor: 'transparent',
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#D8EAFF',
    marginBottom: 16,
  },
  collegeBannerDesktop: {
    borderRadius: 18,
    marginBottom: 24,
  },
  collegeBannerContent: {
    paddingHorizontal: 14,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 10,
    backgroundColor: 'transparent',
  },
  collegeBannerContentDesktop: {
    paddingHorizontal: 22,
    paddingVertical: 16,
    gap: 16,
  },
  collegeLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
    gap: 10,
    minWidth: 0,
  },
  collegeCapBox: {
    width: 36,
    height: 36,
    borderRadius: 10,
    backgroundColor: '#E0F2FE',
    alignItems: 'center',
    justifyContent: 'center',
  },
  collegeCapBoxDesktop: {
    width: 44,
    height: 44,
    borderRadius: 12,
  },
  collegeTextCol: {
    flex: 1,
    minWidth: 0,
  },
  collegeBannerTitle: {
    fontSize: 14,
    fontWeight: '800',
    color: '#0F172A',
  },
  collegeBannerTitleDesktop: {
    fontSize: 16.5,
  },
  collegeBannerSub: {
    fontSize: 11,
    color: '#64748B',
    marginTop: 2,
  },
  collegeBannerSubDesktop: {
    fontSize: 13,
    marginTop: 3,
  },
  openWorkspaceBtn: {
    backgroundColor: '#E0F2FE',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 16,
    flexShrink: 0,
    borderWidth: 1,
    borderColor: '#BAE6FD',
  },
  openWorkspaceBtnDesktop: {
    paddingHorizontal: 16,
    paddingVertical: 9,
    borderRadius: 20,
  },
  openWorkspaceText: {
    color: '#0284C7',
    fontSize: 11.5,
    fontWeight: '700',
  },
  openWorkspaceTextDesktop: {
    fontSize: 13,
  },

  // 4. Quick Practice
  quickPracticeHeader: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  exploreAllText: {
    fontSize: 12.5,
    color: '#0284C7',
    fontWeight: '700',
  },
  exploreAllTextDesktop: {
    fontSize: 14,
  },
  quickGrid: {
    flexDirection: 'row',
    gap: 8,
    marginBottom: 14,
  },
  quickGridDesktop: {
    gap: 14,
    marginBottom: 20,
  },
  quickCard: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    paddingVertical: 10,
    paddingHorizontal: 4,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Shadows.card,
  },
  quickCardDesktop: {
    borderRadius: 16,
    paddingVertical: 16,
    paddingHorizontal: 10,
  },
  quickIconBox: {
    width: 34,
    height: 34,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 6,
  },
  quickIconBoxDesktop: {
    width: 44,
    height: 44,
    borderRadius: 14,
    marginBottom: 10,
  },
  quickTitle: {
    fontSize: 11.5,
    fontWeight: '700',
    color: '#0F172A',
    textAlign: 'center',
  },
  quickTitleDesktop: {
    fontSize: 13.5,
  },
  quickSub: {
    fontSize: 9.5,
    color: '#64748B',
    marginTop: 2,
    textAlign: 'center',
  },
  quickSubDesktop: {
    fontSize: 11.5,
    marginTop: 3,
  },

  // 5. Action Cards
  actionCardLive: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFF1F2',
    borderWidth: 1,
    borderColor: '#FECDD3',
    borderRadius: 13,
    paddingHorizontal: 12,
    paddingVertical: 10,
    marginBottom: 10,
    gap: 10,
  },
  actionCardLiveDesktop: {
    borderRadius: 16,
    paddingHorizontal: 18,
    paddingVertical: 14,
    marginBottom: 12,
    gap: 14,
  },
  actionIconCircleRed: {
    width: 34,
    height: 34,
    borderRadius: 17,
    backgroundColor: '#FFE4E6',
    alignItems: 'center',
    justifyContent: 'center',
  },
  actionIconCircleRedDesktop: {
    width: 42,
    height: 42,
    borderRadius: 21,
  },
  actionTextCol: {
    flex: 1,
    minWidth: 0,
  },
  actionTitleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 2,
  },
  actionTitle: {
    fontSize: 13,
    fontWeight: '800',
    color: '#0F172A',
  },
  actionTitleDesktop: {
    fontSize: 15,
  },
  liveTag: {
    backgroundColor: '#E11D48',
    paddingHorizontal: 5,
    paddingVertical: 1.5,
    borderRadius: 4,
  },
  liveTagText: {
    color: '#FFFFFF',
    fontSize: 8.5,
    fontWeight: '800',
  },
  actionSub: {
    fontSize: 10.5,
    color: '#64748B',
  },
  actionSubDesktop: {
    fontSize: 12,
  },

  actionCardJobs: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F0F9FF',
    borderWidth: 1,
    borderColor: '#BAE6FD',
    borderRadius: 13,
    paddingHorizontal: 12,
    paddingVertical: 10,
    marginBottom: 16,
    gap: 10,
  },
  actionCardJobsDesktop: {
    borderRadius: 16,
    paddingHorizontal: 18,
    paddingVertical: 14,
    marginBottom: 24,
    gap: 14,
  },
  actionIconCircleBlue: {
    width: 34,
    height: 34,
    borderRadius: 17,
    backgroundColor: '#E0F2FE',
    alignItems: 'center',
    justifyContent: 'center',
  },
  actionIconCircleBlueDesktop: {
    width: 42,
    height: 42,
    borderRadius: 21,
  },

  // 6. Weekly Progress
  weeklyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    padding: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Shadows.card,
  },
  weeklyCardDesktop: {
    borderRadius: 18,
    padding: 22,
  },
  weeklyTitle: {
    fontSize: 14,
    fontWeight: '800',
    color: '#0F172A',
  },
  weeklyTitleDesktop: {
    fontSize: 16,
  },
  weeklySub: {
    fontSize: 11,
    color: '#64748B',
    marginTop: 2,
    marginBottom: 14,
  },
  weeklySubDesktop: {
    fontSize: 12.5,
    marginTop: 3,
    marginBottom: 20,
  },
  barChartRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    height: 65,
  },
  barChartRowDesktop: {
    height: 90,
  },
  barCol: {
    alignItems: 'center',
    flex: 1,
  },
  barTrack: {
    width: 13,
    height: 46,
    backgroundColor: '#F1F5F9',
    borderRadius: 7,
    justifyContent: 'flex-end',
    overflow: 'hidden',
  },
  barTrackDesktop: {
    width: 18,
    height: 60,
    borderRadius: 9,
  },
  barFill: {
    width: '100%',
    backgroundColor: '#BFDBFE',
    borderRadius: 7,
  },
  barFillToday: {
    backgroundColor: '#0284C7',
  },
  barDayLabel: {
    fontSize: 10,
    fontWeight: '600',
    color: '#64748B',
    marginTop: 6,
  },
  barDayLabelDesktop: {
    fontSize: 11.5,
    marginTop: 8,
  },
  barDayToday: {
    color: '#0284C7',
    fontWeight: '800',
  },
});
