// Client logic controller for SkillExa topic learning flow and backend sequence API integration.

class SkillExaTopicFlow {
    constructor() {
        this.appNode = document.getElementById('flow-app');
        if (!this.appNode) return;

        this.topicId = parseInt(this.appNode.dataset.topicId);
        this.currentSection = this.appNode.dataset.section;
        this.studentId = this.appNode.dataset.studentId || '1';
        this.track = this.appNode.dataset.track || 'python';

        const sectionDataNode = document.getElementById('flow-section-data');
        const progressDataNode = document.getElementById('flow-progress-data');

        this.sectionData = sectionDataNode ? JSON.parse(sectionDataNode.textContent) : {};
        this.progress = progressDataNode ? JSON.parse(progressDataNode.textContent) : {};

        this.initSectionHandlers();
    }

    getApiEndpoint(action) {
        if (this.track === 'c') {
            if (action === 'complete-information') return `/c/api/topic/${this.topicId}/complete/information`;
            if (action === 'complete-examples') return `/c/api/topic/${this.topicId}/complete/examples`;
            if (action === 'execute') return `/c/execute`;
            if (action === 'complete-programming') return `/c/api/topic/${this.topicId}/complete/programming`;
            if (action === 'complete-fill-blanks') return `/c/api/topic/${this.topicId}/complete/fill-blanks`;
            if (action === 'submit-test') return `/c/api/topic/${this.topicId}/submit-test`;
        } else if (this.track === 'cpp') {
            if (action === 'complete-information') return `/cpp/api/topic/${this.topicId}/complete/information`;
            if (action === 'complete-examples') return `/cpp/api/topic/${this.topicId}/complete/examples`;
            if (action === 'execute') return `/cpp/execute`;
            if (action === 'complete-programming') return `/cpp/api/topic/${this.topicId}/complete/programming`;
            if (action === 'complete-fill-blanks') return `/cpp/api/topic/${this.topicId}/complete/fill-blanks`;
            if (action === 'submit-test') return `/cpp/api/topic/${this.topicId}/submit-test`;
        } else if (this.track === 'java') {
            if (action === 'complete-information') return `/java/api/topic/${this.topicId}/complete/information`;
            if (action === 'complete-examples') return `/java/api/topic/${this.topicId}/complete/examples`;
            if (action === 'execute') return `/java/execute`;
            if (action === 'complete-programming') return `/java/api/topic/${this.topicId}/complete/programming`;
            if (action === 'complete-fill-blanks') return `/java/api/topic/${this.topicId}/complete/fill-blanks`;
            if (action === 'submit-test') return `/java/api/topic/${this.topicId}/submit-test`;
        } else if (this.track === 'js' || this.track === 'javascript') {
            if (action === 'complete-information') return `/js/api/topic/${this.topicId}/complete/information`;
            if (action === 'complete-examples') return `/js/api/topic/${this.topicId}/complete/examples`;
            if (action === 'execute') return `/js/execute`;
            if (action === 'complete-programming') return `/js/api/topic/${this.topicId}/complete/programming`;
            if (action === 'complete-fill-blanks') return `/js/api/topic/${this.topicId}/complete/fill-blanks`;
            if (action === 'submit-test') return `/js/api/topic/${this.topicId}/submit-test`;
        } else if (this.track === 'python') {
            if (action === 'complete-information') return `/python/api/topic/${this.topicId}/complete/information`;
            if (action === 'complete-examples') return `/python/api/topic/${this.topicId}/complete/examples`;
            if (action === 'execute') return `/python/execute`;
            if (action === 'complete-programming') return `/python/api/topic/${this.topicId}/complete/programming`;
            if (action === 'complete-fill-blanks') return `/python/api/topic/${this.topicId}/complete/fill-blanks`;
            if (action === 'submit-test') return `/python/api/topic/${this.topicId}/submit-test`;
        } else {
            if (action === 'complete-information') return `/api/progress/${this.studentId}/${this.topicId}/complete-information`;
            if (action === 'complete-examples') return `/api/progress/${this.studentId}/${this.topicId}/complete-examples`;
            if (action === 'execute') return `/python/execute`;
            if (action === 'complete-programming') return `/api/progress/${this.studentId}/${this.topicId}/complete-programming`;
            if (action === 'complete-fill-blanks') return `/api/progress/${this.studentId}/${this.topicId}/complete-fill-blanks`;
            if (action === 'submit-test') return `/api/progress/${this.studentId}/${this.topicId}/submit-test`;
        }
        return '';
    }

    getSectionUrl(section) {
        let prefix = '';
        if (this.track === 'c') prefix = '/c';
        else if (this.track === 'cpp') prefix = '/cpp';
        else if (this.track === 'java') prefix = '/java';
        else if (this.track === 'js' || this.track === 'javascript') prefix = '/js';
        else if (this.track === 'python') prefix = '/python';
        return `${prefix}/topic/${this.topicId}/${section}`;
    }

    getSyllabusUrl() {
        if (this.track === 'c') return '/c/topics';
        if (this.track === 'cpp') return '/cpp/topics';
        if (this.track === 'java') return '/java/topics';
        if (this.track === 'js' || this.track === 'javascript') return '/js/topics';
        if (this.track === 'python') return '/python/topics';
        return '/topics';
    }

    initSectionHandlers() {
        if (this.currentSection === 'information') {
            this.initInformationHandlers();
        } else if (this.currentSection === 'examples') {
            this.initExamplesHandlers();
        } else if (this.currentSection === 'programming') {
            this.initProgrammingHandlers();
        } else if (this.currentSection === 'fill-blanks') {
            this.initFillBlanksHandlers();
        } else if (this.currentSection === 'test') {
            this.initTestHandlers();
        }
    }

    async initInformationHandlers() {
        const btn = document.getElementById('btn-complete-info');
        if (!btn) return;

        btn.addEventListener('click', async () => {
            try {
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
                await appEngine.dataRequest(this.getApiEndpoint('complete-information'), {
                    method: 'POST',
                });
                appEngine.showToast('Information completed!', 'success');
                window.location.href = this.getSectionUrl('examples');
            } catch (err) {
                btn.disabled = false;
                btn.innerHTML = 'Complete & Continue to Examples <i class="fas fa-arrow-right"></i>';
                console.error(err);
            }
        });
    }

    async initExamplesHandlers() {
        const codeBox = document.getElementById('annotated-code-container');
        if (codeBox && codeBox.innerText) {
            const lines = codeBox.innerText.split('\n');
            let hasAnnotations = lines.some(l => l.includes('[TRUE') || l.includes('[FALSE') || l.includes('[EXECUTED') || l.includes('[SKIPPED'));
            
            if (hasAnnotations) {
                let html = '';
                lines.forEach((line) => {
                    const isTrue = line.includes('[TRUE') || line.includes('[EXECUTED');
                    const isFalse = line.includes('[FALSE') || line.includes('[SKIPPED');
                    
                    let lineClass = 'code-line';
                    let badge = '';
                    if (isTrue) {
                        lineClass += ' line-true';
                        badge = '<span class="badge-pill badge-blue"><i class="fa-solid fa-check"></i> TRUE / EXECUTED</span>';
                    } else if (isFalse) {
                        lineClass += ' line-false';
                        badge = '<span class="badge-pill badge-red"><i class="fa-solid fa-xmark"></i> FALSE / SKIPPED</span>';
                    }
                    
                    html += `<div class="${lineClass}"><span style="flex:1;">${line}</span>${badge}</div>`;
                });
                codeBox.innerHTML = html;
            }
        }

        const btn = document.getElementById('btn-complete-examples');
        if (!btn) return;

        btn.addEventListener('click', async () => {
            try {
                btn.disabled = true;
                btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
                await appEngine.dataRequest(this.getApiEndpoint('complete-examples'), {
                    method: 'POST',
                });
                appEngine.showToast('Examples completed!', 'success');
                window.location.href = this.getSectionUrl('programming');
            } catch (err) {
                btn.disabled = false;
                btn.innerHTML = 'Complete & Continue to Programming <i class="fas fa-arrow-right"></i>';
                console.error(err);
            }
        });
    }

    initProgrammingHandlers() {
        const runBtn = document.getElementById('run-sandbox-btn');
        const resetBtn = document.getElementById('reset-code-btn');
        const codeInput = document.getElementById('programming-code-input');
        const consoleNode = document.getElementById('programming-console');
        const completeBtn = document.getElementById('btn-complete-programming');
        const optionsContainer = document.getElementById('programming-options-container');

        const initialStarterCode = codeInput ? codeInput.value : '';

        if (optionsContainer && codeInput) {
            optionsContainer.addEventListener('click', (e) => {
                const targetBtn = e.target.closest('.option-pill-btn');
                if (!targetBtn) return;
                
                const optionVal = targetBtn.dataset.val;
                let currentCode = codeInput.value;

                if (/_{3,}/.test(currentCode)) {
                    currentCode = currentCode.replace(/_{3,}/, optionVal);
                } else if (currentCode.includes('[?]')) {
                    currentCode = currentCode.replace('[?]', optionVal);
                } else {
                    const startPos = codeInput.selectionStart || currentCode.length;
                    const endPos = codeInput.selectionEnd || currentCode.length;
                    currentCode = currentCode.substring(0, startPos) + optionVal + currentCode.substring(endPos);
                }

                codeInput.value = currentCode;

                // Visual flash effect on codeInput
                codeInput.style.transition = 'box-shadow 0.2s ease';
                codeInput.style.boxShadow = '0 0 10px rgba(56, 189, 248, 0.8)';
                setTimeout(() => {
                    codeInput.style.boxShadow = 'none';
                }, 300);
            });
        }

        if (resetBtn && codeInput) {
            resetBtn.addEventListener('click', () => {
                codeInput.value = initialStarterCode;
                if (consoleNode) {
                    consoleNode.innerText = 'Code reset to initial template.';
                    consoleNode.style.color = '#94A3B8';
                }
            });
        }

        if (runBtn && codeInput && consoleNode) {
            runBtn.addEventListener('click', async () => {
                const codeText = codeInput.value;
                let userInputs = null;

                // Detect interactive input statements in Python, C, C++, Java, JS
                const isInputCall = /\b(input\s*\(|scanf\s*\(|gets\s*\(|fgets\s*\(|getchar\s*\(|cin\s*>>|getline\s*\(|Scanner|BufferedReader|readline)\b/.test(codeText);

                if (isInputCall) {
                    let promptTitle = 'Program Input Required:';
                    const promptMatch = codeText.match(/input\s*\(\s*["'](.*?)["']\s*\)/);
                    if (promptMatch && promptMatch[1]) {
                        promptTitle = promptMatch[1].trim();
                    }

                    const promptResult = window.prompt(promptTitle, '');
                    if (promptResult === null) {
                        consoleNode.innerText = 'Execution cancelled (Input prompt closed).';
                        consoleNode.style.color = '#94A3B8';
                        return;
                    }
                    userInputs = promptResult;
                }

                const langName = this.track === 'c' ? 'native C compiler' : (this.track === 'cpp' ? 'native C++ compiler' : (this.track === 'java' ? 'native Java compiler (javac)' : 'isolated Python runtime'));
                consoleNode.innerText = `Running ${langName}...`;
                consoleNode.style.color = '#F59E0B';
                try {
                    const reqPayload = { code: codeText };
                    if (userInputs !== null) {
                        reqPayload.inputs = userInputs;
                    }
                    const result = await appEngine.dataRequest(this.getApiEndpoint('execute'), {
                        method: 'POST',
                        body: JSON.stringify(reqPayload),
                    });
                    const output = result.output || result.error || '[No output]';
                    consoleNode.innerText = output;
                    consoleNode.style.color = result.success ? '#10B981' : '#EF4444';
                } catch (err) {
                    consoleNode.innerText = err.message || 'Execution error.';
                    consoleNode.style.color = '#EF4444';
                }
            });
        }

        if (completeBtn) {
            completeBtn.addEventListener('click', async () => {
                try {
                    completeBtn.disabled = true;
                    completeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
                    await appEngine.dataRequest(this.getApiEndpoint('complete-programming'), {
                        method: 'POST',
                    });
                    appEngine.showToast('Programming completed!', 'success');
                    window.location.href = this.getSectionUrl('fill-blanks');
                } catch (err) {
                    completeBtn.disabled = false;
                    completeBtn.innerHTML = 'Complete & Continue to Fill in Blanks <i class="fas fa-arrow-right"></i>';
                    console.error(err);
                }
            });
        }
    }

    initFillBlanksHandlers() {
        const checkBtn = document.getElementById('check-fill-btn');
        const feedbackNode = document.getElementById('fill-feedback');
        const completeBtn = document.getElementById('btn-complete-fill-blanks');
        const optionPills = document.querySelectorAll('.fill-option-pill, .option-pill-btn');

        let activeInput = null;
        document.querySelectorAll('.blank-input').forEach(input => {
            input.addEventListener('focus', () => {
                activeInput = input;
            });
        });

        optionPills.forEach(pill => {
            pill.addEventListener('click', (e) => {
                e.preventDefault();
                const val = pill.dataset.val || pill.textContent.trim();
                const inputs = Array.from(document.querySelectorAll('.blank-input'));
                if (inputs.length === 0) return;

                let targetInput = (activeInput && inputs.includes(activeInput)) ? activeInput : null;
                if (!targetInput) {
                    targetInput = inputs.find(i => !i.value.trim());
                }
                if (!targetInput) {
                    targetInput = inputs[0];
                }

                targetInput.value = val;
                targetInput.focus();

                targetInput.style.transition = 'border-color 0.2s ease, box-shadow 0.2s ease';
                targetInput.style.borderColor = 'var(--cyan-neon, #38bdf8)';
                targetInput.style.boxShadow = '0 0 10px rgba(56, 189, 248, 0.5)';
                setTimeout(() => {
                    targetInput.style.boxShadow = 'none';
                }, 300);

                const currIdx = inputs.indexOf(targetInput);
                if (currIdx >= 0 && currIdx < inputs.length - 1 && !inputs[currIdx + 1].value.trim()) {
                    activeInput = inputs[currIdx + 1];
                    inputs[currIdx + 1].focus();
                } else {
                    activeInput = targetInput;
                }
            });
        });

        if (checkBtn && feedbackNode) {
            checkBtn.addEventListener('click', () => {
                const inputs = Array.from(document.querySelectorAll('.blank-input'));
                const fillData = this.sectionData.fill_blanks || {};
                const expected = fillData.answers || (fillData.answer ? [fillData.answer] : []);
                
                const userAnswers = inputs.map(i => i.value.trim());
                
                if (inputs.length === 0) {
                    feedbackNode.textContent = '❌ No blank inputs found.';
                    feedbackNode.style.color = '#EF4444';
                    return;
                }

                if (userAnswers.some(a => a === '')) {
                    feedbackNode.textContent = '⚠️ Please fill in all blank fields before checking.';
                    feedbackNode.style.color = '#F59E0B';
                    return;
                }

                const isCorrect = expected.length === userAnswers.length && expected.every((ans, idx) => String(ans).trim().toLowerCase() === String(userAnswers[idx] || '').trim().toLowerCase());

                if (isCorrect) {
                    feedbackNode.textContent = '✅ Correct answer!';
                    feedbackNode.style.color = '#10B981';
                } else {
                    feedbackNode.textContent = `❌ Incorrect. Expected: ${expected.join(', ')}`;
                    feedbackNode.style.color = '#EF4444';
                }
            });
        }

        if (completeBtn) {
            completeBtn.addEventListener('click', async () => {
                const inputs = Array.from(document.querySelectorAll('.blank-input'));
                const answers = inputs.map(i => i.value.trim());

                try {
                    completeBtn.disabled = true;
                    completeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Validating & Saving...';
                    await appEngine.dataRequest(this.getApiEndpoint('complete-fill-blanks'), {
                        method: 'POST',
                        body: JSON.stringify({ user_answers: answers }),
                    });
                    appEngine.showToast('Fill in the Blanks completed!', 'success');
                    window.location.href = this.getSectionUrl('test');
                } catch (err) {
                    completeBtn.disabled = false;
                    completeBtn.innerHTML = 'Complete & Continue to SkillExa Test <i class="fas fa-arrow-right"></i>';
                    console.error(err);
                }
            });
        }
    }

    initTestHandlers() {
        // Enable unmarking (unchecking) radio option pills on click
        document.querySelectorAll('input[type="radio"]').forEach(radio => {
            radio.addEventListener('click', function() {
                if (this.dataset.wasChecked === 'true') {
                    this.checked = false;
                    this.dataset.wasChecked = 'false';
                } else {
                    document.querySelectorAll(`input[name="${this.name}"]`).forEach(r => r.dataset.wasChecked = 'false');
                    this.dataset.wasChecked = 'true';
                }
            });
        });

        const submitBtn = document.getElementById('btn-submit-test');
        const testSectionCard = document.getElementById('test-section-card');
        const completionCard = document.getElementById('topic-completion-card');
        const completionIconBox = document.getElementById('completion-icon-box');
        const completionIcon = document.getElementById('completion-icon');
        const completionTitle = document.getElementById('completion-title');
        const resScore = document.getElementById('res-score');
        const resMinPassMsg = document.getElementById('res-min-pass-msg');
        const btnRetryTest = document.getElementById('btn-retry-test');
        const btnNextTopic = document.getElementById('btn-next-topic');

        if (btnRetryTest) {
            btnRetryTest.addEventListener('click', () => {
                document.querySelectorAll('input[type="radio"]').forEach(r => r.checked = false);
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = 'Submit SkillExa Test <i class="fa-solid fa-paper-plane"></i>';
                }
                if (completionCard) completionCard.style.display = 'none';
                if (testSectionCard) testSectionCard.style.display = 'block';
            });
        }

        if (submitBtn) {
            submitBtn.addEventListener('click', async () => {
                const questions = this.sectionData.questions || [];
                const submittedAnswers = {};

                questions.forEach((q, idx) => {
                    const checked = document.querySelector(`input[name="question_${idx}"]:checked`);
                    if (checked) {
                        submittedAnswers[idx] = checked.value;
                    }
                });

                try {
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting Test...';

                    const payload = {
                        user_answers: submittedAnswers,
                        submitted_answers: submittedAnswers,
                    };

                    const res = await appEngine.dataRequest(this.getApiEndpoint('submit-test'), {
                        method: 'POST',
                        body: JSON.stringify(payload),
                    });

                    const isPassed = (res.passed !== undefined) ? res.passed : (res.score >= 50);

                    if (isPassed) {
                        appEngine.showToast('SkillExa Test Passed!', 'success');
                        if (testSectionCard) testSectionCard.style.display = 'none';
                        if (completionCard) completionCard.style.display = 'block';

                        if (completionTitle) completionTitle.textContent = `${this.track.toUpperCase()} Topic Mastered!`;
                        if (completionIconBox) {
                            completionIconBox.style.background = 'rgba(16, 185, 129, 0.2)';
                            completionIconBox.style.color = '#10b981';
                        }
                        if (completionIcon) completionIcon.className = 'fa-solid fa-trophy';
                        if (resScore) {
                            resScore.textContent = `${res.score}%`;
                            resScore.style.color = '#10b981';
                        }
                        if (resMinPassMsg) resMinPassMsg.textContent = 'Passed (>= 50%)!';
                        if (btnRetryTest) btnRetryTest.style.display = 'none';
                        if (btnNextTopic) btnNextTopic.style.display = 'inline-flex';

                        let prefix = '';
                        if (this.track === 'c') prefix = '/c';
                        else if (this.track === 'cpp') prefix = '/cpp';
                        else if (this.track === 'java') prefix = '/java';
                        else if (this.track === 'js' || this.track === 'javascript') prefix = '/js';
                        else if (this.track === 'python') prefix = '/python';

                        if (res.next_topic && btnNextTopic) {
                            btnNextTopic.href = `${prefix}/topic/${res.next_topic.id}/information`;
                            btnNextTopic.innerHTML = `Unlock & Start Topic ${res.next_topic.id}: ${res.next_topic.title} <i class="fas fa-arrow-right"></i>`;
                        } else if (btnNextTopic) {
                            btnNextTopic.href = this.getSyllabusUrl();
                            btnNextTopic.innerHTML = 'Return to Syllabus Catalog <i class="fas fa-check"></i>';
                        }
                    } else {
                        appEngine.showToast('Minimum 50% score required. Please try again!', 'error');
                        if (testSectionCard) testSectionCard.style.display = 'none';
                        if (completionCard) completionCard.style.display = 'block';

                        if (completionTitle) completionTitle.textContent = 'Minimum 50% Score Not Met';
                        if (completionIconBox) {
                            completionIconBox.style.background = 'rgba(244, 63, 94, 0.2)';
                            completionIconBox.style.color = '#f43f5e';
                        }
                        if (completionIcon) completionIcon.className = 'fa-solid fa-rotate-left';
                        if (resScore) {
                            resScore.textContent = `${res.score}%`;
                            resScore.style.color = '#f43f5e';
                        }
                        if (resMinPassMsg) resMinPassMsg.textContent = 'Score is below 50%. You must retry the test to pass this topic!';
                        if (btnRetryTest) btnRetryTest.style.display = 'inline-flex';
                        if (btnNextTopic) btnNextTopic.style.display = 'none';
                    }
                } catch (err) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = 'Submit SkillExa Test <i class="fas fa-paper-plane"></i>';
                    const errMsg = err.message || (typeof err === 'string' ? err : 'Test submission failed.');
                    appEngine.showToast(errMsg, 'error');
                    console.error('Test submission error:', err);
                }
            });
        }
    }
}

function bootTopicFlowApp() {
    window.topicFlowApp = new SkillExaTopicFlow();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootTopicFlowApp);
} else {
    bootTopicFlowApp();
}
