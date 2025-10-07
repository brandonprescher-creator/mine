// ULTIMATE BADASS TUTOR JAVASCRIPT - INSANELY COOL FEATURES!

// Global variables
let socket;
let gameState = {
    level: 1,
    coins: 0,
    streak: 0,
    achievements: []
};

// Sound effects
const sounds = {
    correct: new Howl({ src: ['/static/sounds/correct.mp3'] }),
    incorrect: new Howl({ src: ['/static/sounds/incorrect.mp3'] }),
    levelUp: new Howl({ src: ['/static/sounds/level-up.mp3'] }),
    achievement: new Howl({ src: ['/static/sounds/achievement.mp3'] }),
    click: new Howl({ src: ['/static/sounds/click.mp3'] })
};

// Initialize everything when page loads
document.addEventListener('DOMContentLoaded', function() {
    initializeSocket();
    initializeGameState();
    startBackgroundAnimations();
    initializeVoiceRecognition();
    startParticleSystem();
});

// Socket.IO initialization
function initializeSocket() {
    socket = io();
    
    socket.on('connect', function() {
        console.log('Connected to server!');
        showNotification('Connected to multiplayer!', 'success');
    });
    
    socket.on('answer_feedback', function(data) {
        handleAnswerFeedback(data);
    });
    
    socket.on('achievement_unlocked', function(data) {
        showAchievement(data);
    });
    
    socket.on('player_joined', function(data) {
        showNotification(`${data.user_id} joined the game!`, 'info');
    });
}

// Game state management
function initializeGameState() {
    // Load from localStorage
    const saved = localStorage.getItem('badassTutorGameState');
    if (saved) {
        gameState = { ...gameState, ...JSON.parse(saved) };
    }
    
    updateUI();
}

function saveGameState() {
    localStorage.setItem('badassTutorGameState', JSON.stringify(gameState));
}

function updateUI() {
    const levelEl = document.getElementById('user-level');
    const coinsEl = document.getElementById('user-coins');
    
    if (levelEl) levelEl.textContent = `Level ${gameState.level}`;
    if (coinsEl) coinsEl.textContent = gameState.coins;
}

// Background animations
function startBackgroundAnimations() {
    // Floating characters animation
    const characters = document.querySelectorAll('.character');
    characters.forEach((char, index) => {
        setInterval(() => {
            char.style.transform = `translate(${Math.random() * 20 - 10}px, ${Math.random() * 20 - 10}px) rotate(${Math.random() * 360}deg)`;
        }, 3000 + index * 500);
    });
    
    // Particle system
    createFloatingParticles();
}

function createFloatingParticles() {
    const particleContainer = document.createElement('div');
    particleContainer.className = 'floating-particles';
    particleContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    `;
    document.body.appendChild(particleContainer);
    
    setInterval(() => {
        createParticle(particleContainer);
    }, 2000);
}

function createParticle(container) {
    const particle = document.createElement('div');
    particle.style.cssText = `
        position: absolute;
        width: 4px;
        height: 4px;
        background: ${getRandomColor()};
        border-radius: 50%;
        left: ${Math.random() * 100}%;
        top: 100%;
        animation: floatUp 8s linear forwards;
    `;
    
    container.appendChild(particle);
    
    setTimeout(() => {
        particle.remove();
    }, 8000);
}

// Voice recognition
function initializeVoiceRecognition() {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';
        
        // Add voice button to practice problems
        addVoiceButtons(recognition);
    }
}

function addVoiceButtons(recognition) {
    const answerInputs = document.querySelectorAll('input[type="text"]');
    answerInputs.forEach(input => {
        const voiceBtn = document.createElement('button');
        voiceBtn.innerHTML = '🎤';
        voiceBtn.className = 'voice-btn';
        voiceBtn.style.cssText = `
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            color: white;
            cursor: pointer;
            font-size: 1.2rem;
        `;
        
        input.parentElement.style.position = 'relative';
        input.parentElement.appendChild(voiceBtn);
        
        voiceBtn.addEventListener('click', () => {
            recognition.start();
            voiceBtn.style.background = 'linear-gradient(45deg, #4ecdc4, #ff6b6b)';
            
            recognition.onresult = (event) => {
                const result = event.results[0][0].transcript;
                input.value = result;
                voiceBtn.style.background = 'linear-gradient(45deg, #ff6b6b, #4ecdc4)';
            };
        });
    });
}

// Answer feedback system
function handleAnswerFeedback(data) {
    if (data.correct) {
        showSuccessAnimation();
        playSound('correct');
        addCoins(10);
        updateStreak(true);
        
        if (data.celebration) {
            showCelebration();
        }
    } else {
        showErrorAnimation();
        playSound('incorrect');
        updateStreak(false);
    }
    
    // Check for achievements
    checkAchievements();
}

function showSuccessAnimation() {
    const success = document.createElement('div');
    success.innerHTML = '🎉 CORRECT! 🎉';
    success.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        font-size: 2rem;
        font-weight: bold;
        z-index: 10000;
        animation: successPop 2s ease-out forwards;
    `;
    
    document.body.appendChild(success);
    
    setTimeout(() => {
        success.remove();
    }, 2000);
}

function showErrorAnimation() {
    const error = document.createElement('div');
    error.innerHTML = '🤔 Try Again! 🤔';
    error.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(45deg, #f44336, #d32f2f);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        font-size: 2rem;
        font-weight: bold;
        z-index: 10000;
        animation: errorShake 2s ease-out forwards;
    `;
    
    document.body.appendChild(error);
    
    setTimeout(() => {
        error.remove();
    }, 2000);
}

function showCelebration() {
    // Create confetti explosion
    for (let i = 0; i < 100; i++) {
        createConfetti();
    }
    
    // Screen flash effect
    const flash = document.createElement('div');
    flash.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.8);
        z-index: 9999;
        animation: flash 0.5s ease-out;
    `;
    
    document.body.appendChild(flash);
    
    setTimeout(() => {
        flash.remove();
    }, 500);
}

function createConfetti() {
    const confetti = document.createElement('div');
    confetti.style.cssText = `
        position: fixed;
        width: 10px;
        height: 10px;
        background: ${getRandomColor()};
        left: ${Math.random() * 100}%;
        top: -10px;
        z-index: 10000;
        animation: confettiFall 3s linear forwards;
    `;
    
    document.body.appendChild(confetti);
    
    setTimeout(() => {
        confetti.remove();
    }, 3000);
}

// Achievement system
function checkAchievements() {
    const achievements = [
        {
            id: 'first_correct',
            name: 'First Success!',
            description: 'Got your first answer right!',
            condition: () => gameState.coins >= 10,
            icon: '🎯'
        },
        {
            id: 'streak_5',
            name: 'On Fire!',
            description: 'Got 5 answers right in a row!',
            condition: () => gameState.streak >= 5,
            icon: '🔥'
        },
        {
            id: 'coin_collector',
            name: 'Coin Collector',
            description: 'Earned 100 coins!',
            condition: () => gameState.coins >= 100,
            icon: '💰'
        },
        {
            id: 'level_up',
            name: 'Level Up!',
            description: 'Reached level 5!',
            condition: () => gameState.level >= 5,
            icon: '⭐'
        }
    ];
    
    achievements.forEach(achievement => {
        if (!gameState.achievements.includes(achievement.id) && achievement.condition()) {
            unlockAchievement(achievement);
        }
    });
}

function unlockAchievement(achievement) {
    gameState.achievements.push(achievement.id);
    showAchievement(achievement);
    playSound('achievement');
    addCoins(50);
    saveGameState();
}

function showAchievement(achievement) {
    const popup = document.getElementById('achievement-popup');
    const message = document.getElementById('achievement-message');
    
    popup.querySelector('.achievement-icon').textContent = achievement.icon;
    message.textContent = `${achievement.name}: ${achievement.description}`;
    
    popup.classList.add('show');
    
    setTimeout(() => {
        popup.classList.remove('show');
    }, 4000);
}

// Game mechanics
function addCoins(amount) {
    gameState.coins += amount;
    updateUI();
    saveGameState();
    
    // Show coin animation
    showCoinAnimation(amount);
}

function showCoinAnimation(amount) {
    const coin = document.createElement('div');
    coin.innerHTML = `+${amount} 💰`;
    coin.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #ffd700;
        font-size: 2rem;
        font-weight: bold;
        z-index: 10000;
        animation: coinFloat 2s ease-out forwards;
    `;
    
    document.body.appendChild(coin);
    
    setTimeout(() => {
        coin.remove();
    }, 2000);
}

function updateStreak(correct) {
    if (correct) {
        gameState.streak++;
        if (gameState.streak % 5 === 0) {
            levelUp();
        }
    } else {
        gameState.streak = 0;
    }
    
    saveGameState();
}

function levelUp() {
    gameState.level++;
    playSound('levelUp');
    showLevelUpAnimation();
    addCoins(100);
}

function showLevelUpAnimation() {
    const levelUp = document.createElement('div');
    levelUp.innerHTML = `LEVEL UP! 🎉<br>Level ${gameState.level}`;
    levelUp.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        color: #333;
        padding: 3rem;
        border-radius: 20px;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        z-index: 10000;
        animation: levelUpPop 3s ease-out forwards;
        border: 5px solid #fff;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    `;
    
    document.body.appendChild(levelUp);
    
    setTimeout(() => {
        levelUp.remove();
    }, 3000);
}

// Sound system
function playSound(soundName) {
    if (sounds[soundName]) {
        sounds[soundName].play();
    }
}

// Notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? 'linear-gradient(45deg, #4CAF50, #45a049)' : 
                    type === 'error' ? 'linear-gradient(45deg, #f44336, #d32f2f)' : 
                    'linear-gradient(45deg, #2196F3, #1976D2)'};
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        font-weight: bold;
        z-index: 10000;
        animation: slideInRight 0.5s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.5s ease-out forwards';
        setTimeout(() => {
            notification.remove();
        }, 500);
    }, 3000);
}

// Utility functions
function getRandomColor() {
    const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3'];
    return colors[Math.floor(Math.random() * colors.length)];
}

function randomBetween(min, max) {
    return Math.random() * (max - min) + min;
}

// CSS animations (injected via JavaScript)
const style = document.createElement('style');
style.textContent = `
    @keyframes successPop {
        0% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
        50% { transform: translate(-50%, -50%) scale(1.2); opacity: 1; }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 0; }
    }
    
    @keyframes errorShake {
        0%, 100% { transform: translate(-50%, -50%); }
        25% { transform: translate(-52%, -50%); }
        75% { transform: translate(-48%, -50%); }
    }
    
    @keyframes flash {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
    }
    
    @keyframes confettiFall {
        0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    
    @keyframes coinFloat {
        0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
        50% { transform: translate(-50%, -70%) scale(1.2); opacity: 1; }
        100% { transform: translate(-50%, -100%) scale(1); opacity: 0; }
    }
    
    @keyframes levelUpPop {
        0% { transform: translate(-50%, -50%) scale(0) rotate(0deg); opacity: 0; }
        50% { transform: translate(-50%, -50%) scale(1.1) rotate(5deg); opacity: 1; }
        100% { transform: translate(-50%, -50%) scale(1) rotate(0deg); opacity: 0; }
    }
    
    @keyframes floatUp {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    
    @keyframes slideInRight {
        0% { transform: translateX(100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        0% { transform: translateX(0); opacity: 1; }
        100% { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Export functions for use in other scripts
window.badassTutor = {
    playSound,
    showNotification,
    addCoins,
    unlockAchievement,
    showCelebration,
    gameState
};
