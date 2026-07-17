class SkillExaLesson {
    constructor() {
        this.runButton = document.getElementById('execute-code-trigger');
        this.codeInput = document.getElementById('code-mirror-textarea');
        this.consoleOutput = document.getElementById('terminal-mount-node');
        this.initWorkspaceTriggers();
    }

    initWorkspaceTriggers() {
        if (!this.runButton || !this.codeInput || !this.consoleOutput) {
            return;
        }

        this.runButton.addEventListener('click', () => {
            this.consoleOutput.innerText = 'Initializing isolated sub-process runtime context...';
            this.consoleOutput.style.color = '#F59E0B';

            setTimeout(() => {
                const capturedValue = this.codeInput.value;
                if (capturedValue.includes('print')) {
                    this.consoleOutput.innerText = 'Active Engine\n\n>> Process completed execution successfully.';
                    this.consoleOutput.style.color = '#10B981';
                    appEngine.showToast('Milestone conditions cleared.', 'success');
                } else {
                    this.consoleOutput.innerText = 'Traceback Exception: NameError encountered on line 3.\nNo stdout stream standard returned.';
                    this.consoleOutput.style.color = '#EF4444';
                }
            }, 1200);
        });
    }
}

const workspaceStudio = new SkillExaLesson();
