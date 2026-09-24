import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
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
  const { topicId = '1', language = 'python' } = useLocalSearchParams<{
    topicId: string;
    language: string;
  }>();

  const idNum = parseInt(topicId, 10) || 1;
  const currentDataset = getTopicDatasetForLanguage(language);
  const initialTopic: TopicItem =
    currentDataset.find((t) => t.id === idNum) || currentDataset[0];

  const [topicData, setTopicData] = useState<TopicItem>(initialTopic);
  const [activeStep, setActiveStep] = useState<number>(1);
  const [completedSteps, setCompletedSteps] = useState<number[]>([1]);

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
  }, [idNum, language]);

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

  const submitFinalTest = () => {
    const questionsToGrade = testQuestions.length > 0 ? testQuestions : [
      { id: 1, correct_answer: 0 },
      { id: 2, correct_answer: 0 },
    ];

    let correctCount = 0;
    questionsToGrade.forEach((q) => {
      if (userAnswers[q.id] === q.correct_answer) {
        correctCount++;
      }
    });

    const scorePct = Math.round((correctCount / questionsToGrade.length) * 100);
    setTestScore(scorePct);

    if (scorePct >= 50) {
      advanceToNextStep(5);
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
  };

  const handleGoToNextTopic = () => {
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

      {/* Top Navbar matching Screenshot 2 */}
      <View style={styles.navbar}>
        <View style={styles.brandRow}>
          <View style={styles.brandLogo}>
            <Feather name="code" size={18} color="#FFFFFF" />
          </View>
          <Text style={styles.brandTitle}>
            {language.toUpperCase() === 'CPP' ? 'C++' : language.toUpperCase()} Learning Track
          </Text>
        </View>

        <TouchableOpacity
          onPress={() =>
            router.push({
              pathname: '/coding-problems',
              params: { language: language },
            })
          }
          style={styles.backBtn}
        >
          <Feather name="arrow-left" size={14} color="#38BDF8" />
          <Text style={styles.backBtnText}>← Back to {language.toUpperCase()} Topics</Text>
        </TouchableOpacity>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Topic Banner Header matching Screenshot 2 */}
        <View style={styles.topicBanner}>
          <View style={styles.topicBannerTop}>
            <View style={{ flex: 1 }}>
              <Text style={styles.topicSubtitle}>
                {language.toUpperCase() === 'CPP' ? 'C++' : language.toUpperCase()} TOPIC {topicData.id}
              </Text>
              <Text style={styles.topicTitle}>{topicData.title}</Text>
            </View>

            <View style={styles.badgeRow}>
              <View style={styles.diffBadge}>
                <Text style={styles.diffBadgeText}>{topicData.difficulty}</Text>
              </View>
              <View style={styles.timeBadge}>
                <Feather name="clock" size={12} color="#9CA3AF" />
                <Text style={styles.timeBadgeText}>{topicData.duration}</Text>
              </View>
            </View>
          </View>
        </View>

        {/* 5-Step Horizontal Navigation Stepper matching Screenshot 2 */}
        <View style={styles.stepperContainer}>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.stepperScroll}>
            {[
              { num: 1, title: '1. Information' },
              { num: 2, title: '2. Examples' },
              { num: 3, title: '3. Programming' },
              { num: 4, title: '4. Fill in Blanks' },
              { num: 5, title: '5. SkillExa Test' },
            ].map((step, idx) => {
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

        {/* STEP 1: INFORMATION */}
        {activeStep === 1 && (
          <View style={styles.stepCard}>
            <View style={styles.stepCardHeader}>
              <Feather name="book-open" size={20} color="#38BDF8" />
              <Text style={styles.stepCardTitle}>Concept & Syntax</Text>
            </View>

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
          </View>
        )}

        {/* STEP 2: EXAMPLES */}
        {activeStep === 2 && (
          <View style={styles.stepCard}>
            <View style={styles.stepCardHeader}>
              <Feather name="code" size={20} color="#6366F1" />
              <Text style={styles.stepCardTitle}>Code Example & Output</Text>
            </View>

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
          </View>
        )}

        {/* STEP 3: PROGRAMMING EXERCISE & SANDBOX WITH CODE PILLS */}
        {activeStep === 3 && (
          <View style={styles.stepCard}>
            <View style={styles.stepCardHeader}>
              <Feather name="terminal" size={20} color="#10B981" />
              <Text style={styles.stepCardTitle}>Programming Exercise & Sandbox</Text>
            </View>

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
                <Text style={styles.editorFileName}>main.{language === 'cpp' ? 'cpp' : language === 'c' ? 'c' : language === 'java' ? 'java' : language === 'js' ? 'js' : 'py'}</Text>
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
          </View>
        )}

        {/* STEP 4: FILL IN BLANKS WITH CODE PILLS */}
        {activeStep === 4 && (
          <View style={styles.stepCard}>
            <View style={styles.stepCardHeader}>
              <Feather name="edit-3" size={20} color="#F59E0B" />
              <Text style={styles.stepCardTitle}>Interactive Fill in Blanks</Text>
            </View>

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
          </View>
        )}

        {/* STEP 5: SKILLEXA TEST */}
        {activeStep === 5 && (
          <View style={styles.stepCard}>
            <View style={styles.stepCardHeader}>
              <Feather name="award" size={20} color="#EC4899" />
              <Text style={styles.stepCardTitle}>SkillExa Final Topic Test</Text>
            </View>

            <Text style={styles.conceptParagraph}>
              Score at least 50% on this topic assessment to master {topicData.title} and unlock Topic {topicData.id + 1}!
            </Text>

            {testQuestions.map((q, qIdx) => (
              <View key={q.id || qIdx} style={styles.quizQuestionBox}>
                <Text style={styles.quizQTitle}>
                  Q{qIdx + 1}. {q.question}
                </Text>
                {(q.options || []).map((opt: string, optIdx: number) => {
                  const isSelected = userAnswers[q.id] === optIdx;
                  return (
                    <TouchableOpacity
                      key={optIdx}
                      style={[styles.quizOptionBtn, isSelected && styles.quizOptionActive]}
                      onPress={() => setUserAnswers({ ...userAnswers, [q.id]: optIdx })}
                      activeOpacity={0.8}
                    >
                      <Text style={[styles.quizOptionText, isSelected && styles.quizOptionTextActive]}>
                        {opt}
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            ))}

            <TouchableOpacity style={styles.continueBtn} onPress={submitFinalTest} activeOpacity={0.85}>
              <Text style={styles.continueBtnText}>Submit Topic Test & Verify Mastery</Text>
            </TouchableOpacity>

            {testScore !== null && (
              <View style={styles.scoreResultBox}>
                <Text style={styles.scoreTitle}>Score: {testScore}%</Text>
                {testScore >= 50 ? (
                  <>
                    <Text style={styles.scorePassedText}>
                      🎉 Topic Mastered! Topic {topicData.id + 1} is now unlocked.
                    </Text>
                    <TouchableOpacity
                      style={[styles.continueBtn, { backgroundColor: '#10B981', marginTop: 14 }]}
                      onPress={handleGoToNextTopic}
                      activeOpacity={0.85}
                    >
                      <Text style={styles.continueBtnText}>
                        Continue to Topic {topicData.id + 1} →
                      </Text>
                    </TouchableOpacity>
                  </>
                ) : (
                  <Text style={styles.scoreFailedText}>
                    Minimum 50% required. Please review the Information section and try again!
                  </Text>
                )}
              </View>
            )}
          </View>
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
});
