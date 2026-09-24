import { Feather } from '@expo/vector-icons';
import React, { useEffect, useState } from 'react';
import {
  Alert,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { QuestionMetadata } from '../../data/curriculumSchema';
import { FacultySystemStore } from '../../services/facultyStore';

export default function QuestionBankScreen() {
  const [bank, setBank] = useState<QuestionMetadata[]>([]);
  const [selectedSection, setSelectedSection] = useState<'all' | 'engineering' | 'competitive'>('all');
  const [selectedDiff, setSelectedDiff] = useState<'all' | 'easy' | 'medium' | 'hard'>('all');
  const [searchQuery, setSearchQuery] = useState('');

  // Add Question Modal State
  const [showAddForm, setShowAddForm] = useState(false);
  const [newSection, setNewSection] = useState<'engineering' | 'competitive'>('engineering');
  const [newSubject, setNewSubject] = useState('Embedded Systems');
  const [newTopic, setNewTopic] = useState('Microcontrollers');
  const [newQuestion, setNewQuestion] = useState('');
  const [optA, setOptA] = useState('');
  const [optB, setOptB] = useState('');
  const [optC, setOptC] = useState('');
  const [optD, setOptD] = useState('');
  const [correctAnswer, setCorrectAnswer] = useState(0);
  const [explanation, setExplanation] = useState('');
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('medium');

  useEffect(() => {
    setBank(FacultySystemStore.getQuestionBank());
    return FacultySystemStore.subscribe(() => {
      setBank(FacultySystemStore.getQuestionBank());
    });
  }, []);

  const filtered = bank.filter((q) => {
    const matchSec = selectedSection === 'all' || q.section === selectedSection;
    const matchDiff = selectedDiff === 'all' || q.difficulty === selectedDiff;
    const matchSearch =
      q.question.toLowerCase().includes(searchQuery.toLowerCase()) ||
      q.topic.toLowerCase().includes(searchQuery.toLowerCase()) ||
      q.subject.toLowerCase().includes(searchQuery.toLowerCase());
    return matchSec && matchDiff && matchSearch;
  });

  const handleSaveQuestion = () => {
    if (!newQuestion.trim() || !optA.trim() || !optB.trim() || !optC.trim() || !optD.trim()) {
      Alert.alert('Incomplete Form', 'Please provide question statement and all 4 options.');
      return;
    }

    FacultySystemStore.addQuestionToBank({
      section: newSection,
      category: newSection === 'engineering' ? 'subjects' : 'aptitude',
      subject: newSubject.trim(),
      topic: newTopic.trim(),
      difficulty,
      questionType: 'mcq',
      question: newQuestion.trim(),
      options: [optA.trim(), optB.trim(), optC.trim(), optD.trim()],
      correctAnswer,
      explanation: explanation.trim() || 'Verified by Faculty Educator.',
      marks: 2,
      negativeMarks: 0.5,
      isFacultyCreated: true,
      facultyName: 'Dr. Ramesh Kumar',
    });

    Alert.alert('Added to Bank', 'Question saved to Question Bank successfully.');
    setShowAddForm(false);
    setNewQuestion('');
    setOptA('');
    setOptB('');
    setOptC('');
    setOptD('');
    setExplanation('');
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Question Bank Management" subtitle="Filter, Search & Save Questions" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Top Control Bar */}
        <View style={styles.topControlRow}>
          <View style={styles.searchBox}>
            <Feather name="search" size={16} color={Palette.textSecondary} />
            <TextInput
              style={styles.searchInput}
              placeholder="Search by topic, keyword, or subject..."
              placeholderTextColor={Palette.textMuted}
              value={searchQuery}
              onChangeText={setSearchQuery}
            />
          </View>

          <TouchableOpacity style={styles.addBtn} onPress={() => setShowAddForm(!showAddForm)}>
            <Feather name={showAddForm ? 'x' : 'plus'} size={18} color="#FFFFFF" />
            <Text style={styles.addBtnText}>{showAddForm ? 'Close' : 'Add Question'}</Text>
          </TouchableOpacity>
        </View>

        {/* Section Filters */}
        <View style={styles.filterPillsRow}>
          {(['all', 'engineering', 'competitive'] as const).map((sec) => (
            <TouchableOpacity
              key={sec}
              style={[styles.filterPill, selectedSection === sec && styles.filterPillActive]}
              onPress={() => setSelectedSection(sec)}
            >
              <Text style={[styles.filterText, selectedSection === sec && styles.filterTextActive]}>
                {sec === 'all' ? 'All Sections' : sec.charAt(0).toUpperCase() + sec.slice(1)}
              </Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Form Drawer if open */}
        {showAddForm && (
          <View style={styles.addFormCard}>
            <Text style={styles.formTitle}>Add New Question to Bank</Text>

            <View style={styles.rowInputs}>
              <View style={{ flex: 1 }}>
                <Text style={styles.label}>SECTION</Text>
                <TextInput style={styles.input} value={newSection} onChangeText={(t) => setNewSection(t as any)} />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.label}>SUBJECT</Text>
                <TextInput style={styles.input} value={newSubject} onChangeText={setNewSubject} />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.label}>TOPIC</Text>
                <TextInput style={styles.input} value={newTopic} onChangeText={setNewTopic} />
              </View>
            </View>

            <Text style={[styles.label, { marginTop: 10 }]}>QUESTION STATEMENT</Text>
            <TextInput
              style={[styles.input, styles.textArea]}
              placeholder="Type question..."
              placeholderTextColor={Palette.textMuted}
              multiline
              value={newQuestion}
              onChangeText={setNewQuestion}
            />

            <Text style={[styles.label, { marginTop: 10 }]}>4 MULTIPLE-CHOICE OPTIONS</Text>
            {[
              { text: optA, set: setOptA, idx: 0 },
              { text: optB, set: setOptB, idx: 1 },
              { text: optC, set: setOptC, idx: 2 },
              { text: optD, set: setOptD, idx: 3 },
            ].map((o) => (
              <View key={o.idx} style={styles.optRow}>
                <TouchableOpacity
                  style={[styles.radio, correctAnswer === o.idx && styles.radioActive]}
                  onPress={() => setCorrectAnswer(o.idx)}
                >
                  {correctAnswer === o.idx && <View style={styles.radioDot} />}
                </TouchableOpacity>
                <TextInput
                  style={styles.optInput}
                  placeholder={`Option ${String.fromCharCode(65 + o.idx)}`}
                  placeholderTextColor={Palette.textMuted}
                  value={o.text}
                  onChangeText={o.set}
                />
              </View>
            ))}

            <Text style={[styles.label, { marginTop: 10 }]}>EXPLANATION</Text>
            <TextInput
              style={[styles.input, { height: 50 }]}
              placeholder="Explanation..."
              placeholderTextColor={Palette.textMuted}
              multiline
              value={explanation}
              onChangeText={setExplanation}
            />

            <TouchableOpacity style={styles.saveBankBtn} onPress={handleSaveQuestion}>
              <Text style={styles.saveBankBtnText}>Save to Question Bank</Text>
            </TouchableOpacity>
          </View>
        )}

        {/* Questions List */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Saved Question Repository ({filtered.length})</Text>
        </View>

        <View style={styles.list}>
          {filtered.map((item, idx) => (
            <View key={item.id} style={styles.bankCard}>
              <View style={styles.bankCardHeader}>
                <View style={styles.badge}>
                  <Text style={styles.badgeText}>{item.subject} • {item.topic}</Text>
                </View>
                <TouchableOpacity onPress={() => FacultySystemStore.deleteQuestionFromBank(item.id)}>
                  <Feather name="trash-2" size={15} color={Palette.danger} />
                </TouchableOpacity>
              </View>

              <Text style={styles.qStatement}>Q{idx + 1}: {item.question}</Text>

              <View style={styles.optionsList}>
                {item.options?.map((op, i) => (
                  <Text key={i} style={[styles.opText, i === item.correctAnswer && styles.opCorrect]}>
                    {String.fromCharCode(65 + i)}. {op} {i === item.correctAnswer ? '✓' : ''}
                  </Text>
                ))}
              </View>

              <Text style={styles.expBox}>💡 {item.explanation}</Text>
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
  topControlRow: { flexDirection: 'row', gap: 10, marginBottom: 12 },
  searchBox: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.input,
    paddingHorizontal: 12,
    borderWidth: 1,
    borderColor: Palette.border,
    gap: 8,
  },
  searchInput: { flex: 1, paddingVertical: 10, fontSize: 13, color: Palette.textTitle },
  addBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingHorizontal: 14,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    ...Shadows.button,
  },
  addBtnText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },
  filterPillsRow: { flexDirection: 'row', gap: 8, marginBottom: 16 },
  filterPill: { paddingHorizontal: 14, paddingVertical: 6, borderRadius: Radii.pill, backgroundColor: '#FFFFFF', borderWidth: 1, borderColor: Palette.border },
  filterPillActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  filterText: { fontSize: 12, fontWeight: '600', color: Palette.textSecondary },
  filterTextActive: { color: '#FFFFFF', fontWeight: '700' },
  addFormCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 16, borderWidth: 1, borderColor: Palette.border, marginBottom: 18, ...Shadows.card },
  formTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  rowInputs: { flexDirection: 'row', gap: 8 },
  label: { fontSize: 10, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 4 },
  input: { backgroundColor: Palette.backgroundSecondary, borderRadius: Radii.input, borderWidth: 1, borderColor: Palette.border, padding: 8, fontSize: 12.5, color: Palette.textTitle },
  textArea: { height: 55, textAlignVertical: 'top' },
  optRow: { flexDirection: 'row', alignItems: 'center', gap: 8, marginBottom: 6 },
  radio: { width: 20, height: 20, borderRadius: 10, borderWidth: 2, borderColor: Palette.border, alignItems: 'center', justifyContent: 'center' },
  radioActive: { borderColor: Palette.primary },
  radioDot: { width: 8, height: 8, borderRadius: 4, backgroundColor: Palette.primary },
  optInput: { flex: 1, backgroundColor: Palette.backgroundSecondary, borderRadius: Radii.input, borderWidth: 1, borderColor: Palette.border, paddingHorizontal: 8, paddingVertical: 6, fontSize: 12, color: Palette.textTitle },
  saveBankBtn: { backgroundColor: Palette.primary, borderRadius: Radii.button, paddingVertical: 11, alignItems: 'center', marginTop: 12 },
  saveBankBtnText: { color: '#FFFFFF', fontSize: 13.5, fontWeight: '700' },
  sectionHeaderRow: { marginBottom: 10 },
  sectionTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  list: { gap: 10 },
  bankCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  bankCardHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  badge: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  badgeText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  qStatement: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle, marginBottom: 8, lineHeight: 19 },
  optionsList: { gap: 3, marginBottom: 8 },
  opText: { fontSize: 12, color: Palette.textSecondary },
  opCorrect: { color: Palette.success, fontWeight: '700' },
  expBox: { backgroundColor: Palette.backgroundSecondary, padding: 8, borderRadius: 6, fontSize: 11.5, color: Palette.textBody },
});
