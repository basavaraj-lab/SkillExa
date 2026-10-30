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
import { Palette, Radii, Shadows } from '../../constants/theme';
import { FacultyNote } from '../../data/curriculumSchema';
import { ApiClient, getApiBaseUrl } from '../../services/api';
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
    'Microcontrollers',
  ],
  'Competitive Exams': [
    'Quantitative Aptitude',
    'Logical Reasoning',
    'English Language',
    'General Science',
    'General Awareness',
  ],
};

function formatBytes(bytes?: number): string {
  if (!bytes || bytes <= 0) return '1.2 MB';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
}

export default function FacultyNotesScreen() {
  const { profile } = useAuth();
  const [notes, setNotes] = useState<FacultyNote[]>([]);
  const [selectedSection, setSelectedSection] = useState<'Engineering' | 'Competitive Exams'>('Engineering');
  const [selectedSubject, setSelectedSubject] = useState('Embedded Systems');
  const [customSubject, setCustomSubject] = useState('');
  const [isCustomSubject, setIsCustomSubject] = useState(false);

  // Simplified Form Fields: Notes Name, Subject, Description, File Upload
  const [title, setTitle] = useState('');
  const [topic, setTopic] = useState('');
  const [description, setDescription] = useState('');
  const [selectedFile, setSelectedFile] = useState<any>(null);
  const [selectedFileName, setSelectedFileName] = useState('');
  const [selectedFileSize, setSelectedFileSize] = useState<number | undefined>(undefined);
  const [isUploading, setIsUploading] = useState(false);

  const collegeName = profile.collegeName || 'KVG College of Engineering';
  const departmentName = profile.department || 'ECE';

  // Load notes from backend database and local store
  const refreshNotes = async () => {
    try {
      const res = await ApiClient.getNotes();
      if (res?.success && Array.isArray(res.data)) {
        const backendNotes: FacultyNote[] = res.data.map((n: any) => ({
          id: n.id,
          section: n.section || 'engineering',
          subject: n.subject || 'Engineering',
          topic: n.topic || n.title,
          subtopic: n.subtopic || '',
          title: n.title,
          introduction: n.description || '',
          theory: n.content || n.description || '',
          description: n.description,
          fileName: n.file_name || undefined,
          fileSize: n.file_size_bytes || undefined,
          downloadUrl: n.download_url || (n.file_path ? `/api/notes/${n.id}/download` : undefined),
          importantConcepts: n.important_concepts || [],
          formulas: [],
          examples: [],
          importantPoints: [],
          commonMistakes: [],
          quickRevision: n.quick_revision || '',
          facultyName: n.faculty_name || 'Dr. Ramesh Kumar',
          collegeId: n.college_id || '0f669a91-5c8d-4304-a815-818bde05e996',
          collegeName: n.college_name || collegeName,
          isVerifiedFaculty: true,
          visibility: 'college',
          published: n.published !== false,
          createdAt: n.created_at ? n.created_at.split('T')[0] : new Date().toISOString().split('T')[0],
        }));

        FacultySystemStore.setNotes(backendNotes);
        setNotes(backendNotes);
        return;
      }
    } catch (e) {
      console.log('Error fetching backend notes:', e);
    }
    const localNotes = FacultySystemStore.getNotes();
    setNotes(localNotes);
  };

  useEffect(() => {
    refreshNotes();
    const unsub = FacultySystemStore.subscribe(() => {
      refreshNotes();
    });
    return unsub;
  }, []);

  const handleDeleteNote = async (id: string, noteTitle?: string) => {
    const doDelete = async () => {
      try {
        // 1. Delete permanently in database and file storage
        await ApiClient.deleteFacultyNote(id);
        await ApiClient.deleteCompetitiveNote(id).catch(() => {});

        // 2. Remove from local store & state
        FacultySystemStore.deleteNote(id);
        setNotes((prev) => prev.filter((x) => x.id !== id));

        Alert.alert(
          'Deleted Permanently',
          `"${noteTitle || 'Note'}" has been permanently deleted from the database.`
        );
      } catch (err: any) {
        console.error('Delete note failed:', err);
        FacultySystemStore.deleteNote(id);
        setNotes((prev) => prev.filter((x) => x.id !== id));
      }
    };

    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      if (window.confirm(`Permanently delete "${noteTitle || 'this note'}" from the database?`)) {
        await doDelete();
      }
    } else {
      Alert.alert(
        'Delete Note Permanently',
        `Are you sure you want to permanently delete "${noteTitle || 'this note'}" from the database?`,
        [
          { text: 'Cancel', style: 'cancel' },
          { text: 'Delete Permanently', style: 'destructive', onPress: doDelete },
        ]
      );
    }
  };

  // Web File Picker Handler
  const handlePickFile = () => {
    if (Platform.OS === 'web' && typeof document !== 'undefined') {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = '.pdf,.doc,.docx,.ppt,.pptx,.txt,.zip,.png,.jpg,.jpeg';
      input.onchange = (e: any) => {
        const file = e.target?.files?.[0];
        if (file) {
          setSelectedFile(file);
          setSelectedFileName(file.name);
          setSelectedFileSize(file.size);
          // Pre-fill notes title if empty
          if (!title.trim()) {
            const cleanName = file.name.replace(/\.[^/.]+$/, '').replace(/[-_]/g, ' ');
            setTitle(cleanName);
          }
        }
      };
      input.click();
    } else {
      Alert.alert('File Picker', 'Please choose a document from your device.');
    }
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
    setSelectedFileName('');
    setSelectedFileSize(undefined);
  };

  const openDocument = (downloadUrl?: string) => {
    if (!downloadUrl) {
      Alert.alert('No File', 'No physical document file is attached to this note.');
      return;
    }
    const apiBase = getApiBaseUrl().replace(/\/api$/, '');
    const fullUrl = downloadUrl.startsWith('http')
      ? downloadUrl
      : `${apiBase}${downloadUrl.startsWith('/') ? '' : '/'}${downloadUrl}`;

    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      window.open(fullUrl, '_blank');
    } else {
      Linking.openURL(fullUrl).catch(() => {
        Alert.alert('Error', 'Unable to open file link');
      });
    }
  };

  const handleUploadAndPublish = async () => {
    const finalSubject = isCustomSubject ? customSubject.trim() : selectedSubject;

    if (!title.trim()) {
      Alert.alert('Missing Field', 'Please provide a Notes Name (Title).');
      return;
    }
    if (!finalSubject) {
      Alert.alert('Missing Field', 'Please select or enter a Subject.');
      return;
    }
    if (!description.trim() && !selectedFile) {
      Alert.alert('Missing Field', 'Please provide a Description or upload a File.');
      return;
    }

    setIsUploading(true);

    try {
      // 1. Submit to Backend DB via Multipart FormData
      const formData = new FormData();
      formData.append('title', title.trim());
      formData.append('description', description.trim());
      formData.append('subject', finalSubject);
      formData.append('topic', topic.trim() || title.trim());
      formData.append('section', selectedSection === 'Engineering' ? 'engineering' : 'competitive');
      formData.append('visibility', 'college');

      if (selectedFile) {
        formData.append('file', selectedFile);
      }

      const res = await ApiClient.uploadFacultyNote(formData);

      const savedNote = res?.data || {};
      const downloadUrl =
        savedNote.download_url || (savedNote.id ? `/api/notes/${savedNote.id}/download` : undefined);

      // 2. Also save to local FacultySystemStore for immediate offline/client reactivity
      FacultySystemStore.addNote({
        section: selectedSection === 'Engineering' ? 'engineering' : 'competitive',
        subject: finalSubject,
        topic: topic.trim() || title.trim(),
        title: title.trim(),
        description: description.trim(),
        fileName: selectedFileName || savedNote.file_name || undefined,
        fileSize: selectedFileSize || savedNote.file_size_bytes || undefined,
        downloadUrl: downloadUrl,
        pdfUrl: downloadUrl,
        introduction: description.trim(),
        theory: description.trim(),
        importantConcepts: [],
        formulas: [],
        examples: [],
        importantPoints: ['Verified Faculty Study Material'],
        commonMistakes: [],
        quickRevision: description.trim(),
        facultyName: profile.name || 'Dr. Ramesh Kumar',
        facultyDesignation: profile.facultyDesignation || 'Associate Professor',
        facultyDepartment: departmentName,
        collegeId: profile.collegeId || 'clg-kvg',
        collegeName: collegeName,
        isVerifiedFaculty: true,
        visibility: 'college',
        published: true,
      });

      // 3. If Competitive Exams, also mirror directly to Competitive Portal
      if (selectedSection === 'Competitive Exams') {
        try {
          const compFormData = new FormData();
          compFormData.append('title', title.trim());
          compFormData.append('subject_name', finalSubject);
          compFormData.append('topic_name', topic.trim() || title.trim());
          compFormData.append('description', description.trim());
          compFormData.append('faculty_name', profile.name || 'Dr. Ramesh Kumar');
          if (selectedFile) {
            compFormData.append('pdf', selectedFile);
            compFormData.append('file', selectedFile);
          }
          await ApiClient.uploadCompetitiveNote(compFormData);
        } catch (compErr) {
          console.warn('Competitive mirror sync error:', compErr);
        }
      }

      Alert.alert(
        'Upload Successful! 🎉',
        `Notes "${title.trim()}" successfully stored in database and published for ${collegeName} students!`
      );

      // Reset form
      setTitle('');
      setTopic('');
      setDescription('');
      setSelectedFile(null);
      setSelectedFileName('');
      setSelectedFileSize(undefined);
      if (isCustomSubject) {
        setCustomSubject('');
        setIsCustomSubject(false);
      }

      await refreshNotes();
    } catch (err: any) {
      console.error('Failed to upload notes:', err);
      Alert.alert('Upload Failed', err?.message || 'Could not upload notes. Please try again.');
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        onBack={() => router.replace('/faculty-dashboard' as any)}
        title="Faculty Notes & File Upload"
        subtitle="Publish Study Documents to KVG Students"
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* College & Department Identity Banner */}
        <View style={styles.banner}>
          <View style={styles.bannerIconBox}>
            <Feather name="file-text" size={24} color={Palette.primary} />
          </View>
          <View style={{ flex: 1 }}>
            <View style={styles.bannerBadgeRow}>
              <View style={styles.verifiedBadge}>
                <Feather name="check-circle" size={11} color={Palette.success} />
                <Text style={styles.verifiedText}>OFFICIAL WORKSPACE</Text>
              </View>
              <Text style={styles.deptText}>Department of {departmentName}</Text>
            </View>
            <Text style={styles.bannerTitle}>{collegeName}</Text>
            <Text style={styles.bannerDesc}>
              Upload PDF notes, lecture slides, and study guides. Notes are immediately stored in the database and visible to your enrolled students.
            </Text>
          </View>
        </View>

        {/* Clean & Simplified Upload Form Card */}
        <View style={styles.card}>
          <View style={styles.cardHeaderRow}>
            <View style={styles.stepNumBox}>
              <Text style={styles.stepNum}>1</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.cardHeader}>Upload Notes & Study Material</Text>
              <Text style={styles.cardSubHeader}>Fill in the details and attach your document</Text>
            </View>
          </View>

          {/* 1. Section Selection */}
          <Text style={styles.label}>ACADEMIC TRACK</Text>
          <View style={styles.sectionRow}>
            {SECTIONS.map((sec) => (
              <TouchableOpacity
                key={sec}
                style={[styles.pill, selectedSection === sec && styles.pillActive]}
                onPress={() => {
                  setSelectedSection(sec as any);
                  setSelectedSubject(SUBJECTS[sec][0]);
                  setIsCustomSubject(false);
                }}
              >
                <Text style={[styles.pillText, selectedSection === sec && styles.pillTextActive]}>
                  {sec}
                </Text>
              </TouchableOpacity>
            ))}
          </View>

          {/* 2. Subject Selection Chips */}
          <Text style={[styles.label, { marginTop: 12 }]}>SELECT SUBJECT *</Text>
          <ScrollView
            horizontal
            showsHorizontalScrollIndicator={false}
            contentContainerStyle={styles.chipsScroll}
          >
            {(SUBJECTS[selectedSection] || []).map((sub) => (
              <TouchableOpacity
                key={sub}
                style={[styles.chip, !isCustomSubject && selectedSubject === sub && styles.chipActive]}
                onPress={() => {
                  setSelectedSubject(sub);
                  setIsCustomSubject(false);
                }}
              >
                <Text
                  style={[
                    styles.chipText,
                    !isCustomSubject && selectedSubject === sub && styles.chipTextActive,
                  ]}
                >
                  {sub}
                </Text>
              </TouchableOpacity>
            ))}
            <TouchableOpacity
              style={[styles.chip, isCustomSubject && styles.chipActive]}
              onPress={() => setIsCustomSubject(true)}
            >
              <Text style={[styles.chipText, isCustomSubject && styles.chipTextActive]}>
                + Custom Subject
              </Text>
            </TouchableOpacity>
          </ScrollView>

          {isCustomSubject && (
            <TextInput
              style={[styles.input, { marginBottom: 12 }]}
              placeholder="Type custom subject name (e.g. Signals & Systems)..."
              placeholderTextColor={Palette.textMuted}
              value={customSubject}
              onChangeText={setCustomSubject}
            />
          )}

          {/* 3. Notes Name / Title */}
          <Text style={[styles.label, { marginTop: 4 }]}>NOTES NAME / TITLE *</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. Unit 2: ARM Architecture, Registers & GPIO Interfacing"
            placeholderTextColor={Palette.textMuted}
            value={title}
            onChangeText={setTitle}
          />

          {/* 4. Topic / Module (Optional) */}
          <Text style={[styles.label, { marginTop: 12 }]}>TOPIC / MODULE (OPTIONAL)</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. Microcontroller Architecture / RTOS"
            placeholderTextColor={Palette.textMuted}
            value={topic}
            onChangeText={setTopic}
          />

          {/* 5. Description */}
          <Text style={[styles.label, { marginTop: 12 }]}>NOTES DESCRIPTION & INSTRUCTIONS *</Text>
          <TextInput
            style={[styles.input, styles.textArea]}
            placeholder="Provide a clear description, key points covered, chapter references, or exam instructions for students..."
            placeholderTextColor={Palette.textMuted}
            multiline
            numberOfLines={4}
            value={description}
            onChangeText={setDescription}
          />

          {/* 6. Document / File Upload Box */}
          <Text style={[styles.label, { marginTop: 14 }]}>ATTACH DOCUMENT / PDF FILE *</Text>

          {!selectedFile ? (
            <TouchableOpacity
              style={styles.uploadDropzone}
              onPress={handlePickFile}
              activeOpacity={0.8}
            >
              <View style={styles.uploadIconCircle}>
                <Feather name="upload-cloud" size={26} color={Palette.primary} />
              </View>
              <Text style={styles.uploadDropzoneTitle}>Click to Choose File from Device</Text>
              <Text style={styles.uploadDropzoneSub}>
                Supports PDF, DOCX, PPTX, TXT, Images (Max 50 MB)
              </Text>
              <View style={styles.browseButton}>
                <Feather name="folder" size={14} color="#FFFFFF" />
                <Text style={styles.browseButtonText}>Browse Document</Text>
              </View>
            </TouchableOpacity>
          ) : (
            <View style={styles.fileSelectedCard}>
              <View style={styles.fileIconBox}>
                <Feather name="file-text" size={24} color={Palette.primary} />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.fileNameText} numberOfLines={1}>
                  {selectedFileName}
                </Text>
                <Text style={styles.fileSizeText}>
                  {formatBytes(selectedFileSize)} • Ready to upload to database
                </Text>
              </View>
              <TouchableOpacity
                style={styles.removeFileBtn}
                onPress={handleRemoveFile}
                hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
              >
                <Feather name="x" size={18} color={Palette.danger} />
              </TouchableOpacity>
            </View>
          )}

          {/* 7. Action Button */}
          <TouchableOpacity
            style={[styles.publishBtn, isUploading && styles.publishBtnDisabled]}
            onPress={handleUploadAndPublish}
            disabled={isUploading}
            activeOpacity={0.85}
          >
            {isUploading ? (
              <>
                <ActivityIndicator size="small" color="#FFFFFF" />
                <Text style={styles.publishBtnText}>Uploading & Storing in Database...</Text>
              </>
            ) : (
              <>
                <Feather name="upload-cloud" size={18} color="#FFFFFF" />
                <Text style={styles.publishBtnText}>Upload & Publish Notes to Students</Text>
              </>
            )}
          </TouchableOpacity>
        </View>

        {/* Existing Published Notes Section */}
        <View style={styles.sectionHeaderRow}>
          <View style={{ flex: 1 }}>
            <Text style={styles.sectionTitle}>Published Notes ({notes.length})</Text>
            <Text style={styles.sectionSubtitle}>
              Available to KVG College of Engineering students
            </Text>
          </View>
          <TouchableOpacity
            style={styles.refreshBtn}
            onPress={refreshNotes}
            activeOpacity={0.7}
          >
            <Feather name="refresh-cw" size={14} color={Palette.primary} />
            <Text style={styles.refreshBtnText}>Refresh</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.notesList}>
          {notes.length === 0 ? (
            <View style={styles.emptyCard}>
              <Feather name="book-open" size={32} color={Palette.textMuted} />
              <Text style={styles.emptyTitle}>No notes uploaded yet</Text>
              <Text style={styles.emptyDesc}>
                Upload your first notes or PDF guide using the form above.
              </Text>
            </View>
          ) : (
            notes.map((n) => (
              <View key={n.id} style={styles.noteCard}>
                <View style={styles.noteCardHeader}>
                  <View style={styles.subjectBadge}>
                    <Text style={styles.subjectBadgeText}>
                      📚 {n.subject} {n.topic ? `• ${n.topic}` : ''}
                    </Text>
                  </View>
                  <TouchableOpacity
                    onPress={() => handleDeleteNote(n.id, n.title)}
                    hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
                  >
                    <Feather name="trash-2" size={15} color={Palette.danger} />
                  </TouchableOpacity>
                </View>

                <Text style={styles.noteTitle}>{n.title}</Text>

                {(n.description || n.theory || n.introduction) ? (
                  <Text style={styles.noteIntro} numberOfLines={3}>
                    {n.description || n.theory || n.introduction}
                  </Text>
                ) : null}

                {/* File Attachment & Download Button */}
                {(n.fileName || n.downloadUrl) && (
                  <View style={styles.attachmentBox}>
                    <View style={styles.attachmentInfo}>
                      <Feather name="file" size={16} color={Palette.primary} />
                      <Text style={styles.attachmentName} numberOfLines={1}>
                        {n.fileName || `${n.title}.pdf`}
                      </Text>
                      {n.fileSize ? (
                        <Text style={styles.attachmentSize}>
                          ({typeof n.fileSize === 'number' ? formatBytes(n.fileSize) : n.fileSize})
                        </Text>
                      ) : null}
                    </View>

                    {n.downloadUrl && (
                      <TouchableOpacity
                        style={styles.downloadBtn}
                        onPress={() => openDocument(n.downloadUrl)}
                        activeOpacity={0.8}
                      >
                        <Feather name="download" size={13} color="#FFFFFF" />
                        <Text style={styles.downloadBtnText}>View / Download</Text>
                      </TouchableOpacity>
                    )}
                  </View>
                )}

                <View style={styles.noteFooter}>
                  <Text style={styles.noteAuthor}>
                    By {n.facultyName || 'Dr. Ramesh Kumar'} • {n.collegeName || collegeName}
                  </Text>
                  <Text style={styles.noteDate}>{n.createdAt}</Text>
                </View>
              </View>
            ))
          )}
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
    alignItems: 'flex-start',
    gap: 12,
    marginBottom: 18,
    ...Shadows.card,
  },
  bannerIconBox: {
    width: 44,
    height: 44,
    borderRadius: 10,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
  },
  bannerBadgeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 4,
  },
  verifiedBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#ECFDF5',
    paddingHorizontal: 7,
    paddingVertical: 2,
    borderRadius: Radii.pill,
  },
  verifiedText: {
    fontSize: 10,
    fontWeight: '800',
    color: Palette.success,
    letterSpacing: 0.5,
  },
  deptText: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.textSecondary,
  },
  bannerTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginBottom: 3 },
  bannerDesc: { fontSize: 12.5, color: Palette.textSecondary, lineHeight: 18 },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 20,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  cardHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 16,
    paddingBottom: 14,
    borderBottomWidth: 1,
    borderBottomColor: Palette.border,
  },
  stepNumBox: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: Palette.primary,
    alignItems: 'center',
    justifyContent: 'center',
  },
  stepNum: { color: '#FFFFFF', fontWeight: '800', fontSize: 15 },
  cardHeader: { fontSize: 16.5, fontWeight: '800', color: Palette.textTitle },
  cardSubHeader: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  label: {
    fontSize: 11,
    fontWeight: '800',
    color: Palette.textTitle,
    letterSpacing: 0.6,
    marginBottom: 6,
  },
  sectionRow: { flexDirection: 'row', gap: 8, marginBottom: 12 },
  pill: {
    flex: 1,
    paddingVertical: 9,
    borderRadius: Radii.pill,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
  },
  pillActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  pillText: { fontSize: 13, fontWeight: '700', color: Palette.textSecondary },
  pillTextActive: { color: '#FFFFFF' },
  chipsScroll: { gap: 8, paddingVertical: 2, marginBottom: 12 },
  chip: {
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: Radii.pill,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  chipActive: { backgroundColor: Palette.primaryLight, borderColor: Palette.primary },
  chipText: { fontSize: 12, fontWeight: '600', color: Palette.textSecondary },
  chipTextActive: { color: Palette.primary, fontWeight: '700' },
  input: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 12,
    fontSize: 13.5,
    color: Palette.textTitle,
  },
  textArea: {
    height: 90,
    textAlignVertical: 'top',
  },
  uploadDropzone: {
    backgroundColor: '#F8FAFC',
    borderRadius: Radii.card,
    borderWidth: 2,
    borderColor: Palette.primaryBorder,
    borderStyle: 'dashed',
    paddingVertical: 22,
    paddingHorizontal: 16,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 4,
    marginBottom: 16,
  },
  uploadIconCircle: {
    width: 52,
    height: 52,
    borderRadius: 26,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 10,
  },
  uploadDropzoneTitle: {
    fontSize: 14.5,
    fontWeight: '700',
    color: Palette.textTitle,
    marginBottom: 3,
  },
  uploadDropzoneSub: {
    fontSize: 11.5,
    color: Palette.textSecondary,
    marginBottom: 12,
  },
  browseButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: Palette.primary,
    paddingHorizontal: 14,
    paddingVertical: 7,
    borderRadius: Radii.pill,
  },
  browseButtonText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  fileSelectedCard: {
    backgroundColor: '#F0F9FF',
    borderRadius: Radii.card,
    borderWidth: 1.5,
    borderColor: '#BAE6FD',
    padding: 12,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginTop: 4,
    marginBottom: 16,
  },
  fileIconBox: {
    width: 40,
    height: 40,
    borderRadius: 8,
    backgroundColor: '#E0F2FE',
    alignItems: 'center',
    justifyContent: 'center',
  },
  fileNameText: {
    fontSize: 13.5,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  fileSizeText: {
    fontSize: 11.5,
    color: Palette.primary,
    fontWeight: '600',
    marginTop: 2,
  },
  removeFileBtn: {
    padding: 6,
  },
  publishBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 14,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    marginTop: 6,
    ...Shadows.button,
  },
  publishBtnDisabled: {
    opacity: 0.7,
  },
  publishBtnText: { color: '#FFFFFF', fontSize: 14.5, fontWeight: '700' },
  sectionHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  refreshBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: Radii.pill,
    backgroundColor: Palette.primaryLight,
  },
  refreshBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.primary,
  },
  notesList: { gap: 12 },
  emptyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 32,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  emptyTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
    marginTop: 10,
  },
  emptyDesc: {
    fontSize: 12.5,
    color: Palette.textSecondary,
    textAlign: 'center',
    marginTop: 4,
  },
  noteCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  noteCardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  subjectBadge: {
    backgroundColor: Palette.primaryLight,
    paddingHorizontal: 9,
    paddingVertical: 3,
    borderRadius: 6,
  },
  subjectBadgeText: { fontSize: 11.5, fontWeight: '700', color: Palette.primary },
  noteTitle: { fontSize: 15.5, fontWeight: '700', color: Palette.textTitle, marginBottom: 5 },
  noteIntro: { fontSize: 13, color: Palette.textSecondary, lineHeight: 18, marginBottom: 10 },
  attachmentBox: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: 8,
    padding: 10,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 10,
    borderWidth: 1,
    borderColor: Palette.border,
    gap: 8,
  },
  attachmentInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    flex: 1,
  },
  attachmentName: {
    fontSize: 12.5,
    fontWeight: '600',
    color: Palette.textTitle,
    flexShrink: 1,
  },
  attachmentSize: {
    fontSize: 11.5,
    color: Palette.textMuted,
  },
  downloadBtn: {
    backgroundColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: 6,
  },
  downloadBtnText: {
    color: '#FFFFFF',
    fontSize: 11.5,
    fontWeight: '700',
  },
  noteFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderTopWidth: 1,
    borderTopColor: Palette.borderSubtle,
    paddingTop: 8,
    marginTop: 4,
  },
  noteAuthor: { fontSize: 11.5, color: Palette.textMuted },
  noteDate: { fontSize: 11, color: Palette.textMuted },
});
