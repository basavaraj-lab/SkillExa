class SkillExaQuizEngine {
    constructor() {
        this.submitButton = document.getElementById('quiz-submit-action');
        this.timerDisplay = document.getElementById('quiz-countdown-timer');
        this.timeLeftSeconds = 899;
        this.timerInterval = null;

        const urlParams = new URLSearchParams(window.location.search);
        this.topicId = Number.parseInt(urlParams.get('id') || '2', 10);

        this.checkAccessAndInitialize();
    }

    async checkAccessAndInitialize() {
        if (!this.submitButton || !this.timerDisplay) {
            return;
        }

        try {
            const limits = await appEngine.dataRequest('/user/limits');
            const remaining = limits.max_free_daily_quizzes - limits.daily_quizzes_completed;

            if (remaining <= 0) {
                appEngine.showToast('Daily limit reached! Locks are in place.', 'danger');
                this.submitButton.disabled = true;
                this.submitButton.innerText = 'Daily Limit Reached';
                return;
            }

            appEngine.showToast(`Active Daily Free Quizzes Remaining: ${remaining}`, 'info');
            this.startTimerLoop();
            this.bindEvents();
        } catch (error) {
            console.error('Initial limit verification fault:', error);
        }
    }

    startTimerLoop() {
        this.timerInterval = setInterval(() => {
            const minutes = Math.floor(this.timeLeftSeconds / 60);
            const seconds = this.timeLeftSeconds % 60;
            this.timerDisplay.innerText = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

            if (this.timeLeftSeconds <= 0) {
                clearInterval(this.timerInterval);
                this.evaluateQuizSubmission(true);
                return;
            }

            this.timeLeftSeconds -= 1;
        }, 1000);
    }

    bindEvents() {
        this.submitButton.addEventListener('click', () => this.evaluateQuizSubmission(false));
    }

    async evaluateQuizSubmission(isTimeOut = false) {
        clearInterval(this.timerInterval);
        const selectedOption = document.querySelector('input[name="quiz-selection"]:checked');

        if (!selectedOption && !isTimeOut) {
            appEngine.showToast('Please select an option before submitting.', 'danger');
            this.startTimerLoop();
            return;
        }

        const payload = {
            topic_id: this.topicId,
            selected_option: selectedOption ? selectedOption.value : 'None',
            time_remaining: this.timeLeftSeconds,
        };

        try {
            const result = await appEngine.dataRequest('/quiz/submit', {
                method: 'POST',
                body: JSON.stringify(payload),
            });

            appEngine.showToast(result.message, 'success');
            if (result.new_topic_unlocked) {
                appEngine.showToast('System Cracked! Next Lesson Unlocked!', 'success');
            }

            setTimeout(() => {
                window.location.href = '/topics';
            }, 1200);
        } catch (error) {
            console.error('Quiz submission failed:', error);
            this.startTimerLoop();
        }
    }
}

const quizSessionController = new SkillExaQuizEngine();
