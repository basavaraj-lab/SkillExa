import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  Dimensions,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { PYTHON_FUNDAMENTALS_17_TOPICS, TopicItem } from '../data/topicCatalogData';
import { ApiClient } from '../services/api';

const { width } = Dimensions.get('window');
const isDesktop = width > 768;

export default function CodingProblemsPage() {
  const params = useLocalSearchParams<{ language?: string }>();
  const initialLanguage = (typeof params.language === 'string' && params.language) ? params.language.toLowerCase() : 'python';
  const [selectedLanguage, setSelectedLanguage] = useState<string>(initialLanguage);
  const [topics, setTopics] = useState<TopicItem[]>(PYTHON_FUNDAMENTALS_17_TOPICS);
  const [categoryName, setCategoryName] = useState<string>('Python Track (67 Topics)');

  useEffect(() => {
    if (params.language && typeof params.language === 'string') {
      const paramLang = params.language.toLowerCase();
      if (paramLang !== selectedLanguage) {
        setSelectedLanguage(paramLang);
      }
    }
  }, [params.language]);

  const languages = [
    { key: 'python', label: '🐍 Python', count: '67 Topics' },
    { key: 'c', label: '⚡ C Program', count: '54 Topics' },
    { key: 'cpp', label: '🚀 C++', count: '73 Topics' },
    { key: 'java', label: '☕ Java', count: '120 Topics' },
    { key: 'js', label: '🌐 JavaScript', count: '108 Topics' },
  ];

  useEffect(() => {
    let isMounted = true;
    ApiClient.getTopics(selectedLanguage).then((res) => {
      if (isMounted && res.success && res.data && res.data.topics) {
        setCategoryName(res.data.category_name || `${selectedLanguage.toUpperCase()} Track (${res.data.topics.length} Topics)`);
        setTopics(
          res.data.topics.map((t: any) => ({
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

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#090D16" />

      {/* Top Navbar matching Screenshot 1 */}
      <View style={styles.navbar}>
        <View style={styles.brandRow}>
          <View style={styles.brandLogo}>
            <Feather name="code" size={20} color="#FFFFFF" />
          </View>
          <Text style={styles.brandText}>
            SkillExa {selectedLanguage.toUpperCase() === 'CPP' ? 'C++' : selectedLanguage.toUpperCase()} Track
          </Text>
        </View>

        {isDesktop && (
          <View style={styles.navLinks}>
            <TouchableOpacity onPress={() => router.push('/home')}>
              <Text style={styles.navLinkText}>🏠 Home</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => setSelectedLanguage('python')}>
              <Text style={[styles.navLinkText, styles.navLinkActive]}>🌐 Languages</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => router.push('/dsa-practice')}>
              <Text style={styles.navLinkText}>🎓 DSA Practice</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => router.push('/mock-interviews')}>
              <Text style={styles.navLinkText}>💬 AI Mock Interview</Text>
            </TouchableOpacity>
            <TouchableOpacity onPress={() => router.push('/resume-builder')}>
              <Text style={styles.navLinkText}>📄 Resume Builder</Text>
            </TouchableOpacity>
          </View>
        )}
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Language Selection Tabs */}
        <View style={styles.langTabsContainer}>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.langTabsScroll}>
            {languages.map((lang) => {
              const isActive = selectedLanguage === lang.key;
              return (
                <TouchableOpacity
                  key={lang.key}
                  style={[styles.langTabBtn, isActive && styles.langTabBtnActive]}
                  onPress={() => setSelectedLanguage(lang.key)}
                  activeOpacity={0.8}
                >
                  <Text style={[styles.langTabText, isActive && styles.langTabTextActive]}>
                    {lang.label}
                  </Text>
                  <View style={[styles.langBadge, isActive && styles.langBadgeActive]}>
                    <Text style={[styles.langBadgeText, isActive && styles.langBadgeTextActive]}>
                      {lang.count}
                    </Text>
                  </View>
                </TouchableOpacity>
              );
            })}
          </ScrollView>
        </View>

        {/* Category Header matching Screenshot 1 */}
        <View style={styles.categoryHeaderRow}>
          <Feather name="folder" size={22} color="#38BDF8" />
          <Text style={styles.categoryTitle}>{categoryName}</Text>
        </View>

        {/* 4-Column Responsive Topic Cards Grid */}
        <View style={styles.topicsGrid}>
          {topics.map((topic) => {
            const isLocked = topic.status === 'LOCKED';
            const isInProgress = topic.status === 'IN_PROGRESS';
            const isCompleted = topic.status === 'COMPLETED';

            return (
              <TouchableOpacity
                key={topic.id}
                style={[
                  styles.topicCard,
                  isLocked && styles.topicCardLocked,
                  isInProgress && styles.topicCardActive,
                  isCompleted && styles.topicCardCompleted,
                ]}
                onPress={() => handleTopicPress(topic)}
                activeOpacity={0.85}
              >
                {/* Top Row: Topic # + Status Pill */}
                <View style={styles.cardTopRow}>
                  <View style={[styles.topicNumBadge, (isInProgress || isCompleted) && styles.topicNumBadgeActive]}>
                    <Text style={[styles.topicNumText, (isInProgress || isCompleted) && styles.topicNumTextActive]}>
                      Topic {topic.id}
                    </Text>
                  </View>

                  <View
                    style={[
                      styles.statusPill,
                      isCompleted
                        ? styles.statusPillCompleted
                        : isInProgress
                        ? styles.statusPillInProgress
                        : styles.statusPillLocked,
                    ]}
                  >
                    <Text
                      style={[
                        styles.statusPillText,
                        isCompleted
                          ? styles.statusPillTextCompleted
                          : isInProgress
                          ? styles.statusPillTextInProgress
                          : styles.statusPillTextLocked,
                      ]}
                    >
                      {topic.status}
                    </Text>
                  </View>
                </View>

                {/* Topic Title */}
                <Text style={styles.topicTitle} numberOfLines={2}>
                  {topic.title}
                </Text>

                {/* Completeness Bar */}
                <View style={styles.completenessSection}>
                  <Text style={styles.completenessLabel}>Completeness {topic.completeness}%</Text>
                  <View style={styles.progressBarTrack}>
                    <View
                      style={[
                        styles.progressBarFill,
                        { width: `${topic.completeness}%` },
                        isCompleted
                          ? { backgroundColor: '#10B981' }
                          : isInProgress
                          ? { backgroundColor: '#6366F1' }
                          : { backgroundColor: '#38BDF8' },
                      ]}
                    />
                  </View>
                </View>
              </TouchableOpacity>
            );
          })}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#090D16',
  },
  navbar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 24,
    paddingVertical: 14,
    backgroundColor: 'rgba(9, 13, 22, 0.95)',
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(99, 102, 241, 0.25)',
  },
  brandRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  brandLogo: {
    width: 38,
    height: 38,
    borderRadius: 10,
    backgroundColor: '#6366F1',
    alignItems: 'center',
    justifyContent: 'center',
  },
  brandText: {
    fontSize: 18,
    fontWeight: '800',
    color: '#FFFFFF',
    letterSpacing: 0.3,
  },
  navLinks: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 20,
  },
  navLinkText: {
    fontSize: 13,
    fontWeight: '600',
    color: '#9CA3AF',
  },
  navLinkActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  scrollContent: {
    paddingHorizontal: 24,
    paddingTop: 20,
    paddingBottom: 60,
  },
  langTabsContainer: {
    marginBottom: 20,
    backgroundColor: 'rgba(18, 26, 43, 0.85)',
    borderRadius: 14,
    padding: 8,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
  },
  langTabsScroll: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  langTabBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 10,
    backgroundColor: 'rgba(255, 255, 255, 0.04)',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
  },
  langTabBtnActive: {
    backgroundColor: '#6366F1',
    borderColor: '#6366F1',
  },
  langTabText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#9CA3AF',
  },
  langTabTextActive: {
    color: '#FFFFFF',
  },
  langBadge: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 6,
  },
  langBadgeActive: {
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
  },
  langBadgeText: {
    fontSize: 10,
    color: '#9CA3AF',
    fontWeight: '600',
  },
  langBadgeTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  categoryHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    marginBottom: 20,
  },
  categoryTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  topicsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 16,
  },
  topicCard: {
    width: isDesktop ? '23.5%' : width > 520 ? '48%' : '100%',
    backgroundColor: 'rgba(18, 26, 43, 0.85)',
    borderWidth: 1,
    borderColor: 'rgba(99, 102, 241, 0.3)',
    borderRadius: 16,
    padding: 16,
    justifyContent: 'space-between',
    minHeight: 130,
  },
  topicCardActive: {
    borderColor: '#6366F1',
    backgroundColor: 'rgba(28, 40, 66, 0.95)',
    shadowColor: '#6366F1',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 10,
  },
  topicCardCompleted: {
    borderColor: '#10B981',
    backgroundColor: 'rgba(16, 185, 129, 0.1)',
  },
  topicCardLocked: {
    opacity: 0.65,
    borderColor: 'rgba(255, 255, 255, 0.08)',
  },
  cardTopRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  topicNumBadge: {
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  topicNumBadgeActive: {
    backgroundColor: 'rgba(99, 102, 241, 0.2)',
  },
  topicNumText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#9CA3AF',
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
  },
  topicNumTextActive: {
    color: '#A5B4FC',
  },
  statusPill: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 999,
  },
  statusPillInProgress: {
    backgroundColor: 'rgba(99, 102, 241, 0.25)',
    borderWidth: 1,
    borderColor: 'rgba(99, 102, 241, 0.5)',
  },
  statusPillCompleted: {
    backgroundColor: 'rgba(16, 185, 129, 0.25)',
    borderWidth: 1,
    borderColor: '#10B981',
  },
  statusPillLocked: {
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
  },
  statusPillText: {
    fontSize: 9.5,
    fontWeight: '800',
    letterSpacing: 0.5,
  },
  statusPillTextInProgress: {
    color: '#A5B4FC',
  },
  statusPillTextCompleted: {
    color: '#10B981',
  },
  statusPillTextLocked: {
    color: '#6B7280',
  },
  topicTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: '#FFFFFF',
    marginBottom: 12,
    lineHeight: 20,
  },
  completenessSection: {
    gap: 4,
  },
  completenessLabel: {
    fontSize: 10,
    color: '#9CA3AF',
    fontWeight: '600',
  },
  progressBarTrack: {
    height: 3,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 2,
    overflow: 'hidden',
  },
  progressBarFill: {
    height: '100%',
    backgroundColor: '#38BDF8',
    borderRadius: 2,
  },
});