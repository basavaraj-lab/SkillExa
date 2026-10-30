import { Feather, Ionicons } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  useWindowDimensions,
  View,
} from 'react-native';
import { ThemeToggle } from '../components/theme-context';
import {
  C_ALL_54_TOPICS,
  CPP_ALL_73_TOPICS,
  JAVA_ALL_120_TOPICS,
  JS_ALL_108_TOPICS,
  PYTHON_ALL_67_TOPICS,
  TopicItem,
} from '../data/topicCatalogData';
import { ApiClient } from '../services/api';

export const getLanguageDetails = (langKey: string) => {
  const l = (langKey || 'python').toLowerCase();
  if (l === 'c') {
    return {
      title: 'C Programming Track (54 Topics)',
      shortTitle: 'C Track',
      dataset: C_ALL_54_TOPICS,
    };
  }
  if (l === 'cpp' || l === 'c++') {
    return {
      title: 'C++ Programming Track (73 Topics)',
      shortTitle: 'C++ Track',
      dataset: CPP_ALL_73_TOPICS,
    };
  }
  if (l === 'java') {
    return {
      title: 'Java Programming Track (120 Topics)',
      shortTitle: 'Java Track',
      dataset: JAVA_ALL_120_TOPICS,
    };
  }
  if (l === 'js' || l === 'javascript') {
    return {
      title: 'JavaScript Programming Track (108 Topics)',
      shortTitle: 'JavaScript Track',
      dataset: JS_ALL_108_TOPICS,
    };
  }
  return {
    title: 'Python Programming Track (67 Topics)',
    shortTitle: 'Python Track',
    dataset: PYTHON_ALL_67_TOPICS,
  };
};

export default function CodingProblemsPage() {
  const { width } = useWindowDimensions();
  const isLaptop = width >= 960;
  const isTablet = width >= 600 && width < 960;
  const isDesktop = width >= 768;

  const getCardWidth = () => {
    if (isLaptop) {
      return Platform.OS === 'web' ? ('calc(25% - 10.5px)' as any) : '23.8%';
    }
    if (isTablet) {
      return Platform.OS === 'web' ? ('calc(50% - 7px)' as any) : '48.5%';
    }
    return '100%';
  };

  const params = useLocalSearchParams<{ language?: string }>();
  const initialLanguage =
    typeof params.language === 'string' && params.language ? params.language.toLowerCase() : 'c';
  const [selectedLanguage, setSelectedLanguage] = useState<string>(initialLanguage);

  const initialInfo = getLanguageDetails(initialLanguage);
  const [topics, setTopics] = useState<TopicItem[]>(initialInfo.dataset);
  const [categoryName, setCategoryName] = useState<string>(initialInfo.title);
  const [shortTrackName, setShortTrackName] = useState<string>(initialInfo.shortTitle);

  useEffect(() => {
    if (params.language && typeof params.language === 'string') {
      const paramLang = params.language.toLowerCase();
      if (paramLang !== selectedLanguage) {
        setSelectedLanguage(paramLang);
      }
    }
  }, [params.language]);

  const languages = [
    { key: 'python', label: 'Python', icon: '🐍', count: '67 Topics' },
    { key: 'c', label: 'C Program', icon: '⚡', count: '54 Topics' },
    { key: 'cpp', label: 'C++', icon: '🚀', count: '73 Topics' },
    { key: 'java', label: 'Java', icon: '☕', count: '120 Topics' },
    { key: 'js', label: 'JavaScript', icon: '🌐', count: '108 Topics' },
  ];

  useEffect(() => {
    let isMounted = true;
    const currentInfo = getLanguageDetails(selectedLanguage);
    setCategoryName(currentInfo.title);
    setShortTrackName(currentInfo.shortTitle);
    setTopics(currentInfo.dataset);

    ApiClient.getTopics(selectedLanguage).then((res) => {
      if (isMounted && res && res.success) {
        const resTopics = res.data?.topics || (Array.isArray(res.data) ? res.data : null);
        if (resTopics && resTopics.length > 0) {
          const apiCatName =
            res.data?.category_name ||
            `${selectedLanguage.toUpperCase()} Programming Track (${resTopics.length} Topics)`;
          setCategoryName(apiCatName);
          setTopics(
            resTopics.map((t: any) => ({
              id: t.id,
              title: t.title,
              status: t.status,
              completeness: t.completeness,
              isUnlocked: t.is_unlocked,
              difficulty: t.difficulty,
              duration: t.duration,
            }))
          );
        }
      }
    });
    return () => {
      isMounted = false;
    };
  }, [selectedLanguage]);

  const handleTopicPress = (topic: TopicItem) => {
    if (!topic.isUnlocked && topic.status === 'LOCKED') {
      alert(`Topic ${topic.id}: "${topic.title}" is currently locked. Complete previous topics first to unlock!`);
      return;
    }
    router.push({
      pathname: '/topic-learning',
      params: {
        topicId: topic.id.toString(),
        language: selectedLanguage,
      },
    });
  };

  const handleGoBack = () => {
    if (router.canGoBack()) {
      router.back();
    } else {
      router.replace('/engineering' as any);
    }
  };

  const completedCount = topics.filter((t) => t.status === 'COMPLETED').length;
  const overallPercentage = topics.length > 0 ? Math.round((completedCount / topics.length) * 100) : 0;

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Top Navigation Row matching Screenshot: < on left, ... on right */}
      <View style={styles.topNavBar}>
        <TouchableOpacity style={styles.topNavBackBtn} onPress={handleGoBack} activeOpacity={0.7}>
          <Feather name="chevron-left" size={24} color="#0F172A" />
        </TouchableOpacity>

        <TouchableOpacity style={styles.topNavMoreBtn} activeOpacity={0.7}>
          <Feather name="more-horizontal" size={20} color="#0F172A" />
        </TouchableOpacity>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        <View style={[styles.container, isDesktop && styles.containerDesktop]}>
          {/* Header Card matching Screenshot: [< >] SkillExa C Track | ThemeToggle */}
          <View style={styles.trackHeaderCard}>
            <View style={styles.trackIconBox}>
              <Text style={styles.trackIconText}>{'< >'}</Text>
            </View>

            <View style={styles.trackInfoCol}>
              <Text style={styles.trackTitle}>SkillExa {shortTrackName}</Text>
              <Text style={styles.trackSubtitle}>Interactive Learning Path</Text>
            </View>

            <View style={styles.themeToggleBox}>
              <ThemeToggle />
            </View>
          </View>

          {/* Language Selection Pills Scroll */}
          <View style={styles.langPillsWrapper}>
            <ScrollView
              horizontal
              showsHorizontalScrollIndicator={false}
              contentContainerStyle={styles.langPillsScroll}
            >
              {languages.map((lang) => {
                const isActive = selectedLanguage === lang.key;
                return (
                  <TouchableOpacity
                    key={lang.key}
                    style={[styles.langPill, isActive && styles.langPillActive]}
                    onPress={() => setSelectedLanguage(lang.key)}
                    activeOpacity={0.8}
                  >
                    <Text style={styles.langEmoji}>{lang.icon}</Text>
                    <Text style={[styles.langPillLabel, isActive && styles.langPillLabelActive]}>
                      {lang.label}
                    </Text>
                    <View style={[styles.langCountBadge, isActive && styles.langCountBadgeActive]}>
                      <Text style={[styles.langCountBadgeText, isActive && styles.langCountBadgeTextActive]}>
                        {lang.count}
                      </Text>
                    </View>
                  </TouchableOpacity>
                );
              })}
            </ScrollView>
          </View>

          {/* Track Section Title Row matching Screenshot: [Folder] C Programming Track (54 Topics) | 0% Overall */}
          <View style={styles.trackSectionRow}>
            <View style={styles.trackSectionLeft}>
              <View style={styles.folderIconBox}>
                <Feather name="folder" size={18} color="#2563EB" />
              </View>
              <Text style={styles.trackSectionHeading}>{categoryName}</Text>
            </View>

            <View style={styles.overallPercentBadge}>
              <Text style={styles.overallPercentText}>{overallPercentage}% Overall</Text>
            </View>
          </View>

          {/* Topics Cards List matching Screenshot */}
          <View style={styles.topicsList}>
            {topics.map((topic) => {
              const isLocked = topic.status === 'LOCKED';
              const isInProgress = topic.status === 'IN_PROGRESS';
              const isCompleted = topic.status === 'COMPLETED';

              return (
                <TouchableOpacity
                  key={topic.id}
                  style={[
                    styles.topicCard,
                    { width: getCardWidth() },
                    isLaptop && styles.topicCardGrid,
                    isInProgress && styles.topicCardInProgress,
                    isCompleted && styles.topicCardCompleted,
                    isLocked && styles.topicCardLocked,
                  ]}
                  onPress={() => handleTopicPress(topic)}
                  activeOpacity={isLocked ? 0.9 : 0.75}
                >
                  {/* Top Row: Topic Pill + Status Pill */}
                  <View style={styles.cardHeaderRow}>
                    <View style={[styles.topicBadgePill, isInProgress && styles.topicBadgePillActive]}>
                      <Text style={[styles.topicBadgeText, isInProgress && styles.topicBadgeTextActive]}>
                        Topic {topic.id}
                      </Text>
                    </View>

                    {isCompleted ? (
                      <View style={styles.completedBadgePill}>
                        <Feather name="check" size={12} color="#10B981" />
                        <Text style={styles.completedBadgeText}>COMPLETED</Text>
                      </View>
                    ) : isInProgress ? (
                      <View style={styles.inProgressBadgePill}>
                        <Text style={styles.inProgressBadgeText}>IN_PROGRESS</Text>
                      </View>
                    ) : (
                      <View style={styles.lockedBadgePill}>
                        <Feather name="lock" size={11} color="#94A3B8" />
                        <Text style={styles.lockedBadgeText}>LOCKED</Text>
                      </View>
                    )}
                  </View>

                  {/* Middle Row: Title + Arrow */}
                  <View style={styles.cardTitleRow}>
                    <Text
                      style={[styles.cardTitleText, isLocked && styles.cardTitleTextLocked]}
                      numberOfLines={2}
                    >
                      {topic.title}
                    </Text>
                    {!isLocked && (
                      <Feather name="arrow-right" size={18} color="#2563EB" style={styles.arrowIcon} />
                    )}
                  </View>

                  {/* Bottom Row: Completeness + Status Meta */}
                  <View style={styles.cardFooterRow}>
                    <Text style={styles.completenessText}>
                      Completeness {topic.completeness || 0}%
                    </Text>
                    {isInProgress && (
                      <Text style={styles.readyToStartText}>Ready to start</Text>
                    )}
                    {isCompleted && (
                      <Text style={styles.completedMetaText}>Completed ✓</Text>
                    )}
                  </View>

                  {/* Progress Track Line across Bottom */}
                  <View style={styles.cardProgressTrack}>
                    <View
                      style={[
                        styles.cardProgressFill,
                        {
                          width: `${isCompleted ? 100 : topic.completeness || 0}%`,
                          backgroundColor: isCompleted ? '#10B981' : '#2563EB',
                        },
                      ]}
                    />
                  </View>
                </TouchableOpacity>
              );
            })}
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

  // Top Minimal Navigation Row
  topNavBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingTop: 8,
    paddingBottom: 6,
    backgroundColor: '#FFFFFF',
  },
  topNavBackBtn: {
    width: 36,
    height: 36,
    alignItems: 'flex-start',
    justifyContent: 'center',
  },
  topNavMoreBtn: {
    width: 36,
    height: 36,
    alignItems: 'flex-end',
    justifyContent: 'center',
  },

  scrollContent: {
    paddingHorizontal: 16,
    paddingTop: 4,
    paddingBottom: 90,
  },
  container: {
    width: '100%',
  },
  containerDesktop: {
    maxWidth: 1320,
    alignSelf: 'center',
  },

  // Track Header Card
  trackHeaderCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 14,
    paddingVertical: 12,
    marginBottom: 16,
    gap: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.04,
    shadowRadius: 2,
    elevation: 1,
  },
  trackIconBox: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    alignItems: 'center',
    justifyContent: 'center',
  },
  trackIconText: {
    fontSize: 16,
    fontWeight: '800',
    color: '#2563EB',
    letterSpacing: 1,
  },
  trackInfoCol: {
    flex: 1,
  },
  trackTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#0F172A',
    letterSpacing: -0.2,
  },
  trackSubtitle: {
    fontSize: 12.5,
    color: '#64748B',
    marginTop: 2,
  },
  themeToggleBox: {
    width: 40,
    height: 40,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFFFFF',
  },

  // Language Selection Pills Scroll
  langPillsWrapper: {
    marginBottom: 18,
  },
  langPillsScroll: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    paddingRight: 10,
  },
  langPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingVertical: 7,
    paddingHorizontal: 14,
    borderRadius: 22,
    gap: 8,
  },
  langPillActive: {
    backgroundColor: '#2563EB',
    borderColor: '#2563EB',
  },
  langEmoji: {
    fontSize: 14,
  },
  langPillLabel: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1E293B',
  },
  langPillLabelActive: {
    color: '#FFFFFF',
  },
  langCountBadge: {
    backgroundColor: '#EDF2F7',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 12,
  },
  langCountBadgeActive: {
    backgroundColor: '#1D4ED8',
  },
  langCountBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#64748B',
  },
  langCountBadgeTextActive: {
    color: '#FFFFFF',
  },

  // Track Section Row (Folder + Title + Overall %)
  trackSectionRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 16,
    gap: 10,
  },
  trackSectionLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    flex: 1,
  },
  folderIconBox: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    alignItems: 'center',
    justifyContent: 'center',
  },
  trackSectionHeading: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
    flexShrink: 1,
  },
  overallPercentBadge: {
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 14,
  },
  overallPercentText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#2563EB',
  },

  // Topics Grid / Stack (4 in a row on laptop, 1 by 1 on phone)
  topicsList: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 14,
  },
  topicCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 16,
    overflow: 'hidden',
  },
  topicCardGrid: {
    minHeight: 145,
    justifyContent: 'space-between',
  },
  topicCardInProgress: {
    borderWidth: 2,
    borderColor: '#2563EB',
  },
  topicCardCompleted: {
    borderWidth: 1.5,
    borderColor: '#86EFAC',
  },
  topicCardLocked: {
    borderColor: '#E5E7EB',
    backgroundColor: '#FFFFFF',
  },

  // Card Header Row (Topic # + Badge)
  cardHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  topicBadgePill: {
    backgroundColor: '#F1F5F9',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 8,
  },
  topicBadgePillActive: {
    backgroundColor: '#EFF6FF',
  },
  topicBadgeText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#64748B',
  },
  topicBadgeTextActive: {
    color: '#2563EB',
  },

  // Status Badges
  inProgressBadgePill: {
    backgroundColor: '#2563EB',
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
  },
  inProgressBadgeText: {
    fontSize: 10.5,
    fontWeight: '800',
    color: '#FFFFFF',
    letterSpacing: 0.5,
  },
  lockedBadgePill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 8,
  },
  lockedBadgeText: {
    fontSize: 10.5,
    fontWeight: '700',
    color: '#94A3B8',
    letterSpacing: 0.5,
  },
  completedBadgePill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#ECFDF5',
    borderWidth: 1,
    borderColor: '#A7F3D0',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 8,
  },
  completedBadgeText: {
    fontSize: 10.5,
    fontWeight: '800',
    color: '#059669',
    letterSpacing: 0.5,
  },

  // Card Title & Arrow
  cardTitleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  cardTitleText: {
    fontSize: 16.5,
    fontWeight: '800',
    color: '#0F172A',
    flex: 1,
    marginRight: 8,
  },
  cardTitleTextLocked: {
    color: '#1E293B',
  },
  arrowIcon: {
    marginLeft: 6,
  },

  // Card Footer Row
  cardFooterRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  completenessText: {
    fontSize: 12,
    color: '#64748B',
    fontWeight: '500',
  },
  readyToStartText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#2563EB',
  },
  completedMetaText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#10B981',
  },

  // Card Progress Track at Bottom
  cardProgressTrack: {
    height: 4,
    backgroundColor: '#F1F5F9',
    borderRadius: 2,
    overflow: 'hidden',
  },
  cardProgressFill: {
    height: '100%',
    borderRadius: 2,
  },
});
