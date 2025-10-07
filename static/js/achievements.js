// ACHIEVEMENTS SYSTEM - Track progress and unlock rewards!

class AchievementSystem {
    constructor() {
        this.achievements = {
            first_lesson: {
                id: 'first_lesson',
                name: 'First Steps',
                description: 'Complete your first lesson',
                icon: '🎓',
                points: 10,
                unlocked: false
            },
            problem_master_10: {
                id: 'problem_master_10',
                name: 'Problem Solver',
                description: 'Solve 10 practice problems',
                icon: '🎯',
                points: 25,
                unlocked: false
            },
            problem_master_50: {
                id: 'problem_master_50',
                name: 'Math Wizard',
                description: 'Solve 50 practice problems',
                icon: '🧙',
                points: 100,
                unlocked: false
            },
            problem_master_100: {
                id: 'problem_master_100',
                name: 'Math Champion',
                description: 'Solve 100 practice problems',
                icon: '🏆',
                points: 250,
                unlocked: false
            },
            streak_3: {
                id: 'streak_3',
                name: 'On Fire!',
                description: 'Get 3 correct answers in a row',
                icon: '🔥',
                points: 15,
                unlocked: false
            },
            streak_10: {
                id: 'streak_10',
                name: 'Unstoppable!',
                description: 'Get 10 correct answers in a row',
                icon: '⚡',
                points: 50,
                unlocked: false
            },
            game_master: {
                id: 'game_master',
                name: 'Game Master',
                description: 'Play all 4 games',
                icon: '🎮',
                points: 75,
                unlocked: false
            },
            perfect_score: {
                id: 'perfect_score',
                name: 'Perfect!',
                description: 'Get 100% on a practice session',
                icon: '💯',
                points: 50,
                unlocked: false
            },
            speed_demon: {
                id: 'speed_demon',
                name: 'Speed Demon',
                description: 'Answer 10 questions in under 2 minutes',
                icon: '⚡',
                points: 40,
                unlocked: false
            },
            helpful_hero: {
                id: 'helpful_hero',
                name: 'Helpful Hero',
                description: 'Help another student',
                icon: '🦸',
                points: 30,
                unlocked: false
            }
        };
        
        this.totalPoints = 0;
        this.level = 1;
        this.loadProgress();
    }
    
    checkAchievement(achievementId) {
        if (this.achievements[achievementId] && !this.achievements[achievementId].unlocked) {
            this.unlockAchievement(achievementId);
        }
    }
    
    unlockAchievement(achievementId) {
        const achievement = this.achievements[achievementId];
        if (!achievement || achievement.unlocked) return;
        
        achievement.unlocked = true;
        this.totalPoints += achievement.points;
        
        // Update level
        this.level = Math.floor(this.totalPoints / 100) + 1;
        
        // Show notification
        this.showAchievementNotification(achievement);
        
        // Save progress
        this.saveProgress();
        
        // Emit event
        if (typeof socketio !== 'undefined') {
            socketio.emit('achievement_unlocked', {
                achievement_id: achievementId,
                points: achievement.points
            });
        }
    }
    
    showAchievementNotification(achievement) {
        const notification = document.createElement('div');
        notification.className = 'achievement-notification';
        notification.innerHTML = `
            <div class="achievement-content">
                <div class="achievement-icon">${achievement.icon}</div>
                <div class="achievement-info">
                    <div class="achievement-title">Achievement Unlocked!</div>
                    <div class="achievement-name">${achievement.name}</div>
                    <div class="achievement-points">+${achievement.points} points</div>
                </div>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Play sound
        if (typeof playSound === 'function') {
            playSound('achievement');
        }
        
        // Particle effect
        this.createAchievementParticles();
        
        // Remove after 5 seconds
        setTimeout(() => {
            notification.classList.add('fade-out');
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 500);
        }, 5000);
    }
    
    createAchievementParticles() {
        for (let i = 0; i < 30; i++) {
            const particle = document.createElement('div');
            particle.className = 'achievement-particle';
            particle.style.left = Math.random() * window.innerWidth + 'px';
            particle.style.top = Math.random() * window.innerHeight + 'px';
            particle.style.background = `hsl(${Math.random() * 360}, 70%, 60%)`;
            particle.textContent = ['⭐', '🌟', '✨', '💫'][Math.floor(Math.random() * 4)];
            document.body.appendChild(particle);
            
            setTimeout(() => {
                particle.remove();
            }, 2000);
        }
    }
    
    getProgress() {
        return {
            totalPoints: this.totalPoints,
            level: this.level,
            achievements: Object.values(this.achievements).filter(a => a.unlocked).length,
            totalAchievements: Object.keys(this.achievements).length
        };
    }
    
    saveProgress() {
        localStorage.setItem('achievement_progress', JSON.stringify({
            achievements: this.achievements,
            totalPoints: this.totalPoints,
            level: this.level
        }));
    }
    
    loadProgress() {
        const saved = localStorage.getItem('achievement_progress');
        if (saved) {
            try {
                const data = JSON.parse(saved);
                this.achievements = data.achievements || this.achievements;
                this.totalPoints = data.totalPoints || 0;
                this.level = data.level || 1;
            } catch (e) {
                console.error('Error loading progress:', e);
            }
        }
    }
}

// Global instance
window.achievementSystem = new AchievementSystem();

// Event listeners for achievements
document.addEventListener('DOMContentLoaded', function() {
    // Check for first visit
    if (!localStorage.getItem('visited_before')) {
        localStorage.setItem('visited_before', 'true');
        setTimeout(() => {
            achievementSystem.checkAchievement('first_lesson');
        }, 2000);
    }
});

// Function to update achievement display
function updateAchievementDisplay() {
    const progress = achievementSystem.getProgress();
    
    // Update UI elements if they exist
    const levelElement = document.getElementById('user-level');
    if (levelElement) {
        levelElement.textContent = progress.level;
    }
    
    const pointsElement = document.getElementById('user-points');
    if (pointsElement) {
        pointsElement.textContent = progress.totalPoints;
    }
    
    const achievementsElement = document.getElementById('achievements-count');
    if (achievementsElement) {
        achievementsElement.textContent = `${progress.achievements}/${progress.totalAchievements}`;
    }
}

// Call on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateAchievementDisplay);
} else {
    updateAchievementDisplay();
}

