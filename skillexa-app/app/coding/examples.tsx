import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  SafeAreaView,
  StatusBar,
} from 'react-native';
import { router, useLocalSearchParams } from 'expo-router';
import { Feather, MaterialCommunityIcons } from '@expo/vector-icons';

// --- Types ---
interface ExampleSnippet {
  id: string;
  title: string;
  tag: string;
  code: string;
  output: string;
  explanation: string[];
}

// --- Multi-Language Example Dataset ---
const EXAMPLES_DATA: Record<string, ExampleSnippet[]> = {
  c: [
    {
      id: 'c1',
      title: 'Hello World & Print Formatting',
      tag: 'Basics',
      code: `#include <stdio.h>\n\nint main() {\n    printf("Welcome to SkillExa C Track!\\n");\n    int value = 42;\n    printf("Sample integer value: %d\\n", value);\n    return 0;\n}`,
      output: 'Welcome to SkillExa C Track!\nSample integer value: 42',
      explanation: [
        '#include <stdio.h> imports standard input/output functions like printf().',
        'int main() defines the main execution entry point.',
        '%d is a format specifier for printing signed integer variables.',
      ],
    },
    {
      id: 'c2',
      title: 'Swapping Values Using Pointers',
      tag: 'Pointers',
      code: `#include <stdio.h>\n\nvoid swap(int *a, int *b) {\n    int temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nint main() {\n    int x = 10, y = 20;\n    swap(&x, &y);\n    printf("x = %d, y = %d\\n", x, y);\n    return 0;\n}`,
      output: 'x = 20, y = 10',
      explanation: [
        'int *a defines pointer parameters holding variable memory addresses.',
        '&x passes the memory address of x to the swap function.',
        '*a dereferences the pointer to modify the actual stored memory value.',
      ],
    },
  ],
  cpp: [
    {
      id: 'cpp1',
      title: 'Vector Dynamic Array Operations',
      tag: 'STL',
      code: `#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> numbers = {10, 20, 30};\n    numbers.push_back(40);\n    for (int n : numbers) {\n        cout << n << " ";\n    }\n    return 0;\n}`,
      output: '10 20 30 40',
      explanation: [
        'vector<int> creates a dynamically resizing integer array container.',
        '.push_back() appends a new element to the tail of the vector.',
        'for (int n : numbers) uses range-based iteration over the container.',
      ],
    },
  ],
  python: [
    {
      id: 'py1',
      title: 'List Comprehension & Filtering',
      tag: 'Data Structures',
      code: `numbers = [1, 2, 3, 4, 5, 6]\nevens = [n for n in numbers if n % 2 == 0]\nprint(f"Even numbers: {evens}")`,
      output: 'Even numbers: [2, 4, 6]',
      explanation: [
        'List comprehension creates a new list in a single concise line.',
        'if n % 2 == 0 filters elements based on the modulo arithmetic condition.',
        'f"" enables string interpolation directly embedding expression values.',
      ],
    },
  ],
  java: [
    {
      id: 'j1',
      title: 'String Builder Palindrome Check',
      tag: 'Strings',
      code: `public class Main {\n    public static void main(String[] args) {\n        String input = "radar";\n        String reversed = new StringBuilder(input).reverse().toString();\n        System.out.println("Is Palindrome: " + input.equals(reversed));\n    }\n}`,
      output: 'Is Palindrome: true',
      explanation: [
        'StringBuilder offers mutable character sequences for memory efficiency.',
        '.reverse() reverses the character order in place.',
        '.equals() evaluates content value equality between String objects.',
      ],
    },
  ],
  javascript: [
    {
      id: 'js1',
      title: 'Array Transformation via map() & filter()',
      tag: 'ES6 Methods',
      code: `const nums = [1, 2, 3, 4, 5];\nconst doubledEvens = nums\n  .filter(n => n % 2 === 0)\n  .map(n => n * 2);\nconsole.log(doubledEvens);`,
      output: '[ 4, 8 ]',
      explanation: [
        '.filter() produces a subset matching the Boolean predicate.',
        '.map() executes a callback function modifying every array item.',
        'Arrow functions (=>) offer concise inline function declarations.',
      ],
    },
  ],
};

export default function ExamplesScreen() {
  const { langId, langName } = useLocalSearchParams<{ langId: string; langName: string }>();

  const activeKey = (langId || 'c').toLowerCase();
  const examples = EXAMPLES_DATA[activeKey] || EXAMPLES_DATA.c;
  const displayTitle = langName || 'C Programming';

  const [expandedId, setExpandedId] = useState<string>(examples[0]?.id || '');

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
          <Feather name="arrow-left" size={20} color="#1E293B" />
        </TouchableOpacity>
        <View style={styles.headerTitleBox}>
          <Text style={styles.headerTitle}>Syntax & Examples</Text>
          <Text style={styles.headerSub}>{displayTitle}</Text>
        </View>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {examples.map((item, index) => {
          const isExpanded = expandedId === item.id;
          return (
            <View key={item.id} style={styles.exampleCard}>
              
              {/* Card Header Accordion Trigger */}
              <TouchableOpacity
                style={styles.cardHeaderRow}
                onPress={() => setExpandedId(isExpanded ? '' : item.id)}
                activeOpacity={0.7}
              >
                <View style={styles.headerTitleContainer}>
                  <View style={styles.indexBadge}>
                    <Text style={styles.indexText}>#{index + 1}</Text>
                  </View>
                  <View style={{ flex: 1 }}>
                    <Text style={styles.cardTitle}>{item.title}</Text>
                    <View style={styles.tagBadge}>
                      <Text style={styles.tagText}>{item.tag}</Text>
                    </View>
                  </View>
                </View>
                <Feather
                  name={isExpanded ? 'chevron-up' : 'chevron-down'}
                  size={20}
                  color="#64748B"
                />
              </TouchableOpacity>

              {/* Accordion Content */}
              {isExpanded && (
                <View style={styles.cardBody}>
                  
                  {/* Code Snippet Box */}
                  <View style={styles.codeContainer}>
                    <View style={styles.codeHeader}>
                      <Feather name="code" size={12} color="#94A3B8" />
                      <Text style={styles.codeHeaderTitle}>Source Code</Text>
                    </View>
                    <Text style={styles.codeText}>{item.code}</Text>
                  </View>

                  {/* Output Terminal Stream Box */}
                  <View style={styles.outputContainer}>
                    <View style={styles.outputHeader}>
                      <Feather name="terminal" size={12} color="#10B981" />
                      <Text style={styles.outputHeaderTitle}>Expected Output</Text>
                    </View>
                    <Text style={styles.outputText}>{item.output}</Text>
                  </View>

                  {/* Step-by-Step Breakdown */}
                  <Text style={styles.explanationTitle}>Line-by-Line Breakdown:</Text>
                  {item.explanation.map((exp, i) => (
                    <View key={i} style={styles.explanationRow}>
                      <View style={styles.bulletDot} />
                      <Text style={styles.explanationText}>{exp}</Text>
                    </View>
                  ))}

                  {/* Open in Compiler Button */}
                  <TouchableOpacity
                    style={styles.openCompilerBtn}
                    onPress={() =>
                      router.push({
                        pathname: '/coding/compiler',
                        params: { langId: activeKey, langName: displayTitle },
                      })
                    }
                  >
                    <Feather name="play" size={12} color="#FFFFFF" style={{ marginRight: 6 }} />
                    <Text style={styles.openCompilerBtnText}>Run Example in Compiler</Text>
                  </TouchableOpacity>

                </View>
              )}
            </View>
          );
        })}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 24,
    paddingTop: 12,
    paddingBottom: 14,
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
  },
  backBtn: {
    marginRight: 14,
  },
  headerTitleBox: {
    flex: 1,
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#1E293B',
  },
  headerSub: {
    fontSize: 12,
    color: '#64748B',
    fontWeight: '500',
  },
  scrollContent: {
    padding: 24,
  },
  exampleCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    marginBottom: 16,
    overflow: 'hidden',
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.03,
    shadowRadius: 8,
    elevation: 2,
  },
  cardHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: 16,
    backgroundColor: '#F8FAFC',
  },
  headerTitleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
    marginRight: 12,
  },
  indexBadge: {
    backgroundColor: '#EFF6FF',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 8,
    marginRight: 12,
  },
  indexText: {
    fontSize: 12,
    fontWeight: '800',
    color: '#2563EB',
  },
  cardTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: '#1E293B',
  },
  tagBadge: {
    alignSelf: 'flex-start',
    marginTop: 4,
  },
  tagText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#64748B',
  },
  cardBody: {
    padding: 16,
    borderTopWidth: 1,
    borderTopColor: '#F1F5F9',
  },
  codeContainer: {
    backgroundColor: '#0F172A',
    borderRadius: 12,
    padding: 12,
    marginBottom: 12,
  },
  codeHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
    paddingBottom: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#1E293B',
  },
  codeHeaderTitle: {
    fontSize: 11,
    fontWeight: '700',
    color: '#94A3B8',
    marginLeft: 6,
    textTransform: 'uppercase',
  },
  codeText: {
    fontFamily: 'monospace',
    fontSize: 12,
    color: '#F8FAFC',
    lineHeight: 18,
  },
  outputContainer: {
    backgroundColor: '#F1F5F9',
    borderRadius: 10,
    padding: 12,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  outputHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 6,
  },
  outputHeaderTitle: {
    fontSize: 11,
    fontWeight: '700',
    color: '#15803D',
    marginLeft: 6,
    textTransform: 'uppercase',
  },
  outputText: {
    fontFamily: 'monospace',
    fontSize: 12,
    color: '#0F172A',
    fontWeight: '700',
  },
  explanationTitle: {
    fontSize: 13,
    fontWeight: '700',
    color: '#1E293B',
    marginBottom: 8,
  },
  explanationRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 6,
  },
  bulletDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#2563EB',
    marginTop: 6,
    marginRight: 8,
  },
  explanationText: {
    fontSize: 12,
    color: '#475569',
    flex: 1,
    lineHeight: 18,
  },
  openCompilerBtn: {
    backgroundColor: '#2563EB',
    borderRadius: 10,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 14,
  },
  openCompilerBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
});