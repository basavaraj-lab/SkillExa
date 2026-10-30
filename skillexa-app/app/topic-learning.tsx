import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
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
import {
  C_ALL_54_TOPICS,
  CPP_ALL_73_TOPICS,
  JAVA_ALL_120_TOPICS,
  JS_ALL_108_TOPICS,
  PYTHON_ALL_67_TOPICS,
  PYTHON_FUNDAMENTALS_17_TOPICS,
  TopicItem,
} from '../data/topicCatalogData';
import { ApiClient } from '../services/api';
import { CodeExecutionService, ExecutionResult } from '../services/codeExecutionService';

export const getTopicDatasetForLanguage = (lang: string): TopicItem[] => {
  const l = (lang || 'python').toLowerCase();
  if (l === 'c') return C_ALL_54_TOPICS;
  if (l === 'cpp' || l === 'c++') return CPP_ALL_73_TOPICS;
  if (l === 'java') return JAVA_ALL_120_TOPICS;
  if (l === 'js' || l === 'javascript') return JS_ALL_108_TOPICS;
  return PYTHON_ALL_67_TOPICS;
};

export default function TopicLearningPage() {
  const params = useLocalSearchParams<{
    topicId?: string;
    language?: string;
    subject?: string;
    topic?: string;
  }>();

  const language = params.language || 'python';
  const topicId = params.topicId || '1';
  const paramSubject = params.subject;
  const paramTopic = params.topic;

  // Determine if this is a subject/aptitude curriculum (e.g. Mathematics, Reasoning, English, etc.)
  // or a programming track (c, cpp, java, js, python)
  const isSubjectLearning = Boolean(
    paramSubject && !['c', 'cpp', 'c++', 'java', 'js', 'javascript', 'python'].includes(paramSubject.toLowerCase())
  ) || Boolean(
    paramTopic && !params.topicId && (!params.language || params.language === 'python')
  );

  const currentSubject = paramSubject || (paramTopic ? 'Mathematics' : 'Programming');
  const currentTopicTitle = paramTopic || (isSubjectLearning ? 'Percentage & Profit/Loss' : '');

  const idNum = parseInt(topicId, 10) || 1;
  const currentDataset = getTopicDatasetForLanguage(language);
  const initialTopic: TopicItem =
    currentDataset.find((t) => t.id === idNum) || currentDataset[0];

  const [topicData, setTopicData] = useState<TopicItem>(initialTopic);
  const [activeStep, setActiveStep] = useState<number>(1);
  const [completedSteps, setCompletedSteps] = useState<number[]>([1]);

  // Subject / Aptitude module state
  const [subjectModule, setSubjectModule] = useState<any>(null);
  const [isLoadingSubject, setIsLoadingSubject] = useState<boolean>(false);
  const [isRegeneratingMCQs, setIsRegeneratingMCQs] = useState<boolean>(false);

  // Dynamic Options & Questions from Backend/Dataset
  const [progOptions, setProgOptions] = useState<string[]>(
    initialTopic.progOptions || ['print', 'input', 'echo', 'printf']
  );
  const [fillQuestion, setFillQuestion] = useState<string>(
    initialTopic.fillQuestion || '# Display output on the screen\n_____("Hello, World!")\n'
  );
  const [fillOptions, setFillOptions] = useState<string[]>(
    initialTopic.fillOptions || ['print', 'input', 'write', 'display']
  );
  const [fillAnswers, setFillAnswers] = useState<string[]>(
    initialTopic.fillAnswers || ['print']
  );
  const [testQuestions, setTestQuestions] = useState<any[]>(
    initialTopic.skillExaTest || []
  );

  const [activePill, setActivePill] = useState<string | null>(null);
  const [progAnswer, setProgAnswer] = useState<string | null>(null);

  // Step 3: Programming Sandbox State
  const [userCode, setUserCode] = useState<string>(
    topicData.starterCode || '_____("Hello, World!")'
  );
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [executionResult, setExecutionResult] = useState<ExecutionResult | null>(null);

  // Step 4: Fill in Blanks State (Multi-blank support)
  const [blankInputs, setBlankInputs] = useState<{ [index: number]: string }>({});
  const [activeBlankIdx, setActiveBlankIdx] = useState<number>(0);
  const [blankFeedback, setBlankFeedback] = useState<string | null>(null);

  // Step 5: Test State (All 5 questions)
  const [userAnswers, setUserAnswers] = useState<{ [qId: number]: number }>({});
  const [testScore, setTestScore] = useState<number | null>(null);

  useEffect(() => {
    let isMounted = true;
    // Reset state for new topic
    setActiveStep(1);
    setCompletedSteps([1]);
    setTestScore(null);
    setUserAnswers({});
    setBlankInputs({});
    setActiveBlankIdx(0);
    setBlankFeedback(null);
    setExecutionResult(null);
    setActivePill(null);
    setProgAnswer(null);

    // If this is an aptitude or non-programming subject topic, route to dedicated Aptitude Test with LLM questions
    if (isSubjectLearning) {
      const targetCategory =
        currentSubject?.toLowerCase() === 'mathematics' ? 'Quantitative Aptitude'
        : currentSubject?.toLowerCase().includes('reason') ? 'Logical Reasoning'
        : currentSubject?.toLowerCase().includes('english') ? 'Verbal Ability'
        : 'Quantitative Aptitude';

      router.replace({
        pathname: '/aptitude-test',
        params: {
          category: targetCategory,
          topic: currentTopicTitle || 'Percentages',
          autoStart: 'true',
        },
      });
      return;
    }

    // Otherwise standard programming track logic
    const normalizeExp = (exp: any): string[] => {
      if (Array.isArray(exp)) return exp.map(String);
      if (typeof exp === 'string' && exp.trim()) {
        return exp.includes('\n') ? exp.split('\n').filter((s) => s.trim().length > 0) : [exp];
      }
      return [];
    };

    const ensureBlankInCode = (code: string): string => {
      if (!code || typeof code !== 'string') return '_____("Hello, World!")';
      if (/_{2,}/.test(code)) return code;
      const cSym = code.includes('#include') || code.includes('import') || code.includes('class') || code.includes('using namespace') || code.includes('//') ? '//' : '#';
      return `${cSym} Select option pill to fill blank below:\n${cSym} _____\n\n${code}`;
    };

    const langDataset = getTopicDatasetForLanguage(language);
    const freshTopic = langDataset.find((t: TopicItem) => t.id === idNum) || langDataset[0];
    const initialCode = ensureBlankInCode(freshTopic.starterCode || '_____("Hello, World!")');

    setTopicData({
      ...freshTopic,
      explanation: normalizeExp(freshTopic.explanation),
      starterCode: initialCode,
    });
    setUserCode(initialCode);
    setProgOptions(freshTopic.progOptions || ['print', 'input', 'echo', 'printf']);
    setFillQuestion(freshTopic.fillQuestion || '# Display output on screen\n_____("Hello, World!")\n');
    setFillOptions(freshTopic.fillOptions || ['print', 'input', 'write', 'display']);
    setFillAnswers(freshTopic.fillAnswers || ['print']);
    setTestQuestions(freshTopic.skillExaTest || []);

    ApiClient.getTopicDetails(idNum, language).then((res) => {
      if (isMounted && res.success && res.data) {
        const d = res.data;
        const apiStarterCode = d.programming?.starter_code ? ensureBlankInCode(d.programming.starter_code) : initialCode;
        setTopicData((prev) => {
          const rawExp = d.examples?.explanation !== undefined ? d.examples.explanation : prev.explanation;
          return {
            ...prev,
            id: d.id,
            title: d.title,
            difficulty: d.difficulty,
            duration: d.duration,
            concept: d.information?.concept || prev.concept,
            syntax: d.information?.syntax || prev.syntax,
            exampleCode: d.examples?.code || prev.exampleCode,
            exampleOutput: d.examples?.output || prev.exampleOutput,
            explanation: normalizeExp(rawExp),
            starterCode: apiStarterCode,
          };
        });

        if (d.programming) {
          if (d.programming.starter_code) setUserCode(apiStarterCode);
          if (d.programming.options && Array.isArray(d.programming.options)) {
            setProgOptions(d.programming.options);
          }
          if (d.programming.answer) {
            setProgAnswer(d.programming.answer);
          }
        }

        if (d.fill_blanks) {
          if (d.fill_blanks.question) setFillQuestion(d.fill_blanks.question);
          if (d.fill_blanks.answers) setFillAnswers(d.fill_blanks.answers);
          if (d.fill_blanks.options && Array.isArray(d.fill_blanks.options)) {
            setFillOptions(d.fill_blanks.options);
          }
        }

        if (d.test && Array.isArray(d.test) && d.test.length > 0) {
          setTestQuestions(d.test);
        }
      }
    });
    return () => {
      isMounted = false;
    };
  }, [idNum, language, isSubjectLearning, currentSubject, currentTopicTitle]);

  const handleStepClick = (stepNum: number) => {
    if (stepNum > Math.max(...completedSteps) + 1) {
      alert(`Step ${stepNum} is locked! Complete previous sections first.`);
      return;
    }
    setActiveStep(stepNum);
  };

  const advanceToNextStep = (currentStep: number) => {
    if (!completedSteps.includes(currentStep + 1)) {
      setCompletedSteps([...completedSteps, currentStep + 1]);
    }
    if (currentStep < 5) {
      setActiveStep(currentStep + 1);
    }
  };

  const handleRunCode = async () => {
    setIsRunning(true);
    setExecutionResult(null);

    try {
      const res = await CodeExecutionService.executeCode(language || 'python', userCode);

      // Validate selected option against progAnswer if specified
      if (progAnswer && activePill && activePill.trim() !== progAnswer.trim()) {
        setExecutionResult({
          status: 'Wrong Answer',
          output: res.output || `Program executed with option "${activePill}".`,
          error: `Execution completed, but option "${activePill}" did not satisfy the exercise requirements. Try another option!`,
          runtimeMs: res.runtimeMs || 0,
          memoryMb: 0,
          testCasesPassed: 0,
          totalTestCases: 1,
        });
      } else {
        setExecutionResult(res);
      }
    } catch (err: any) {
      setExecutionResult({
        status: 'Runtime Error',
        output: '',
        error: err.message || 'Execution error',
        runtimeMs: 0,
        memoryMb: 0,
        testCasesPassed: 0,
        totalTestCases: 1,
      });
    } finally {
      setIsRunning(false);
    }
  };

  const insertPillIntoCode = (pillVal: string) => {
    const blankRegex = /_{2,}/;

    let newCode = userCode;
    if (blankRegex.test(userCode)) {
      newCode = userCode.replace(blankRegex, pillVal);
    } else if (activePill && userCode.includes(activePill)) {
      newCode = userCode.replace(activePill, pillVal);
    } else {
      const foundOpt = progOptions.find((opt) => opt !== pillVal && userCode.includes(opt));
      if (foundOpt) {
        newCode = userCode.replace(foundOpt, pillVal);
      } else {
        newCode = `${userCode.trim()}\n${pillVal}`;
      }
    }

    setUserCode(newCode);
    setActivePill(pillVal);
    setExecutionResult(null);
  };

  const handleResetCode = () => {
    setUserCode(topicData.starterCode || '_____("Hello, World!")');
    setActivePill(null);
    setExecutionResult(null);
  };

  const handlePillClickFillBlanks = (opt: string) => {
    setBlankInputs((prev) => ({
      ...prev,
      [activeBlankIdx]: opt,
    }));
    setBlankFeedback(null);

    // Auto-advance activeBlankIdx to the next unfilled blank if available
    const totalBlanks = (fillQuestion.match(/_{2,}/g) || []).length;
    for (let next = 0; next < totalBlanks; next++) {
      if (!blankInputs[next] && next !== activeBlankIdx) {
        setActiveBlankIdx(next);
        break;
      }
    }
  };

  const verifyFillBlanks = () => {
    if (!fillAnswers || fillAnswers.length === 0) return;

    let allCorrect = true;
    for (let i = 0; i < fillAnswers.length; i++) {
      const userVal = (blankInputs[i] || '').trim().toLowerCase();
      const expectedVal = (fillAnswers[i] || '').trim().toLowerCase();
      if (userVal !== expectedVal) {
        allCorrect = false;
        break;
      }
    }

    if (allCorrect) {
      setBlankFeedback('✓ Correct! All blanks are filled correctly.');
    } else {
      setBlankFeedback('❌ Incorrect. Please check your answers and try again!');
    }
  };

  const handleRegenerateMCQs = async () => {
    if (!isSubjectLearning) return;
    setIsRegeneratingMCQs(true);
    setUserAnswers({});
    setTestScore(null);
    try {
      const res = await ApiClient.getAptitudeTopicModule(currentSubject, currentTopicTitle, 'Intermediate', 5);
      if (res.success && res.data?.mcqs) {
        setTestQuestions(res.data.mcqs);
      }
    } catch (err) {
      console.error('Error regenerating MCQs:', err);
    } finally {
      setIsRegeneratingMCQs(false);
    }
  };

  const submitFinalTest = () => {
    const questionsToGrade = testQuestions.length > 0 ? testQuestions : [
      { id: 1, correct_answer: 0 },
      { id: 2, correct_answer: 0 },
    ];

    let correctCount = 0;
    questionsToGrade.forEach((q) => {
      const expected = q.correct_option !== undefined ? q.correct_option : q.correct_answer;
      if (userAnswers[q.id] === expected) {
        correctCount++;
      }
    });

    const scorePct = Math.round((correctCount / questionsToGrade.length) * 100);
    setTestScore(scorePct);

    if (scorePct >= 50) {
      advanceToNextStep(5);
      if (!isSubjectLearning) {
        // Notify backend and unlock next topic for this language
        ApiClient.completeTopic(topicData.id, scorePct, language);

        // Unlock next topic in local language dataset
        const langDataset = getTopicDatasetForLanguage(language);
        const nextTopic = langDataset.find((t) => t.id === topicData.id + 1);
        if (nextTopic) {
          nextTopic.isUnlocked = true;
          nextTopic.status = 'IN_PROGRESS';
        }
      }
    }
  };

  const handleGoToNextTopic = () => {
    if (isSubjectLearning) {
      if (currentSubject.toLowerCase() === 'mathematics') {
        router.push('/mathematics');
      } else if (currentSubject.toLowerCase().includes('reasoning')) {
        router.push('/reasoning');
      } else if (currentSubject.toLowerCase().includes('english')) {
        router.push('/english');
      } else if (currentSubject.toLowerCase().includes('science')) {
        router.push('/science');
      } else if (currentSubject.toLowerCase().includes('awareness')) {
        router.push('/awareness');
      } else {
        router.back();
      }
      return;
    }

    const langDataset = getTopicDatasetForLanguage(language);
    const nextId = topicData.id + 1;
    if (nextId <= langDataset.length) {
      router.push({
        pathname: '/topic-learning',
        params: {
          topicId: nextId.toString(),
          language: language,
        },
      });
    } else {
      alert(`🎉 Congratulations! You have completed all ${langDataset.length} topics in the ${language.toUpperCase()} Track!`);
      router.push({
        pathname: '/coding-problems',
        params: { language: language },
      });
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#090D16" />

      {/* Top Navbar */}
      <View style={styles.navbar}>
        <View style={styles.brandRow}>
          <View style={[styles.brandLogo, isSubjectLearning && { backgroundColor: '#8B5CF6' }]}>
            <Feather name={isSubjectLearning ? 'book-open' : 'code'} size={18} color="#FFFFFF" />
          </View>
          <Text style={styles.brandTitle}>
            {isSubjectLearning
              ? `${currentSubject} Track`
              : `${language.toUpperCase() === 'CPP' ? 'C++' : language.toUpperCase()} Learning Track`}
          </Text>
        </View>

        <TouchableOpacity
          onPress={() => {
            if (isSubjectLearning) {
              if (currentSubject.toLowerCase() === 'mathematics') {
                router.push('/mathematics');
              } else if (currentSubject.toLowerCase().includes('reasoning')) {
                router.push('/reasoning');
              } else if (currentSubject.toLowerCase().includes('english')) {
                router.push('/english');
              } else if (currentSubject.toLowerCase().includes('science')) {
                router.push('/science');
              } else if (currentSubject.toLowerCase().includes('awareness')) {
                router.push('/awareness');
              } else {
                router.back();
              }
            } else {
              router.push({
                pathname: '/coding-problems',
                params: { language: language },
              });
            }
          }}
          style={styles.backBtn}
        >
          <Feather name="arrow-left" size={14} color="#38BDF8" />
          <Text style={styles.backBtnText}>
            ← Back to {isSubjectLearning ? currentSubject : `${language.toUpperCase()} Topics`}
          </Text>
        </TouchableOpacity>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {isLoadingSubject ? (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#6366F1" />
            <Text style={styles.loadingText}>Loading curriculum grounded in Wikipedia knowledge...</Text>
          </View>
        ) : (
          <>
            {/* Topic Banner Header */}
            <View style={styles.topicBanner}>
              <View style={styles.topicBannerTop}>
                <View style={{ flex: 1 }}>
                  <Text style={styles.topicSubtitle}>
                    {isSubjectLearning
                      ? `${currentSubject.toUpperCase()} • TOPIC MODULE`
                      : `${language.toUpperCase() === 'CPP' ? 'C++' : language.toUpperCase()} TOPIC ${topicData.id}`}
                  </Text>
                  <Text style={styles.topicTitle}>
                    {isSubjectLearning ? (subjectModule?.topic || currentTopicTitle) : topicData.title}
                  </Text>
                </View>

                <View style={styles.badgeRow}>
                  <View style={[styles.diffBadge, isSubjectLearning && { backgroundColor: 'rgba(139, 92, 246, 0.2)' }]}>
                    <Text style={[styles.diffBadgeText, isSubjectLearning && { color: '#C4B5FD' }]}>
                      {isSubjectLearning ? (subjectModule?.category || 'Aptitude') : topicData.difficulty}
                    </Text>
                  </View>
                  <View style={styles.timeBadge}>
                    <Feather name={isSubjectLearning ? 'globe' : 'clock'} size={12} color="#9CA3AF" />
                    <Text style={styles.timeBadgeText}>
                      {isSubjectLearning ? 'Wikipedia Grounded' : topicData.duration}
                    </Text>
                  </View>
                </View>
              </View>
            </View>

            {/* 5-Step Horizontal Navigation Stepper */}
            <View style={styles.stepperContainer}>
              <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.stepperScroll}>
                {(isSubjectLearning
                  ? [
                      { num: 1, title: '1. Theory & Wikipedia' },
                      { num: 2, title: '2. Formulas & Tricks' },
                      { num: 3, title: '3. Solved Problem' },
                      { num: 4, title: '4. Practice Drill' },
                      { num: 5, title: '5. LLM Assessment' },
                    ]
                  : [
                      { num: 1, title: '1. Information' },
                      { num: 2, title: '2. Examples' },
                      { num: 3, title: '3. Programming' },
                      { num: 4, title: '4. Fill in Blanks' },
                      { num: 5, title: '5. SkillExa Test' },
                    ]
                ).map((step, idx) => {
                  const isActive = activeStep === step.num;
                  const isUnlocked = completedSteps.includes(step.num) || step.num <= Math.max(...completedSteps) + 1;

                  return (
                    <React.Fragment key={step.num}>
                      <TouchableOpacity
                        style={[styles.stepperTab, isActive && styles.stepperTabActive]}
                        onPress={() => handleStepClick(step.num)}
                        activeOpacity={0.8}
                      >
                        {!isUnlocked && <Feather name="lock" size={11} color="#6B7280" style={{ marginRight: 4 }} />}
                        <Text style={[styles.stepperTabText, isActive && styles.stepperTabTextActive, !isUnlocked && styles.stepperTabTextLocked]}>
                          {step.title}
                        </Text>
                      </TouchableOpacity>

                      {idx < 4 && <Feather name="chevron-right" size={12} color="#4B5563" style={{ marginHorizontal: 4 }} />}
                    </React.Fragment>
                  );
                })}
              </ScrollView>
            </View>

            {/* STEP 1: INFORMATION / THEORY & WIKIPEDIA GROUNDING */}
            {activeStep === 1 && (
              <View style={styles.stepCard}>
                <View style={styles.stepCardHeader}>
                  <Feather name="book-open" size={20} color="#38BDF8" />
                  <Text style={styles.stepCardTitle}>
                    {isSubjectLearning ? 'Theoretical Grounding & Concepts' : 'Concept & Syntax'}
                  </Text>
                </View>

                {isSubjectLearning ? (
                  <>
                    <Text style={styles.conceptParagraph}>
                      {subjectModule?.concept ||
                        'Strengthen your fundamental mathematical reasoning, arithmetic operations, and speed solving skills for this topic.'}
                    </Text>

                    {/* Wikipedia Educational Grounding Card */}
                    {subjectModule?.wikipedia && (
                      <View style={styles.wikiCard}>
                        <View style={styles.wikiHeaderRow}>
                          <View style={styles.wikiBadge}>
                            <Feather name="globe" size={12} color="#38BDF8" />
                            <Text style={styles.wikiBadgeText}>WIKIPEDIA KNOWLEDGE SOURCE</Text>
                          </View>
                          <Text style={styles.wikiAttributionText}>CC BY-SA 4.0</Text>
                        </View>

                        <Text style={styles.wikiArticleTitle}>{subjectModule.wikipedia.title}</Text>
                        <Text style={styles.wikiSummaryText}>{subjectModule.wikipedia.summary}</Text>

                        {subjectModule.wikipedia.source_url && (
                          <TouchableOpacity
                            style={styles.wikiLinkBtn}
                            onPress={() => Linking.openURL(subjectModule.wikipedia.source_url)}
                            activeOpacity={0.8}
                          >
                            <Feather name="external-link" size={13} color="#38BDF8" />
                            <Text style={styles.wikiLinkBtnText}>Read Full Article on Wikipedia ↗</Text>
                          </TouchableOpacity>
                        )}
                      </View>
                    )}

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(1)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to Formulas & Shortcuts →</Text>
                    </TouchableOpacity>
                  </>
                ) : (
                  <>
                    <Text style={styles.conceptParagraph}>{topicData.concept}</Text>

                    <Text style={styles.specSubhead}>
                      {language.toUpperCase() === 'CPP' ? 'C++' : language.toUpperCase()} SYNTAX SPECIFICATION
                    </Text>
                    <View style={styles.codeSnippetBox}>
                      <Text style={styles.codeSnippetText}>{topicData.syntax}</Text>
                    </View>

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(1)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to Examples →</Text>
                    </TouchableOpacity>
                  </>
                )}
              </View>
            )}

            {/* STEP 2: EXAMPLES / FORMULAS & SHORTCUT TRICKS */}
            {activeStep === 2 && (
              <View style={styles.stepCard}>
                <View style={styles.stepCardHeader}>
                  <Feather name={isSubjectLearning ? 'zap' : 'code'} size={20} color="#6366F1" />
                  <Text style={styles.stepCardTitle}>
                    {isSubjectLearning ? 'Core Formulas & Speed Math Shortcuts' : 'Code Example & Output'}
                  </Text>
                </View>

                {isSubjectLearning ? (
                  <>
                    <Text style={styles.conceptParagraph}>
                      Master these essential formulas and time-saving calculation shortcuts tested in competitive examinations.
                    </Text>

                    {(subjectModule?.formulas || []).map((f: any, idx: number) => (
                      <View key={idx} style={styles.formulaCard}>
                        <View style={styles.formulaTitleRow}>
                          <Text style={styles.formulaName}>{f.name}</Text>
                          <View style={styles.formulaIndexBadge}>
                            <Text style={styles.formulaIndexText}>Formula #{idx + 1}</Text>
                          </View>
                        </View>

                        <View style={styles.formulaFormulaBox}>
                          <Text style={styles.formulaFormulaText}>{f.formula}</Text>
                        </View>

                        {f.shortcut ? (
                          <View style={styles.formulaShortcutBox}>
                            <Feather name="zap" size={13} color="#F59E0B" />
                            <Text style={styles.formulaShortcutText}>
                              <Text style={{ fontWeight: '800', color: '#FCD34D' }}>Speed Trick: </Text>
                              {f.shortcut}
                            </Text>
                          </View>
                        ) : null}
                      </View>
                    ))}

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(2)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to Solved Drill →</Text>
                    </TouchableOpacity>
                  </>
                ) : (
                  <>
                    <Text style={styles.specSubhead}>SAMPLE CODE SNIPPET</Text>
                    <View style={styles.codeSnippetBox}>
                      <Text style={styles.codeSnippetText}>{topicData.exampleCode}</Text>
                    </View>

                    <Text style={styles.specSubhead}>EXPECTED OUTPUT</Text>
                    <View style={styles.outputBox}>
                      <Text style={styles.outputText}>{topicData.exampleOutput}</Text>
                    </View>

                    <Text style={[styles.specSubhead, { marginTop: 14 }]}>CONCEPT BREAKDOWN</Text>
                    <View style={styles.explanationList}>
                      {(Array.isArray(topicData.explanation)
                        ? topicData.explanation
                        : typeof topicData.explanation === 'string'
                        ? [topicData.explanation]
                        : []
                      ).map((exp, i) => (
                        <Text key={i} style={styles.expItem}>{exp}</Text>
                      ))}
                    </View>

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(2)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to Programming →</Text>
                    </TouchableOpacity>
                  </>
                )}
              </View>
            )}

            {/* STEP 3: PROGRAMMING SANDBOX OR SOLVED STEP-BY-STEP PROBLEM */}
            {activeStep === 3 && (
              <View style={styles.stepCard}>
                <View style={styles.stepCardHeader}>
                  <Feather name={isSubjectLearning ? 'check-circle' : 'terminal'} size={20} color="#10B981" />
                  <Text style={styles.stepCardTitle}>
                    {isSubjectLearning ? 'Step-by-Step Solved Problem' : 'Programming Exercise & Sandbox'}
                  </Text>
                </View>

                {isSubjectLearning ? (
                  <>
                    {subjectModule?.solved_example ? (
                      <View style={styles.solvedBox}>
                        <View style={styles.solvedProblemHeader}>
                          <Text style={styles.specSubhead}>PRACTICE PROBLEM</Text>
                          <Text style={styles.solvedProblemText}>{subjectModule.solved_example.problem}</Text>
                        </View>

                        <View style={styles.solvedRow}>
                          <View style={styles.solvedChip}>
                            <Text style={styles.solvedChipLabel}>GIVEN DATA</Text>
                            <Text style={styles.solvedChipValue}>{subjectModule.solved_example.given}</Text>
                          </View>
                          <View style={styles.solvedChip}>
                            <Text style={styles.solvedChipLabel}>APPLIED FORMULA</Text>
                            <Text style={styles.solvedChipValue}>{subjectModule.solved_example.formula}</Text>
                          </View>
                        </View>

                        <Text style={[styles.specSubhead, { marginTop: 16 }]}>STEP-BY-STEP SOLUTION</Text>
                        <View style={styles.stepsContainer}>
                          {(subjectModule.solved_example.steps || []).map((st: string, sIdx: number) => (
                            <View key={sIdx} style={styles.stepItemRow}>
                              <View style={styles.stepNumberBadge}>
                                <Text style={styles.stepNumberText}>{sIdx + 1}</Text>
                              </View>
                              <Text style={styles.stepItemText}>{st}</Text>
                            </View>
                          ))}
                        </View>

                        <View style={styles.finalAnswerBox}>
                          <Feather name="check" size={16} color="#10B981" />
                          <Text style={styles.finalAnswerText}>
                            <Text style={{ fontWeight: '800' }}>Final Answer: </Text>
                            {subjectModule.solved_example.answer}
                          </Text>
                        </View>
                      </View>
                    ) : null}

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(3)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to Practice Drill →</Text>
                    </TouchableOpacity>
                  </>
                ) : (
                  <>
                    <Text style={styles.pillInstructionLabel}>CLICK TO INSERT CODE PILL INTO BLANK (_____)</Text>
                    <View style={styles.codePillsRow}>
                      {progOptions.map((opt, i) => (
                        <TouchableOpacity
                          key={i}
                          style={[styles.codePillBtn, activePill === opt && styles.codePillBtnActive]}
                          onPress={() => insertPillIntoCode(opt)}
                          activeOpacity={0.7}
                        >
                          <Text style={[styles.codePillText, activePill === opt && styles.codePillTextActive]}>{opt}</Text>
                        </TouchableOpacity>
                      ))}
                    </View>

                    {/* Dark Code Editor */}
                    <View style={styles.editorBox}>
                      <View style={styles.editorTopBar}>
                        <Text style={styles.editorFileName}>
                          main.{language === 'cpp' ? 'cpp' : language === 'c' ? 'c' : language === 'java' ? 'java' : language === 'js' ? 'js' : 'py'}
                        </Text>
                        <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                          <TouchableOpacity onPress={handleResetCode} style={styles.resetSmallBtn} activeOpacity={0.7}>
                            <Feather name="rotate-ccw" size={12} color="#9CA3AF" />
                            <Text style={styles.resetSmallBtnText}>Reset</Text>
                          </TouchableOpacity>
                          <TouchableOpacity onPress={handleRunCode} disabled={isRunning} style={styles.runSmallBtn}>
                            {isRunning ? (
                              <ActivityIndicator size="small" color="#FFFFFF" />
                            ) : (
                              <>
                                <Feather name="play" size={12} color="#FFFFFF" />
                                <Text style={styles.runSmallBtnText}>Run Code</Text>
                              </>
                            )}
                          </TouchableOpacity>
                        </View>
                      </View>

                      <TextInput
                        style={styles.editorInput}
                        multiline
                        value={userCode}
                        onChangeText={(val) => {
                          setUserCode(val);
                        }}
                        autoCapitalize="none"
                        autoCorrect={false}
                        spellCheck={false}
                      />
                    </View>

                    {/* Execution Result Box */}
                    {executionResult && (
                      <View style={styles.executionBox}>
                        <Text style={styles.execStatusText}>
                          Status: <Text style={{ color: executionResult.status === 'Accepted' ? '#10B981' : '#F43F5E' }}>{executionResult.status}</Text>
                          {' • '}⏱ {executionResult.runtimeMs} ms
                        </Text>

                        {executionResult.error ? (
                          <Text style={styles.execErrorText}>{executionResult.error}</Text>
                        ) : (
                          <Text style={styles.execOutputText}>{executionResult.output}</Text>
                        )}
                      </View>
                    )}

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(3)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to Fill in Blanks →</Text>
                    </TouchableOpacity>
                  </>
                )}
              </View>
            )}

            {/* STEP 4: INTERACTIVE FORMULA DRILL / FILL IN BLANKS */}
            {activeStep === 4 && (
              <View style={styles.stepCard}>
                <View style={styles.stepCardHeader}>
                  <Feather name="edit-3" size={20} color="#F59E0B" />
                  <Text style={styles.stepCardTitle}>
                    {isSubjectLearning ? 'Interactive Formula & Concept Drill' : 'Interactive Fill in Blanks'}
                  </Text>
                </View>

                {isSubjectLearning ? (
                  <>
                    <Text style={styles.conceptParagraph}>
                      Fill in the missing values or formula terms below to test your operational calculation speed.
                    </Text>

                    <Text style={styles.pillInstructionLabel}>CLICK A PILL TO INSERT VALUE INTO BLANK (_____)</Text>
                    <View style={styles.codePillsRow}>
                      {fillOptions.map((opt, i) => {
                        const isSelected = blankInputs[0] === opt;
                        return (
                          <TouchableOpacity
                            key={i}
                            style={[styles.codePillBtn, isSelected && styles.codePillBtnActive]}
                            onPress={() => {
                              setBlankInputs({ 0: opt });
                              setBlankFeedback(null);
                            }}
                            activeOpacity={0.7}
                          >
                            <Text style={[styles.codePillText, isSelected && styles.codePillTextActive]}>{opt}</Text>
                          </TouchableOpacity>
                        );
                      })}
                    </View>

                    <View style={styles.drillEquationBox}>
                      <Text style={styles.drillEquationTitle}>EXERCISE QUESTION</Text>
                      <Text style={styles.drillEquationText}>
                        {subjectModule?.fill_blanks?.question || fillQuestion}
                      </Text>

                      {subjectModule?.fill_blanks?.blank_text ? (
                        <View style={styles.drillBlankContainer}>
                          <Text style={styles.drillBlankPrompt}>Working Equation: </Text>
                          <Text style={styles.drillBlankFormula}>
                            {subjectModule.fill_blanks.blank_text.replace('_____', `[ ${blankInputs[0] || '_____'} ]`)}
                          </Text>
                        </View>
                      ) : null}
                    </View>

                    <TouchableOpacity
                      style={styles.verifyBtn}
                      onPress={() => {
                        const userVal = (blankInputs[0] || '').trim().toLowerCase();
                        const expected = (fillAnswers[0] || subjectModule?.fill_blanks?.answer || '').trim().toLowerCase();
                        if (userVal && (userVal === expected || userVal.replace('%', '') === expected.replace('%', ''))) {
                          setBlankFeedback('✓ Correct! You solved the formula drill accurately.');
                        } else {
                          setBlankFeedback('❌ Incorrect. Please check your answer and try another pill!');
                        }
                      }}
                      activeOpacity={0.8}
                    >
                      <Text style={styles.verifyBtnText}>Verify Formula Answer</Text>
                    </TouchableOpacity>

                    {blankFeedback && (
                      <Text style={[styles.feedbackText, blankFeedback.startsWith('✓') ? { color: '#10B981' } : { color: '#F43F5E' }]}>
                        {blankFeedback}
                      </Text>
                    )}

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(4)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to SkillExa Test →</Text>
                    </TouchableOpacity>
                  </>
                ) : (
                  <>
                    <Text style={styles.pillInstructionLabel}>CLICK A CODE PILL TO FILL BLANK ({activeBlankIdx + 1})</Text>
                    <View style={styles.codePillsRow}>
                      {fillOptions.map((opt, i) => {
                        const isSelectedInAny = Object.values(blankInputs).includes(opt);
                        const isSelectedInActive = blankInputs[activeBlankIdx] === opt;
                        return (
                          <TouchableOpacity
                            key={i}
                            style={[styles.codePillBtn, isSelectedInAny && styles.codePillBtnActive]}
                            onPress={() => handlePillClickFillBlanks(opt)}
                            activeOpacity={0.7}
                          >
                            <Text style={[styles.codePillText, isSelectedInActive && styles.codePillTextActive]}>{opt}</Text>
                          </TouchableOpacity>
                        );
                      })}
                    </View>

                    <View style={styles.codeSnippetBox}>
                      {(() => {
                        let blankCounter = 0;
                        return fillQuestion.split('\n').map((lineText, lineIdx) => {
                          const parts = lineText.split(/_{2,}/);
                          if (parts.length < 2) {
                            return (
                              <Text key={lineIdx} style={styles.codeSnippetText}>
                                {lineText}
                              </Text>
                            );
                          }
                          return (
                            <View key={lineIdx} style={{ flexDirection: 'row', alignItems: 'center', flexWrap: 'wrap', marginVertical: 2 }}>
                              {parts.map((part, pIdx) => {
                                const currentBlankIdx = blankCounter;
                                if (pIdx < parts.length - 1) {
                                  blankCounter++;
                                }
                                const isFocused = activeBlankIdx === currentBlankIdx;
                                return (
                                  <React.Fragment key={pIdx}>
                                    <Text style={styles.codeSnippetText}>{part}</Text>
                                    {pIdx < parts.length - 1 && (
                                      <TextInput
                                        style={[
                                          styles.blankInput,
                                          { marginHorizontal: 6 },
                                          isFocused && styles.blankInputActive,
                                        ]}
                                        placeholder="____"
                                        placeholderTextColor="#6B7280"
                                        value={blankInputs[currentBlankIdx] || ''}
                                        onFocus={() => setActiveBlankIdx(currentBlankIdx)}
                                        onChangeText={(val) => {
                                          setBlankInputs((prev) => ({ ...prev, [currentBlankIdx]: val }));
                                        }}
                                        autoCapitalize="none"
                                      />
                                    )}
                                  </React.Fragment>
                                );
                              })}
                            </View>
                          );
                        });
                      })()}
                    </View>

                    <TouchableOpacity style={styles.verifyBtn} onPress={verifyFillBlanks}>
                      <Text style={styles.verifyBtnText}>Verify Answer</Text>
                    </TouchableOpacity>

                    {blankFeedback && (
                      <Text style={[styles.feedbackText, blankFeedback.startsWith('✓') ? { color: '#10B981' } : { color: '#F43F5E' }]}>
                        {blankFeedback}
                      </Text>
                    )}

                    <TouchableOpacity style={styles.continueBtn} onPress={() => advanceToNextStep(4)} activeOpacity={0.85}>
                      <Text style={styles.continueBtnText}>Complete & Continue to SkillExa Test →</Text>
                    </TouchableOpacity>
                  </>
                )}
              </View>
            )}

            {/* STEP 5: SKILLEXA TEST (LLM MCQs) */}
            {activeStep === 5 && (
              <View style={styles.stepCard}>
                <View style={styles.stepCardHeader}>
                  <Feather name="award" size={20} color="#EC4899" />
                  <Text style={styles.stepCardTitle}>SkillExa Assessment Test</Text>
                </View>

                {isSubjectLearning && (
                  <View style={styles.llmHeaderBadgeRow}>
                    <View style={styles.llmAiBadge}>
                      <Feather name="cpu" size={12} color="#A78BFA" />
                      <Text style={styles.llmAiBadgeText}>
                        {subjectModule?.provider_used === 'gemini' ? 'Gemini 2.5 Flash' : 'LLM Aptitude Generator'} Grounded in Wikipedia
                      </Text>
                    </View>

                    <TouchableOpacity
                      style={styles.regenerateBtn}
                      onPress={handleRegenerateMCQs}
                      disabled={isRegeneratingMCQs}
                      activeOpacity={0.7}
                    >
                      {isRegeneratingMCQs ? (
                        <ActivityIndicator size="small" color="#38BDF8" />
                      ) : (
                        <>
                          <Feather name="refresh-cw" size={12} color="#38BDF8" />
                          <Text style={styles.regenerateBtnText}>Regenerate Fresh MCQs</Text>
                        </>
                      )}
                    </TouchableOpacity>
                  </View>
                )}

                <Text style={styles.conceptParagraph}>
                  Score at least 50% on this topic assessment to master {isSubjectLearning ? currentTopicTitle : topicData.title}!
                </Text>

                {testQuestions.map((q, qIdx) => {
                  const selectedOpt = userAnswers[q.id];
                  const correctIdx = q.correct_option !== undefined ? q.correct_option : q.correct_answer;
                  const isGraded = testScore !== null;
                  const isUserCorrect = selectedOpt === correctIdx;

                  return (
                    <View key={q.id || qIdx} style={styles.quizQuestionBox}>
                      <Text style={styles.quizQTitle}>
                        Q{qIdx + 1}. {q.question}
                      </Text>

                      {(q.options || []).map((opt: string, optIdx: number) => {
                        const isSelected = selectedOpt === optIdx;
                        let optStyle = [styles.quizOptionBtn, isSelected && styles.quizOptionActive];

                        if (isGraded) {
                          if (optIdx === correctIdx) {
                            optStyle = [styles.quizOptionBtn, styles.quizOptionCorrect];
                          } else if (isSelected && !isUserCorrect) {
                            optStyle = [styles.quizOptionBtn, styles.quizOptionWrong];
                          }
                        }

                        return (
                          <TouchableOpacity
                            key={optIdx}
                            style={optStyle}
                            onPress={() => {
                              if (testScore === null) {
                                setUserAnswers({ ...userAnswers, [q.id]: optIdx });
                              }
                            }}
                            activeOpacity={testScore === null ? 0.8 : 1}
                          >
                            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                              <View
                                style={[
                                  styles.optRadio,
                                  isSelected && styles.optRadioActive,
                                  isGraded && optIdx === correctIdx && styles.optRadioCorrect,
                                ]}
                              >
                                <Text style={styles.optRadioLetter}>{String.fromCharCode(65 + optIdx)}</Text>
                              </View>
                              <Text style={[styles.quizOptionText, isSelected && styles.quizOptionTextActive, { flex: 1 }]}>
                                {opt}
                              </Text>
                            </View>
                          </TouchableOpacity>
                        );
                      })}

                      {/* Detailed Step-by-Step Explanation when Graded */}
                      {isGraded && q.explanation && (
                        <View style={styles.explanationBox}>
                          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 4 }}>
                            <Feather
                              name={isUserCorrect ? 'check-circle' : 'info'}
                              size={14}
                              color={isUserCorrect ? '#10B981' : '#38BDF8'}
                            />
                            <Text style={[styles.explanationHeader, { color: isUserCorrect ? '#10B981' : '#38BDF8' }]}>
                              {isUserCorrect ? 'Correct! Detailed Solution:' : 'Explanation & Calculation:'}
                            </Text>
                          </View>
                          <Text style={styles.explanationBody}>{q.explanation}</Text>
                        </View>
                      )}
                    </View>
                  );
                })}

                <TouchableOpacity style={styles.continueBtn} onPress={submitFinalTest} activeOpacity={0.85}>
                  <Text style={styles.continueBtnText}>
                    {testScore !== null ? 'Re-Submit Assessment' : 'Submit Topic Test & Verify Mastery'}
                  </Text>
                </TouchableOpacity>

                {testScore !== null && (
                  <View style={styles.scoreResultBox}>
                    <Text style={styles.scoreTitle}>Score: {testScore}%</Text>
                    {testScore >= 50 ? (
                      <>
                        <Text style={styles.scorePassedText}>
                          🎉 Topic Mastered! Verified by SkillExa Assessment.
                        </Text>
                        <TouchableOpacity
                          style={[styles.continueBtn, { backgroundColor: '#10B981', marginTop: 14 }]}
                          onPress={handleGoToNextTopic}
                          activeOpacity={0.85}
                        >
                          <Text style={styles.continueBtnText}>
                            {isSubjectLearning ? `← Back to ${currentSubject}` : `Continue to Topic ${topicData.id + 1} →`}
                          </Text>
                        </TouchableOpacity>
                      </>
                    ) : (
                      <Text style={styles.scoreFailedText}>
                        Minimum 50% required. Review the theory & formulas, or click &quot;Regenerate Fresh MCQs&quot; to try a new test!
                      </Text>
                    )}
                  </View>
                )}
              </View>
            )}
          </>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#090D16',
  },
  navbar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingVertical: 14,
    backgroundColor: 'rgba(9, 13, 22, 0.95)',
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(99, 102, 241, 0.25)',
  },
  brandRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  brandLogo: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#6366F1',
    alignItems: 'center',
    justifyContent: 'center',
  },
  brandTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  backBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  backBtnText: {
    fontSize: 13,
    color: '#38BDF8',
    fontWeight: '600',
  },
  scrollContent: {
    paddingHorizontal: 20,
    paddingTop: 20,
    paddingBottom: 60,
  },
  topicBanner: {
    backgroundColor: 'rgba(18, 26, 43, 0.85)',
    borderWidth: 1,
    borderColor: 'rgba(99, 102, 241, 0.3)',
    borderRadius: 20,
    padding: 20,
    marginBottom: 20,
  },
  topicBannerTop: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
  },
  topicSubtitle: {
    fontSize: 11,
    fontWeight: '800',
    color: '#38BDF8',
    letterSpacing: 0.8,
    marginBottom: 4,
  },
  topicTitle: {
    fontSize: 26,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  badgeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  diffBadge: {
    backgroundColor: 'rgba(99, 102, 241, 0.2)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 8,
  },
  diffBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#A5B4FC',
  },
  timeBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 8,
  },
  timeBadgeText: {
    fontSize: 11,
    color: '#9CA3AF',
  },
  stepperContainer: {
    marginBottom: 20,
    backgroundColor: 'rgba(18, 26, 43, 0.85)',
    borderRadius: 14,
    padding: 8,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
  },
  stepperScroll: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  stepperTab: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 10,
  },
  stepperTabActive: {
    backgroundColor: '#6366F1',
  },
  stepperTabText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#9CA3AF',
  },
  stepperTabTextActive: {
    color: '#FFFFFF',
    fontWeight: '800',
  },
  stepperTabTextLocked: {
    color: '#6B7280',
  },
  stepCard: {
    backgroundColor: 'rgba(18, 26, 43, 0.85)',
    borderWidth: 1,
    borderColor: 'rgba(99, 102, 241, 0.3)',
    borderRadius: 20,
    padding: 20,
  },
  stepCardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    marginBottom: 14,
  },
  stepCardTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  conceptParagraph: {
    fontSize: 14,
    color: '#9CA3AF',
    lineHeight: 22,
    marginBottom: 16,
  },
  specSubhead: {
    fontSize: 11,
    fontWeight: '800',
    color: '#38BDF8',
    letterSpacing: 0.8,
    marginBottom: 8,
  },
  pillInstructionLabel: {
    fontSize: 11,
    fontWeight: '800',
    color: '#38BDF8',
    letterSpacing: 0.8,
    marginBottom: 10,
  },
  codePillsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 10,
    marginBottom: 16,
  },
  codePillBtn: {
    backgroundColor: 'rgba(255, 255, 255, 0.06)',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.15)',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 10,
  },
  codePillBtnActive: {
    backgroundColor: 'rgba(99, 102, 241, 0.35)',
    borderColor: '#818CF8',
  },
  codePillText: {
    color: '#A5B4FC',
    fontSize: 13,
    fontWeight: '700',
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
  },
  codePillTextActive: {
    color: '#38BDF8',
    fontWeight: '800',
  },
  codeSnippetBox: {
    backgroundColor: '#0F172A',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 20,
  },
  codeSnippetText: {
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 13,
    color: '#A5B4FC',
    lineHeight: 20,
  },
  outputBox: {
    backgroundColor: '#1E293B',
    borderRadius: 10,
    padding: 12,
    marginBottom: 16,
  },
  outputText: {
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 13,
    color: '#10B981',
  },
  explanationList: {
    gap: 6,
    marginBottom: 20,
  },
  expItem: {
    fontSize: 13,
    color: '#9CA3AF',
    lineHeight: 20,
  },
  continueBtn: {
    backgroundColor: '#6366F1',
    paddingVertical: 14,
    borderRadius: 12,
    alignItems: 'center',
    marginTop: 10,
  },
  continueBtnText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  editorBox: {
    backgroundColor: '#0F172A',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    marginBottom: 16,
    overflow: 'hidden',
  },
  editorTopBar: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    paddingHorizontal: 12,
    paddingVertical: 8,
  },
  editorFileName: {
    fontSize: 12,
    color: '#9CA3AF',
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
  },
  resetSmallBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.15)',
  },
  resetSmallBtnText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#9CA3AF',
  },
  runSmallBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#10B981',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
  },
  runSmallBtnText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  editorInput: {
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 13,
    color: '#F3F4F6',
    padding: 12,
    minHeight: 120,
    textAlignVertical: 'top',
  },
  executionBox: {
    backgroundColor: '#1E293B',
    borderRadius: 10,
    padding: 12,
    marginBottom: 16,
  },
  execStatusText: {
    fontSize: 12,
    color: '#9CA3AF',
    marginBottom: 6,
    fontWeight: '600',
  },
  execOutputText: {
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 12,
    color: '#10B981',
  },
  execErrorText: {
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 12,
    color: '#F43F5E',
  },
  blankInput: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    color: '#10B981',
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 13,
    fontWeight: '800',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
    minWidth: 80,
    borderWidth: 1,
    borderColor: 'transparent',
  },
  blankInputActive: {
    borderColor: '#38BDF8',
    backgroundColor: 'rgba(56, 189, 248, 0.2)',
  },
  verifyBtn: {
    backgroundColor: 'rgba(245, 158, 11, 0.2)',
    borderWidth: 1,
    borderColor: '#F59E0B',
    paddingVertical: 10,
    borderRadius: 10,
    alignItems: 'center',
    marginBottom: 10,
  },
  verifyBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#F59E0B',
  },
  feedbackText: {
    fontSize: 13,
    fontWeight: '600',
    marginBottom: 12,
  },
  quizQuestionBox: {
    marginBottom: 16,
  },
  quizQTitle: {
    fontSize: 14,
    fontWeight: '700',
    color: '#FFFFFF',
    marginBottom: 10,
  },
  quizOptionBtn: {
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    padding: 12,
    borderRadius: 10,
    marginBottom: 6,
  },
  quizOptionActive: {
    backgroundColor: 'rgba(99, 102, 241, 0.25)',
    borderColor: '#6366F1',
  },
  quizOptionText: {
    fontSize: 13,
    color: '#9CA3AF',
  },
  quizOptionTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  scoreResultBox: {
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
    borderWidth: 1,
    borderColor: '#10B981',
    borderRadius: 12,
    padding: 16,
    marginTop: 16,
    alignItems: 'center',
  },
  scoreTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#FFFFFF',
    marginBottom: 4,
  },
  scorePassedText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#10B981',
    textAlign: 'center',
  },
  scoreFailedText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#F43F5E',
    textAlign: 'center',
  },
  wikiCard: {
    backgroundColor: '#0F172A',
    borderWidth: 1,
    borderColor: 'rgba(56, 189, 248, 0.35)',
    borderRadius: 14,
    padding: 16,
    marginBottom: 20,
  },
  wikiHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  wikiBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(56, 189, 248, 0.15)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
  },
  wikiBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#38BDF8',
    letterSpacing: 0.5,
  },
  wikiAttributionText: {
    fontSize: 10,
    color: '#94A3B8',
    fontWeight: '600',
  },
  wikiArticleTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#FFFFFF',
    marginBottom: 8,
  },
  wikiSummaryText: {
    fontSize: 13,
    color: '#CBD5E1',
    lineHeight: 20,
    marginBottom: 12,
  },
  wikiLinkBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 14,
    paddingVertical: 8,
    backgroundColor: 'rgba(56, 189, 248, 0.1)',
    borderWidth: 1,
    borderColor: 'rgba(56, 189, 248, 0.3)',
    borderRadius: 8,
    alignSelf: 'flex-start',
  },
  wikiLinkBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#38BDF8',
  },
  formulaCard: {
    backgroundColor: 'rgba(30, 41, 59, 0.6)',
    borderWidth: 1,
    borderColor: 'rgba(99, 102, 241, 0.25)',
    borderRadius: 12,
    padding: 14,
    marginBottom: 14,
  },
  formulaTitleRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  formulaName: {
    fontSize: 14,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  formulaIndexBadge: {
    backgroundColor: 'rgba(99, 102, 241, 0.2)',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
  },
  formulaIndexText: {
    fontSize: 10,
    fontWeight: '700',
    color: '#A5B4FC',
  },
  formulaFormulaBox: {
    backgroundColor: '#0F172A',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 8,
    padding: 12,
    marginBottom: 8,
  },
  formulaFormulaText: {
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 13,
    fontWeight: '700',
    color: '#10B981',
  },
  formulaShortcutBox: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 8,
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.2)',
    padding: 10,
    borderRadius: 8,
  },
  formulaShortcutText: {
    fontSize: 12,
    color: '#E2E8F0',
    lineHeight: 18,
    flex: 1,
  },
  solvedBox: {
    backgroundColor: 'rgba(15, 23, 42, 0.7)',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 14,
    padding: 16,
    marginBottom: 16,
  },
  solvedProblemHeader: {
    marginBottom: 14,
  },
  solvedProblemText: {
    fontSize: 15,
    fontWeight: '600',
    color: '#FFFFFF',
    lineHeight: 22,
  },
  solvedRow: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 12,
  },
  solvedChip: {
    flex: 1,
    backgroundColor: 'rgba(255, 255, 255, 0.04)',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 8,
    padding: 10,
  },
  solvedChipLabel: {
    fontSize: 10,
    fontWeight: '800',
    color: '#94A3B8',
    letterSpacing: 0.5,
    marginBottom: 4,
  },
  solvedChipValue: {
    fontSize: 12,
    fontWeight: '600',
    color: '#38BDF8',
  },
  stepsContainer: {
    gap: 10,
    marginBottom: 16,
  },
  stepItemRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 10,
  },
  stepNumberBadge: {
    width: 22,
    height: 22,
    borderRadius: 11,
    backgroundColor: 'rgba(99, 102, 241, 0.3)',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 1,
  },
  stepNumberText: {
    fontSize: 11,
    fontWeight: '800',
    color: '#A5B4FC',
  },
  stepItemText: {
    fontSize: 13,
    color: '#E2E8F0',
    flex: 1,
    lineHeight: 19,
  },
  finalAnswerBox: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
    borderWidth: 1,
    borderColor: '#10B981',
    borderRadius: 10,
    padding: 12,
  },
  finalAnswerText: {
    fontSize: 13,
    color: '#10B981',
  },
  drillEquationBox: {
    backgroundColor: '#0F172A',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
  },
  drillEquationTitle: {
    fontSize: 10,
    fontWeight: '800',
    color: '#94A3B8',
    letterSpacing: 0.8,
    marginBottom: 6,
  },
  drillEquationText: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FFFFFF',
    lineHeight: 20,
    marginBottom: 12,
  },
  drillBlankContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.04)',
    padding: 12,
    borderRadius: 8,
  },
  drillBlankPrompt: {
    fontSize: 11,
    fontWeight: '700',
    color: '#A5B4FC',
    marginBottom: 4,
  },
  drillBlankFormula: {
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 13,
    fontWeight: '700',
    color: '#38BDF8',
  },
  llmHeaderBadgeRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 14,
    flexWrap: 'wrap',
    gap: 8,
  },
  llmAiBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(168, 85, 247, 0.15)',
    borderWidth: 1,
    borderColor: 'rgba(168, 85, 247, 0.3)',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 8,
  },
  llmAiBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#C084FC',
  },
  regenerateBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(56, 189, 248, 0.15)',
    borderWidth: 1,
    borderColor: 'rgba(56, 189, 248, 0.35)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 8,
  },
  regenerateBtnText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#38BDF8',
  },
  optRadio: {
    width: 22,
    height: 22,
    borderRadius: 11,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  optRadioActive: {
    backgroundColor: '#6366F1',
  },
  optRadioCorrect: {
    backgroundColor: '#10B981',
  },
  optRadioLetter: {
    fontSize: 11,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  quizOptionCorrect: {
    backgroundColor: 'rgba(16, 185, 129, 0.2)',
    borderColor: '#10B981',
  },
  quizOptionWrong: {
    backgroundColor: 'rgba(244, 63, 94, 0.2)',
    borderColor: '#F43F5E',
  },
  explanationBox: {
    backgroundColor: '#0F172A',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.08)',
    borderRadius: 10,
    padding: 12,
    marginTop: 8,
  },
  explanationHeader: {
    fontSize: 12,
    fontWeight: '700',
  },
  explanationBody: {
    fontSize: 12,
    color: '#94A3B8',
    lineHeight: 18,
  },
  loadingContainer: {
    paddingVertical: 60,
    alignItems: 'center',
    justifyContent: 'center',
  },
  loadingText: {
    fontSize: 13,
    color: '#9CA3AF',
    marginTop: 14,
    fontWeight: '600',
  },
});
