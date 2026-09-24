import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useMemo, useState } from 'react';
import {
  Alert,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { getEngineeringTopic } from '../../data/engineeringCurriculum';

interface QuizQuestion {
  question: string;
  options: string[];
  correctIndex: number;
  explanation?: string;
}

interface LessonDetail {
  overview: string;
  points: string[];
  syntax: string;
  exampleCode: string;
  quiz: QuizQuestion[];
}

const LESSON_DATABASE: Record<string, LessonDetail> = {
  // Python 3
  python_intro: {
    overview: 'Python is a high-level, interpreted language designed for readability and developer ergonomics. Created by Guido van Rossum, it relies on whitespace indentation for code structure.',
    points: ['Bytecode is executed on the Python Virtual Machine (PVM).', 'Dynamic typing allows runtime variable reassignment.', 'Clean syntax accelerates development speed in AI, Data Science & Backend systems.'],
    syntax: 'print("Hello, World!")',
    exampleCode: '# Python 3 Core Syntax\nimport sys\n\nname = "SkillExa Scholar"\nversion = sys.version.split()[0]\nprint(f"Welcome {name}! Running Python {version}")',
    quiz: [
      { question: '1. Who originally designed and created Python?', options: ['Dennis Ritchie', 'Guido van Rossum', 'Bjarne Stroustrup', 'James Gosling'], correctIndex: 1, explanation: 'Guido van Rossum released Python in 1991.' },
      { question: '2. How are code blocks and scopes demarcated in Python?', options: ['Curly Braces {}', 'Semicolons ;', 'Whitespace Indentation', 'Parentheses ()'], correctIndex: 2, explanation: 'Python strictly enforces indentation for scope blocks.' },
      { question: '3. What type of language execution model does Python use?', options: ['Compiled to machine code only', 'Interpreted bytecode on VM', 'Assembly transcription', 'Hardware FPGA synthesis'], correctIndex: 1, explanation: 'Python compiles source code to .pyc bytecode and interprets it on the PVM.' },
      { question: '4. Which built-in function writes text output to the console?', options: ['echo()', 'cout <<', 'printf()', 'print()'], correctIndex: 3, explanation: 'print() is Python’s standard output function.' },
      { question: '5. What is the standard file extension for Python source files?', options: ['.pt', '.py', '.python', '.exe'], correctIndex: 1, explanation: 'Python scripts use the .py file extension.' },
    ],
  },
  python_variables: {
    overview: 'Variables in Python act as dynamic name-tags referencing heap memory objects without requiring explicit datatype declarations.',
    points: ['Core primitive types include int, float, str, and bool.', 'Inspect runtime object class using the type() function.', 'Immutable primitives cannot have their in-place value altered in memory.'],
    syntax: 'variable_name = value',
    exampleCode: '# Variable Binding & Dynamic Types\nuser_id = 101\ngpa = 3.92\nuser_name = "Ganesh"\nis_enrolled = True\n\nprint(f"Student: {user_name} (ID: {user_id}), GPA: {gpa}, Status: {is_enrolled}")',
    quiz: [
      { question: '1. Which of the following is a valid Python variable declaration?', options: ['int x = 5;', 'var x = 5;', 'x = 5', 'declare x = 5'], correctIndex: 2, explanation: 'Python assigns variables dynamically via name = value.' },
      { question: '2. What function inspects an object’s runtime datatype?', options: ['typeof()', 'type()', 'class()', 'gettype()'], correctIndex: 1, explanation: 'type(obj) returns the class type of the object.' },
      { question: '3. Which Python type represents Unicode character sequences?', options: ['int', 'float', 'str', 'bool'], correctIndex: 2, explanation: 'str stores text strings in Python 3.' },
      { question: '4. Are variable identifiers case-sensitive in Python?', options: ['Yes (val and Val are distinct)', 'No', 'Only in function arguments', 'Only in class names'], correctIndex: 0, explanation: 'Python is strictly case-sensitive.' },
      { question: '5. Which symbol is used for variable assignment in Python?', options: ['==', '=', ':=', '->'], correctIndex: 1, explanation: '= is the basic assignment operator.' },
    ],
  },
  python_functions: {
    overview: 'Functions in Python are first-class citizens defined using the def keyword. They can accept positional arguments, *args, and **kwargs, and return any object.',
    points: ['Functions can be assigned to variables, passed as arguments, and returned from functions.', 'Variable scope resolution strictly follows the LEGB rule (Local, Enclosing, Global, Built-in).', 'Docstrings enclosed in triple quotes provide built-in documentation.'],
    syntax: 'def function_name(param1, param2=default):\n    return result',
    exampleCode: 'def calculate_metrics(score, max_score=100):\n    """Computes percentage score."""\n    pct = (score / max_score) * 100\n    return round(pct, 2)\n\nprint(f"Percentage: {calculate_metrics(87)}%")',
    quiz: [
      { question: '1. Which keyword defines a function in Python?', options: ['func', 'function', 'def', 'fn'], correctIndex: 2, explanation: 'def begins a function definition in Python.' },
      { question: '2. What does *args collect in a function signature?', options: ['Keyword arguments as dict', 'Positional arguments as tuple', 'Memory pointer address', 'Return values'], correctIndex: 1, explanation: '*args gathers extra positional arguments into a tuple.' },
      { question: '3. What order does Python search when resolving variable scope?', options: ['Global -> Local -> Builtin', 'Local -> Enclosing -> Global -> Built-in (LEGB)', 'Built-in -> Global -> Local', 'Random order'], correctIndex: 1, explanation: 'LEGB rule governs scope resolution in Python.' },
      { question: '4. What keyword creates anonymous inline functions?', options: ['def', 'lambda', 'inline', 'arrow'], correctIndex: 1, explanation: 'lambda creates lightweight anonymous functions.' },
      { question: '5. What happens if a function body executes without an explicit return statement?', options: ['Returns 0', 'Returns None', 'Throws SyntaxError', 'Returns False'], correctIndex: 1, explanation: 'Python functions implicitly return None when no return statement is encountered.' },
    ],
  },

  // C Programming
  c_intro: {
    overview: 'C is a general-purpose, procedural programming language developed by Dennis Ritchie at Bell Labs. It provides low-level memory access and compiles directly to native machine code.',
    points: ['Standard entry point is the main() function.', 'Code execution begins with preprocessor directives (#include, #define).', 'Static typing requires explicit datatype declarations.'],
    syntax: '#include <stdio.h>\nint main() {\n    printf("Hello World\\n");\n    return 0;\n}',
    exampleCode: '#include <stdio.h>\n\nint main() {\n    int student_id = 101;\n    printf("SkillExa C System - Enrolled ID: %d\\n", student_id);\n    return 0;\n}',
    quiz: [
      { question: '1. Who designed and created the C programming language?', options: ['Dennis Ritchie', 'Bjarne Stroustrup', 'James Gosling', 'Ken Thompson'], correctIndex: 0, explanation: 'Dennis Ritchie developed C at Bell Labs in 1972.' },
      { question: '2. What is the required entry-point function for every C program?', options: ['start()', 'main()', 'init()', '_start()'], correctIndex: 1, explanation: 'int main() is the standard C program entry point.' },
      { question: '3. What format specifier in printf prints an integer?', options: ['%f', '%s', '%d', '%c'], correctIndex: 2, explanation: '%d or %i outputs signed decimal integers.' },
      { question: '4. What symbol terminates statements in C?', options: [':', ';', '.', ','], correctIndex: 1, explanation: 'Semicolons ; terminate statements in C.' },
      { question: '5. Which preprocessor directive imports standard I/O headers?', options: ['import stdio;', '#include <stdio.h>', 'using namespace std;', '#require <stdio>'], correctIndex: 1, explanation: '#include <stdio.h> includes the standard input/output header.' },
    ],
  },
  c_pointers: {
    overview: 'A pointer in C is a variable that stores the virtual memory address of another variable. Pointers are essential for dynamic memory allocation, arrays, and low-level system hardware programming.',
    points: ['& is the address-of operator; * is the dereference operator.', 'Pointer arithmetic scales addresses by sizeof(type).', 'Always check for NULL before dereferencing heap-allocated memory.'],
    syntax: 'int *ptr = &variable;\n*ptr = 50;',
    exampleCode: '#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    int val = 42;\n    int *ptr = &val;\n    printf("Value: %d, Address: %p\\n", *ptr, (void*)ptr);\n    return 0;\n}',
    quiz: [
      { question: '1. Which operator retrieves the memory address of a variable in C?', options: ['*', '&', '->', '%'], correctIndex: 1, explanation: '& is the address-of operator.' },
      { question: '2. What happens when an integer pointer ptr is incremented by 1 (ptr++) on a 32-bit architecture with sizeof(int)=4?', options: ['Address increments by 1 byte', 'Address increments by 4 bytes', 'Value pointed to increments by 1', 'Syntax error'], correctIndex: 1, explanation: 'Pointer arithmetic scales by sizeof(type), moving 4 bytes.' },
      { question: '3. What is a pointer that points to deallocated memory called?', options: ['Null pointer', 'Void pointer', 'Dangling pointer', 'Wild pointer'], correctIndex: 2, explanation: 'A dangling pointer points to freed or invalid memory.' },
      { question: '4. Which standard library function dynamically allocates memory on the heap?', options: ['alloc()', 'malloc()', 'create()', 'new()'], correctIndex: 1, explanation: 'malloc() allocates raw uninitialized heap memory.' },
      { question: '5. What function must be called to release heap memory allocated with malloc?', options: ['delete()', 'free()', 'release()', 'dispose()'], correctIndex: 1, explanation: 'free(ptr) releases allocated heap blocks.' },
    ],
  },
};

export default function LessonTheoryScreen() {
  const { langId, langName, moduleNum, topicTitle, topicKey } = useLocalSearchParams<{
    langId: string;
    langName: string;
    moduleNum: string;
    topicTitle: string;
    topicKey: string;
  }>();

  const title = topicTitle || 'Language Fundamentals & Theory';
  const language = langName || 'Python';

  // Dynamic lesson resolver: checks LESSON_DATABASE or falls back to structured curriculum database
  const lesson: LessonDetail = useMemo(() => {
    const rawKey = `${(langId || 'python').toLowerCase()}_${(topicKey || topicTitle || 'intro').toLowerCase().replace(/[^a-z0-9]/g, '_')}`;
    
    // Check direct key match
    if (LESSON_DATABASE[rawKey]) {
      return LESSON_DATABASE[rawKey];
    }

    // Check partial key matches
    if (rawKey.includes('var') && LESSON_DATABASE.python_variables) {
      return LESSON_DATABASE.python_variables;
    }
    if (rawKey.includes('func') && LESSON_DATABASE.python_functions) {
      return LESSON_DATABASE.python_functions;
    }
    if (rawKey.includes('pointer') && LESSON_DATABASE.c_pointers) {
      return LESSON_DATABASE.c_pointers;
    }
    if ((langId === 'c' || language.toLowerCase() === 'c') && LESSON_DATABASE.c_intro) {
      return LESSON_DATABASE.c_intro;
    }
    if (LESSON_DATABASE[`${(langId || 'python').toLowerCase()}_intro`]) {
      return LESSON_DATABASE[`${(langId || 'python').toLowerCase()}_intro`];
    }

    // Dynamic curriculum lookup from engineering database
    const topicCurriculum = getEngineeringTopic(language, title);
    return {
      overview: topicCurriculum.overview || `${title} is a core foundation topic in ${language}. It establishes key syntax rules, memory management patterns, and production idioms.`,
      points: topicCurriculum.importantConcepts && topicCurriculum.importantConcepts.length > 0
        ? topicCurriculum.importantConcepts
        : [
            `Core syntax and structural guarantees of ${title}.`,
            `Runtime memory considerations and deterministic flow.`,
            `Best practices for testability, clean code, and zero runtime errors.`,
          ],
      syntax: topicCurriculum.formulas && topicCurriculum.formulas.length > 0 ? topicCurriculum.formulas[0] : `// ${language}: ${title} syntax pattern`,
      exampleCode: topicCurriculum.examples && topicCurriculum.examples.length > 0 && topicCurriculum.examples[0].example
        ? topicCurriculum.examples[0].example
        : `// SkillExa ${language} Live Example\n// Topic: ${title}\n\nfunction executeTopic() {\n    console.log("Mastering ${title} in ${language}");\n}\nexecuteTopic();`,
      quiz: topicCurriculum.questions && topicCurriculum.questions.length > 0
        ? topicCurriculum.questions.map((q, idx) => ({
            question: `${idx + 1}. ${q.question}`,
            options: q.options || ['Option A', 'Option B', 'Option C', 'Option D'],
            correctIndex: typeof q.correctAnswer === 'number' ? q.correctAnswer : 0,
            explanation: q.explanation || 'Verified principle.',
          }))
        : [
            { question: `1. What is the fundamental principle of ${title} in ${language}?`, options: ['Maintain deterministic execution', 'Random memory indexing', 'Bypass type checking', 'Ignore error bounds'], correctIndex: 0, explanation: 'Deterministic flow guarantees clean execution.' },
            { question: `2. Which approach represents best practice when working with ${title}?`, options: ['Encapsulate logic cleanly', 'Hardcode magic values', 'Ignore memory safety', 'Avoid unit testing'], correctIndex: 0, explanation: 'Encapsulation fosters modularity and reuse.' },
            { question: `3. How is scope managed during ${title} execution?`, options: ['Via lexical block scope', 'Unbounded global pollution', 'Hardware bypass', 'None of the above'], correctIndex: 0, explanation: 'Lexical block scoping isolates variables.' },
            { question: `4. Why is test verification important in ${title}?`, options: ['Prevents edge-case regressions', 'Increases bundle bloat', 'Slows compiler down', 'No specific reason'], correctIndex: 0, explanation: 'Testing prevents runtime regression bugs.' },
            { question: `5. What is the optimal time complexity for standard operations in ${title}?`, options: ['O(1) to O(N)', 'O(N^4)', 'O(2^N)', 'Unbounded'], correctIndex: 0, explanation: 'Standard algorithmic operations target linear or constant time.' },
          ],
    };
  }, [langId, topicKey, topicTitle, language, title]);

  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, number>>({});
  const [quizCompleted, setQuizCompleted] = useState<boolean>(false);
  const [score, setScore] = useState<number>(0);

  const handleSelectOption = (qIdx: number, oIdx: number) => {
    setSelectedAnswers((prev) => ({ ...prev, [qIdx]: oIdx }));
  };

  const handleSubmitQuiz = () => {
    const totalQ = (lesson?.quiz || []).length;
    if (Object.keys(selectedAnswers).length < totalQ) {
      Alert.alert('Incomplete Quiz', `Please answer all ${totalQ} questions before submitting.`);
      return;
    }

    let calculatedScore = 0;
    (lesson?.quiz || []).forEach((q, idx) => {
      if (selectedAnswers[idx] === q.correctIndex) {
        calculatedScore += 1;
      }
    });

    setScore(calculatedScore);
    setQuizCompleted(true);
    Alert.alert('Unit Complete! 🎉', `You scored ${calculatedScore} out of ${totalQ}! Module progress marked as 100%.`);
  };

  const handleLaunchCompiler = () => {
    router.push({
      pathname: '/coding/compiler',
      params: {
        langId: langId || 'python',
        langName: language,
        initialCode: lesson?.exampleCode || '',
      },
    });
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        title={title}
        subtitle={`${language} • ${moduleNum || 'MODULE 01'}`}
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Theory Card */}
        <View style={styles.roundedCard}>
          <View style={styles.cardHeaderRow}>
            <Feather name="book-open" size={18} color={Palette.primary} />
            <Text style={styles.cardHeaderTitle}>In-Depth Theory & Concepts</Text>
          </View>
          <Text style={styles.descText}>{lesson?.overview}</Text>

          <Text style={styles.subHeading}>Key Takeaways & Core Rules:</Text>
          {(lesson?.points || []).map((pt, idx) => (
            <View key={idx} style={styles.bulletRow}>
              <Text style={styles.bulletDot}>•</Text>
              <Text style={styles.bulletText}>{pt}</Text>
            </View>
          ))}
        </View>

        {/* Runnable Code Snippet */}
        <View style={styles.roundedCard}>
          <View style={styles.cardHeaderRow}>
            <Feather name="code" size={18} color={Palette.aiPurple} />
            <Text style={styles.cardHeaderTitle}>Executable Code Demonstration</Text>
          </View>
          <View style={styles.codeBox}>
            <Text style={styles.codeText}>{lesson?.exampleCode}</Text>
          </View>

          <TouchableOpacity style={styles.compilerPillBtn} onPress={handleLaunchCompiler} activeOpacity={0.85}>
            <Feather name="play" size={15} color="#FFFFFF" style={{ marginRight: 8 }} />
            <Text style={styles.compilerPillBtnText}>Open & Run in Live Compiler</Text>
          </TouchableOpacity>
        </View>

        {/* Module Quiz */}
        <View style={styles.roundedCard}>
          <View style={styles.cardHeaderRow}>
            <Feather name="check-circle" size={18} color={Palette.success} />
            <Text style={styles.cardHeaderTitle}>
              Module Knowledge Quiz ({(lesson?.quiz || []).length} Questions)
            </Text>
          </View>
          <Text style={styles.descText}>
            Test your understanding to complete this module unit and update your SkillExa progress.
          </Text>

          {(lesson?.quiz || []).map((q, qIdx) => (
            <View key={qIdx} style={styles.quizBox}>
              <Text style={styles.questionText}>{q.question}</Text>
              {q.options.map((opt, oIdx) => {
                const isSelected = selectedAnswers[qIdx] === oIdx;
                const isCorrect = q.correctIndex === oIdx;

                let optionStyle: any = styles.optionBtn;
                if (quizCompleted) {
                  if (isCorrect) optionStyle = [styles.optionBtn, styles.correctOption];
                  else if (isSelected) optionStyle = [styles.optionBtn, styles.wrongOption];
                } else if (isSelected) {
                  optionStyle = [styles.optionBtn, styles.selectedOption];
                }

                return (
                  <TouchableOpacity
                    key={oIdx}
                    style={optionStyle}
                    onPress={() => !quizCompleted && handleSelectOption(qIdx, oIdx)}
                    activeOpacity={0.8}
                  >
                    <Text style={styles.optionText}>{opt}</Text>
                  </TouchableOpacity>
                );
              })}
              {quizCompleted && q.explanation ? (
                <Text style={styles.explanationText}>💡 {q.explanation}</Text>
              ) : null}
            </View>
          ))}

          {!quizCompleted ? (
            <TouchableOpacity style={styles.submitQuizBtn} onPress={handleSubmitQuiz} activeOpacity={0.85}>
              <Text style={styles.submitQuizBtnText}>Submit Quiz & Verify Answers</Text>
            </TouchableOpacity>
          ) : (
            <View style={styles.resultBox}>
              <Text style={styles.resultText}>
                Quiz Score: {score} / {(lesson?.quiz || []).length} Correct!
              </Text>
            </View>
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  roundedCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  cardHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 10,
  },
  cardHeaderTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  descText: { fontSize: 13, color: Palette.textBody, lineHeight: 19, marginBottom: 12 },
  subHeading: { fontSize: 12, fontWeight: '700', color: Palette.textTitle, marginBottom: 8 },
  bulletRow: { flexDirection: 'row', marginBottom: 6 },
  bulletDot: { fontSize: 12, color: Palette.primary, marginRight: 8, fontWeight: '800' },
  bulletText: { fontSize: 12.5, color: Palette.textSecondary, flex: 1, lineHeight: 18 },
  codeBox: {
    backgroundColor: Palette.bgDark,
    borderRadius: Radii.card,
    padding: 14,
    marginBottom: 14,
    borderWidth: 1,
    borderColor: '#1E293B',
  },
  codeText: { fontFamily: 'monospace', fontSize: 12, color: Palette.cyan, lineHeight: 18 },
  compilerPillBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    ...Shadows.button,
  },
  compilerPillBtnText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },

  /* Quiz Styling */
  quizBox: {
    marginBottom: 14,
    backgroundColor: Palette.backgroundSecondary,
    padding: 14,
    borderRadius: Radii.card,
    borderWidth: 1,
    borderColor: Palette.borderSubtle,
  },
  questionText: { fontSize: 13.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 10 },
  optionBtn: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: Radii.button,
    paddingVertical: 10,
    paddingHorizontal: 12,
    marginBottom: 6,
  },
  selectedOption: { borderColor: Palette.primary, backgroundColor: Palette.primaryLight },
  correctOption: { borderColor: Palette.success, backgroundColor: Palette.successLight },
  wrongOption: { borderColor: Palette.danger, backgroundColor: Palette.dangerLight },
  optionText: { fontSize: 12.5, fontWeight: '600', color: Palette.textTitle },
  explanationText: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 6, fontStyle: 'italic' },
  submitQuizBtn: {
    backgroundColor: Palette.success,
    borderRadius: Radii.button,
    paddingVertical: 12,
    alignItems: 'center',
    marginTop: 6,
    ...Shadows.button,
  },
  submitQuizBtnText: { color: '#FFFFFF', fontSize: 13.5, fontWeight: '700' },
  resultBox: {
    padding: 14,
    backgroundColor: Palette.successLight,
    borderRadius: Radii.card,
    alignItems: 'center',
    marginTop: 6,
    borderWidth: 1,
    borderColor: Palette.successBorder,
  },
  resultText: { fontSize: 14.5, fontWeight: '800', color: Palette.success },
});