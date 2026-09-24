import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useState } from 'react';
import {
  Dimensions,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

const { width } = Dimensions.get('window');

interface TopicItem {
  id: number;
  title: string;
  moduleNum: string;
}

const TRACKS_DATA: Record<string, TopicItem[]> = {
  python: [
    { id: 1, moduleNum: '01', title: 'Variables and Data Types' },
    { id: 2, moduleNum: '02', title: 'Input and Output' },
    { id: 3, moduleNum: '03', title: 'Operators' },
    { id: 4, moduleNum: '04', title: 'Conditional Statements (if, else)' },
    { id: 5, moduleNum: '05', title: 'Loops (for, while)' },
    { id: 6, moduleNum: '06', title: 'Functions' },
    { id: 7, moduleNum: '07', title: 'Lists, Tuples, Dictionaries, Sets' },
    { id: 8, moduleNum: '08', title: 'File Handling' },
    { id: 9, moduleNum: '09', title: 'Exception Handling' },
    { id: 10, moduleNum: '10', title: 'OOP (Classes and Objects)' },
  ],
  c: [
    { id: 1, moduleNum: '01', title: 'Structure of a C program' },
    { id: 2, moduleNum: '02', title: 'Variables and Data Types' },
    { id: 3, moduleNum: '03', title: 'Input/Output (printf, scanf)' },
    { id: 4, moduleNum: '04', title: 'Operators' },
    { id: 5, moduleNum: '05', title: 'Conditional Statements' },
    { id: 6, moduleNum: '06', title: 'Loops' },
    { id: 7, moduleNum: '07', title: 'Functions' },
    { id: 8, moduleNum: '08', title: 'Arrays' },
    { id: 9, moduleNum: '09', title: 'Strings' },
    { id: 10, moduleNum: '10', title: 'Pointers' },
    { id: 11, moduleNum: '11', title: 'Structures' },
    { id: 12, moduleNum: '12', title: 'File Handling' },
  ],
  cpp: [
    { id: 1, moduleNum: '01', title: 'C++ Program Structure' },
    { id: 2, moduleNum: '02', title: 'Variables and Data Types' },
    { id: 3, moduleNum: '03', title: 'Input/Output (cin, cout)' },
    { id: 4, moduleNum: '04', title: 'Functions' },
    { id: 5, moduleNum: '05', title: 'Arrays and Strings' },
    { id: 6, moduleNum: '06', title: 'Classes and Objects' },
    { id: 7, moduleNum: '07', title: 'Inheritance' },
    { id: 8, moduleNum: '08', title: 'Polymorphism' },
    { id: 9, moduleNum: '09', title: 'Templates' },
    { id: 10, moduleNum: '10', title: 'STL (Vector, Map, etc.)' },
  ],
  javascript: [
    { id: 1, moduleNum: '01', title: 'Variables (let, const)' },
    { id: 2, moduleNum: '02', title: 'Data Types' },
    { id: 3, moduleNum: '03', title: 'Operators' },
    { id: 4, moduleNum: '04', title: 'Functions' },
    { id: 5, moduleNum: '05', title: 'Arrays and Objects' },
    { id: 6, moduleNum: '06', title: 'Loops and Conditions' },
    { id: 7, moduleNum: '07', title: 'DOM Manipulation' },
    { id: 8, moduleNum: '08', title: 'Events' },
    { id: 9, moduleNum: '09', title: 'ES6 Features (Arrow Functions, Destructuring)' },
    { id: 10, moduleNum: '10', title: 'Promises and Async/Await' },
  ],
  reactnative: [
    { id: 1, moduleNum: '01', title: 'React Native Setup' },
    { id: 2, moduleNum: '02', title: 'Components' },
    { id: 3, moduleNum: '03', title: 'JSX' },
    { id: 4, moduleNum: '04', title: 'Props and State' },
    { id: 5, moduleNum: '05', title: 'Styling with StyleSheet' },
    { id: 6, moduleNum: '06', title: 'Navigation' },
    { id: 7, moduleNum: '07', title: 'Lists (FlatList)' },
    { id: 8, moduleNum: '08', title: 'User Input (TextInput, Button)' },
    { id: 9, moduleNum: '09', title: 'API Calls (fetch)' },
    { id: 10, moduleNum: '10', title: 'Hooks (useState, useEffect)' },
    { id: 11, moduleNum: '11', title: 'Debugging and App Building' },
  ],
};

const LANGUAGES_LIST = [
  { id: 'python', name: 'Python' },
  { id: 'c', name: 'C' },
  { id: 'cpp', name: 'C++' },
  { id: 'javascript', name: 'JavaScript' },
  { id: 'reactnative', name: 'React Native' },
];

export default function SeparateModulesZigZagRoadmap() {
  const [selectedLang, setSelectedLang] = useState<string>('python');

  const topics = TRACKS_DATA[selectedLang] || TRACKS_DATA.python;
  const currentLangObj = LANGUAGES_LIST.find((l) => l.id === selectedLang);
  const displayTitle = currentLangObj ? currentLangObj.name : 'Python';

  const handleOpenTopic = (topicTitle: string) => {
    router.push({
      pathname: '/coding/theory',
      params: {
        langId: selectedLang,
        langName: displayTitle,
        topicTitle: topicTitle,
      },
    });
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Top Header */}
      <View style={styles.topBar}>
        <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
          <Feather name="arrow-left" size={20} color="#1E293B" />
        </TouchableOpacity>
        <Text style={styles.topBarTitle}>SkillExa Track</Text>
      </View>

      {/* Navigation Bar */}
      <View style={styles.horizontalNavRow}>
        <View style={[styles.navTabBtn, styles.navTabBtnActive]}>
          <Feather name="book-open" size={16} color="#2563EB" />
          <Text style={[styles.navTabLabel, styles.navTabLabelActive]}>Syllabus</Text>
        </View>

        <TouchableOpacity
          style={styles.navTabBtn}
          onPress={() =>
            router.push({
              pathname: '/coding/compiler',
              params: { langId: selectedLang, langName: displayTitle },
            })
          }
        >
          <Feather name="terminal" size={16} color="#64748B" />
          <Text style={styles.navTabLabel}>Compiler</Text>
        </TouchableOpacity>
      </View>

      {/* Language Selector Bar */}
      <View style={styles.langPillContainer}>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.langPillScroll}>
          {LANGUAGES_LIST.map((lang) => {
            const isSelected = selectedLang === lang.id;
            return (
              <TouchableOpacity
                key={lang.id}
                style={[styles.langPill, isSelected && styles.langPillActive]}
                onPress={() => setSelectedLang(lang.id)}
              >
                <Text style={[styles.langPillText, isSelected && styles.langPillTextActive]}>
                  {lang.name}
                </Text>
              </TouchableOpacity>
            );
          })}
        </ScrollView>
      </View>

      {/* Zig-Zag Module Path */}
      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        <Text style={styles.sectionHeading}>{displayTitle} Syllabus</Text>
        <Text style={styles.sectionSub}>Tap any topic module to study concepts and run code live in the compiler!</Text>

        <View style={styles.zigzagContainer}>
          {topics.map((item, index) => {
            const isLeft = index % 2 === 0;

            return (
              <View key={item.id} style={styles.cardNodeWrapper}>
                {index > 0 && <View style={styles.dottedConnector} />}

                <View style={[styles.cardAlignRow, isLeft ? styles.alignLeft : styles.alignRight]}>
                  <View style={styles.roundedModuleCard}>
                    <View style={styles.cardHeaderRow}>
                      <Text style={styles.moduleNumText}>MODULE {item.moduleNum}</Text>
                      <View style={styles.badgePill}>
                        <Text style={styles.badgeText}>Core Topic</Text>
                      </View>
                    </View>

                    <Text style={styles.moduleTitle}>{item.title}</Text>

                    <TouchableOpacity
                      style={styles.roundedBtnActive}
                      onPress={() => handleOpenTopic(item.title)}
                    >
                      <Text style={styles.roundedBtnActiveText}>Open Topic</Text>
                      <Feather name="arrow-right" size={14} color="#FFFFFF" style={{ marginLeft: 6 }} />
                    </TouchableOpacity>
                  </View>
                </View>
              </View>
            );
          })}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FFFFFF' },
  topBar: { flexDirection: 'row', alignItems: 'center', paddingHorizontal: 20, paddingTop: 12, paddingBottom: 8 },
  backBtn: { marginRight: 12 },
  topBarTitle: { fontSize: 18, fontWeight: '800', color: '#1E293B' },
  horizontalNavRow: { flexDirection: 'row', justifyContent: 'space-around', alignItems: 'center', backgroundColor: '#F8FAFC', paddingVertical: 10, borderTopWidth: 1, borderBottomWidth: 1, borderColor: '#E2E8F0' },
  navTabBtn: { flexDirection: 'row', alignItems: 'center', paddingHorizontal: 12, paddingVertical: 6, borderRadius: 20 },
  navTabBtnActive: { backgroundColor: '#EFF6FF' },
  navTabLabel: { fontSize: 12, fontWeight: '600', color: '#64748B', marginLeft: 6 },
  navTabLabelActive: { color: '#2563EB', fontWeight: '700' },
  langPillContainer: { borderBottomWidth: 1, borderBottomColor: '#E2E8F0', paddingVertical: 10 },
  langPillScroll: { paddingHorizontal: 20 },
  langPill: { paddingHorizontal: 16, paddingVertical: 6, borderRadius: 20, backgroundColor: '#F1F5F9', marginRight: 8 },
  langPillActive: { backgroundColor: '#2563EB' },
  langPillText: { fontSize: 12, fontWeight: '600', color: '#64748B' },
  langPillTextActive: { color: '#FFFFFF', fontWeight: '700' },
  scrollContent: { padding: 20 },
  sectionHeading: { fontSize: 22, fontWeight: '800', color: '#0F172A' },
  sectionSub: { fontSize: 12, color: '#64748B', marginTop: 2, marginBottom: 20 },
  zigzagContainer: { position: 'relative', marginTop: 8 },
  cardNodeWrapper: { marginBottom: 20, position: 'relative' },
  dottedConnector: {
    position: 'absolute',
    top: -20,
    left: '50%',
    width: 2,
    height: 20,
    borderWidth: 1,
    borderColor: '#2563EB',
    borderStyle: 'dashed',
    zIndex: -1,
  },
  cardAlignRow: { flexDirection: 'row', width: '100%' },
  alignLeft: { justifyContent: 'flex-start' },
  alignRight: { justifyContent: 'flex-end' },
  roundedModuleCard: {
    width: width * 0.82,
    backgroundColor: '#FFFFFF',
    borderRadius: 32,
    padding: 18,
    borderWidth: 1.5,
    borderColor: '#DBEAFE',
    elevation: 3,
    shadowColor: '#2563EB',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.08,
    shadowRadius: 10,
  },
  cardHeaderRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  moduleNumText: { fontSize: 11, fontWeight: '800', color: '#2563EB' },
  badgePill: { paddingHorizontal: 10, paddingVertical: 3, borderRadius: 12, backgroundColor: '#EFF6FF' },
  badgeText: { color: '#2563EB', fontSize: 10, fontWeight: '700' },
  moduleTitle: { fontSize: 15, fontWeight: '800', color: '#1E293B', marginBottom: 14 },
  roundedBtnActive: { backgroundColor: '#2563EB', borderRadius: 25, paddingVertical: 10, paddingHorizontal: 16, flexDirection: 'row', alignItems: 'center', justifyContent: 'center' },
  roundedBtnActiveText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },
});