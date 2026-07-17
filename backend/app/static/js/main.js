// frontend/js/main.js
class SkillExaEngine {
    constructor() {
        this.apiBase = '';
        this.initTheme();
        this.setupGlobalListeners();
    }

    initTheme() {
        const activeTheme = localStorage.getItem('skillexa-theme') || 'light';
        document.documentElement.setAttribute('data-theme', activeTheme);
    }

    toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme');
        const nextTheme = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', nextTheme);
        localStorage.setItem('skillexa-theme', nextTheme);
        this.showToast(`Theme changed to ${nextTheme} mode`, 'info');
    }

    // Dynamic, global fetch execution module
    async dataRequest(endpoint, options = {}) {
        const normalizedEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
        try {
            const response = await fetch(`${this.apiBase}${normalizedEndpoint}`, {
                headers: { 'Content-Type': 'application/json' },
                ...options
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'API operation error encountered.');
            }
            return await response.json();
        } catch (error) {
            this.showToast(error.message, 'danger');
            throw error;
        }
    }

    showToast(message, type = 'primary') {
        const container = document.getElementById('toast-pipeline') || this.createToastContainer();
        const element = document.createElement('div');
        element.className = `toast toast-${type}`;
        element.innerHTML = `<i class="fas ${this.getToastIcon(type)}"></i><span>${message}</span>`;
        container.appendChild(element);
        setTimeout(() => element.remove(), 4000);
    }

    createToastContainer() {
        const el = document.createElement('div');
        el.id = 'toast-pipeline';
        el.className = 'toast-container';
        document.body.appendChild(el);
        return el;
    }

    getToastIcon(type) {
        const icons = { success: 'fa-check-circle', danger: 'fa-exclamation', info: 'fa-info-circle' };
        return icons[type] || 'fa-bell';
    }

    setupGlobalListeners() {
        document.addEventListener('DOMContentLoaded', () => {
            const systemBtn = document.querySelector('.theme-toggle-trigger');
            if(systemBtn) systemBtn.addEventListener('click', () => this.toggleTheme());
        });
    }
}

const appEngine = new SkillExaEngine();