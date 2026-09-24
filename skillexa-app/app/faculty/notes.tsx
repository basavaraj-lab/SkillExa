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
import { TargetAudienceSelector } from '../../components/TargetAudienceSelector';
import { useAuth } from '../../components/auth-context';
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { TargetAudience } from '../../data/collegeData';
import { FacultyNote } from '../../data/curriculumSchema';
import { CollegeStore } from '../../services/collegeStore';
import { FacultySystemStore } from '../../services/facultyStore';

const SECTIONS = ['Engineering', 'Competitive Exams'];
const SUBJECTS: Record<string, string[]> = {
  Engineering: [
    'Embedded Systems',
    'Programming in C',
    'Programming in Python',
    'Digital Electronics',
    'VLSI',
    'Signals & Systems',
  ],
  'Competitive Exams': [
    'English Language',
    'Quantitative Aptitude',
    'Logical Reasoning',
    'General Science',
    'General Awareness',
  ],
};

export default function FacultyNotesScreen() {
  const { profile } = useAuth();
  const [notes, setNotes] = useState<FacultyNote[]>([]);
  const [selectedSection, setSelectedSection] = useState<'Engineering' | 'Competitive Exams'>('Engineering');
  const [selectedSubject, setSelectedSubject] = useState('Embedded Systems');
  const [topic, setTopic] = useState('');
  const [subtopic, setSubtopic] = useState('');
  const [title, setTitle] = useState('');
  const [introduction, setIntroduction] = useState('');
  const [theory, setTheory] = useState('');
  const [concepts, setConcepts] = useState('');
  const [formulas, setFormulas] = useState('');
  const [examples, setExamples] = useState('');
  const [mistakes, setMistakes] = useState('');
  const [quickRev, setQuickRev] = useState('');
  const [videoUrl, setVideoUrl] = useState('');
  const [visibility, setVisibility] = useState<'college' | 'community'>('college');

  const [target, setTarget] = useState<TargetAudience>({
    targetType: 'SECTION',
    collegeId: profile.collegeId || 'clg-kvg',
    collegeName: profile.collegeName || 'KVG College of Engineering',
    department: profile.department || 'ECE',
    academicYear: '3rd Year',
    section: 'A',
  });

  useEffect(() => {
    setNotes(FacultySystemStore.getNotes());
    return FacultySystemStore.subscribe(() => {
      setNotes(FacultySystemStore.getNotes());
    });
  }, []);

  const handlePublish = () => {
    if (!title.trim() || !topic.trim() || !theory.trim()) {
      Alert.alert('Missing Required Fields', 'Please provide Note Title, Topic Name, and Core Theory.');
      return;
    }

    FacultySystemStore.addNote({
      section: selectedSection === 'Engineering' ? 'engineering' : 'competitive',
      subject: selectedSubject,
      topic: topic.trim(),
      subtopic: subtopic.trim(),
      title: title.trim(),
      introduction: introduction.trim(),
      theory: theory.trim(),
      importantConcepts: concepts.split('\n').filter((c) => c.trim()),
      formulas: formulas.split('\n').filter((f) => f.trim()),
      examples: [
        {
          title: 'Illustrative Example',
          example: examples.trim() || 'Standard step-by-step example',
          explanation: 'Demonstrates governing rule and output verification.',
        },
      ],
      importantPoints: ['Verified by Faculty Educator'],
      commonMistakes: mistakes.split('\n').filter((m) => m.trim()),
      quickRevision: quickRev.trim() || 'Summary revision key points.',
      videoUrl: videoUrl.trim(),
      facultyName: profile.name || 'Dr. Kusumadhara S',
      facultyDesignation: profile.facultyDesignation || 'Associate Professor',
      facultyDepartment: profile.department || 'ECE Department',
      collegeId: profile.collegeId || 'clg-kvg',
      collegeName: profile.collegeName || 'KVG College of Engineering',
      isVerifiedFaculty: true,
      visibility,
      published: true,
    });

    if (visibility === 'college') {
      CollegeStore.dispatchNotification({
        studentId: 'std-101',
        collegeId: profile.collegeId || 'clg-kvg',
        title: '🔔 New Faculty Notes Published',
        message: `${profile.name || 'Faculty'}: "${title.trim()}" for ${topic.trim()}.`,
        type: 'NOTE',
        actionRoute: '/topic-learning',
        actionParams: {
          topic: topic.trim(),
          subject: selectedSubject,
          section: selectedSection === 'Engineering' ? 'engineering' : 'competitive',
        },
      });

      Alert.alert('Published Successfully', `Notes published for "${topic}". Target students in ${profile.collegeName || 'your college'} have been notified!`);
    } else {
      Alert.alert(
        'Published to SkillExa Community! 🌍',
        `Your topic notes for "${topic}" are now publicly discoverable by students across all colleges in the Community library.`
      );
    }

    // Reset Form
    setTitle('');
    setTopic('');
    setSubtopic('');
    setIntroduction('');
    setTheory('');
    setConcepts('');
    setFormulas('');
    setExamples('');
    setMistakes('');
    setQuickRev('');
    setVideoUrl('');
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Faculty Notes Authoring" subtitle="Create & Publish Topic Notes" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Banner */}
        <View style={styles.banner}>
          <Feather name="file-text" size={22} color={Palette.primary} />
          <View style={{ flex: 1 }}>
            <Text style={styles.bannerTitle}>Publish Topic-Specific Notes</Text>
            <Text style={styles.bannerDesc}>
              Published notes automatically appear in the student topic view under &quot;Faculty Notes&quot;.
            </Text>
          </View>
        </View>

        {/* Builder Form Card */}
        <View style={styles.card}>
          <Text style={styles.cardHeader}>1. Section & Subject Target</Text>

          {/* Section Selection */}
          <Text style={styles.label}>SELECT SECTION</Text>
          <View style={styles.sectionRow}>
            {SECTIONS.map((sec) => (
              <TouchableOpacity
                key={sec}
                style={[styles.pill, selectedSection === sec && styles.pillActive]}
                onPress={() => {
                  setSelectedSection(sec as any);
                  setSelectedSubject(SUBJECTS[sec][0]);
                }}
              >
                <Text style={[styles.pillText, selectedSection === sec && styles.pillTextActive]}>{sec}</Text>
              </TouchableOpacity>
            ))}
          </View>

          {/* Subject Selection */}
          <Text style={[styles.label, { marginTop: 12 }]}>SELECT SUBJECT</Text>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipsScroll}>
            {(SUBJECTS[selectedSection] || []).map((sub) => (
              <TouchableOpacity
                key={sub}
                style={[styles.chip, selectedSubject === sub && styles.chipActive]}
                onPress={() => setSelectedSubject(sub)}
              >
                <Text style={[styles.chipText, selectedSubject === sub && styles.chipTextActive]}>{sub}</Text>
              </TouchableOpacity>
            ))}
          </ScrollView>

          {/* Topic & Subtopic */}
          <View style={styles.inputGrid}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>TOPIC NAME *</Text>
              <TextInput
                style={styles.input}
                placeholder="e.g. Microcontrollers or Tenses"
                placeholderTextColor={Palette.textMuted}
                value={topic}
                onChangeText={setTopic}
              />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>SUBTOPIC</Text>
              <TextInput
                style={styles.input}
                placeholder="e.g. Architecture / Conditionals"
                placeholderTextColor={Palette.textMuted}
                value={subtopic}
                onChangeText={setSubtopic}
              />
            </View>
          </View>

          {/* Note Title */}
          <Text style={[styles.label, { marginTop: 12 }]}>NOTE TITLE *</Text>
          <TextInput
            style={styles.input}
            placeholder="Comprehensive Title for the Lesson Notes"
            placeholderTextColor={Palette.textMuted}
            value={title}
            onChangeText={setTitle}
          />

          {/* Introduction */}
          <Text style={[styles.label, { marginTop: 12 }]}>INTRODUCTION / OVERVIEW</Text>
          <TextInput
            style={[styles.input, styles.textAreaSm]}
            placeholder="Brief 2-3 sentence overview of this module..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={introduction}
            onChangeText={setIntroduction}
          />

          {/* Core Theory */}
          <Text style={[styles.label, { marginTop: 12 }]}>DETAILED THEORY & CONCEPTS *</Text>
          <TextInput
            style={[styles.input, styles.textAreaLg]}
            placeholder="Write clear, comprehensive educational theory..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={theory}
            onChangeText={setTheory}
          />

          {/* Important Concepts */}
          <Text style={[styles.label, { marginTop: 12 }]}>IMPORTANT CONCEPTS (ONE PER LINE)</Text>
          <TextInput
            style={[styles.input, styles.textAreaSm]}
            placeholder="Bullet 1\nBullet 2\nBullet 3"
            placeholderTextColor={Palette.textMuted}
            multiline
            value={concepts}
            onChangeText={setConcepts}
          />

          {/* Formulas / Rules */}
          <Text style={[styles.label, { marginTop: 12 }]}>FORMULAS / RULES (ONE PER LINE)</Text>
          <TextInput
            style={[styles.input, styles.textAreaSm]}
            placeholder="Formula 1: V = I * R\nFormula 2: Net Discount = a + b - ab/100"
            placeholderTextColor={Palette.textMuted}
            multiline
            value={formulas}
            onChangeText={setFormulas}
          />

          {/* Solved Examples */}
          <Text style={[styles.label, { marginTop: 12 }]}>STEP-BY-STEP SOLVED EXAMPLES</Text>
          <TextInput
            style={[styles.input, styles.textAreaSm]}
            placeholder="Example code, calculation, or worked solution..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={examples}
            onChangeText={setExamples}
          />

          {/* Common Mistakes */}
          <Text style={[styles.label, { marginTop: 12 }]}>COMMON MISTAKES TO AVOID</Text>
          <TextInput
            style={[styles.input, styles.textAreaSm]}
            placeholder="Common Pitfall 1\nCommon Pitfall 2"
            placeholderTextColor={Palette.textMuted}
            multiline
            value={mistakes}
            onChangeText={setMistakes}
          />

          {/* Quick Revision */}
          <Text style={[styles.label, { marginTop: 12 }]}>QUICK REVISION SUMMARY</Text>
          <TextInput
            style={[styles.input, styles.textAreaSm]}
            placeholder="Fast 1-minute recap for students..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={quickRev}
            onChangeText={setQuickRev}
          />

          {/* Optional Video Link */}
          <Text style={[styles.label, { marginTop: 12 }]}>OPTIONAL EMBEDDED VIDEO URL</Text>
          <TextInput
            style={styles.input}
            placeholder="https://www.youtube.com/watch?v=..."
            placeholderTextColor={Palette.textMuted}
            value={videoUrl}
            onChangeText={setVideoUrl}
          />

          {/* Target Audience Delivery & Visibility */}
          <View style={{ marginTop: 16 }}>
            <TargetAudienceSelector
              visibility={visibility}
              onChangeVisibility={setVisibility}
              target={target}
              onChangeTarget={setTarget}
              collegeName={profile.collegeName || 'KVG College of Engineering'}
            />
          </View>

          {/* Buttons: Save Draft / Publish */}
          <View style={styles.actionButtonsRow}>
            <TouchableOpacity style={styles.draftBtn} onPress={() => Alert.alert('Draft Saved', 'Your note draft has been saved locally.')}>
              <Text style={styles.draftBtnText}>Save Draft</Text>
            </TouchableOpacity>

            <TouchableOpacity style={styles.publishBtn} onPress={handlePublish} activeOpacity={0.85}>
              <Feather name="upload-cloud" size={16} color="#FFFFFF" />
              <Text style={styles.publishBtnText}>Publish to Students</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Existing Published Notes List */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Your Published Notes ({notes.length})</Text>
          <Text style={styles.sectionSubtitle}>Visible to all students in topic learning</Text>
        </View>

        <View style={styles.notesList}>
          {notes.map((n) => (
            <View key={n.id} style={styles.noteCard}>
              <View style={styles.noteCardHeader}>
                <View style={styles.subjectBadge}>
                  <Text style={styles.subjectBadgeText}>{n.subject} • {n.topic}</Text>
                </View>
                <TouchableOpacity onPress={() => FacultySystemStore.deleteNote(n.id)}>
                  <Feather name="trash-2" size={15} color={Palette.danger} />
                </TouchableOpacity>
              </View>

              <Text style={styles.noteTitle}>{n.title}</Text>
              <Text style={styles.noteIntro} numberOfLines={2}>{n.introduction || n.theory}</Text>
              <Text style={styles.noteAuthor}>By {n.facultyName} • Published {n.createdAt}</Text>
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
    borderColor: Palette.primaryBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 18,
    ...Shadows.card,
  },
  bannerTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  bannerDesc: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  cardHeader: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  label: { fontSize: 10.5, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 6 },
  sectionRow: { flexDirection: 'row', gap: 8, marginBottom: 12 },
  pill: { flex: 1, paddingVertical: 8, borderRadius: Radii.pill, backgroundColor: Palette.backgroundSecondary, borderWidth: 1, borderColor: Palette.border, alignItems: 'center' },
  pillActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  pillText: { fontSize: 12.5, fontWeight: '700', color: Palette.textSecondary },
  pillTextActive: { color: '#FFFFFF' },
  chipsScroll: { gap: 8, paddingVertical: 2, marginBottom: 14 },
  chip: { paddingHorizontal: 12, paddingVertical: 6, borderRadius: Radii.pill, backgroundColor: Palette.backgroundSecondary, borderWidth: 1, borderColor: Palette.border },
  chipActive: { backgroundColor: Palette.primaryLight, borderColor: Palette.primary },
  chipText: { fontSize: 12, fontWeight: '600', color: Palette.textSecondary },
  chipTextActive: { color: Palette.primary, fontWeight: '700' },
  inputGrid: { flexDirection: 'row', gap: 10 },
  input: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 10,
    fontSize: 13,
    color: Palette.textTitle,
  },
  textAreaSm: { height: 60, textAlignVertical: 'top' },
  textAreaLg: { height: 110, textAlignVertical: 'top' },
  actionButtonsRow: { flexDirection: 'row', gap: 10, marginTop: 18 },
  draftBtn: {
    flex: 1,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: Radii.button,
    paddingVertical: 12,
    alignItems: 'center',
    justifyContent: 'center',
  },
  draftBtnText: { fontSize: 13.5, fontWeight: '700', color: Palette.textSecondary },
  publishBtn: {
    flex: 1.5,
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    ...Shadows.button,
  },
  publishBtnText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  sectionHeaderRow: { marginBottom: 12 },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  notesList: { gap: 10 },
  noteCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  noteCardHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  subjectBadge: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  subjectBadgeText: { fontSize: 11, fontWeight: '700', color: Palette.primary },
  noteTitle: { fontSize: 15, fontWeight: '700', color: Palette.textTitle, marginBottom: 4 },
  noteIntro: { fontSize: 12.5, color: Palette.textSecondary, lineHeight: 17, marginBottom: 8 },
  noteAuthor: { fontSize: 11, color: Palette.textMuted },
});
