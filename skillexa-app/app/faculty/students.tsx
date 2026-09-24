import { Feather } from '@expo/vector-icons';
import React, { useState } from 'react';
import {
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
import { ProgressBar } from '../../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { StudentTopicPerformance } from '../../data/curriculumSchema';
import { FacultySystemStore } from '../../services/facultyStore';

export default function FacultyStudentsScreen() {
  const { profile } = useAuth();
  const [students] = useState<StudentTopicPerformance[]>(
    FacultySystemStore.getStudentPerformances()
  );
  const [selectedYear, setSelectedYear] = useState<string>('3rd Year');
  const [selectedSection, setSelectedSection] = useState<string>('A');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedStudent, setSelectedStudent] = useState<StudentTopicPerformance | null>(null);

  const filteredStudents = students.filter((s) => {
    return s.studentName.toLowerCase().includes(searchQuery.toLowerCase());
  });

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        title="My Students"
        subtitle={`${profile.collegeName || 'KVG College of Engineering'} • ${profile.department || 'ECE'} Dept`}
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Class Filter Bar */}
        <View style={styles.filterCard}>
          <Text style={styles.filterTitle}>SELECT CLASS BATCH</Text>

          <View style={styles.pillsRow}>
            {['1st Year', '2nd Year', '3rd Year', '4th Year'].map((y) => (
              <TouchableOpacity
                key={y}
                style={[styles.pill, selectedYear === y && styles.pillActive]}
                onPress={() => setSelectedYear(y)}
              >
                <Text style={[styles.pillText, selectedYear === y && styles.pillTextActive]}>{y}</Text>
              </TouchableOpacity>
            ))}
          </View>

          <View style={[styles.pillsRow, { marginTop: 8 }]}>
            {['A', 'B', 'C'].map((sec) => (
              <TouchableOpacity
                key={sec}
                style={[styles.pill, selectedSection === sec && styles.pillActive]}
                onPress={() => setSelectedSection(sec)}
              >
                <Text style={[styles.pillText, selectedSection === sec && styles.pillTextActive]}>
                  Section {sec}
                </Text>
              </TouchableOpacity>
            ))}
          </View>

          {/* Search Box */}
          <View style={styles.searchBox}>
            <Feather name="search" size={16} color={Palette.textSecondary} />
            <TextInput
              style={styles.searchInput}
              placeholder="Search student by name or ID..."
              placeholderTextColor={Palette.textMuted}
              value={searchQuery}
              onChangeText={setSearchQuery}
            />
          </View>
        </View>

        {/* Student Cards List */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>
            Enrolled Students ({filteredStudents.length})
          </Text>
          <Text style={styles.sectionSubtitle}>
            {profile.department || 'ECE'} • {selectedYear} • Section {selectedSection}
          </Text>
        </View>

        <View style={styles.studentsList}>
          {filteredStudents.map((std) => (
            <TouchableOpacity
              key={std.studentId}
              style={styles.stdCard}
              onPress={() => setSelectedStudent(std)}
              activeOpacity={0.8}
            >
              <View style={styles.stdCardHeader}>
                <View style={styles.avatar}>
                  <Text style={styles.avatarLetter}>{std.studentName.charAt(0)}</Text>
                </View>

                <View style={{ flex: 1 }}>
                  <Text style={styles.stdName}>{std.studentName}</Text>
                  <Text style={styles.stdEmail}>{std.email} • {selectedYear} Sec {selectedSection}</Text>
                </View>

                <View style={styles.scorePill}>
                  <Text style={styles.scorePillText}>{std.overallScore}% Avg</Text>
                </View>
              </View>

              {/* 4-Stat Grid */}
              <View style={styles.statsGrid}>
                <View style={styles.statBox}>
                  <Text style={styles.statLabel}>QUIZ ACCURACY</Text>
                  <Text style={[styles.statVal, { color: Palette.success }]}>{std.quizAccuracy}%</Text>
                </View>

                <View style={styles.statBox}>
                  <Text style={styles.statLabel}>NOTES READ</Text>
                  <Text style={styles.statVal}>{std.notesCompletedCount}</Text>
                </View>

                <View style={styles.statBox}>
                  <Text style={styles.statLabel}>CODING</Text>
                  <Text style={[styles.statVal, { color: Palette.primary }]}>{std.codingSolvedCount}</Text>
                </View>

                <View style={styles.statBox}>
                  <Text style={styles.statLabel}>INTERVIEW</Text>
                  <Text style={[styles.statVal, { color: Palette.aiPurple }]}>{std.interviewsScore}%</Text>
                </View>
              </View>

              {/* Topic Progress Sample */}
              <View style={styles.topicMiniRow}>
                <Text style={styles.topicMiniTitle}>Embedded Systems • Microcontrollers:</Text>
                <Text style={styles.topicMiniVal}>74%</Text>
              </View>
              <ProgressBar progress={0.74} color={Palette.primary} />
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  filterCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 16,
    ...Shadows.card,
  },
  filterTitle: { fontSize: 10, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.8, marginBottom: 8 },
  pillsRow: { flexDirection: 'row', gap: 6 },
  pill: {
    flex: 1,
    paddingVertical: 7,
    borderRadius: Radii.pill,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
  },
  pillActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  pillText: { fontSize: 11.5, fontWeight: '600', color: Palette.textSecondary },
  pillTextActive: { color: '#FFFFFF', fontWeight: '700' },
  searchBox: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    paddingHorizontal: 10,
    borderWidth: 1,
    borderColor: Palette.border,
    gap: 8,
    marginTop: 12,
  },
  searchInput: { flex: 1, paddingVertical: 8, fontSize: 12.5, color: Palette.textTitle },
  sectionHeaderRow: { marginBottom: 12 },
  sectionTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  studentsList: { gap: 12 },
  stdCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  stdCardHeader: { flexDirection: 'row', alignItems: 'center', gap: 12, marginBottom: 12 },
  avatar: { width: 42, height: 42, borderRadius: 21, backgroundColor: Palette.primaryLight, alignItems: 'center', justifyContent: 'center' },
  avatarLetter: { fontSize: 16, fontWeight: '800', color: Palette.primary },
  stdName: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  stdEmail: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 1 },
  scorePill: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  scorePillText: { fontSize: 11, fontWeight: '800', color: Palette.primary },
  statsGrid: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 10, borderTopWidth: 1, borderBottomWidth: 1, borderColor: Palette.borderSubtle, marginBottom: 10 },
  statBox: { alignItems: 'center' },
  statLabel: { fontSize: 8.5, fontWeight: '800', color: Palette.textSecondary, letterSpacing: 0.6 },
  statVal: { fontSize: 13.5, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
  topicMiniRow: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 4 },
  topicMiniTitle: { fontSize: 11, fontWeight: '600', color: Palette.textSecondary },
  topicMiniVal: { fontSize: 11, fontWeight: '800', color: Palette.primary },
});
