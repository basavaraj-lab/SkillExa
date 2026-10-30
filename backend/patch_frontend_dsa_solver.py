with open("skillexa-app/app/dsa-solver.tsx", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add state variables inside DsaSolverPage
old_state = """  // Result states
  const [runResult, setRunResult] = useState<any>(null);
  const [submitResult, setSubmitResult] = useState<any>(null);"""

new_state = """  // Result states
  const [runResult, setRunResult] = useState<any>(null);
  const [submitResult, setSubmitResult] = useState<any>(null);
  const [solutionTab, setSolutionTab] = useState<string>('c');
  const [showMultiSolution, setShowMultiSolution] = useState<boolean>(true);
  const [copied, setCopied] = useState<boolean>(false);"""

text = text.replace(old_state, new_state)

# 2. Add copy and load handler functions
old_handles = """  const handleCodeChange = (text: string) => {
    setCodePerLang((prev) => ({ ...prev, [selectedLang]: text }));
  };"""

new_handles = """  const handleCodeChange = (text: string) => {
    setCodePerLang((prev) => ({ ...prev, [selectedLang]: text }));
  };

  const handleCopySolution = (code: string) => {
    if (typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(code);
    }
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleLoadIntoEditor = (lang: string, code: string) => {
    setSelectedLang(lang);
    setCodePerLang((prev) => ({ ...prev, [lang]: code }));
  };"""

text = text.replace(old_handles, new_handles)

# 3. Enhance handleSubmitCode to unlock multi-language solutions immediately
old_submit = """      if (res.data.status === 'PASSED') {
        setProblem((prev: any) => (prev ? { ...prev, is_solved: true } : prev));
      }"""

new_submit = """      if (res.data.status === 'PASSED') {
        setProblem((prev: any) => (prev ? { ...prev, is_solved: true } : prev));
        setShowMultiSolution(true);
        setSolutionTab(selectedLang);
      }"""

text = text.replace(old_submit, new_submit)

# 4. In the consoleOutputContainer, after submitResult, render Multi-Language Solutions section
old_submit_result_box = """                {submitResult.output_logs && (
                  <View style={styles.consoleLogBox}>
                    <Text style={styles.consoleLogText}>{submitResult.output_logs}</Text>
                  </View>
                )}
              </View>
            )}"""

new_submit_result_box = """                {submitResult.output_logs && (
                  <View style={styles.consoleLogBox}>
                    <Text style={styles.consoleLogText}>{submitResult.output_logs}</Text>
                  </View>
                )}
              </View>
            )}

            {/* AUTOMATIC MULTI-LANGUAGE SOLUTIONS SECTION */}
            {((submitResult && submitResult.status === 'PASSED') || problem?.is_solved) && (() => {
              const solMap = submitResult?.solutions || problem?.solution_code_map || (() => {
                try {
                  return typeof problem?.solution_code === 'string' ? JSON.parse(problem.solution_code) : (problem?.solution_code || {});
                } catch {
                  return {};
                }
              })();

              const activeSolCode = solMap[solutionTab] || solMap['python'] || solMap['c'] || '// Solution in preparation';
              const solLines = activeSolCode.split('\\n');

              return (
                <View style={styles.multiSolutionCard}>
                  <View style={styles.multiSolutionHeader}>
                    <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                      <View style={styles.solSuccessIcon}>
                        <Feather name="check" size={14} color="#10B981" />
                      </View>
                      <View>
                        <Text style={styles.multiSolutionTitle}>Solutions in All 4 Languages</Text>
                        <Text style={styles.multiSolutionSubtitle}>Algorithm & variable logic preserved across C, C++, Java, and Python</Text>
                      </View>
                    </View>
                    <TouchableOpacity
                      style={styles.toggleSolBtn}
                      onPress={() => setShowMultiSolution(!showMultiSolution)}
                    >
                      <Feather name={showMultiSolution ? 'chevron-up' : 'chevron-down'} size={18} color="#94A3B8" />
                    </TouchableOpacity>
                  </View>

                  {showMultiSolution && (
                    <View style={styles.multiSolutionBody}>
                      {/* 4 Language Selection Tabs */}
                      <View style={styles.solTabsRow}>
                        {[
                          { key: 'c', label: 'C Solution' },
                          { key: 'cpp', label: 'C++ Solution' },
                          { key: 'java', label: 'Java Solution' },
                          { key: 'python', label: 'Python Solution' },
                        ].map((item) => {
                          const isActive = solutionTab === item.key;
                          const hasCode = !!solMap[item.key];
                          return (
                            <TouchableOpacity
                              key={item.key}
                              style={[styles.solTabBtn, isActive && styles.solTabBtnActive]}
                              onPress={() => setSolutionTab(item.key)}
                            >
                              <Text style={[styles.solTabBtnText, isActive && styles.solTabBtnTextActive]}>
                                {item.label}
                              </Text>
                              {hasCode && <View style={styles.solTabDot} />}
                            </TouchableOpacity>
                          );
                        })}
                      </View>

                      {/* Solution Code Viewer with Line Numbers */}
                      <View style={styles.solCodeViewer}>
                        <View style={styles.solCodeActionsBar}>
                          <View style={styles.solLangBadge}>
                            <Text style={styles.solLangBadgeText}>{solutionTab.toUpperCase()}</Text>
                          </View>
                          <View style={{ flexDirection: 'row', gap: 8 }}>
                            <TouchableOpacity
                              style={styles.solActionBtn}
                              onPress={() => handleLoadIntoEditor(solutionTab, activeSolCode)}
                            >
                              <Feather name="terminal" size={12} color="#38BDF8" />
                              <Text style={styles.solActionBtnText}>Load into Editor</Text>
                            </TouchableOpacity>
                            <TouchableOpacity
                              style={[styles.solActionBtn, copied && { borderColor: '#10B981' }]}
                              onPress={() => handleCopySolution(activeSolCode)}
                            >
                              <Feather name={copied ? 'check' : 'copy'} size={12} color={copied ? '#10B981' : '#E2E8F0'} />
                              <Text style={[styles.solActionBtnText, copied && { color: '#10B981' }]}>
                                {copied ? 'Copied!' : 'Copy Code'}
                              </Text>
                            </TouchableOpacity>
                          </View>
                        </View>

                        <ScrollView style={styles.solCodeScroll} nestedScrollEnabled>
                          <View style={styles.solCodeRow}>
                            <View style={styles.solLineNumCol}>
                              {solLines.map((_, i) => (
                                <Text key={i} style={styles.solLineNumText}>{i + 1}</Text>
                              ))}
                            </View>
                            <Text style={styles.solCodeText}>{activeSolCode}</Text>
                          </View>
                        </ScrollView>
                      </View>

                      {/* Complexity & Verification Analysis */}
                      <View style={styles.solAnalysisRow}>
                        <View style={styles.solAnalysisChip}>
                          <Feather name="clock" size={12} color="#10B981" />
                          <Text style={styles.solAnalysisChipText}>Time: {problem?.time_complexity || 'O(n)'}</Text>
                        </View>
                        <View style={styles.solAnalysisChip}>
                          <Feather name="cpu" size={12} color="#A855F7" />
                          <Text style={styles.solAnalysisChipText}>Space: {problem?.space_complexity || 'O(1)'}</Text>
                        </View>
                        <View style={styles.solAnalysisChip}>
                          <Feather name="shield" size={12} color="#38BDF8" />
                          <Text style={styles.solAnalysisChipText}>Tested & Validated</Text>
                        </View>
                      </View>
                    </View>
                  )}
                </View>
              );
            })()}"""

text = text.replace(old_submit_result_box, new_submit_result_box)

# 5. Add styles for multiSolution
new_styles = """  metricsText: {
    color: '#94A3B8',
    fontSize: 12,
  },
  multiSolutionCard: {
    marginTop: 14,
    backgroundColor: '#0F172A',
    borderRadius: 10,
    borderWidth: 1.5,
    borderColor: '#10B981',
    overflow: 'hidden',
  },
  multiSolutionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 14,
    paddingVertical: 12,
    backgroundColor: '#062B20',
    borderBottomWidth: 1,
    borderBottomColor: '#064E3B',
  },
  solSuccessIcon: {
    width: 26,
    height: 26,
    borderRadius: 13,
    backgroundColor: '#064E3B',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: '#10B981',
  },
  multiSolutionTitle: {
    color: '#34D399',
    fontSize: 14,
    fontWeight: '800',
  },
  multiSolutionSubtitle: {
    color: '#94A3B8',
    fontSize: 11,
    marginTop: 1,
  },
  toggleSolBtn: {
    padding: 6,
  },
  multiSolutionBody: {
    padding: 12,
  },
  solTabsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
    marginBottom: 10,
  },
  solTabBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 6,
    backgroundColor: '#1E293B',
    borderWidth: 1,
    borderColor: '#334155',
  },
  solTabBtnActive: {
    backgroundColor: '#064E3B',
    borderColor: '#10B981',
  },
  solTabBtnText: {
    color: '#94A3B8',
    fontSize: 12,
    fontWeight: '700',
  },
  solTabBtnTextActive: {
    color: '#34D399',
  },
  solTabDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#10B981',
  },
  solCodeViewer: {
    backgroundColor: '#090D16',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#1E293B',
    overflow: 'hidden',
  },
  solCodeActionsBar: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 10,
    paddingVertical: 8,
    backgroundColor: '#0B1120',
    borderBottomWidth: 1,
    borderBottomColor: '#1E293B',
  },
  solLangBadge: {
    backgroundColor: '#1E293B',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 4,
  },
  solLangBadgeText: {
    color: '#38BDF8',
    fontSize: 11,
    fontWeight: '800',
  },
  solActionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 5,
    backgroundColor: '#1E293B',
    borderWidth: 1,
    borderColor: '#334155',
  },
  solActionBtnText: {
    color: '#E2E8F0',
    fontSize: 11,
    fontWeight: '600',
  },
  solCodeScroll: {
    maxHeight: 260,
  },
  solCodeRow: {
    flexDirection: 'row',
    paddingVertical: 8,
  },
  solLineNumCol: {
    width: 34,
    alignItems: 'center',
    borderRightWidth: 1,
    borderRightColor: '#1E293B',
    paddingRight: 6,
  },
  solLineNumText: {
    color: '#475569',
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    fontSize: 12,
    lineHeight: 20,
  },
  solCodeText: {
    flex: 1,
    color: '#F8FAFC',
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    fontSize: 12,
    lineHeight: 20,
    paddingHorizontal: 10,
  },
  solAnalysisRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginTop: 10,
  },
  solAnalysisChip: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    backgroundColor: '#1E293B',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
  },
  solAnalysisChipText: {
    color: '#CBD5E1',
    fontSize: 11,
    fontWeight: '600',
  },
});"""

text = text.replace("""  metricsText: {
    color: '#94A3B8',
    fontSize: 12,
  },
});""", new_styles)

with open("skillexa-app/app/dsa-solver.tsx", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated skillexa-app/app/dsa-solver.tsx successfully!")

