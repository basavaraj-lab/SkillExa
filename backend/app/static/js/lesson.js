class SkillExaLesson {
    constructor() {
        this.runButton = document.getElementById('execute-code-trigger');
        this.codeInput = document.getElementById('code-mirror-textarea');
        this.consoleOutput = document.getElementById('terminal-mount-node');
        this.topic = window.__LESSON_TOPIC__ || {};

        // Fill in the blanks
        this.checkButton = document.getElementById('check-answer');
        this.result = document.getElementById('fill-result');

        this.initWorkspaceTriggers();
        this.initFillBlanks();
    }

    initWorkspaceTriggers() {
        if (!this.runButton || !this.codeInput || !this.consoleOutput) {
            return;
        }

        this.runButton.addEventListener('click', async () => {
            this.consoleOutput.innerText =
                'Initializing isolated sub-process runtime context...';
            this.consoleOutput.style.color = '#F59E0B';

            try {
                const result = await appEngine.dataRequest('/python/execute', {
                    method: 'POST',
                    body: JSON.stringify({
                        code: this.codeInput.value,
                    }),
                });

                const outputText =
                    result.output || result.error || '[No output]';

                this.consoleOutput.innerText = outputText;
                this.consoleOutput.style.color =
                    result.success ? '#10B981' : '#EF4444';

                appEngine.showToast(
                    result.success
                        ? 'Code executed successfully.'
                        : 'Code execution failed.',
                    result.success ? 'success' : 'danger'
                );
            } catch (error) {
                this.consoleOutput.innerText =
                    error.message || 'Execution request failed.';
                this.consoleOutput.style.color = '#EF4444';
            }
        });
    }

    initFillBlanks() {
          initFillBlanks() {
            console.log("initFillBlanks called");

            if (!this.checkButton) {
                console.log("Check button not found");
            return;
            }

            this.checkButton.addEventListener("click", () => {
            console.log("Button clicked");
    });
}
        if (!this.checkButton) return;

        this.checkButton.addEventListener('click', () => {

            const inputs = document.querySelectorAll('.blank-input');

            const answers = this.topic.fill_blanks.answers || [];

            let correct = true;

            inputs.forEach((input, index) => {

                if (
                    input.value.trim().toLowerCase() !==
                    answers[index].toLowerCase()
                ) {
                    correct = false;
                }

            });

            if (correct) {

                this.result.innerHTML = "✅ Correct!";
                this.result.style.color = "#10B981";

                appEngine.showToast(
                    "Excellent! Fill in the blanks completed.",
                    "success"
                );

            } else {

                this.result.innerHTML = "❌ Try Again!";
                this.result.style.color = "#EF4444";

                appEngine.showToast(
                    "Incorrect answer. Please try again.",
                    "danger"
                );
            }

        });
    }
}

const workspaceStudio = new SkillExaLesson();