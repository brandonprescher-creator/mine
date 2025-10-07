// BADASS GAMES JAVASCRIPT - INTERACTIVE MINI-GAMES!

// Game instances
const games = {
    mathBattle: null,
    wordHunt: null,
    scienceLab: null,
    spaceRace: null
};

// Math Battle Game
class MathBattleGame {
    constructor() {
        this.monsters = [];
        this.player = { health: 100, level: 1, damage: 10 };
        this.currentProblem = null;
        this.score = 0;
        this.gameArea = null;
    }
    
    start() {
        this.createGameArea();
        this.spawnMonster();
        this.updateUI();
    }
    
    createGameArea() {
        this.gameArea = document.createElement('div');
        this.gameArea.className = 'math-battle-game';
        this.gameArea.innerHTML = `
            <div class="game-header">
                <div class="player-stats">
                    <div class="stat">❤️ Health: <span id="player-health">${this.player.health}</span></div>
                    <div class="stat">⚔️ Level: <span id="player-level">${this.player.level}</span></div>
                    <div class="stat">🏆 Score: <span id="player-score">${this.score}</span></div>
                </div>
            </div>
            <div class="battle-area">
                <div class="monster" id="monster">
                    <div class="monster-sprite">👹</div>
                    <div class="monster-health">❤️ <span id="monster-hp">50</span></div>
                </div>
                <div class="player-character">
                    <div class="player-sprite">🛡️</div>
                </div>
            </div>
            <div class="problem-area">
                <div class="problem" id="current-problem"></div>
                <div class="answer-input">
                    <input type="number" id="answer-input" placeholder="Your answer...">
                    <button onclick="games.mathBattle.attack()">⚔️ ATTACK!</button>
                </div>
            </div>
        `;
        
        this.gameArea.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            z-index: 10000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Fredoka One', cursive;
        `;
        
        document.body.appendChild(this.gameArea);
        
        // Add event listener for Enter key
        document.getElementById('answer-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.attack();
            }
        });
    }
    
    spawnMonster() {
        const monsterTypes = [
            { name: 'Addition Goblin', hp: 30, problems: 'addition' },
            { name: 'Subtraction Troll', hp: 40, problems: 'subtraction' },
            { name: 'Multiplication Dragon', hp: 60, problems: 'multiplication' },
            { name: 'Division Demon', hp: 80, problems: 'division' }
        ];
        
        const monster = monsterTypes[Math.floor(Math.random() * monsterTypes.length)];
        this.currentMonster = { ...monster, currentHp: monster.hp };
        
        this.generateProblem();
        this.updateMonsterDisplay();
    }
    
    generateProblem() {
        const { problems } = this.currentMonster;
        let problem, answer;
        
        switch (problems) {
            case 'addition':
                const a = Math.floor(Math.random() * 50) + 1;
                const b = Math.floor(Math.random() * 50) + 1;
                problem = `${a} + ${b} = ?`;
                answer = a + b;
                break;
            case 'subtraction':
                const c = Math.floor(Math.random() * 50) + 25;
                const d = Math.floor(Math.random() * 25) + 1;
                problem = `${c} - ${d} = ?`;
                answer = c - d;
                break;
            case 'multiplication':
                const e = Math.floor(Math.random() * 12) + 1;
                const f = Math.floor(Math.random() * 12) + 1;
                problem = `${e} × ${f} = ?`;
                answer = e * f;
                break;
            case 'division':
                const g = Math.floor(Math.random() * 10) + 2;
                const h = Math.floor(Math.random() * 10) + 2;
                const product = g * h;
                problem = `${product} ÷ ${g} = ?`;
                answer = h;
                break;
        }
        
        this.currentProblem = { problem, answer };
        document.getElementById('current-problem').innerHTML = `
            <h3>${this.currentMonster.name} challenges you!</h3>
            <div class="problem-text">${problem}</div>
        `;
    }
    
    attack() {
        const userAnswer = parseInt(document.getElementById('answer-input').value);
        const correctAnswer = this.currentProblem.answer;
        
        if (userAnswer === correctAnswer) {
            // Correct answer - damage monster
            const damage = this.player.damage + Math.floor(Math.random() * 10);
            this.currentMonster.currentHp -= damage;
            
            this.showDamage(damage, 'monster');
            badassTutor.playSound('correct');
            badassTutor.showNotification(`You dealt ${damage} damage!`, 'success');
            
            if (this.currentMonster.currentHp <= 0) {
                this.defeatMonster();
            } else {
                this.updateMonsterDisplay();
                this.generateProblem();
            }
            
            this.score += 10;
        } else {
            // Wrong answer - take damage
            const damage = Math.floor(Math.random() * 15) + 5;
            this.player.health -= damage;
            
            this.showDamage(damage, 'player');
            badassTutor.playSound('incorrect');
            badassTutor.showNotification(`You took ${damage} damage!`, 'error');
            
            if (this.player.health <= 0) {
                this.gameOver();
            }
        }
        
        document.getElementById('answer-input').value = '';
        this.updateUI();
    }
    
    showDamage(amount, target) {
        const damageText = document.createElement('div');
        damageText.textContent = `-${amount}`;
        damageText.style.cssText = `
            position: absolute;
            color: ${target === 'monster' ? '#ff6b6b' : '#4ecdc4'};
            font-size: 2rem;
            font-weight: bold;
            animation: damageFloat 2s ease-out forwards;
            pointer-events: none;
            z-index: 10001;
        `;
        
        if (target === 'monster') {
            damageText.style.left = '60%';
            damageText.style.top = '30%';
        } else {
            damageText.style.left = '40%';
            damageText.style.top = '70%';
        }
        
        this.gameArea.appendChild(damageText);
        
        setTimeout(() => {
            damageText.remove();
        }, 2000);
    }
    
    defeatMonster() {
        badassTutor.showCelebration();
        badassTutor.addCoins(20);
        badassTutor.showNotification('Monster defeated!', 'success');
        
        setTimeout(() => {
            this.spawnMonster();
        }, 2000);
    }
    
    gameOver() {
        this.gameArea.innerHTML = `
            <div class="game-over">
                <h2>Game Over!</h2>
                <p>Final Score: ${this.score}</p>
                <button onclick="games.mathBattle.close()">Play Again</button>
            </div>
        `;
    }
    
    updateUI() {
        document.getElementById('player-health').textContent = this.player.health;
        document.getElementById('player-level').textContent = this.player.level;
        document.getElementById('player-score').textContent = this.score;
    }
    
    updateMonsterDisplay() {
        document.getElementById('monster-hp').textContent = this.currentMonster.currentHp;
    }
    
    close() {
        this.gameArea.remove();
        games.mathBattle = null;
    }
}

// Word Hunt Game
class WordHuntGame {
    constructor() {
        this.words = ['CAT', 'DOG', 'SUN', 'MOON', 'STAR', 'TREE', 'BIRD', 'FISH'];
        this.currentWord = '';
        this.foundLetters = [];
        this.score = 0;
        this.gameArea = null;
    }
    
    start() {
        this.createGameArea();
        this.generateWord();
    }
    
    createGameArea() {
        this.gameArea = document.createElement('div');
        this.gameArea.className = 'word-hunt-game';
        this.gameArea.innerHTML = `
            <div class="game-header">
                <h2>🔍 Word Hunt</h2>
                <div class="score">Score: <span id="word-score">0</span></div>
            </div>
            <div class="word-display">
                <div class="word-letters" id="word-letters"></div>
            </div>
            <div class="letter-grid" id="letter-grid"></div>
            <div class="game-controls">
                <button onclick="games.wordHunt.newWord()">New Word</button>
                <button onclick="games.wordHunt.close()">Close</button>
            </div>
        `;
        
        this.gameArea.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #96ceb4 0%, #feca57 100%);
            z-index: 10000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Fredoka One', cursive;
            padding: 2rem;
        `;
        
        document.body.appendChild(this.gameArea);
    }
    
    generateWord() {
        this.currentWord = this.words[Math.floor(Math.random() * this.words.length)];
        this.foundLetters = new Array(this.currentWord.length).fill(false);
        this.createLetterGrid();
        this.updateWordDisplay();
    }
    
    createLetterGrid() {
        const grid = document.getElementById('letter-grid');
        grid.innerHTML = '';
        
        // Create a 6x6 grid of random letters
        const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        const gridSize = 6;
        
        // Place the word letters randomly in the grid
        const wordPositions = [];
        for (let i = 0; i < this.currentWord.length; i++) {
            let position;
            do {
                position = Math.floor(Math.random() * (gridSize * gridSize));
            } while (wordPositions.includes(position));
            wordPositions.push(position);
        }
        
        for (let i = 0; i < gridSize * gridSize; i++) {
            const letter = document.createElement('div');
            letter.className = 'grid-letter';
            
            if (wordPositions.includes(i)) {
                const wordIndex = wordPositions.indexOf(i);
                letter.textContent = this.currentWord[wordIndex];
                letter.dataset.wordIndex = wordIndex;
                letter.addEventListener('click', () => this.selectLetter(letter, wordIndex));
            } else {
                letter.textContent = letters[Math.floor(Math.random() * letters.length)];
            }
            
            letter.style.cssText = `
                width: 50px;
                height: 50px;
                background: rgba(255, 255, 255, 0.2);
                border: 2px solid white;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.5rem;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 2px;
            `;
            
            grid.appendChild(letter);
        }
        
        grid.style.cssText = `
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 5px;
            margin: 2rem 0;
        `;
    }
    
    selectLetter(letter, wordIndex) {
        if (this.foundLetters[wordIndex]) return;
        
        this.foundLetters[wordIndex] = true;
        letter.style.background = 'linear-gradient(45deg, #4CAF50, #45a049)';
        letter.style.transform = 'scale(1.1)';
        
        badassTutor.playSound('correct');
        
        if (this.foundLetters.every(found => found)) {
            this.completeWord();
        }
        
        this.updateWordDisplay();
    }
    
    completeWord() {
        this.score += 100;
        badassTutor.showCelebration();
        badassTutor.addCoins(15);
        badassTutor.showNotification(`Word found: ${this.currentWord}!`, 'success');
        
        setTimeout(() => {
            this.generateWord();
        }, 2000);
    }
    
    updateWordDisplay() {
        const wordDisplay = document.getElementById('word-letters');
        wordDisplay.innerHTML = '';
        
        for (let i = 0; i < this.currentWord.length; i++) {
            const letter = document.createElement('span');
            letter.textContent = this.foundLetters[i] ? this.currentWord[i] : '_';
            letter.style.cssText = `
                font-size: 2rem;
                margin: 0 0.5rem;
                color: ${this.foundLetters[i] ? '#4CAF50' : 'white'};
                font-weight: bold;
            `;
            wordDisplay.appendChild(letter);
        }
    }
    
    newWord() {
        this.generateWord();
    }
    
    close() {
        this.gameArea.remove();
        games.wordHunt = null;
    }
}

// Science Lab Game
class ScienceLabGame {
    constructor() {
        this.experiments = [
            { name: 'Volcano', ingredients: ['baking soda', 'vinegar', 'red dye'], result: '🌋' },
            { name: 'Rainbow', ingredients: ['water', 'food coloring', 'sugar'], result: '🌈' },
            { name: 'Slime', ingredients: ['glue', 'borax', 'water'], result: '🟢' }
        ];
        this.currentExperiment = null;
        this.selectedIngredients = [];
        this.gameArea = null;
    }
    
    start() {
        this.createGameArea();
        this.startExperiment();
    }
    
    createGameArea() {
        this.gameArea = document.createElement('div');
        this.gameArea.className = 'science-lab-game';
        this.gameArea.innerHTML = `
            <div class="game-header">
                <h2>🧪 Science Lab</h2>
                <div class="experiment-name" id="experiment-name"></div>
            </div>
            <div class="lab-area">
                <div class="ingredients-shelf">
                    <h3>Available Ingredients:</h3>
                    <div class="ingredients" id="ingredients"></div>
                </div>
                <div class="mixing-bowl">
                    <h3>Mixing Bowl:</h3>
                    <div class="bowl" id="mixing-bowl"></div>
                    <button onclick="games.scienceLab.mix()" id="mix-btn">🧪 MIX!</button>
                </div>
            </div>
            <div class="game-controls">
                <button onclick="games.scienceLab.newExperiment()">New Experiment</button>
                <button onclick="games.scienceLab.close()">Close</button>
            </div>
        `;
        
        this.gameArea.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            z-index: 10000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Fredoka One', cursive;
            padding: 2rem;
        `;
        
        document.body.appendChild(this.gameArea);
    }
    
    startExperiment() {
        this.currentExperiment = this.experiments[Math.floor(Math.random() * this.experiments.length)];
        this.selectedIngredients = [];
        
        document.getElementById('experiment-name').textContent = `Create: ${this.currentExperiment.name}`;
        this.createIngredients();
        this.updateMixingBowl();
    }
    
    createIngredients() {
        const ingredientsContainer = document.getElementById('ingredients');
        ingredientsContainer.innerHTML = '';
        
        const allIngredients = [...new Set(this.experiments.flatMap(exp => exp.ingredients))];
        
        allIngredients.forEach(ingredient => {
            const ingredientBtn = document.createElement('button');
            ingredientBtn.textContent = ingredient;
            ingredientBtn.className = 'ingredient-btn';
            ingredientBtn.onclick = () => this.addIngredient(ingredient, ingredientBtn);
            
            ingredientBtn.style.cssText = `
                background: linear-gradient(45deg, #4ecdc4, #45b7d1);
                border: none;
                border-radius: 10px;
                padding: 0.5rem 1rem;
                margin: 0.25rem;
                color: white;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
            `;
            
            ingredientsContainer.appendChild(ingredientBtn);
        });
    }
    
    addIngredient(ingredient, button) {
        if (this.selectedIngredients.includes(ingredient)) return;
        
        this.selectedIngredients.push(ingredient);
        button.style.background = 'linear-gradient(45deg, #ff6b6b, #feca57)';
        button.disabled = true;
        
        this.updateMixingBowl();
    }
    
    updateMixingBowl() {
        const bowl = document.getElementById('mixing-bowl');
        bowl.innerHTML = '';
        
        this.selectedIngredients.forEach(ingredient => {
            const ingredientDiv = document.createElement('div');
            ingredientDiv.textContent = ingredient;
            ingredientDiv.style.cssText = `
                background: rgba(255, 255, 255, 0.2);
                padding: 0.5rem;
                margin: 0.25rem;
                border-radius: 5px;
                display: inline-block;
            `;
            bowl.appendChild(ingredientDiv);
        });
    }
    
    mix() {
        const correctIngredients = this.currentExperiment.ingredients.sort();
        const selectedIngredients = this.selectedIngredients.sort();
        
        const isCorrect = correctIngredients.length === selectedIngredients.length &&
                         correctIngredients.every((ingredient, index) => ingredient === selectedIngredients[index]);
        
        if (isCorrect) {
            this.showResult(true);
        } else {
            this.showResult(false);
        }
    }
    
    showResult(success) {
        const resultDiv = document.createElement('div');
        resultDiv.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: ${success ? 'linear-gradient(45deg, #4CAF50, #45a049)' : 'linear-gradient(45deg, #f44336, #d32f2f)'};
            color: white;
            padding: 2rem;
            border-radius: 20px;
            font-size: 2rem;
            text-align: center;
            z-index: 10001;
        `;
        
        if (success) {
            resultDiv.innerHTML = `
                <h3>🎉 Experiment Successful! 🎉</h3>
                <div style="font-size: 4rem; margin: 1rem 0;">${this.currentExperiment.result}</div>
                <p>You created ${this.currentExperiment.name}!</p>
            `;
            badassTutor.playSound('correct');
            badassTutor.addCoins(25);
        } else {
            resultDiv.innerHTML = `
                <h3>💥 Experiment Failed! 💥</h3>
                <p>Try again with the right ingredients!</p>
            `;
            badassTutor.playSound('incorrect');
        }
        
        this.gameArea.appendChild(resultDiv);
        
        setTimeout(() => {
            resultDiv.remove();
            if (success) {
                this.newExperiment();
            }
        }, 3000);
    }
    
    newExperiment() {
        this.startExperiment();
    }
    
    close() {
        this.gameArea.remove();
        games.scienceLab = null;
    }
}

// Space Race Game
class SpaceRaceGame {
    constructor() {
        this.player = { x: 50, y: 80, speed: 2 };
        this.obstacles = [];
        this.powerUps = [];
        this.score = 0;
        this.gameArea = null;
        this.gameLoop = null;
    }
    
    start() {
        this.createGameArea();
        this.startGameLoop();
    }
    
    createGameArea() {
        this.gameArea = document.createElement('div');
        this.gameArea.className = 'space-race-game';
        this.gameArea.innerHTML = `
            <div class="game-header">
                <h2>🚀 Space Race</h2>
                <div class="score">Score: <span id="space-score">0</span></div>
            </div>
            <div class="space-canvas" id="space-canvas">
                <div class="spaceship" id="spaceship">🚀</div>
            </div>
            <div class="game-controls">
                <button onclick="games.spaceRace.close()">Close</button>
            </div>
        `;
        
        this.gameArea.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(180deg, #000428 0%, #004e92 100%);
            z-index: 10000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Fredoka One', cursive;
        `;
        
        const canvas = document.getElementById('space-canvas');
        canvas.style.cssText = `
            width: 400px;
            height: 600px;
            background: linear-gradient(180deg, #000428 0%, #004e92 100%);
            position: relative;
            overflow: hidden;
            border: 2px solid white;
            border-radius: 10px;
        `;
        
        const spaceship = document.getElementById('spaceship');
        spaceship.style.cssText = `
            position: absolute;
            font-size: 2rem;
            left: 50%;
            top: 80%;
            transform: translateX(-50%);
            transition: left 0.1s ease;
        `;
        
        document.body.appendChild(this.gameArea);
        
        // Add keyboard controls
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') {
                this.moveLeft();
            } else if (e.key === 'ArrowRight') {
                this.moveRight();
            }
        });
    }
    
    startGameLoop() {
        this.gameLoop = setInterval(() => {
            this.update();
        }, 50);
        
        setInterval(() => {
            this.spawnObstacle();
        }, 2000);
        
        setInterval(() => {
            this.spawnPowerUp();
        }, 5000);
    }
    
    update() {
        this.moveObstacles();
        this.movePowerUps();
        this.checkCollisions();
        this.updateScore();
    }
    
    moveLeft() {
        this.player.x = Math.max(0, this.player.x - 10);
        this.updateSpaceshipPosition();
    }
    
    moveRight() {
        this.player.x = Math.min(90, this.player.x + 10);
        this.updateSpaceshipPosition();
    }
    
    updateSpaceshipPosition() {
        const spaceship = document.getElementById('spaceship');
        spaceship.style.left = `${this.player.x}%`;
    }
    
    spawnObstacle() {
        const obstacle = {
            x: Math.random() * 80 + 10,
            y: -5,
            speed: 2 + Math.random() * 2
        };
        
        const obstacleEl = document.createElement('div');
        obstacleEl.textContent = '💥';
        obstacleEl.style.cssText = `
            position: absolute;
            font-size: 1.5rem;
            left: ${obstacle.x}%;
            top: ${obstacle.y}%;
        `;
        
        obstacle.element = obstacleEl;
        this.obstacles.push(obstacle);
        document.getElementById('space-canvas').appendChild(obstacleEl);
    }
    
    spawnPowerUp() {
        const powerUp = {
            x: Math.random() * 80 + 10,
            y: -5,
            speed: 1 + Math.random()
        };
        
        const powerUpEl = document.createElement('div');
        powerUpEl.textContent = '⭐';
        powerUpEl.style.cssText = `
            position: absolute;
            font-size: 1.5rem;
            left: ${powerUp.x}%;
            top: ${powerUp.y}%;
        `;
        
        powerUp.element = powerUpEl;
        this.powerUps.push(powerUp);
        document.getElementById('space-canvas').appendChild(powerUpEl);
    }
    
    moveObstacles() {
        this.obstacles.forEach((obstacle, index) => {
            obstacle.y += obstacle.speed;
            obstacle.element.style.top = `${obstacle.y}%`;
            
            if (obstacle.y > 100) {
                obstacle.element.remove();
                this.obstacles.splice(index, 1);
            }
        });
    }
    
    movePowerUps() {
        this.powerUps.forEach((powerUp, index) => {
            powerUp.y += powerUp.speed;
            powerUp.element.style.top = `${powerUp.y}%`;
            
            if (powerUp.y > 100) {
                powerUp.element.remove();
                this.powerUps.splice(index, 1);
            }
        });
    }
    
    checkCollisions() {
        // Check obstacle collisions
        this.obstacles.forEach((obstacle, index) => {
            if (this.isColliding(this.player, obstacle)) {
                this.gameOver();
            }
        });
        
        // Check power-up collisions
        this.powerUps.forEach((powerUp, index) => {
            if (this.isColliding(this.player, powerUp)) {
                this.collectPowerUp(powerUp, index);
            }
        });
    }
    
    isColliding(obj1, obj2) {
        const threshold = 5;
        return Math.abs(obj1.x - obj2.x) < threshold && Math.abs(obj1.y - obj2.y) < threshold;
    }
    
    collectPowerUp(powerUp, index) {
        powerUp.element.remove();
        this.powerUps.splice(index, 1);
        this.score += 50;
        badassTutor.addCoins(10);
        badassTutor.showNotification('Power-up collected!', 'success');
    }
    
    updateScore() {
        this.score += 1;
        document.getElementById('space-score').textContent = this.score;
    }
    
    gameOver() {
        clearInterval(this.gameLoop);
        badassTutor.showNotification(`Game Over! Final Score: ${this.score}`, 'error');
        
        setTimeout(() => {
            this.close();
        }, 3000);
    }
    
    close() {
        if (this.gameLoop) {
            clearInterval(this.gameLoop);
        }
        this.gameArea.remove();
        games.spaceRace = null;
    }
}

// Game launcher functions
function playGame(gameType) {
    switch (gameType) {
        case 'math-battle':
            games.mathBattle = new MathBattleGame();
            games.mathBattle.start();
            break;
        case 'word-hunt':
            games.wordHunt = new WordHuntGame();
            games.wordHunt.start();
            break;
        case 'science-lab':
            games.scienceLab = new ScienceLabGame();
            games.scienceLab.start();
            break;
        case 'space-race':
            games.spaceRace = new SpaceRaceGame();
            games.spaceRace.start();
            break;
    }
}

// Add CSS for game animations
const gameStyles = document.createElement('style');
gameStyles.textContent = `
    @keyframes damageFloat {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(-50px); opacity: 0; }
    }
    
    .grid-letter:hover {
        background: rgba(255, 255, 255, 0.4) !important;
        transform: scale(1.1);
    }
    
    .ingredient-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
`;
document.head.appendChild(gameStyles);

// Export games for global access
window.games = games;
window.playGame = playGame;
