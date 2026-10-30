import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  Linking,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { useAuth } from '../../components/auth-context';
import { AppHeader } from '../../components/common/AppHeader';
import { Radii } from '../../constants/theme';
import { ApiClient } from '../../services/api';

// Verified Competitive Subjects & Recommended Topics
const COMPETITIVE_SUBJECTS = [
  'Quantitative Aptitude',
  'Logical Reasoning',
  'Verbal English',
  'General Awareness',
  'General Science',
  'Computer Knowledge',
  'Mathematics',
  'Other',
];

const SUGGESTED_TOPICS: Record<string, string[]> = {
  'Quantitative Aptitude': [
    'Percentage & Profit/Loss',
    'Ratio & Proportion',
    'Time & Work, Pipes/Cisterns',
    'Time, Speed & Distance',
    'Simple & Compound Interest',
    'Number System & Simplification',
    'Permutation, Combination & Probability',
    'Data Interpretation (DI)',
    'Mensuration (2D & 3D)',
  ],
  'Logical Reasoning': [
    'Syllogisms & Deductive Logic',
    'Coding-Decoding',
    'Blood Relations',
    'Seating Arrangement & Puzzles',
    'Direction Sense Test',
    'Series & Analogy',
    'Statement & Assumptions',
  ],
  'Verbal English': [
    'Reading Comprehension',
    'Error Spotting & Grammar Rules',
    'Vocabulary, Synonyms & Antonyms',
    'Idioms & Phrases',
    'Cloze Test',
    'Para Jumbles',
    'Sentence Improvement',
  ],
  'General Awareness': [
    'Indian Polity & Constitution',
    'Modern Indian History',
    'Indian & World Geography',
    'Indian Economy & Budget',
    'Current Affairs 2026',
    'Awards & Honors',
  ],
  'General Science': [
    'Physics: Mechanics & Energy',
    'Chemistry: Common Elements & Compounds',
    'Biology: Human Body & Diseases',
    'Environmental Ecology',
    'Scientific Inventions & Discoveries',
  ],
  'Computer Knowledge': [
    'Fundamentals of Computer Hardware',
    'Operating Systems & Networking',
    'MS Office Shortcuts & Formulas',
    'Cyber Security & Internet Protocols',
    'DBMS & SQL Basics',
  ],
  Mathematics: [
    'Algebra & Quadratic Equations',
    'Trigonometry & Heights/Distances',
    'Coordinate Geometry',
    'Calculus Basics',
  ],
};

function formatBytes(bytes?: number): string {
  if (!bytes || bytes <= 0) return '1.2 MB';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
}

export default function FacultyCompetitiveNotesScreen() {
  const { profile } = useAuth();

  // Published notes state
  const [notes, setNotes] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [filterSubject, setFilterSubject] = useState('All');
  const [searchQuery, setSearchQuery] = useState('');

  // Upload Form State
  const [selectedSubject, setSelectedSubject] = useState('Quantitative Aptitude');
  const [customSubject, setCustomSubject] = useState('');
  const [isCustomSubject, setIsCustomSubject] = useState(false);
  const [topic, setTopic] = useState('');
  const [subtopic, setSubtopic] = useState('');
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [source, setSource] = useState('KVG Faculty Study Material');

  // File Upload State
  const [selectedFile, setSelectedFile] = useState<any>(null);
  const [selectedFileName, setSelectedFileName] = useState('');
  const [selectedFileSize, setSelectedFileSize] = useState<number | undefined>(undefined);
  const [isUploading, setIsUploading] = useState(false);

  const facultyName = profile?.name || 'Dr. Ramesh Kumar';
  const collegeName = profile?.collegeName || 'KVG College of Engineering';
  const departmentName = profile?.department || 'ECE';

  // Load published competitive notes
  const fetchCompetitiveNotes = async () => {
    try {
      setLoading(true);
      const res = await ApiClient.getCompetitiveNotes(
        filterSubject !== 'All' ? filterSubject : undefined,
        searchQuery
      );
      if (res?.data) {
        setNotes(res.data);
      }
    } catch (err) {
      console.warn('Error fetching competitive notes:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCompetitiveNotes();
  }, [filterSubject]);

  // File Picker for Web & Native
  const handlePickFile = () => {
    if (Platform.OS === 'web' && typeof document !== 'undefined') {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.pdf,.doc,.docx,.ppt,.pptx,.txt';
      input.onchange = (e: any) => {
        const file = e.target?.files?.[0];
        if (file) {
          setSelectedFile(file);
          setSelectedFileName(file.name);
          setSelectedFileSize(file.size);
          if (!title.trim()) {
            const cleanTitle = file.name.replace(/\.[^/.]+$/, '').replace(/[-_]/g, ' ');
            setTitle(cleanTitle);
          }
        }
      };
      input.click();
    } else {
      Alert.alert('File Picker', 'Please choose a study PDF document from your device.');
    }
  };

  const handleClearFile = () => {
    setSelectedFile(null);
    setSelectedFileName('');
    setSelectedFileSize(undefined);
  };

  // Upload and publish competitive note
  const handlePublishNote = async () => {
    const finalSubject = isCustomSubject ? customSubject.trim() : selectedSubject;

    if (!title.trim()) {
      Alert.alert('Missing Title', 'Please enter a title for the study note.');
      return;
    }
    if (!finalSubject) {
      Alert.alert('Missing Subject', 'Please select or specify a competitive subject.');
      return;
    }
    if (!topic.trim()) {
      Alert.alert('Missing Topic', 'Please specify a curriculum topic for this study note.');
      return;
    }

    setIsUploading(true);

    try {
      // 1. Prepare FormData for competitive server
      const formData = new FormData();
      formData.append('title', title.trim());
      formData.append('subject_name', finalSubject);
      formData.append('topic_name', topic.trim());
      formData.append('subtopic_name', subtopic.trim());
      formData.append('description', description.trim());
      formData.append('source', source.trim() || `${collegeName} Faculty Material`);
      formData.append('faculty_name', facultyName);
      formData.append('uploaded_by', facultyName);

      if (selectedFile) {
        formData.append('pdf', selectedFile);
        formData.append('file', selectedFile);
      }

      // 2. Upload directly to Competitive Server API (/api/faculty/notes)
      const res = await ApiClient.uploadCompetitiveNote(formData);

      if (res.success) {
        // Also sync to SkillExa Backend DB as a competitive note
        try {
          const backendFormData = new FormData();
          backendFormData.append('title', title.trim());
          backendFormData.append('description', description.trim());
          backendFormData.append('subject', finalSubject);
          backendFormData.append('topic', topic.trim());
          backendFormData.append('subtopic', subtopic.trim());
          backendFormData.append('section', 'competitive');
          backendFormData.append('visibility', 'college');
          if (selectedFile) backendFormData.append('file', selectedFile);
          await ApiClient.uploadFacultyNote(backendFormData);
        } catch (syncErr) {
          console.warn('Backend mirror sync note:', syncErr);
        }

        Alert.alert(
          'Note Published! 🎉',
          `"${title.trim()}" is now live in the Competitive Notes section for all students.`
        );

        // Reset form
        setTitle('');
        setTopic('');
        setSubtopic('');
        setDescription('');
        handleClearFile();
        if (isCustomSubject) {
          setCustomSubject('');
          setIsCustomSubject(false);
        }

        // Refresh notes list
        await fetchCompetitiveNotes();
      } else {
        throw new Error(res.message || 'Server rejected note upload.');
      }
    } catch (err: any) {
      console.error('Competitive note publish failed:', err);
      Alert.alert('Upload Failed', err?.message || 'Failed to publish note to Competitive Portal.');
    } finally {
      setIsUploading(false);
    }
  };

  // Delete note
  const handleDeleteNote = async (id: number | string, noteTitle: string) => {
    const doDelete = async () => {
      try {
        await ApiClient.deleteCompetitiveNote(id);
        setNotes((prev) => prev.filter((n) => String(n.id) !== String(id)));
        Alert.alert('Deleted', `"${noteTitle}" has been removed from the competitive portal.`);
      } catch (err: any) {
        console.error('Delete failed:', err);
        Alert.alert('Error', err?.message || 'Could not delete note.');
      }
    };

    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      if (window.confirm(`Are you sure you want to permanently delete "${noteTitle}" from Competitive Notes?`)) {
        await doDelete();
      }
    } else {
      Alert.alert(
        'Delete Note',
        `Are you sure you want to remove "${noteTitle}" from the Competitive Portal?`,
        [
          { text: 'Cancel', style: 'cancel' },
          { text: 'Delete', style: 'destructive', onPress: doDelete },
        ]
      );
    }
  };

  // Open PDF in browser or viewer
  const handleOpenPdf = (fileUrl?: string) => {
    if (!fileUrl) {
      Alert.alert('No Document', 'No physical PDF attachment is linked with this note.');
      return;
    }
    const fullUrl = fileUrl.startsWith('http')
      ? fileUrl
      : `http://localhost:3001${fileUrl.startsWith('/') ? '' : '/'}${fileUrl}`;

    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      window.open(fullUrl, '_blank');
    } else {
      Linking.openURL(fullUrl).catch(() => {
        Alert.alert('Error', 'Unable to open file link');
      });
    }
  };

  // Open Competitive Student Interface preview
  const handleOpenCompetitivePortal = () => {
    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      window.open('/competitive', '_blank');
    } else {
      router.push('/competitive' as any);
    }
  };

  const filteredNotes = notes.filter((n) => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase();
    return (
      (n.title || '').toLowerCase().includes(q) ||
      (n.subject_name || '').toLowerCase().includes(q) ||
      (n.topic_name || '').toLowerCase().includes(q) ||
      (n.description || '').toLowerCase().includes(q)
    );
  });

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        onBack={() => router.replace('/faculty-dashboard' as any)}
        title="Competitive Notes Upload"
        subtitle="Publish Aptitude & Govt Exam Study Materials Directly to Students"
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Banner with Live Competitive Portal Link */}
        <View style={styles.banner}>
          <View style={styles.bannerIconBox}>
            <Feather name="award" size={26} color="#4F46E5" />
          </View>
          <View style={{ flex: 1 }}>
            <View style={styles.badgeRow}>
              <View style={styles.bannerBadge}>
                <Text style={styles.bannerBadgeText}>COMPETITIVE EXAMS SUITE</Text>
              </View>
              <View style={styles.livePill}>
                <View style={styles.liveDot} />
                <Text style={styles.liveText}>AUTO-PUBLISH LIVE</Text>
              </View>
            </View>
            <Text style={styles.bannerTitle}>Upload Verified Competitive Study Notes</Text>
            <Text style={styles.bannerDesc}>
              Any notes uploaded here will immediately appear in the{' '}
              <Text style={{ fontWeight: '700', color: '#111827' }}>Competitive Notes</Text> section
              for students preparing for Campus Placements, Quantitative Aptitude, Banking, SSC, and Government Exams.
            </Text>
          </View>
          <TouchableOpacity
            style={styles.portalPreviewBtn}
            onPress={handleOpenCompetitivePortal}
            activeOpacity={0.8}
          >
            <Feather name="external-link" size={15} color="#FFFFFF" />
            <Text style={styles.portalPreviewBtnText}>View Student Notes</Text>
          </TouchableOpacity>
        </View>

        {/* Upload Form Card */}
        <View style={styles.card}>
          <View style={styles.cardHeader}>
            <View style={styles.cardHeaderLeft}>
              <View style={styles.iconCircle}>
                <Feather name="upload-cloud" size={20} color="#4F46E5" />
              </View>
              <View>
                <Text style={styles.cardTitle}>New Competitive Study Note</Text>
                <Text style={styles.cardSubtitle}>
                  Contributed by {facultyName} • {departmentName}, {collegeName}
                </Text>
              </View>
            </View>
          </View>

          {/* Subject Selector */}
          <Text style={styles.fieldLabel}>1. Select Competitive Subject *</Text>
          <View style={styles.subjectChipsRow}>
            {COMPETITIVE_SUBJECTS.map((sub) => {
              const isSelected = !isCustomSubject && selectedSubject === sub;
              return (
                <TouchableOpacity
                  key={sub}
                  style={[styles.subjectChip, isSelected && styles.subjectChipActive]}
                  onPress={() => {
                    if (sub === 'Other') {
                      setIsCustomSubject(true);
                    } else {
                      setIsCustomSubject(false);
                      setSelectedSubject(sub);
                    }
                  }}
                  activeOpacity={0.7}
                >
                  <Text style={[styles.subjectChipText, isSelected && styles.subjectChipTextActive]}>
                    {sub}
                  </Text>
                </TouchableOpacity>
              );
            })}
          </View>

          {isCustomSubject && (
            <View style={{ marginTop: 10 }}>
              <TextInput
                style={styles.input}
                placeholder="Enter custom subject name (e.g. Current Affairs 2026)"
                placeholderTextColor="#94A3B8"
                value={customSubject}
                onChangeText={setCustomSubject}
              />
            </View>
          )}

          {/* Topic Field with Suggestions */}
          <Text style={[styles.fieldLabel, { marginTop: 18 }]}>2. Topic Name *</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. Percentage & Profit/Loss, Syllogisms, Reading Comprehension..."
            placeholderTextColor="#94A3B8"
            value={topic}
            onChangeText={setTopic}
          />

          {/* Suggested Topic Quick Pills */}
          {SUGGESTED_TOPICS[selectedSubject] && (
            <View style={styles.suggestionsContainer}>
              <Text style={styles.suggestionsTitle}>Recommended Topics:</Text>
              <View style={styles.suggestionsPills}>
                {SUGGESTED_TOPICS[selectedSubject].map((item) => (
                  <TouchableOpacity
                    key={item}
                    style={[styles.pill, topic === item && styles.pillActive]}
                    onPress={() => setTopic(item)}
                    activeOpacity={0.7}
                  >
                    <Text style={[styles.pillText, topic === item && styles.pillTextActive]}>
                      {item}
                    </Text>
                  </TouchableOpacity>
                ))}
              </View>
            </View>
          )}

          {/* Subtopic / Concept Tag (Optional) */}
          <Text style={[styles.fieldLabel, { marginTop: 18 }]}>3. Subtopic / Topic Tag (Optional)</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. Shortcut Formulas, Solved PYQs, Concept Revision..."
            placeholderTextColor="#94A3B8"
            value={subtopic}
            onChangeText={setSubtopic}
          />

          {/* Notes Title */}
          <Text style={[styles.fieldLabel, { marginTop: 18 }]}>4. Note Title *</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. Quantitative Aptitude Master Compendium 2026"
            placeholderTextColor="#94A3B8"
            value={title}
            onChangeText={setTitle}
          />

          {/* Description / Summary */}
          <Text style={[styles.fieldLabel, { marginTop: 18 }]}>5. Summary / Key Highlights (Optional)</Text>
          <TextInput
            style={[styles.input, styles.textArea]}
            placeholder="Briefly describe what formulas, short tricks, or exam patterns this study document covers..."
            placeholderTextColor="#94A3B8"
            value={description}
            onChangeText={setDescription}
            multiline
            numberOfLines={3}
          />

          {/* Source / Attribution */}
          <Text style={[styles.fieldLabel, { marginTop: 18 }]}>6. Material Source / Attribution</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. KVG Faculty Study Material"
            placeholderTextColor="#94A3B8"
            value={source}
            onChangeText={setSource}
          />

          {/* File Picker */}
          <Text style={[styles.fieldLabel, { marginTop: 18 }]}>7. PDF / Document File Attachment *</Text>
          {selectedFile ? (
            <View style={styles.selectedFileBox}>
              <View style={styles.fileIconBox}>
                <Feather name="file-text" size={24} color="#DC2626" />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.selectedFileName} numberOfLines={1}>
                  {selectedFileName}
                </Text>
                <Text style={styles.selectedFileSize}>{formatBytes(selectedFileSize)}</Text>
              </View>
              <TouchableOpacity style={styles.clearFileBtn} onPress={handleClearFile}>
                <Feather name="x" size={18} color="#64748B" />
              </TouchableOpacity>
            </View>
          ) : (
            <TouchableOpacity style={styles.filePickerBox} onPress={handlePickFile} activeOpacity={0.7}>
              <View style={styles.pickerIconCircle}>
                <Feather name="file-plus" size={24} color="#4F46E5" />
              </View>
              <Text style={styles.pickerPromptTitle}>Choose Study PDF or Document</Text>
              <Text style={styles.pickerPromptDesc}>
                Supports PDF, DOC, DOCX up to 50MB. Click to browse files from your computer.
              </Text>
            </TouchableOpacity>
          )}

          {/* Publish Action Button */}
          <TouchableOpacity
            style={[styles.publishBtn, isUploading && styles.publishBtnDisabled]}
            onPress={handlePublishNote}
            disabled={isUploading}
            activeOpacity={0.8}
          >
            {isUploading ? (
              <ActivityIndicator color="#FFFFFF" size="small" />
            ) : (
              <>
                <Feather name="send" size={18} color="#FFFFFF" />
                <Text style={styles.publishBtnText}>Publish to Competitive Notes</Text>
              </>
            )}
          </TouchableOpacity>
        </View>

        {/* Currently Published Notes Section */}
        <View style={styles.sectionHeaderRow}>
          <View>
            <Text style={styles.sectionTitle}>📚 Currently Published Competitive Notes</Text>
            <Text style={styles.sectionSubtitle}>
              Live study materials accessible to students in the Competitive Exams Suite
            </Text>
          </View>
          <TouchableOpacity
            style={styles.refreshBtn}
            onPress={fetchCompetitiveNotes}
            activeOpacity={0.7}
          >
            <Feather name="refresh-cw" size={14} color="#4F46E5" />
            <Text style={styles.refreshBtnText}>Refresh</Text>
          </TouchableOpacity>
        </View>

        {/* Filter and Search Bar */}
        <View style={styles.filterBar}>
          <View style={styles.searchBox}>
            <Feather name="search" size={16} color="#64748B" />
            <TextInput
              style={styles.searchInput}
              placeholder="Search by title, subject or topic..."
              placeholderTextColor="#94A3B8"
              value={searchQuery}
              onChangeText={setSearchQuery}
            />
            {searchQuery ? (
              <TouchableOpacity onPress={() => setSearchQuery('')}>
                <Feather name="x" size={16} color="#64748B" />
              </TouchableOpacity>
            ) : null}
          </View>

          {/* Filter Subject Picker */}
          <ScrollView
            horizontal
            showsHorizontalScrollIndicator={false}
            contentContainerStyle={styles.filterScroll}
          >
            {['All', ...COMPETITIVE_SUBJECTS.filter((s) => s !== 'Other')].map((sub) => {
              const active = filterSubject === sub;
              return (
                <TouchableOpacity
                  key={sub}
                  style={[styles.filterChip, active && styles.filterChipActive]}
                  onPress={() => setFilterSubject(sub)}
                  activeOpacity={0.7}
                >
                  <Text style={[styles.filterChipText, active && styles.filterChipTextActive]}>
                    {sub}
                  </Text>
                </TouchableOpacity>
              );
            })}
          </ScrollView>
        </View>

        {/* Notes Cards List */}
        {loading ? (
          <View style={styles.loadingBox}>
            <ActivityIndicator size="large" color="#4F46E5" />
            <Text style={styles.loadingText}>Fetching published competitive notes...</Text>
          </View>
        ) : filteredNotes.length === 0 ? (
          <View style={styles.emptyState}>
            <Feather name="file-text" size={40} color="#94A3B8" />
            <Text style={styles.emptyTitle}>No Notes Found</Text>
            <Text style={styles.emptyDesc}>
              No study notes published yet for the selected filters. Use the form above to upload the first one!
            </Text>
          </View>
        ) : (
          <View style={styles.notesGrid}>
            {filteredNotes.map((note) => (
              <View key={note.id} style={styles.noteCard}>
                <View style={styles.noteTopRow}>
                  <View style={styles.badgeRowWrap}>
                    <View style={styles.subjectBadge}>
                      <Text style={styles.subjectBadgeText}>{note.subject_name || 'Competitive'}</Text>
                    </View>
                    {note.topic_name && (
                      <View style={styles.topicBadge}>
                        <Text style={styles.topicBadgeText}>{note.topic_name}</Text>
                      </View>
                    )}
                  </View>
                  <View style={styles.statusVerified}>
                    <Feather name="check-circle" size={12} color="#16A34A" />
                    <Text style={styles.statusVerifiedText}>Live</Text>
                  </View>
                </View>

                <View style={styles.noteTitleRow}>
                  <View style={styles.noteFileIcon}>
                    <Feather name="file-text" size={18} color="#4F46E5" />
                  </View>
                  <View style={{ flex: 1 }}>
                    <Text style={styles.noteCardTitle}>{note.title}</Text>
                    {note.subtopic_name ? (
                      <Text style={styles.noteCardSubtopic}>{note.subtopic_name}</Text>
                    ) : null}
                  </View>
                </View>

                {note.description ? (
                  <Text style={styles.noteDescription} numberOfLines={2}>
                    {note.description}
                  </Text>
                ) : null}

                <View style={styles.noteMetaRow}>
                  {note.file_size && (
                    <Text style={styles.noteMetaText}>
                      <Text style={{ fontWeight: '600' }}>Size:</Text> {note.file_size}
                    </Text>
                  )}
                  <Text style={styles.noteMetaText}>
                    <Text style={{ fontWeight: '600' }}>By:</Text> {note.uploaded_by || 'Faculty'}
                  </Text>
                </View>

                <View style={styles.noteActionsRow}>
                  <TouchableOpacity
                    style={styles.openPdfBtn}
                    onPress={() => handleOpenPdf(note.file_url)}
                    activeOpacity={0.8}
                  >
                    <Feather name="eye" size={14} color="#FFFFFF" />
                    <Text style={styles.openPdfBtnText}>Open Document</Text>
                  </TouchableOpacity>

                  <TouchableOpacity
                    style={styles.deleteNoteBtn}
                    onPress={() => handleDeleteNote(note.id, note.title)}
                    activeOpacity={0.7}
                  >
                    <Feather name="trash-2" size={14} color="#DC2626" />
                  </TouchableOpacity>
                </View>
              </View>
            ))}
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
  scrollContent: {
    padding: 24,
    paddingBottom: 60,
    maxWidth: 1100,
    alignSelf: 'center',
    width: '100%',
  },
  banner: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#EEF2FF',
    borderRadius: Radii.lg,
    padding: 20,
    marginBottom: 24,
    borderWidth: 1,
    borderColor: '#C7D2FE',
    gap: 16,
    flexWrap: 'wrap',
  },
  bannerIconBox: {
    width: 52,
    height: 52,
    borderRadius: 14,
    backgroundColor: '#FFFFFF',
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#4F46E5',
    shadowOpacity: 0.1,
    shadowRadius: 8,
  },
  badgeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 6,
  },
  bannerBadge: {
    backgroundColor: '#E0E7FF',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  bannerBadgeText: {
    fontSize: 10.5,
    fontWeight: '800',
    color: '#4F46E5',
    letterSpacing: 0.5,
  },
  livePill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    backgroundColor: '#DCFCE7',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  liveDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#16A34A',
  },
  liveText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#16A34A',
  },
  bannerTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#111827',
    marginBottom: 4,
  },
  bannerDesc: {
    fontSize: 13.5,
    color: '#475569',
    lineHeight: 20,
  },
  portalPreviewBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#4F46E5',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: 8,
    alignSelf: 'center',
  },
  portalPreviewBtnText: {
    color: '#FFFFFF',
    fontSize: 13.5,
    fontWeight: '600',
  },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    padding: 24,
    marginBottom: 32,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.04,
    shadowRadius: 10,
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingBottom: 16,
    marginBottom: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#F1F5F9',
  },
  cardHeaderLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  iconCircle: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: '#EEF2FF',
    alignItems: 'center',
    justifyContent: 'center',
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#111827',
  },
  cardSubtitle: {
    fontSize: 13,
    color: '#64748B',
    marginTop: 2,
  },
  fieldLabel: {
    fontSize: 13.5,
    fontWeight: '700',
    color: '#1E293B',
    marginBottom: 8,
  },
  subjectChipsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  subjectChip: {
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 8,
    backgroundColor: '#F1F5F9',
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  subjectChipActive: {
    backgroundColor: '#EEF2FF',
    borderColor: '#4F46E5',
  },
  subjectChipText: {
    fontSize: 13,
    fontWeight: '600',
    color: '#475569',
  },
  subjectChipTextActive: {
    color: '#4F46E5',
    fontWeight: '700',
  },
  input: {
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    borderRadius: 8,
    paddingHorizontal: 14,
    paddingVertical: 10,
    fontSize: 14,
    color: '#111827',
  },
  textArea: {
    minHeight: 76,
    textAlignVertical: 'top',
  },
  suggestionsContainer: {
    marginTop: 10,
    backgroundColor: '#F8FAFC',
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#F1F5F9',
  },
  suggestionsTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: '#64748B',
    marginBottom: 8,
    textTransform: 'uppercase',
  },
  suggestionsPills: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
  },
  pill: {
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  pillActive: {
    backgroundColor: '#4F46E5',
    borderColor: '#4F46E5',
  },
  pillText: {
    fontSize: 12,
    color: '#334155',
    fontWeight: '500',
  },
  pillTextActive: {
    color: '#FFFFFF',
    fontWeight: '600',
  },
  filePickerBox: {
    backgroundColor: '#F8FAFC',
    borderWidth: 2,
    borderColor: '#CBD5E1',
    borderStyle: 'dashed',
    borderRadius: 10,
    padding: 24,
    alignItems: 'center',
    justifyContent: 'center',
  },
  pickerIconCircle: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#EEF2FF',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 8,
  },
  pickerPromptTitle: {
    fontSize: 14.5,
    fontWeight: '700',
    color: '#111827',
    marginBottom: 4,
  },
  pickerPromptDesc: {
    fontSize: 12.5,
    color: '#64748B',
    textAlign: 'center',
  },
  selectedFileBox: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    borderRadius: 10,
    padding: 14,
    gap: 12,
  },
  fileIconBox: {
    width: 42,
    height: 42,
    borderRadius: 8,
    backgroundColor: '#FEE2E2',
    alignItems: 'center',
    justifyContent: 'center',
  },
  selectedFileName: {
    fontSize: 14,
    fontWeight: '700',
    color: '#111827',
  },
  selectedFileSize: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 2,
  },
  clearFileBtn: {
    padding: 8,
  },
  publishBtn: {
    marginTop: 24,
    backgroundColor: '#4F46E5',
    paddingVertical: 14,
    borderRadius: 8,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
  },
  publishBtnDisabled: {
    backgroundColor: '#94A3B8',
  },
  publishBtnText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '700',
  },
  sectionHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
    flexWrap: 'wrap',
    gap: 12,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: '#111827',
  },
  sectionSubtitle: {
    fontSize: 13.5,
    color: '#64748B',
    marginTop: 2,
  },
  refreshBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 6,
    backgroundColor: '#EEF2FF',
    borderWidth: 1,
    borderColor: '#C7D2FE',
  },
  refreshBtnText: {
    fontSize: 12.5,
    fontWeight: '600',
    color: '#4F46E5',
  },
  filterBar: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 20,
    flexWrap: 'wrap',
  },
  searchBox: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 8,
    flex: 1,
    minWidth: 260,
  },
  searchInput: {
    flex: 1,
    fontSize: 13.5,
    color: '#111827',
    borderWidth: 0,
    outlineWidth: 0,
  },
  filterScroll: {
    flexDirection: 'row',
    gap: 6,
    paddingVertical: 2,
  },
  filterChip: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 6,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  filterChipActive: {
    backgroundColor: '#4F46E5',
    borderColor: '#4F46E5',
  },
  filterChipText: {
    fontSize: 12.5,
    color: '#475569',
    fontWeight: '600',
  },
  filterChipTextActive: {
    color: '#FFFFFF',
  },
  loadingBox: {
    padding: 60,
    alignItems: 'center',
    justifyContent: 'center',
  },
  loadingText: {
    marginTop: 12,
    fontSize: 14,
    color: '#64748B',
  },
  emptyState: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    padding: 48,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  emptyTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#111827',
    marginTop: 12,
    marginBottom: 4,
  },
  emptyDesc: {
    fontSize: 13,
    color: '#64748B',
    textAlign: 'center',
    maxWidth: 360,
  },
  notesGrid: {
    display: 'flex',
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 16,
  },
  noteCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 18,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    flex: 1,
    minWidth: 320,
    maxWidth: 520,
    justifyContent: 'space-between',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.03,
    shadowRadius: 6,
  },
  noteTopRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  badgeRowWrap: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    flexWrap: 'wrap',
  },
  subjectBadge: {
    backgroundColor: '#EEF2FF',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 4,
  },
  subjectBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#4F46E5',
  },
  topicBadge: {
    backgroundColor: '#F1F5F9',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 4,
  },
  topicBadgeText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#334155',
  },
  statusVerified: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
  },
  statusVerifiedText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#16A34A',
  },
  noteTitleRow: {
    flexDirection: 'row',
    gap: 10,
    alignItems: 'flex-start',
    marginBottom: 8,
  },
  noteFileIcon: {
    width: 32,
    height: 32,
    borderRadius: 6,
    backgroundColor: '#EEF2FF',
    alignItems: 'center',
    justifyContent: 'center',
  },
  noteCardTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: '#111827',
    lineHeight: 20,
  },
  noteCardSubtopic: {
    fontSize: 12,
    color: '#4F46E5',
    fontWeight: '600',
    marginTop: 2,
  },
  noteDescription: {
    fontSize: 12.5,
    color: '#64748B',
    lineHeight: 18,
    marginBottom: 12,
  },
  noteMetaRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    paddingVertical: 8,
    borderTopWidth: 1,
    borderTopColor: '#F8FAFC',
    marginBottom: 12,
  },
  noteMetaText: {
    fontSize: 11.5,
    color: '#64748B',
  },
  noteActionsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#F1F5F9',
  },
  openPdfBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    backgroundColor: '#4F46E5',
    paddingVertical: 8,
    borderRadius: 6,
  },
  openPdfBtnText: {
    color: '#FFFFFF',
    fontSize: 12.5,
    fontWeight: '600',
  },
  deleteNoteBtn: {
    width: 34,
    height: 34,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#FECACA',
    backgroundColor: '#FEF2F2',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
