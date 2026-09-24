import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  StatusBar,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { router, useLocalSearchParams } from 'expo-router';
import { Feather, MaterialCommunityIcons } from '@expo/vector-icons';

interface TopicDetail {
  id: string;
  title: string;
  definition: string;
  keyPoints: string[];
  codeExample: string;
}

interface LanguageBasics {
  langName: string;
  topics: TopicDetail[];
}

const LANGUAGE_TOPICS: Record<string, LanguageBasics> = {
  python: {
    langName: 'Python 3',
    topics: [
      {
        id: 'intro',
        title: '1. Introduction to Python Core',
        definition: 'Python is a high-level, interpreted, dynamically-typed programming language built for simplicity and rapid prototyping.',
        keyPoints: [
          'Interpreted execution (no manual compilation required).',
          'Enforces clear readable code using indentation.',
          'Cross-platform support across Windows, macOS, and Linux.',
        ],
        codeExample: `# Introduction Example\nprint("Welcome to SkillExa Python Track!")`,
      },
      {
        id: 'variables',
        title: '2. Variables & Assignment',
        definition: 'Variables are symbolic names that act as references to objects stored in memory.',
        keyPoints: [
          'Created automatically on value assignment.',
          'No explicit type declaration needed.',
          'Case-sensitive naming (age vs Age).',
        ],
        codeExample: `name = "SkillExa"\nversion = 3.12\nprint(f"{name} running Python {version}")`,
      },
      {
        id: 'data-types',
        title: '3. Data Types',
        definition: 'Python provides diverse built-in types including numeric, sequence, mapping, and boolean types.',
        keyPoints: [
          'Primitives: int, float, str, bool.',
          'Data Structures: list, tuple, dict, set.',
          'Check type using type() function.',
        ],
        codeExample: `count = 100\nratio = 4.5\nis_active = True\nprint(type(count), type(ratio), type(is_active))`,
      },
      {
        id: 'conditions',
        title: '4. Conditional Statements',
        definition: 'Conditionals allow branching execution flow based on boolean expressions using if, elif, and else.',
        keyPoints: [
          'Uses 4-space indentation for code blocks.',
          'Logical operators: and, or, not.',
        ],
        codeExample: `score = 85\nif score >= 90:\n    print("Grade A")\nelif score >= 75:\n    print("Grade B")\nelse:\n    print("Grade C")`,
      },
      {
        id: 'strings',
        title: '5. Strings & Formatting',
        definition: 'Strings are immutable sequences of characters enclosed within single, double, or triple quotes.',
        keyPoints: [
          'Supports indexing and slicing [start:end].',
          'f-strings provide clean variable interpolation.',
        ],
        codeExample: `msg = "Python Programming"\nprint(msg.upper())\nprint(msg[:6])`,
      },
      {
        id: 'call-by-ref',
        title: '6. Call by Reference / Object Passing',
        definition: 'Python passes references to objects. Modifying a mutable object inside a function alters the original data.',
        keyPoints: [
          'Immutable types (int, str, tuple) cannot be modified in-place.',
          'Mutable types (list, dict) reflect changes caller-side.',
        ],
        codeExample: `def add_element(arr):\n    arr.append(99)\n\nnums = [1, 2, 3]\nadd_element(nums)\nprint(nums)  # Output: [1, 2, 3, 99]`,
      },
      {
        id: 'structures',
        title: '7. Data Structures & Classes',
        definition: 'Object-oriented classes and structs allow modeling real-world custom data structures.',
        keyPoints: [
          'Defined using class keyword.',
          '__init__ constructor initializes instance attributes.',
        ],
        codeExample: `class User:\n    def __init__(self, name, role):\n        self.name = name\n        self.role = role\n\nu = User("Srujan", "Developer")\nprint(u.name, u.role)`,
      },
    ],
  },
  c: {
    langName: 'C Programming',
    topics: [
      {
        id: 'intro',
        title: '1. Introduction & Main Function',
        definition: 'C is a general-purpose procedural language delivering fast speed and direct hardware control.',
        keyPoints: [
          'Compiled language producing native binaries.',
          'Header inclusion via #include directives.',
          'Program execution starts inside main().',
        ],
        codeExample: `#include <stdio.h>\nint main() {\n    printf("Welcome to C Language Track!\\n");\n    return 0;\n}`,
      },
      {
        id: 'call-by-ref',
        title: '6. Call by Reference (Pointers)',
        definition: 'C passes memory addresses using pointers to modify variables in caller scope.',
        keyPoints: [
          'Use & to obtain variable memory address.',
          'Use * operator to dereference pointers.',
        ],
        codeExample: `#include <stdio.h>\nvoid increment(int *val) {\n    (*val)++;\n}\nint main() {\n    int x = 10;\n    increment(&x);\n    printf("Value: %d\\n", x);\n    return 0;\n}`,
      },
      {
        id: 'structures',
        title: '7. Structures (struct)',
        definition: 'A struct packs multiple variables of different data types under one identifier.',
        keyPoints: [
          'Declared using struct keyword.',
          'Access fields using dot (.) operator.',
        ],
        codeExample: `#include <stdio.h>\nstruct Student {\n    int id;\n    float gpa;\n};\nint main() {\n    struct Student s1 = {101, 3.9};\n    printf("ID: %d, GPA: %.1f\\n", s1.id, s1.gpa);\n    return 0;\n}`,
      },
    ],
  },
};

export default function LanguageBasicsDocScreen() {
  const { langId, langName } = useLocalSearchParams<{ langId: string; langName: string }>();

  const currentLangKey = (langId || 'python').toLowerCase();
  const langData = LANGUAGE_TOPICS[currentLangKey] || LANGUAGE_TOPICS.python;
  const displayTitle = langName || langData.langName;

  const [activeTopicId, setActiveTopicId] = useState<string>(langData.topics[0]?.id || 'intro');
  const selectedTopic = langData.topics.find((t) => t.id === activeTopicId) || langData.topics[0];

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Top Bar Header */}
      <View style={styles.topBar}>
        <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
          <Feather name="arrow-left" size={20} color="#1E293B" />
        </TouchableOpacity>
        <View style={{ flex: 1 }}>
          <Text style={styles.topBarSub}>{displayTitle} Essentials</Text>
          <Text style={styles.topBarTitle}>Topic Documentation</Text>
        </View>
      </View>

      {/* Horizontal Topic Pill Selector */}
      <View style={styles.topicBar}>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.topicScroll}>
          {langData.topics.map((t) => {
            const isSelected = activeTopicId === t.id;
            return (
              <TouchableOpacity
                key={t.id}
                style={[styles.topicPill, isSelected && styles.topicPillActive]}
                onPress={() => setActiveTopicId(t.id)}
              >
                <Text style={[styles.topicPillText, isSelected && styles.topicPillTextActive]}>
                  {t.title}
                </Text>
              </TouchableOpacity>
            );
          })}
        </ScrollView>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        
        {/* Definition & Concept Card */}
        <View style={styles.card}>
          <Text style={styles.topicHeaderTitle}>{selectedTopic.title}</Text>
          <Text style={styles.topicDefinition}>{selectedTopic.definition}</Text>

          <Text style={styles.subHeading}>Key Points:</Text>
          {selectedTopic.keyPoints.map((pt, idx) => (
            <View key={idx} style={styles.bulletRow}>
              <Text style={styles.bulletDot}>•</Text>
              <Text style={styles.bulletText}>{pt}</Text>
            </View>
          ))}
        </View>

        {/* Code Example Card */}
        <View style={styles.card}>
          <View style={styles.cardHeaderRow}>
            <Feather name="code" size={16} color="#2563EB" style={{ marginRight: 6 }} />
            <Text style={styles.cardHeaderTitle}>Example Syntax</Text>
          </View>

          <View style={styles.codeBox}>
            <Text style={styles.codeText}>{selectedTopic.codeExample}</Text>
          </View>
        </View>

        {/* Bottom Rounded Done Button */}
        <TouchableOpacity style={styles.roundedBackBtn} onPress={() => router.back()}>
          <Feather name="check-circle" size={16} color="#FFFFFF" style={{ marginRight: 6 }} />
          <Text style={styles.roundedBackText}>Back to Syllabus</Text>
        </TouchableOpacity>

      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: 12,
    paddingBottom: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  backBtn: {
    marginRight: 12,
  },
  topBarSub: {
    fontSize: 11,
    fontWeight: '700',
    color: '#2563EB',
    textTransform: 'uppercase',
  },
  topBarTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#0F172A',
  },
  topicBar: {
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
    paddingVertical: 10,
    backgroundColor: '#F8FAFC',
  },
  topicScroll: {
    paddingHorizontal: 20,
  },
  topicPill: {
    paddingHorizontal: 16,
    paddingVertical: 6,
    borderRadius: 20,
    backgroundColor: '#E2E8F0',
    marginRight: 8,
  },
  topicPillActive: {
    backgroundColor: '#2563EB',
  },
  topicPillText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
  },
  topicPillTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  scrollContent: {
    padding: 20,
  },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 18,
    padding: 18,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    elevation: 2,
  },
  topicHeaderTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: '#0F172A',
    marginBottom: 8,
  },
  topicDefinition: {
    fontSize: 13,
    color: '#334155',
    lineHeight: 19,
    marginBottom: 14,
  },
  subHeading: {
    fontSize: 12,
    fontWeight: '700',
    color: '#0F172A',
    marginBottom: 6,
  },
  bulletRow: {
    flexDirection: 'row',
    marginBottom: 4,
  },
  bulletDot: {
    fontSize: 12,
    color: '#2563EB',
    marginRight: 6,
    fontWeight: '800',
  },
  bulletText: {
    fontSize: 12,
    color: '#475569',
    flex: 1,
  },
  cardHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  cardHeaderTitle: {
    fontSize: 14,
    fontWeight: '700',
    color: '#0F172A',
  },
  codeBox: {
    backgroundColor: '#0F172A',
    borderRadius: 14,
    padding: 14,
  },
  codeText: {
    fontFamily: 'monospace',
    fontSize: 12,
    color: '#38BDF8',
    lineHeight: 18,
  },
  roundedBackBtn: {
    backgroundColor: '#2563EB',
    borderRadius: 25,
    paddingVertical: 14,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 8,
    marginBottom: 20,
  },
  roundedBackText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '700',
  },
});