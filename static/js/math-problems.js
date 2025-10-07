// BADASS MATH PROBLEMS WITH VISUAL SOLUTIONS!

class MathProblems {
    constructor() {
        this.problems = {
            division: [
                {
                    id: 1,
                    question: "What is 24 ÷ 6?",
                    correct_answer: "4",
                    explanation: "6 goes into 24 exactly 4 times. 6 × 4 = 24",
                    visual_type: "division",
                    visual_data: { dividend: 24, divisor: 6, quotient: 4 },
                    difficulty: "easy",
                    options: ["3", "4", "5", "6"]
                },
                {
                    id: 2,
                    question: "What is 48 ÷ 8?",
                    correct_answer: "6",
                    explanation: "8 goes into 48 exactly 6 times. 8 × 6 = 48",
                    visual_type: "division",
                    visual_data: { dividend: 48, divisor: 8, quotient: 6 },
                    difficulty: "easy",
                    options: ["5", "6", "7", "8"]
                },
                {
                    id: 3,
                    question: "What is 72 ÷ 9?",
                    correct_answer: "8",
                    explanation: "9 goes into 72 exactly 8 times. 9 × 8 = 72",
                    visual_type: "division",
                    visual_data: { dividend: 72, divisor: 9, quotient: 8 },
                    difficulty: "medium",
                    options: ["7", "8", "9", "10"]
                }
            ],
            fractions: [
                {
                    id: 4,
                    question: "What is 1/2 + 1/4?",
                    correct_answer: "3/4",
                    explanation: "First find common denominator (4), then add: 2/4 + 1/4 = 3/4",
                    visual_type: "fraction",
                    visual_data: { 
                        fractions: [
                            { numerator: 1, denominator: 2 },
                            { numerator: 1, denominator: 4 }
                        ],
                        operation: "add",
                        result: { numerator: 3, denominator: 4 }
                    },
                    difficulty: "medium",
                    options: ["1/3", "2/6", "3/4", "2/4"]
                },
                {
                    id: 5,
                    question: "What is 2/3 + 1/6?",
                    correct_answer: "5/6",
                    explanation: "Common denominator is 6: 4/6 + 1/6 = 5/6",
                    visual_type: "fraction",
                    visual_data: { 
                        fractions: [
                            { numerator: 2, denominator: 3 },
                            { numerator: 1, denominator: 6 }
                        ],
                        operation: "add",
                        result: { numerator: 5, denominator: 6 }
                    },
                    difficulty: "medium",
                    options: ["3/9", "5/6", "4/6", "3/6"]
                }
            ],
            geometry: [
                {
                    id: 6,
                    question: "What is the area of a rectangle with length 8 and width 5?",
                    correct_answer: "40",
                    explanation: "Area = length × width = 8 × 5 = 40 square units",
                    visual_type: "geometry",
                    visual_data: { 
                        shape: "rectangle",
                        length: 8,
                        width: 5,
                        area: 40
                    },
                    difficulty: "easy",
                    options: ["13", "26", "40", "45"]
                },
                {
                    id: 7,
                    question: "What is the perimeter of a square with side length 6?",
                    correct_answer: "24",
                    explanation: "Perimeter = 4 × side = 4 × 6 = 24 units",
                    visual_type: "geometry",
                    visual_data: { 
                        shape: "square",
                        side: 6,
                        perimeter: 24
                    },
                    difficulty: "easy",
                    options: ["12", "18", "24", "36"]
                }
            ],
            multiplication: [
                {
                    id: 8,
                    question: "What is 7 × 8?",
                    correct_answer: "56",
                    explanation: "7 × 8 = 56. You can think of it as 7 groups of 8",
                    visual_type: "multiplication",
                    visual_data: { 
                        multiplier: 7,
                        multiplicand: 8,
                        product: 56
                    },
                    difficulty: "medium",
                    options: ["54", "56", "58", "64"]
                },
                {
                    id: 9,
                    question: "What is 9 × 6?",
                    correct_answer: "54",
                    explanation: "9 × 6 = 54. You can think of it as 9 groups of 6",
                    visual_type: "multiplication",
                    visual_data: { 
                        multiplier: 9,
                        multiplicand: 6,
                        product: 54
                    },
                    difficulty: "medium",
                    options: ["45", "54", "63", "72"]
                }
            ],
            word_problems: [
                {
                    id: 10,
                    question: "Sarah has 24 stickers. She wants to share them equally among 6 friends. How many stickers does each friend get?",
                    correct_answer: "4",
                    explanation: "24 ÷ 6 = 4. Each friend gets 4 stickers",
                    visual_type: "division",
                    visual_data: { 
                        total: 24,
                        groups: 6,
                        per_group: 4,
                        context: "stickers"
                    },
                    difficulty: "easy",
                    options: ["3", "4", "5", "6"]
                },
                {
                    id: 11,
                    question: "A pizza is cut into 8 equal slices. Tom eats 3 slices. What fraction of the pizza did he eat?",
                    correct_answer: "3/8",
                    explanation: "Tom ate 3 out of 8 slices, which is 3/8 of the pizza",
                    visual_type: "fraction",
                    visual_data: { 
                        total_slices: 8,
                        eaten_slices: 3,
                        fraction: { numerator: 3, denominator: 8 },
                        context: "pizza"
                    },
                    difficulty: "medium",
                    options: ["1/8", "3/8", "5/8", "8/3"]
                }
            ]
        };
    }
    
    getProblemsByType(type) {
        return this.problems[type] || [];
    }
    
    getRandomProblem() {
        const allProblems = Object.values(this.problems).flat();
        return allProblems[Math.floor(Math.random() * allProblems.length)];
    }
    
    getProblemById(id) {
        const allProblems = Object.values(this.problems).flat();
        return allProblems.find(p => p.id === id);
    }
    
    createVisualSolution(problem) {
        const container = document.createElement('div');
        container.className = 'problem-visual-solution';
        
        switch (problem.visual_type) {
            case 'division':
                return this.createDivisionVisual(problem, container);
            case 'fraction':
                return this.createFractionVisual(problem, container);
            case 'geometry':
                return this.createGeometryVisual(problem, container);
            case 'multiplication':
                return this.createMultiplicationVisual(problem, container);
            default:
                return this.createGenericVisual(problem, container);
        }
    }
    
    createDivisionVisual(problem, container) {
        const data = problem.visual_data;
        container.innerHTML = `
            <div class="visual-solution">
                <h3>🎯 Visual Solution: ${problem.question}</h3>
                <div class="division-visual">
                    <div class="division-setup">
                        <div class="division-box">
                            <div class="divisor">${data.divisor}</div>
                            <div class="dividend">${data.dividend}</div>
                        </div>
                        <p>We want to divide ${data.dividend} by ${data.divisor}</p>
                    </div>
                    
                    <div class="division-steps">
                        <div class="step">
                            <h4>Step 1: How many times does ${data.divisor} go into ${data.dividend}?</h4>
                            <div class="counting-visual">
                                ${this.createCountingVisual(data.divisor, data.dividend)}
                            </div>
                        </div>
                        
                        <div class="step">
                            <h4>Step 2: Check your answer</h4>
                            <div class="verification">
                                <p>${data.divisor} × ${data.quotient} = ${data.divisor * data.quotient}</p>
                                <p>✅ ${data.dividend} ÷ ${data.divisor} = ${data.quotient}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        return container;
    }
    
    createFractionVisual(problem, container) {
        const data = problem.visual_data;
        container.innerHTML = `
            <div class="visual-solution">
                <h3>🎯 Visual Solution: ${problem.question}</h3>
                <div class="fraction-visual">
                    <div class="fraction-problem">
                        <div class="fraction-display">
                            <div class="fraction">${this.createFractionHTML(data.fractions[0])}</div>
                            <span class="operator">+</span>
                            <div class="fraction">${this.createFractionHTML(data.fractions[1])}</div>
                        </div>
                    </div>
                    
                    <div class="fraction-steps">
                        <div class="step">
                            <h4>Step 1: Find common denominator</h4>
                            <p>LCM of ${data.fractions[0].denominator} and ${data.fractions[1].denominator} = ${this.findLCM(data.fractions[0].denominator, data.fractions[1].denominator)}</p>
                        </div>
                        
                        <div class="step">
                            <h4>Step 2: Convert fractions</h4>
                            <div class="fraction-display">
                                <div class="fraction">${this.createFractionHTML({numerator: data.fractions[0].numerator * (this.findLCM(data.fractions[0].denominator, data.fractions[1].denominator) / data.fractions[0].denominator), denominator: this.findLCM(data.fractions[0].denominator, data.fractions[1].denominator)})}</div>
                                <span class="operator">+</span>
                                <div class="fraction">${this.createFractionHTML({numerator: data.fractions[1].numerator * (this.findLCM(data.fractions[0].denominator, data.fractions[1].denominator) / data.fractions[1].denominator), denominator: this.findLCM(data.fractions[0].denominator, data.fractions[1].denominator)})}</div>
                            </div>
                        </div>
                        
                        <div class="step">
                            <h4>Final Answer</h4>
                            <div class="fraction-display">
                                <div class="fraction large">${this.createFractionHTML(data.result)}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        return container;
    }
    
    createGeometryVisual(problem, container) {
        const data = problem.visual_data;
        container.innerHTML = `
            <div class="visual-solution">
                <h3>🎯 Visual Solution: ${problem.question}</h3>
                <div class="geometry-visual">
                    <canvas id="geometry-canvas-${problem.id}" width="300" height="200"></canvas>
                    <div class="geometry-explanation">
                        ${this.getGeometryExplanation(data)}
                    </div>
                </div>
            </div>
        `;
        
        // Draw the shape
        setTimeout(() => {
            this.drawGeometryShape(problem.id, data);
        }, 100);
        
        return container;
    }
    
    createMultiplicationVisual(problem, container) {
        const data = problem.visual_data;
        container.innerHTML = `
            <div class="visual-solution">
                <h3>🎯 Visual Solution: ${problem.question}</h3>
                <div class="multiplication-visual">
                    <div class="multiplication-problem">
                        <h4>${data.multiplier} × ${data.multiplicand} = ?</h4>
                    </div>
                    
                    <div class="multiplication-steps">
                        <div class="step">
                            <h4>Step 1: Visualize ${data.multiplier} groups of ${data.multiplicand}</h4>
                            <div class="groups-visual">
                                ${this.createGroupsVisual(data.multiplier, data.multiplicand)}
                            </div>
                        </div>
                        
                        <div class="step">
                            <h4>Step 2: Count all items</h4>
                            <div class="total-count">
                                <p>Total: ${data.product} items</p>
                                <div class="count-visual">
                                    ${this.createCountVisual(data.product)}
                                </div>
                            </div>
                        </div>
                        
                        <div class="step">
                            <h4>Final Answer</h4>
                            <div class="final-answer">
                                <h3>${data.multiplier} × ${data.multiplicand} = ${data.product}</h3>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        return container;
    }
    
    createGenericVisual(problem, container) {
        container.innerHTML = `
            <div class="visual-solution">
                <h3>🎯 Solution: ${problem.question}</h3>
                <div class="generic-visual">
                    <div class="solution-steps">
                        <div class="step">
                            <h4>Answer: ${problem.correct_answer}</h4>
                            <p>${problem.explanation}</p>
                        </div>
                    </div>
                </div>
            </div>
        `;
        return container;
    }
    
    createCountingVisual(divisor, dividend) {
        let visual = '';
        const quotient = Math.floor(dividend / divisor);
        for (let i = 1; i <= quotient; i++) {
            visual += `<span class="count-item">${i}</span>`;
        }
        return `<div class="counting-items">${visual}</div>`;
    }
    
    createFractionHTML(fraction) {
        return `
            <div class="fraction-container">
                <div class="numerator">${fraction.numerator}</div>
                <div class="fraction-line"></div>
                <div class="denominator">${fraction.denominator}</div>
            </div>
        `;
    }
    
    createGroupsVisual(groups, itemsPerGroup) {
        let visual = '';
        for (let i = 0; i < groups; i++) {
            visual += `
                <div class="group">
                    <h5>Group ${i + 1}</h5>
                    <div class="group-items">
                        ${Array(itemsPerGroup).fill().map(() => '<span class="item">●</span>').join('')}
                    </div>
                </div>
            `;
        }
        return `<div class="groups-container">${visual}</div>`;
    }
    
    createCountVisual(count) {
        let visual = '';
        for (let i = 0; i < Math.min(count, 20); i++) {
            visual += '<span class="count-dot">●</span>';
        }
        if (count > 20) {
            visual += `<span class="count-more">... and ${count - 20} more</span>`;
        }
        return `<div class="count-dots">${visual}</div>`;
    }
    
    getGeometryExplanation(data) {
        switch (data.shape) {
            case 'rectangle':
                return `
                    <div class="explanation">
                        <h4>Rectangle Area Formula</h4>
                        <p>Area = length × width</p>
                        <p>Area = ${data.length} × ${data.width} = ${data.area} square units</p>
                    </div>
                `;
            case 'square':
                return `
                    <div class="explanation">
                        <h4>Square Perimeter Formula</h4>
                        <p>Perimeter = 4 × side</p>
                        <p>Perimeter = 4 × ${data.side} = ${data.perimeter} units</p>
                    </div>
                `;
            default:
                return `<p>${data.explanation || 'See the visual above for the solution.'}</p>`;
        }
    }
    
    drawGeometryShape(problemId, data) {
        const canvas = document.getElementById(`geometry-canvas-${problemId}`);
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        switch (data.shape) {
            case 'rectangle':
                this.drawRectangle(ctx, canvas, data);
                break;
            case 'square':
                this.drawSquare(ctx, canvas, data);
                break;
        }
    }
    
    drawRectangle(ctx, canvas, data) {
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const width = data.length * 15;
        const height = data.width * 15;
        
        // Draw rectangle
        ctx.strokeStyle = '#4ecdc4';
        ctx.lineWidth = 3;
        ctx.strokeRect(centerX - width/2, centerY - height/2, width, height);
        
        // Add labels
        ctx.fillStyle = '#333';
        ctx.font = '16px Arial';
        ctx.fillText('Length', centerX, centerY - height/2 - 10);
        ctx.fillText('Width', centerX - width/2 - 30, centerY);
        ctx.fillText(`${data.length}`, centerX, centerY - height/2 - 30);
        ctx.fillText(`${data.width}`, centerX - width/2 - 50, centerY);
    }
    
    drawSquare(ctx, canvas, data) {
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const size = data.side * 20;
        
        // Draw square
        ctx.strokeStyle = '#ff6b6b';
        ctx.lineWidth = 3;
        ctx.strokeRect(centerX - size/2, centerY - size/2, size, size);
        
        // Add labels
        ctx.fillStyle = '#333';
        ctx.font = '16px Arial';
        ctx.fillText('Side', centerX, centerY - size/2 - 10);
        ctx.fillText(`${data.side}`, centerX, centerY - size/2 - 30);
    }
    
    findLCM(a, b) {
        return (a * b) / this.findGCD(a, b);
    }
    
    findGCD(a, b) {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

// Initialize global math problems
window.mathProblems = new MathProblems();
