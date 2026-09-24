import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useState } from 'react';
import {
  Modal,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';
import { DSA_TOPICS_LIST, DsaTopic, getDsaTopic } from '../data/dsaData';

export default function DsaPracticePage() {
  const [selectedLang, setSelectedLang] = useState<'c' | 'python'>('c');
  const [activeTopic, setActiveTopic] = useState<DsaTopic | null>(null);

  const isC = selectedLang === 'c';

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title={`DSA in ${isC ? 'C' : 'Python'}`} subtitle="18 Core Topic Roadmap" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header Title */}
        <View style={styles.header}>
          <Text style={styles.title}>Data Structures & Algorithms</Text>
          <Text style={styles.subtitle}>Choose your programming language track and master DSA systematically.</Text>
        </View>

        {/* 1. Language Track Switcher (DSA in C vs DSA in Python) */}
        <View style={styles.langSwitcher}>
          <TouchableOpacity
            style={[styles.langBtn, isC && styles.langBtnActive]}
            onPress={() => setSelectedLang('c')}
            activeOpacity={0.85}
          >
            <View style={[styles.langIconBox, isC && styles.langIconBoxActive]}>
              <Text style={[styles.langIconText, isC && { color: '#FFFFFF' }]}>C</Text>
            </View>
            <View>
              <Text style={[styles.langBtnTitle, isC && styles.langBtnTitleActive]}>DSA in C</Text>
              <Text style={styles.langBtnSub}>Pointers, Structs, Memory</Text>
            </View>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.langBtn, !isC && styles.langBtnActive]}
            onPress={() => setSelectedLang('python')}
            activeOpacity={0.85}
          >
            <View style={[styles.langIconBox, !isC && { backgroundColor: Palette.primary }]}>
              <Text style={[styles.langIconText, !isC && { color: '#FFFFFF' }]}>Py</Text>
            </View>
            <View>
              <Text style={[styles.langBtnTitle, !isC && styles.langBtnTitleActive]}>DSA in Python</Text>
              <Text style={styles.langBtnSub}>Lists, Dicts, Dynamic OOP</Text>
            </View>
          </TouchableOpacity>
        </View>

        {/* Progress Banner */}
        <View style={styles.progressCard}>
          <View style={styles.progressTopRow}>
            <View>
              <Text style={styles.progressLabel}>CURRICULUM ROADMAP</Text>
              <Text style={styles.progressValue}>18 Structured Topics in {isC ? 'C' : 'Python'}</Text>
            </View>
            <View style={styles.progressBadge}>
              <Text style={styles.progressBadgeText}>3/18 Done</Text>
            </View>
          </View>
          <ProgressBar progress={3 / 18} color={Palette.primary} />
          <Text style={styles.progressMeta}>Theory • Code Syntax • MCQs • Coding Problems</Text>
        </View>

        {/* 18 DSA Topics List */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>18 Comprehensive Modules</Text>
          <Text style={styles.sectionSubtitle}>Click any topic to explore language syntax, MCQs, and solve code</Text>
        </View>

        <View style={styles.topicsGrid}>
          {DSA_TOPICS_LIST.map((topicName, idx) => {
            const isCompleted = idx < 3;
            const isInProgress = idx === 3;

            return (
              <TouchableOpacity
                key={topicName}
                style={[
                  styles.topicCard,
                  isInProgress && styles.topicCardActive,
                ]}
                onPress={() => {
                  const topicData = getDsaTopic(selectedLang, topicName);
                  setActiveTopic(topicData);
                }}
                activeOpacity={0.8}
              >
                <View style={styles.topicCardLeft}>
                  <View
                    style={[
                      styles.nodeIndexCircle,
                      isCompleted && styles.nodeDone,
                      isInProgress && styles.nodeCurrent,
                    ]}
                  >
                    {isCompleted ? (
                      <Feather name="check" size={12} color="#FFFFFF" />
                    ) : (
                      <Text style={[styles.nodeIndexNum, isInProgress && { color: '#FFFFFF' }]}>
                        {idx + 1}
                      </Text>
                    )}
                  </View>

                  <View style={styles.topicInfo}>
                    <Text style={styles.topicName}>{idx + 1}. {topicName}</Text>
                    <Text style={styles.topicMeta}>
                      Theory • {isC ? 'C Code' : 'Python Code'} • MCQs • Practice
                    </Text>
                  </View>
                </View>

                <Feather
                  name="chevron-right"
                  size={18}
                  color={isInProgress ? Palette.primary : Palette.textMuted}
                />
              </TouchableOpacity>
            );
          })}
        </View>
      </ScrollView>

      {/* DSA Topic Deep Dive Modal */}
      {activeTopic && (
        <Modal
          animationType="slide"
          transparent
          visible={!!activeTopic}
          onRequestClose={() => setActiveTopic(null)}
        >
          <View style={styles.modalOverlay}>
            <View style={styles.modalContent}>
              <View style={styles.modalHeader}>
                <View style={{ flex: 1 }}>
                  <Text style={styles.modalBadgeText}>DSA IN {isC ? 'C' : 'PYTHON'}</Text>
                  <Text style={styles.modalTitle}>{activeTopic.name}</Text>
                </View>
                <TouchableOpacity onPress={() => setActiveTopic(null)} style={styles.modalCloseBtn}>
                  <Feather name="x" size={20} color={Palette.textSecondary} />
                </TouchableOpacity>
              </View>

              <ScrollView showsVerticalScrollIndicator={false} contentContainerStyle={styles.modalScroll}>
                {/* Complexity Bar */}
                <View style={styles.complexityBox}>
                  <Feather name="activity" size={14} color={Palette.primary} />
                  <Text style={styles.complexityText}>{activeTopic.complexity}</Text>
                </View>

                {/* Theory Section */}
                <Text style={styles.sheetSectionTitle}>1. Theory & Core Principles</Text>
                <Text style={styles.sheetBodyText}>{activeTopic.theory}</Text>

                {/* Syntax & Code Box in C/Python */}
                <Text style={[styles.sheetSectionTitle, { marginTop: 14 }]}>
                  2. {isC ? 'C Syntax & Memory Layout' : 'Python Implementation'}
                </Text>
                <View style={styles.codeSnippetBox}>
                  <Text style={styles.codeSnippetText}>{activeTopic.syntaxAndCode}</Text>
                </View>
                <Text style={styles.sheetExplanationText}>💡 {activeTopic.explanation}</Text>

                {/* Interview Questions */}
                <Text style={[styles.sheetSectionTitle, { marginTop: 14 }]}>3. Common Interview Questions</Text>
                <View style={styles.interviewList}>
                  {activeTopic.interviewQuestions.map((q, i) => (
                    <Text key={i} style={styles.interviewItem}>• {q}</Text>
                  ))}
                </View>

                {/* Actions Grid */}
                <View style={styles.modalActionButtons}>
                  <TouchableOpacity
                    style={styles.solveBtn}
                    onPress={() => {
                      const prob = activeTopic.problem;
                      setActiveTopic(null);
                      router.push({
                        pathname: '/coding/compiler',
                        params: {
                          langId: selectedLang,
                          langName: isC ? 'C' : 'Python 3',
                          initialCode: prob.starterCode,
                        },
                      });
                    }}
                    activeOpacity={0.85}
                  >
                    <Feather name="terminal" size={15} color="#FFFFFF" />
                    <Text style={styles.solveBtnText}>Open in Coding IDE ({activeTopic.problem.title})</Text>
                  </TouchableOpacity>

                  <TouchableOpacity
                    style={styles.quizBtn}
                    onPress={() => {
                      setActiveTopic(null);
                      router.push({
                        pathname: '/quizzpage',
                        params: {
                          topic: `${activeTopic.name} (${isC ? 'C' : 'Python'})`,
                          count: '5',
                        },
                      });
                    }}
                    activeOpacity={0.85}
                  >
                    <Feather name="check-circle" size={15} color={Palette.primary} />
                    <Text style={styles.quizBtnText}>Take Topic MCQ Quiz</Text>
                  </TouchableOpacity>
                </View>
              </ScrollView>
            </View>
          </View>
        </Modal>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  header: { marginBottom: 18 },
  title: { fontSize: 22, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  subtitle: { fontSize: 13.5, color: Palette.textSecondary },
  langSwitcher: { flexDirection: 'row', gap: 12, marginBottom: 18 },
  langBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  langBtnActive: { borderColor: Palette.primary, borderWidth: 1.5 },
  langIconBox: { width: 36, height: 36, borderRadius: 8, backgroundColor: Palette.backgroundSecondary, alignItems: 'center', justifyContent: 'center' },
  langIconBoxActive: { backgroundColor: Palette.primary },
  langIconText: { fontSize: 14, fontWeight: '800', color: Palette.textTitle },
  langBtnTitle: { fontSize: 14, fontWeight: '800', color: Palette.textTitle },
  langBtnTitleActive: { color: Palette.primary },
  langBtnSub: { fontSize: 11, color: Palette.textSecondary, marginTop: 1 },
  progressCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 22,
    ...Shadows.card,
  },
  progressTopRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  progressLabel: { fontSize: 10.5, fontWeight: '800', color: Palette.primary, letterSpacing: 0.8 },
  progressValue: { fontSize: 15, fontWeight: '700', color: Palette.textTitle, marginTop: 2 },
  progressBadge: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 4, borderRadius: 6 },
  progressBadgeText: { fontSize: 11.5, fontWeight: '700', color: Palette.primary },
  progressMeta: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 8 },
  sectionHeaderRow: { marginBottom: 12 },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  topicsGrid: { gap: 10 },
  topicCard: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  topicCardActive: { borderColor: Palette.primaryBorder, borderWidth: 1.5 },
  topicCardLeft: { flexDirection: 'row', alignItems: 'center', gap: 12, flex: 1, marginRight: 8 },
  nodeIndexCircle: { width: 28, height: 28, borderRadius: 14, backgroundColor: Palette.backgroundSecondary, alignItems: 'center', justifyContent: 'center' },
  nodeDone: { backgroundColor: Palette.success },
  nodeCurrent: { backgroundColor: Palette.primary },
  nodeIndexNum: { fontSize: 11, fontWeight: '800', color: Palette.textSecondary },
  topicInfo: { flex: 1 },
  topicName: { fontSize: 14.5, fontWeight: '700', color: Palette.textTitle },
  topicMeta: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 2 },
  modalOverlay: { flex: 1, backgroundColor: 'rgba(15, 23, 42, 0.5)', justifyContent: 'flex-end' },
  modalContent: {
    backgroundColor: '#FFFFFF',
    borderTopLeftRadius: 24,
    borderTopRightRadius: 24,
    maxHeight: '85%',
    padding: 20,
    paddingBottom: 36,
  },
  modalHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 14 },
  modalBadgeText: { fontSize: 10.5, fontWeight: '800', color: Palette.primary, letterSpacing: 0.8 },
  modalTitle: { fontSize: 19, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
  modalCloseBtn: { padding: 4 },
  modalScroll: { paddingBottom: 20 },
  complexityBox: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: Palette.primaryLight,
    padding: 10,
    borderRadius: 8,
    marginBottom: 14,
  },
  complexityText: { fontSize: 12, fontWeight: '700', color: Palette.primary },
  sheetSectionTitle: { fontSize: 14, fontWeight: '800', color: Palette.textTitle, marginBottom: 6 },
  sheetBodyText: { fontSize: 13, color: Palette.textBody, lineHeight: 19 },
  codeSnippetBox: {
    backgroundColor: Palette.techNavy,
    borderRadius: 10,
    padding: 14,
    marginVertical: 8,
  },
  codeSnippetText: { fontFamily: 'monospace', fontSize: 12, color: '#E2E8F0', lineHeight: 18 },
  sheetExplanationText: { fontSize: 12.5, color: Palette.textSecondary, lineHeight: 18, marginBottom: 10 },
  interviewList: { gap: 6, marginBottom: 18 },
  interviewItem: { fontSize: 12.5, color: Palette.textBody, lineHeight: 18 },
  modalActionButtons: { gap: 10, marginTop: 10 },
  solveBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 13,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    ...Shadows.button,
  },
  solveBtnText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  quizBtn: {
    backgroundColor: Palette.primaryLight,
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
  },
  quizBtnText: { color: Palette.primary, fontSize: 14, fontWeight: '700' },
});
