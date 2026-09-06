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
        return `${prefix}/topic/${this.topicId}/${section}`;
    }

    getSyllabusUrl() {
        if (this.track === 'c') return '/c/topics';
        if (this.track === 'cpp') return '/cpp/topics';
        if (this.track === 'java') return '/java/topics';
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

                if (currentCode.includes('_____')) {
                    currentCode = currentCode.replace('_____', optionVal);
                } else if (currentCode.includes('___')) {
                    currentCode = currentCode.replace('___', optionVal);
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
                const langName = this.track === 'c' ? 'native C compiler' : (this.track === 'cpp' ? 'native C++ compiler' : (this.track === 'java' ? 'native Java compiler (javac)' : 'isolated Python runtime'));
                consoleNode.innerText = `Running ${langName}...`;
                consoleNode.style.color = '#F59E0B';
                try {
                    const result = await appEngine.dataRequest(this.getApiEndpoint('execute'), {
                        method: 'POST',
                        body: JSON.stringify({ code: codeInput.value }),
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

        if (checkBtn && feedbackNode) {
            checkBtn.addEventListener('click', () => {
                const inputs = Array.from(document.querySelectorAll('.blank-input'));
                const fillData = this.sectionData.fill_blanks || {};
                const expected = fillData.answers || (fillData.answer ? [fillData.answer] : []);
                
                const userAnswers = inputs.map(i => i.value.trim());
                const isCorrect = expected.length === userAnswers.length && expected.every((ans, idx) => ans.toLowerCase() === (userAnswers[idx] || '').toLowerCase());

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
        const submitBtn = document.getElementById('btn-submit-test');
        const testSectionCard = document.getElementById('test-section-card');
        const completionCard = document.getElementById('topic-completion-card');
        const resScore = document.getElementById('res-score');
        const btnNextTopic = document.getElementById('btn-next-topic');

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

                    const payloadKey = (this.track === 'c' || this.track === 'cpp' || this.track === 'java') ? 'user_answers' : 'submitted_answers';
                    const payload = {};
                    payload[payloadKey] = submittedAnswers;

                    const res = await appEngine.dataRequest(this.getApiEndpoint('submit-test'), {
                        method: 'POST',
                        body: JSON.stringify(payload),
                    });

                    appEngine.showToast('SkillExa Test Submitted!', 'success');

                    if (testSectionCard) testSectionCard.style.display = 'none';
                    if (completionCard) completionCard.style.display = 'block';
                    if (resScore) resScore.textContent = `${res.score}%`;

                    const prefix = this.track === 'c' ? '/c' : (this.track === 'cpp' ? '/cpp' : (this.track === 'java' ? '/java' : ''));
                    if (res.next_topic && btnNextTopic) {
                        btnNextTopic.href = `${prefix}/topic/${res.next_topic.id}/information`;
                        btnNextTopic.innerHTML = `Unlock & Start Topic ${res.next_topic.id}: ${res.next_topic.title} <i class="fas fa-arrow-right"></i>`;
                    } else if (btnNextTopic) {
                        btnNextTopic.href = this.getSyllabusUrl();
                        btnNextTopic.innerHTML = 'Return to Syllabus Catalog <i class="fas fa-check"></i>';
                    }
                } catch (err) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = 'Submit SkillExa Test <i class="fas fa-paper-plane"></i>';
                    console.error(err);
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
