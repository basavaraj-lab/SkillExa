import { Feather, MaterialCommunityIcons } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useState } from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';

interface ModuleCard {
  id: number;
  moduleNumber: string;
  title: string;
  duration: string;
  completion: number; // 0 to 100
  level: string;
  isLocked: boolean;
}

// --- Comprehensive Syllabus Track Database for All Languages ---
const MODULES_DATA: Record<string, ModuleCard[]> = {
  python: [
    {
      id: 1,
      moduleNumber: 'MODULE 01',
      title: 'Introduction to Python Core',
      duration: '25 min',
      completion: 100,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 2,
      moduleNumber: 'MODULE 02',
      title: 'Variables & Memory Registers',
      duration: '40 min',
      completion: 35,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 3,
      moduleNumber: 'MODULE 03',
      title: 'Advanced Native Data Structures',
      duration: '90 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: true,
    },
    {
      id: 4,
      moduleNumber: 'MODULE 04',
      title: 'Conditional Statements & Logic',
      duration: '45 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: true,
    },
  ],
  c: [
    {
      id: 1,
      moduleNumber: 'MODULE 01',
      title: 'C Fundamentals & Syntax',
      duration: '30 min',
      completion: 100,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 2,
      moduleNumber: 'MODULE 02',
      title: 'Pointers & Memory Allocation',
      duration: '50 min',
      completion: 20,
      level: 'Intermediate',
      isLocked: false,
    },
    {
      id: 3,
      moduleNumber: 'MODULE 03',
      title: 'Structures, Unions & Typedef',
      duration: '60 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: true,
    },
    {
      id: 4,
      moduleNumber: 'MODULE 04',
      title: 'File I/O & Low-Level System Calls',
      duration: '45 min',
      completion: 0,
      level: 'Advanced',
      isLocked: true,
    },
  ],
  cpp: [
    {
      id: 1,
      moduleNumber: 'MODULE 01',
      title: 'C++ Basics & I/O Streams',
      duration: '35 min',
      completion: 100,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 2,
      moduleNumber: 'MODULE 02',
      title: 'Classes, Objects & OOP Principles',
      duration: '60 min',
      completion: 10,
      level: 'Intermediate',
      isLocked: false,
    },
    {
      id: 3,
      moduleNumber: 'MODULE 03',
      title: 'Standard Template Library (STL)',
      duration: '80 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: true,
    },
    {
      id: 4,
      moduleNumber: 'MODULE 04',
      title: 'Templates & Generic Programming',
      duration: '50 min',
      completion: 0,
      level: 'Advanced',
      isLocked: true,
    },
  ],
  java: [
    {
      id: 1,
      moduleNumber: 'MODULE 01',
      title: 'Java Environment & Class Structure',
      duration: '30 min',
      completion: 100,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 2,
      moduleNumber: 'MODULE 02',
      title: 'Inheritance, Polymorphism & Interfaces',
      duration: '55 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: false,
    },
    {
      id: 3,
      moduleNumber: 'MODULE 03',
      title: 'Java Collections Framework',
      duration: '75 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: true,
    },
    {
      id: 4,
      moduleNumber: 'MODULE 04',
      title: 'Multithreading & Exception Handling',
      duration: '65 min',
      completion: 0,
      level: 'Advanced',
      isLocked: true,
    },
  ],
  javascript: [
    {
      id: 1,
      moduleNumber: 'MODULE 01',
      title: 'JavaScript ES6+ Syntax & Scope',
      duration: '25 min',
      completion: 100,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 2,
      moduleNumber: 'MODULE 02',
      title: 'Arrays, Map, Filter & Reduce',
      duration: '45 min',
      completion: 50,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 3,
      moduleNumber: 'MODULE 03',
      title: 'Asynchronous JS, Promises & Async/Await',
      duration: '70 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: true,
    },
    {
      id: 4,
      moduleNumber: 'MODULE 04',
      title: 'Node.js Runtime & Event Loop',
      duration: '60 min',
      completion: 0,
      level: 'Advanced',
      isLocked: true,
    },
  ],
  'react-native': [
    {
      id: 1,
      moduleNumber: 'MODULE 01',
      title: 'React Native Primitives & Flexbox Layout',
      duration: '40 min',
      completion: 100,
      level: 'Beginner',
      isLocked: false,
    },
    {
      id: 2,
      moduleNumber: 'MODULE 02',
      title: 'State Management & Custom Hooks',
      duration: '60 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: false,
    },
    {
      id: 3,
      moduleNumber: 'MODULE 03',
      title: 'Expo Router Navigation Architecture',
      duration: '50 min',
      completion: 0,
      level: 'Intermediate',
      isLocked: true,
    },
    {
      id: 4,
      moduleNumber: 'MODULE 04',
      title: 'Native Device APIs & Performance',
      duration: '90 min',
      completion: 0,
      level: 'Advanced',
      isLocked: true,
    },
  ],
};

// Fallback Module Generator for any unmapped future languages
const getFallbackModules = (langName: string): ModuleCard[] => [
  {
    id: 1,
    moduleNumber: 'MODULE 01',
    title: `Introduction to ${langName}`,
    duration: '30 min',
    completion: 100,
    level: 'Beginner',
    isLocked: false,
  },
  {
    id: 2,
    moduleNumber: 'MODULE 02',
    title: `${langName} Core Syntax & Types`,
    duration: '45 min',
    completion: 0,
    level: 'Beginner',
    isLocked: false,
  },
  {
    id: 3,
    moduleNumber: 'MODULE 03',
    title: `Advanced ${langName} Concepts`,
    duration: '60 min',
    completion: 0,
    level: 'Intermediate',
    isLocked: true,
  },
  {
    id: 4,
    moduleNumber: 'MODULE 04',
    title: `${langName} Projects & Optimization`,
    duration: '75 min',
    completion: 0,
    level: 'Advanced',
    isLocked: true,
  },
];

export default function LanguageDashboardScreen() {
  const { langId, langName } = useLocalSearchParams<{ langId: string; langName: string }>();
  const [activeTab, setActiveTab] = useState<'syllabus' | 'overview'>('syllabus');

  const langKey = (langId || 'python').toLowerCase();
  
  // Format Display Title dynamically
  const displayTitle =
    langName ||
    (langKey === 'c'
      ? 'C Programming'
      : langKey === 'cpp'
      ? 'C++'
      : langKey === 'java'
      ? 'Java'
      : langKey === 'javascript'
      ? 'JavaScript'
      : langKey === 'react-native'
      ? 'React Native'
      : 'Python');

  // Load mapped syllabus array or generate fallback dynamically
  const modules = MODULES_DATA[langKey] || getFallbackModules(displayTitle);

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Top Header Bar */}
      <View style={styles.topBar}>
        <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
          <Feather name="arrow-left" size={20} color="#1E293B" />
        </TouchableOpacity>
        <Text style={styles.topBarTitle}>{displayTitle} Track</Text>
      </View>

      <View style={styles.mainLayout}>
        {/* Left Side Rail Navigation Sidebar */}
        <View style={styles.sideRail}>
          <TouchableOpacity
            style={[styles.railIconBox, activeTab === 'overview' && styles.railIconBoxActive]}
            onPress={() => setActiveTab('overview')}
          >
            <Feather
              name="grid"
              size={20}
              color={activeTab === 'overview' ? '#2563EB' : '#64748B'}
            />
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.railIconBox, activeTab === 'syllabus' && styles.railIconBoxActive]}
            onPress={() => setActiveTab('syllabus')}
          >
            <Feather
              name="book-open"
              size={20}
              color={activeTab === 'syllabus' ? '#2563EB' : '#64748B'}
            />
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.railIconBox}
            onPress={() =>
              router.push({
                pathname: '/coding/compiler',
                params: { langId: langKey, langName: displayTitle },
              })
            }
          >
            <Feather name="terminal" size={20} color="#64748B" />
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.railIconBox}
            onPress={() =>
              router.push({
                pathname: '/coding/progress',
                params: { langId: langKey, langName: displayTitle },
              })
            }
          >
            <Feather name="trending-up" size={20} color="#64748B" />
          </TouchableOpacity>
        </View>

        {/* Right Scrollable View */}
        <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
          {activeTab === 'overview' ? (
            /* OVERVIEW TAB */
            <View>
              <Text style={styles.welcomeTitle}>Welcome Back, {displayTitle} Developer!</Text>
              <Text style={styles.welcomeSub}>
                Continue where you left off and hit your daily milestone goals.
              </Text>

              <View style={styles.statsRow}>
                <View style={styles.statCard}>
                  <View>
                    <Text style={styles.statLabel}>Daily Fire Streak</Text>
                    <Text style={styles.statValue}>12 Days</Text>
                  </View>
                  <MaterialCommunityIcons name="fire" size={32} color="#F59E0B" />
                </View>

                <View style={styles.statCard}>
                  <View>
                    <Text style={styles.statLabel}>Platform Experience</Text>
                    <Text style={styles.statValue}>2,450 XP</Text>
                  </View>
                  <MaterialCommunityIcons name="star-circle" size={32} color="#16A34A" />
                </View>
              </View>

              {/* Quick Resume Unit Banner Card */}
              <View style={styles.quickLaunchCard}>
                <Text style={styles.quickLaunchTitle}>Current Progress: Module 01</Text>
                <Text style={styles.quickLaunchSub}>
                  {modules[0]?.title || 'Introduction & Core Syntax'}
                </Text>
                <TouchableOpacity
                  style={styles.resumeBtn}
                  onPress={() =>
                    router.push({
                      pathname: '/coding/compiler',
                      params: { langId: langKey, langName: displayTitle },
                    })
                  }
                >
                  <Text style={styles.resumeBtnText}>Resume Unit</Text>
                  <Feather name="arrow-right" size={16} color="#FFFFFF" />
                </TouchableOpacity>
              </View>
            </View>
          ) : (
            /* SYLLABUS TAB */
            <View>
              <Text style={styles.syllabusTitle}>{displayTitle} Syllabus</Text>
              <Text style={styles.syllabusSub}>
                Master fundamental concepts down to advanced programmatic principles.
              </Text>

              <View style={styles.gridContainer}>
                {modules.map((item) => (
                  <View key={item.id} style={styles.moduleCard}>
                    <View style={styles.cardTopRow}>
                      <Text style={styles.moduleNumText}>{item.moduleNumber}</Text>
                      <View
                        style={[
                          styles.badge,
                          item.isLocked ? styles.lockedBadge : styles.levelBadge,
                        ]}
                      >
                        {item.isLocked && (
                          <Feather name="lock" size={10} color="#64748B" style={{ marginRight: 4 }} />
                        )}
                        <Text
                          style={[
                            styles.badgeText,
                            item.isLocked ? styles.lockedBadgeText : styles.levelBadgeText,
                          ]}
                        >
                          {item.isLocked ? 'Locked' : item.level}
                        </Text>
                      </View>
                    </View>

                    <Text style={styles.moduleTitle}>{item.title}</Text>

                    <View style={styles.metaRow}>
                      <View style={styles.timeBox}>
                        <Feather name="clock" size={12} color="#64748B" style={{ marginRight: 4 }} />
                        <Text style={styles.metaText}>{item.duration}</Text>
                      </View>
                      <Text style={styles.metaText}>{item.completion}% Complete</Text>
                    </View>

                    {/* Dynamic Action Buttons */}
                    {item.isLocked ? (
                      <View style={styles.disabledBtn}>
                        <Text style={styles.disabledBtnText}>Unlock Previous Lesson First</Text>
                      </View>
                    ) : item.completion === 100 ? (
                      <TouchableOpacity
                        style={styles.activeBtn}
                        onPress={() =>
                          router.push({
                            pathname: '/coding/compiler',
                            params: { langId: langKey, langName: displayTitle },
                          })
                        }
                      >
                        <Text style={styles.activeBtnText}>Resume Track</Text>
                      </TouchableOpacity>
                    ) : (
                      <TouchableOpacity
                        style={styles.activeBtn}
                        onPress={() =>
                          router.push({
                            pathname: '/coding/compiler',
                            params: { langId: langKey, langName: displayTitle },
                          })
                        }
                      >
                        <Text style={styles.activeBtnText}>Launch Unit</Text>
                      </TouchableOpacity>
                    )}
                  </View>
                ))}
              </View>
            </View>
          )}
        </ScrollView>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: 12,
    paddingBottom: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  backBtn: {
    marginRight: 12,
  },
  topBarTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#1E293B',
  },
  mainLayout: {
    flex: 1,
    flexDirection: 'row',
  },
  sideRail: {
    width: 60,
    backgroundColor: '#F8FAFC',
    borderRightWidth: 1,
    borderRightColor: '#E2E8F0',
    paddingTop: 16,
    alignItems: 'center',
  },
  railIconBox: {
    width: 40,
    height: 40,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 16,
  },
  railIconBoxActive: {
    backgroundColor: '#EFF6FF',
  },
  scrollContent: {
    flexGrow: 1,
    padding: 20,
  },
  syllabusTitle: {
    fontSize: 24,
    fontWeight: '800',
    color: '#0F172A',
  },
  syllabusSub: {
    fontSize: 13,
    color: '#64748B',
    marginTop: 4,
    marginBottom: 20,
  },
  welcomeTitle: {
    fontSize: 22,
    fontWeight: '800',
    color: '#0F172A',
  },
  welcomeSub: {
    fontSize: 13,
    color: '#64748B',
    marginTop: 4,
    marginBottom: 20,
  },
  gridContainer: {
    flexDirection: 'column',
  },
  moduleCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 18,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.03,
    shadowRadius: 8,
    elevation: 2,
  },
  cardTopRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  moduleNumText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#2563EB',
    letterSpacing: 0.5,
  },
  badge: {
    paddingHorizontal: 10,
    paddingVertical: 3,
    borderRadius: 8,
    flexDirection: 'row',
    alignItems: 'center',
  },
  levelBadge: {
    backgroundColor: '#EFF6FF',
  },
  lockedBadge: {
    backgroundColor: '#F1F5F9',
  },
  badgeText: {
    fontSize: 11,
    fontWeight: '700',
  },
  levelBadgeText: {
    color: '#2563EB',
  },
  lockedBadgeText: {
    color: '#64748B',
  },
  moduleTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1E293B',
    marginBottom: 12,
  },
  metaRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  timeBox: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  metaText: {
    fontSize: 12,
    color: '#64748B',
    fontWeight: '500',
  },
  activeBtn: {
    backgroundColor: '#2563EB',
    borderRadius: 10,
    paddingVertical: 12,
    alignItems: 'center',
  },
  activeBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
  disabledBtn: {
    backgroundColor: '#E2E8F0',
    borderRadius: 10,
    paddingVertical: 12,
    alignItems: 'center',
  },
  disabledBtnText: {
    color: '#64748B',
    fontSize: 12,
    fontWeight: '600',
  },
  statsRow: {
    flexDirection: 'column',
    marginBottom: 16,
  },
  statCard: {
    backgroundColor: '#F8FAFC',
    borderRadius: 16,
    padding: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  statLabel: {
    fontSize: 12,
    color: '#64748B',
    fontWeight: '600',
  },
  statValue: {
    fontSize: 22,
    fontWeight: '800',
    color: '#0F172A',
    marginTop: 4,
  },
  quickLaunchCard: {
    backgroundColor: '#EFF6FF',
    borderRadius: 16,
    padding: 18,
    borderWidth: 1,
    borderColor: '#BFDBFE',
  },
  quickLaunchTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#1E293B',
  },
  quickLaunchSub: {
    fontSize: 13,
    color: '#475569',
    marginTop: 4,
    marginBottom: 16,
  },
  resumeBtn: {
    backgroundColor: '#2563EB',
    borderRadius: 10,
    paddingVertical: 12,
    paddingHorizontal: 16,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  resumeBtnText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '700',
  },
});