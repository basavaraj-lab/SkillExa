class SkillExaTopics {
    constructor() {
        this.gridMountNode = document.getElementById('topics-target-grid');
        this.initCatalog();
    }

    async initCatalog() {
        if (!this.gridMountNode) {
            this.gridMountNode = document.getElementById('topics-target-grid');
            if (!this.gridMountNode) return;
        }

        this.gridMountNode.innerHTML = '<div class="card-glass skeleton" style="height: 180px;"></div>';

        try {
            const res = await appEngine.dataRequest('/api/topics');
            const topics = Array.isArray(res) ? res : (res.topics || []);
            this.renderCatalogGrid(topics);
        } catch (error) {
            this.gridMountNode.innerHTML = '';
            appEngine.showToast('Failed to load topics.', 'danger');
            console.error('Failed to load topics:', error);
        }
    }

    renderCatalogGrid(topics) {
        if (!Array.isArray(topics)) {
            this.gridMountNode.innerHTML = '';
            return;
        }

        this.gridMountNode.innerHTML = '';

        topics.forEach((topic) => {
            const isUnlocked = topic.status ? topic.status !== 'LOCKED' : Boolean(topic.is_unlocked);
            const topicName = topic.title || topic.name || `Topic ${topic.id}`;
            const duration = topic.duration || topic.time || '20 min';
            const cardElement = document.createElement('div');

            cardElement.className = `card-glass animate-fade-in ${!isUnlocked ? 'topic-locked' : ''}`;
            cardElement.style.opacity = isUnlocked ? '1' : '0.6';
            cardElement.style.pointerEvents = isUnlocked ? 'auto' : 'none';

            cardElement.innerHTML = `
                <div style="display:flex; justify-content:space-between; margin-bottom:1rem; align-items:center;">
                    <span style="font-size:0.75rem; text-transform:uppercase; font-weight:700; color:${isUnlocked ? 'var(--primary)' : 'var(--text-muted)'};">
                        Module ${String(topic.id).padStart(2, '0')}
                    </span>
                    <span>
                        ${isUnlocked
                            ? `<span style="padding:0.25rem 0.5rem; border-radius:4px; font-size:0.75rem; font-weight:600; background:rgba(37,99,235,0.1); color:var(--primary);">${topic.difficulty}</span>`
                            : `<i class="fas fa-lock" style="color:var(--text-muted);"></i> Locked`
                        }
                    </span>
                </div>
                <h3 style="font-size:1.15rem; margin-bottom:0.75rem; color: ${isUnlocked ? 'var(--text-main)' : 'var(--text-muted)'};">${topicName}</h3>
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; color:var(--text-muted); margin-bottom:1rem;">
                    <span><i class="far fa-clock"></i> ${duration}</span>
                    <span>${topic.completeness ?? 0}% Complete</span>
                </div>

                <button ${!isUnlocked ? 'disabled' : ''} onclick="window.location.href='/topic/${topic.id}'"
                        style="width:100%; padding:0.75rem; border:none; background:${isUnlocked ? 'var(--primary-gradient)' : 'var(--border)'}; color:${isUnlocked ? 'white' : 'var(--text-muted)'}; font-weight:600; border-radius:var(--radius-sm); cursor:${isUnlocked ? 'pointer' : 'not-allowed'};">
                    ${!isUnlocked ? 'Unlock Previous Lesson First' : (topic.completeness > 0 ? 'Resume Track' : 'Start Topic')}
                </button>
            `;

            this.gridMountNode.appendChild(cardElement);
        });
    }
}

function bootTopicsApp() {
    window.productCatalog = new SkillExaTopics();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootTopicsApp);
} else {
    bootTopicsApp();
}
