import { Feather } from '@expo/vector-icons';
import { router, useFocusEffect } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  Dimensions,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette } from '../constants/theme';
import { ApiClient } from '../services/api';

const { width } = Dimensions.get('window');
const isDesktop = width > 768;

const CATEGORIES = [
  'All',
  'Arrays',
  'Strings',
  'Searching',
  'Sorting',
  'Linked List',
  'Stack',
  'Queue',
  'Recursion',
  'Hashing',
  'Trees',
  'Graphs',
  'Dynamic Programming',
];

const DIFFICULTIES = ['All', 'Basic', 'Easy', 'Medium', 'Hard'];
const LANGUAGES = ['All', 'Python', 'C', 'C++', 'Java'];
const STATUSES = ['All', 'Solved', 'Unsolved'];

export default function DsaPracticePage() {
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('All');
  const [selectedLang, setSelectedLang] = useState<string>('All');
  const [selectedStatus, setSelectedStatus] = useState<string>('All');

  const [problems, setProblems] = useState<any[]>([]);
  const [progressData, setProgressData] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(true);

  const fetchProblems = () => {
    setLoading(true);
    const filterLang = selectedLang === 'All' ? undefined : selectedLang.toLowerCase();
    const filterCat = selectedCategory === 'All' ? undefined : selectedCategory;
    const filterDiff = selectedDifficulty === 'All' ? undefined : selectedDifficulty.toLowerCase();
    const filterSol = selectedStatus === 'All' ? undefined : selectedStatus.toLowerCase();

    ApiClient.getDsaProblems({
      search: searchQuery || undefined,
      category: filterCat,
      difficulty: filterDiff,
      language: filterLang,
      solved_status: filterSol,
    }).then((res) => {
      if (res.success && res.data) {
        setProblems(res.data);
      } else {
        setProblems([
          {
            id: 'dsa-1',
            problem_num: 1,
            title: 'Largest in Array',
            category: 'Arrays',
            difficulty: 'Basic',
            time_complexity: 'O(n)',
            space_complexity: 'O(1)',
            is_solved: true,
          },
          {
            id: 'dsa-2',
            problem_num: 2,
            title: 'Reverse a String',
            category: 'Strings',
            difficulty: 'Easy',
            time_complexity: 'O(n)',
            space_complexity: 'O(1)',
            is_solved: false,
          },
          {
            id: 'dsa-3',
            problem_num: 3,
            title: 'Binary Search',
            category: 'Searching',
            difficulty: 'Basic',
            time_complexity: 'O(log n)',
            space_complexity: 'O(1)',
            is_solved: false,
          },
          {
            id: 'dsa-4',
            problem_num: 4,
            title: 'Check for Palindrome String',
            category: 'Strings',
            difficulty: 'Basic',
            time_complexity: 'O(n)',
            space_complexity: 'O(1)',
            is_solved: false,
          },
          {
            id: 'dsa-5',
            problem_num: 5,
            title: 'Bubble Sort',
            category: 'Sorting',
            difficulty: 'Easy',
            time_complexity: 'O(n^2)',
            space_complexity: 'O(1)',
            is_solved: false,
          },
        ]);
      }
      setLoading(false);
    });

    ApiClient.getDsaProgress().then((res) => {
      if (res.success && res.data) {
        setProgressData(res.data);
      } else {
        setProgressData({
          total_problems: 150,
          solved_problems: 1,
          unsolved_problems: 149,
          progress_percentage: 0.7,
          streak: 1,
          categories: [
            { category: 'Arrays', solved: 1, total: 25 },
            { category: 'Strings', solved: 0, total: 20 },
            { category: 'Searching', solved: 0, total: 15 },
            { category: 'Sorting', solved: 0, total: 15 },
            { category: 'Linked List', solved: 0, total: 15 },
            { category: 'Stack', solved: 0, total: 12 },
            { category: 'Queue', solved: 0, total: 12 },
            { category: 'Recursion', solved: 0, total: 10 },
            { category: 'Hashing', solved: 0, total: 10 },
            { category: 'Trees', solved: 0, total: 8 },
            { category: 'Graphs', solved: 0, total: 5 },
            { category: 'Dynamic Programming', solved: 0, total: 3 },
          ],
        });
      }
    });
  };

  useEffect(() => {
    fetchProblems();
  }, [selectedCategory, selectedDifficulty, selectedLang, selectedStatus]);

  useFocusEffect(
    React.useCallback(() => {
      fetchProblems();
    }, [selectedCategory, selectedDifficulty, selectedLang, selectedStatus])
  );

  const handleSearchSubmit = () => {
    fetchProblems();
  };

  const solvedCount = progressData?.solved_problems || 0;
  const totalCount = progressData?.total_problems || 150;
  const progressRatio = totalCount > 0 ? solvedCount / totalCount : 0;

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="DSA Problem Solving" subtitle="150+ Coding Problems Platform" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Title Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Data Structures & Algorithms</Text>
          <Text style={styles.subtitle}>
            Master 150+ coding problems in Python, C, C++, and Java with isolated sandboxed execution.
          </Text>
        </View>

        {/* Progress Dashboard Card */}
        <View style={styles.progressCard}>
          <View style={styles.progressTopRow}>
            <View>
              <Text style={styles.progressLabel}>OVERALL DSA MASTERY</Text>
              <Text style={styles.progressValue}>
                {solvedCount} / {totalCount} Problems Solved
              </Text>
            </View>
            <View style={styles.streakBadge}>
              <Feather name="zap" size={14} color="#F59E0B" />
              <Text style={styles.streakText}>Streak: {progressData?.streak || 1} Days</Text>
            </View>
          </View>

          <ProgressBar progress={progressRatio} color={Palette.primary} />

          {/* Category Progress Grid */}
          <Text style={styles.catProgressTitle}>Category Progress Breakdown:</Text>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.catProgressScroll}>
            {(progressData?.categories || []).map((cat: any) => (
              <View key={cat.category} style={styles.catProgressChip}>
                <Text style={styles.catNameText}>{cat.category}</Text>
                <Text style={styles.catRatioText}>
                  {cat.solved}/{cat.total}
                </Text>
              </View>
            ))}
          </ScrollView>
        </View>

        {/* Search & Filter Workbench */}
        <View style={styles.filterSection}>
          {/* Search Box */}
          <View style={styles.searchRow}>
            <View style={styles.searchBox}>
              <Feather name="search" size={18} color="#94A3B8" />
              <TextInput
                style={styles.searchInput}
                placeholder="Search problem by title or keyword..."
                placeholderTextColor="#94A3B8"
                value={searchQuery}
                onChangeText={setSearchQuery}
                onSubmitEditing={handleSearchSubmit}
              />
              {searchQuery ? (
                <TouchableOpacity onPress={() => setSearchQuery('')}>
                  <Feather name="x" size={16} color="#94A3B8" />
                </TouchableOpacity>
              ) : null}
            </View>
            <TouchableOpacity style={styles.searchBtn} onPress={handleSearchSubmit}>
              <Text style={styles.searchBtnText}>Search</Text>
            </TouchableOpacity>
          </View>

          {/* 12 Categories Horizontal Filter */}
          <View style={styles.filterRowContainer}>
            <Text style={styles.filterLabel}>Category:</Text>
            <ScrollView horizontal showsHorizontalScrollIndicator={false}>
              {CATEGORIES.map((cat) => {
                const active = selectedCategory === cat;
                return (
                  <TouchableOpacity
                    key={cat}
                    style={[styles.filterChip, active && styles.filterChipActive]}
                    onPress={() => setSelectedCategory(cat)}
                  >
                    <Text style={[styles.filterChipText, active && styles.filterChipTextActive]}>{cat}</Text>
                  </TouchableOpacity>
                );
              })}
            </ScrollView>
          </View>

          {/* Difficulty / Language / Solved Filters */}
          <View style={styles.subFiltersRow}>
            {/* Difficulty Filter */}
            <View style={styles.subFilterGroup}>
              <Text style={styles.subFilterLabel}>Difficulty:</Text>
              <View style={styles.chipsWrap}>
                {DIFFICULTIES.map((diff) => {
                  const active = selectedDifficulty === diff;
                  return (
                    <TouchableOpacity
                      key={diff}
                      style={[styles.miniChip, active && styles.miniChipActive]}
                      onPress={() => setSelectedDifficulty(diff)}
                    >
                      <Text style={[styles.miniChipText, active && styles.miniChipTextActive]}>{diff}</Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>

            {/* Language Filter */}
            <View style={styles.subFilterGroup}>
              <Text style={styles.subFilterLabel}>Language:</Text>
              <View style={styles.chipsWrap}>
                {LANGUAGES.map((lang) => {
                  const active = selectedLang === lang;
                  return (
                    <TouchableOpacity
                      key={lang}
                      style={[styles.miniChip, active && styles.miniChipActive]}
                      onPress={() => setSelectedLang(lang)}
                    >
                      <Text style={[styles.miniChipText, active && styles.miniChipTextActive]}>{lang}</Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>

            {/* Status Filter */}
            <View style={styles.subFilterGroup}>
              <Text style={styles.subFilterLabel}>Status:</Text>
              <View style={styles.chipsWrap}>
                {STATUSES.map((st) => {
                  const active = selectedStatus === st;
                  return (
                    <TouchableOpacity
                      key={st}
                      style={[styles.miniChip, active && styles.miniChipActive]}
                      onPress={() => setSelectedStatus(st)}
                    >
                      <Text style={[styles.miniChipText, active && styles.miniChipTextActive]}>{st}</Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>
          </View>
        </View>

        {/* Problems List Grid / Table */}
        <View style={styles.problemsContainer}>
          <View style={styles.sectionHeaderRow}>
            <Text style={styles.sectionTitle}>
              Available Problems ({problems.length})
            </Text>
            <Text style={styles.sectionSubtitle}>Select a problem to open the two-panel code solver</Text>
          </View>

          {loading ? (
            <View style={{ paddingVertical: 40, alignItems: 'center' }}>
              <ActivityIndicator size="large" color={Palette.primary} />
              <Text style={{ color: Palette.textMuted, marginTop: 10 }}>Loading problems...</Text>
            </View>
          ) : problems.length === 0 ? (
            <View style={styles.emptyCard}>
              <Feather name="inbox" size={36} color={Palette.textMuted} />
              <Text style={styles.emptyTitle}>No problems found matching criteria</Text>
              <Text style={styles.emptySub}>Try clearing filters or search query to view all problems.</Text>
            </View>
          ) : (
            <View style={styles.problemsGrid}>
              {problems.map((prob) => {
                const isSolved = prob.is_solved;
                const diffLower = (prob.difficulty || '').toLowerCase();

                return (
                  <TouchableOpacity
                    key={prob.id}
                    style={styles.problemRowCard}
                    onPress={() =>
                      router.push({
                        pathname: '/dsa-solver',
                        params: { id: prob.id },
                      })
                    }
                    activeOpacity={0.8}
                  >
                    <View style={styles.problemRowLeft}>
                      <View style={[styles.solvedStatusCircle, isSolved && styles.solvedStatusDone]}>
                        {isSolved ? (
                          <Feather name="check" size={12} color="#FFFFFF" />
                        ) : (
                          <Text style={styles.problemNumText}>#{prob.problem_num || 1}</Text>
                        )}
                      </View>

                      <View style={styles.problemTitleBox}>
                        <Text style={styles.problemItemTitle}>{prob.title}</Text>
                        <View style={styles.problemMetaRow}>
                          <Text style={styles.categoryBadge}>{prob.category || 'Arrays'}</Text>
                          {prob.time_complexity ? (
                            <Text style={styles.metaSubText}>Time: {prob.time_complexity}</Text>
                          ) : null}
                        </View>
                      </View>
                    </View>

                    <View style={styles.problemRowRight}>
                      <View style={[styles.diffPill, getDiffPillStyle(diffLower)]}>
                        <Text style={styles.diffPillText}>{prob.difficulty || 'Medium'}</Text>
                      </View>
                      <TouchableOpacity style={styles.solveBtn}>
                        <Text style={styles.solveBtnText}>{isSolved ? 'Re-solve' : 'Solve'}</Text>
                        <Feather name="arrow-right" size={14} color="#FFFFFF" />
                      </TouchableOpacity>
                    </View>
                  </TouchableOpacity>
                );
              })}
            </View>
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

function getDiffPillStyle(diff: string) {
  if (diff === 'basic' || diff === 'easy') return { backgroundColor: '#DCFCE7', borderColor: '#166534' };
  if (diff === 'hard') return { backgroundColor: '#FFE4E6', borderColor: '#9F1239' };
  return { backgroundColor: '#FEF3C7', borderColor: '#92400E' };
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
  scrollContent: {
    padding: 16,
  },
  header: {
    marginBottom: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: '800',
    color: '#0F172A',
  },
  subtitle: {
    fontSize: 14,
    color: '#64748B',
    marginTop: 4,
  },
  progressCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    padding: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    shadowColor: '#000',
    shadowOpacity: 0.04,
    shadowRadius: 6,
    elevation: 2,
  },
  progressTopRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  progressLabel: {
    fontSize: 11,
    fontWeight: '800',
    color: '#64748B',
    letterSpacing: 0.6,
  },
  progressValue: {
    fontSize: 16,
    fontWeight: '700',
    color: '#0F172A',
    marginTop: 2,
  },
  streakBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#FEF3C7',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: '#F59E0B',
  },
  streakText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#B45309',
  },
  catProgressTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: '#475569',
    marginTop: 14,
    marginBottom: 8,
  },
  catProgressScroll: {
    flexDirection: 'row',
  },
  catProgressChip: {
    backgroundColor: '#F1F5F9',
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 8,
    marginRight: 8,
    alignItems: 'center',
  },
  catNameText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#334155',
  },
  catRatioText: {
    fontSize: 11,
    color: Palette.primary,
    fontWeight: '600',
    marginTop: 2,
  },
  filterSection: {
    backgroundColor: '#FFFFFF',
    borderRadius: 14,
    padding: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  searchRow: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 14,
  },
  searchBox: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#F8FAFC',
    borderRadius: 8,
    paddingHorizontal: 12,
    borderWidth: 1,
    borderColor: '#CBD5E1',
  },
  searchInput: {
    flex: 1,
    height: 40,
    fontSize: 14,
    color: '#0F172A',
  },
  searchBtn: {
    backgroundColor: Palette.primary,
    borderRadius: 8,
    paddingHorizontal: 16,
    justifyContent: 'center',
    alignItems: 'center',
  },
  searchBtnText: {
    color: '#FFFFFF',
    fontWeight: '700',
    fontSize: 14,
  },
  filterRowContainer: {
    marginBottom: 12,
  },
  filterLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: '#475569',
    marginBottom: 6,
  },
  filterChip: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
    backgroundColor: '#F1F5F9',
    marginRight: 8,
  },
  filterChipActive: {
    backgroundColor: Palette.primary,
  },
  filterChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
  },
  filterChipTextActive: {
    color: '#FFFFFF',
  },
  subFiltersRow: {
    gap: 10,
  },
  subFilterGroup: {
    flexDirection: 'row',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: 6,
  },
  subFilterLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: '#64748B',
    width: 70,
  },
  chipsWrap: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
    flex: 1,
  },
  miniChip: {
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
    backgroundColor: '#F1F5F9',
  },
  miniChipActive: {
    backgroundColor: '#0F172A',
  },
  miniChipText: {
    fontSize: 11,
    color: '#475569',
    fontWeight: '600',
  },
  miniChipTextActive: {
    color: '#FFFFFF',
  },
  problemsContainer: {
    marginBottom: 20,
  },
  sectionHeaderRow: {
    marginBottom: 12,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#0F172A',
  },
  sectionSubtitle: {
    fontSize: 13,
    color: '#64748B',
    marginTop: 2,
  },
  problemsGrid: {
    gap: 10,
  },
  problemRowCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 10,
    padding: 14,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  problemRowLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    flex: 1,
  },
  solvedStatusCircle: {
    width: 28,
    height: 28,
    borderRadius: 14,
    backgroundColor: '#F1F5F9',
    justifyContent: 'center',
    alignItems: 'center',
  },
  solvedStatusDone: {
    backgroundColor: '#10B981',
  },
  problemNumText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#64748B',
  },
  problemTitleBox: {
    flex: 1,
  },
  problemItemTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: '#0F172A',
  },
  problemMetaRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginTop: 3,
  },
  categoryBadge: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.primary,
    backgroundColor: '#EFF6FF',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
  },
  metaSubText: {
    fontSize: 11,
    color: '#64748B',
  },
  problemRowRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  diffPill: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    borderWidth: 1,
  },
  diffPillText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#0F172A',
  },
  solveBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: Palette.primary,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 6,
  },
  solveBtnText: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: '700',
  },
  emptyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 30,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  emptyTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#0F172A',
    marginTop: 10,
  },
  emptySub: {
    fontSize: 13,
    color: '#64748B',
    marginTop: 4,
  },
});
