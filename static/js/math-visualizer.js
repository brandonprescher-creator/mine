// BADASS MATH VISUALIZER - VISUAL STEP-BY-STEP SOLUTIONS!

class MathVisualizer {
    constructor() {
        this.canvas = null;
        this.ctx = null;
        this.currentProblem = null;
        this.stepIndex = 0;
        this.animationSpeed = 1000;
    }
    
    // Create visual division example
    createDivisionVisual(problem, container) {
        const visual = document.createElement('div');
        visual.className = 'math-visual';
        visual.innerHTML = `
            <div class="visual-header">
                <h3>🎯 Visual Solution: ${problem}</h3>
            </div>
            <div class="visual-steps" id="division-steps"></div>
            <div class="visual-controls">
                <button onclick="mathVisualizer.previousStep()">⬅️ Previous</button>
                <button onclick="mathVisualizer.nextStep()">Next ➡️</button>
                <button onclick="mathVisualizer.resetVisual()">🔄 Reset</button>
            </div>
        `;
        
        container.appendChild(visual);
        this.currentProblem = problem;
        this.stepIndex = 0;
        this.showDivisionStep();
    }
    
    showDivisionStep() {
        const stepsContainer = document.getElementById('division-steps');
        if (!stepsContainer) return;
        
        const [dividend, divisor] = this.currentProblem.split(' ÷ ').map(x => parseInt(x));
        const quotient = Math.floor(dividend / divisor);
        const remainder = dividend % divisor;
        
        const steps = [
            {
                title: "Step 1: Set up the problem",
                visual: this.createDivisionSetup(dividend, divisor),
                explanation: `We want to divide ${dividend} by ${divisor}`
            },
            {
                title: "Step 2: Start with the first digit",
                visual: this.createDivisionFirstDigit(dividend, divisor),
                explanation: `How many times does ${divisor} go into ${dividend}?`
            },
            {
                title: "Step 3: Multiply and subtract",
                visual: this.createDivisionMultiply(dividend, divisor, quotient),
                explanation: `${divisor} × ${quotient} = ${divisor * quotient}`
            },
            {
                title: "Step 4: Bring down and repeat",
                visual: this.createDivisionBringDown(dividend, divisor, quotient, remainder),
                explanation: `Bring down the next digit and continue`
            },
            {
                title: "Final Answer",
                visual: this.createDivisionResult(dividend, divisor, quotient, remainder),
                explanation: `${dividend} ÷ ${divisor} = ${quotient}${remainder > 0 ? ` remainder ${remainder}` : ''}`
            }
        ];
        
        if (this.stepIndex < steps.length) {
            const step = steps[this.stepIndex];
            stepsContainer.innerHTML = `
                <div class="step-content">
                    <h4>${step.title}</h4>
                    <div class="step-visual">${step.visual}</div>
                    <div class="step-explanation">${step.explanation}</div>
                </div>
            `;
        }
    }
    
    createDivisionSetup(dividend, divisor) {
        return `
            <div class="division-setup">
                <div class="division-box">
                    <div class="divisor">${divisor}</div>
                    <div class="dividend">${dividend}</div>
                </div>
                <div class="setup-explanation">
                    <p>📝 Write the dividend (${dividend}) inside the division box</p>
                    <p>📝 Write the divisor (${divisor}) outside the box</p>
                </div>
            </div>
        `;
    }
    
    createDivisionFirstDigit(dividend, divisor) {
        const firstDigit = Math.floor(dividend / Math.pow(10, dividend.toString().length - 1));
        return `
            <div class="division-first-digit">
                <div class="division-box">
                    <div class="divisor">${divisor}</div>
                    <div class="dividend">${dividend}</div>
                    <div class="quotient-start">?</div>
                </div>
                <div class="digit-explanation">
                    <p>🔍 Look at the first digit: ${firstDigit}</p>
                    <p>🤔 How many times does ${divisor} go into ${firstDigit}?</p>
                    <div class="counting-visual">
                        ${this.createCountingVisual(divisor, firstDigit)}
                    </div>
                </div>
            </div>
        `;
    }
    
    createCountingVisual(divisor, target) {
        let visual = '';
        for (let i = 1; i <= target; i++) {
            const color = i <= target ? '#4CAF50' : '#f44336';
            visual += `<span class="count-item" style="background: ${color}">${i}</span>`;
        }
        return `<div class="counting-items">${visual}</div>`;
    }
    
    createDivisionMultiply(dividend, divisor, quotient) {
        return `
            <div class="division-multiply">
                <div class="division-box">
                    <div class="divisor">${divisor}</div>
                    <div class="dividend">${dividend}</div>
                    <div class="quotient">${quotient}</div>
                    <div class="multiply-result">${divisor * quotient}</div>
                </div>
                <div class="multiply-explanation">
                    <p>✖️ Multiply: ${divisor} × ${quotient} = ${divisor * quotient}</p>
                    <div class="multiplication-visual">
                        ${this.createMultiplicationVisual(divisor, quotient)}
                    </div>
                </div>
            </div>
        `;
    }
    
    createMultiplicationVisual(a, b) {
        let visual = '<div class="multiplication-grid">';
        for (let i = 0; i < a; i++) {
            for (let j = 0; j < b; j++) {
                visual += '<div class="grid-item">●</div>';
            }
        }
        visual += '</div>';
        visual += `<p>${a} rows × ${b} columns = ${a * b} total</p>`;
        return visual;
    }
    
    createDivisionBringDown(dividend, divisor, quotient, remainder) {
        return `
            <div class="division-bring-down">
                <div class="division-box">
                    <div class="divisor">${divisor}</div>
                    <div class="dividend">${dividend}</div>
                    <div class="quotient">${quotient}</div>
                    <div class="multiply-result">${divisor * quotient}</div>
                    <div class="remainder">${remainder}</div>
                </div>
                <div class="bring-down-explanation">
                    <p>📥 Bring down the next digit</p>
                    <p>🔄 Continue the process</p>
                    ${remainder > 0 ? `<p>📊 Remainder: ${remainder}</p>` : ''}
                </div>
            </div>
        `;
    }
    
    createDivisionResult(dividend, divisor, quotient, remainder) {
        return `
            <div class="division-result">
                <div class="final-answer">
                    <h3>🎉 Final Answer: ${quotient}${remainder > 0 ? ` remainder ${remainder}` : ''}</h3>
                </div>
                <div class="verification">
                    <p>✅ Let's verify: ${divisor} × ${quotient} = ${divisor * quotient}</p>
                    ${remainder > 0 ? `<p>➕ Plus remainder: ${divisor * quotient} + ${remainder} = ${dividend}</p>` : ''}
                    <p>🎯 ${dividend} ÷ ${divisor} = ${quotient}${remainder > 0 ? ` remainder ${remainder}` : ''}</p>
                </div>
                <div class="celebration">
                    <div class="celebration-animation">🎉🎊🎉</div>
                </div>
            </div>
        `;
    }
    
    // Create visual fraction example
    createFractionVisual(problem, container) {
        const visual = document.createElement('div');
        visual.className = 'math-visual';
        visual.innerHTML = `
            <div class="visual-header">
                <h3>🎯 Visual Solution: ${problem}</h3>
            </div>
            <div class="fraction-visual" id="fraction-visual"></div>
            <div class="visual-controls">
                <button onclick="mathVisualizer.animateFraction()">🎬 Animate</button>
                <button onclick="mathVisualizer.resetFraction()">🔄 Reset</button>
            </div>
        `;
        
        container.appendChild(visual);
        this.createFractionSteps(problem);
    }
    
    createFractionSteps(problem) {
        const container = document.getElementById('fraction-visual');
        if (!container) return;
        
        // Parse fraction problem (e.g., "1/2 + 1/4")
        const parts = problem.split(' + ');
        const [num1, den1] = parts[0].split('/').map(x => parseInt(x));
        const [num2, den2] = parts[1].split('/').map(x => parseInt(x));
        
        const lcm = this.findLCM(den1, den2);
        const newNum1 = num1 * (lcm / den1);
        const newNum2 = num2 * (lcm / den2);
        const resultNum = newNum1 + newNum2;
        const resultDen = lcm;
        
        container.innerHTML = `
            <div class="fraction-steps">
                <div class="step">
                    <h4>Step 1: Original Fractions</h4>
                    <div class="fraction-display">
                        <div class="fraction">${this.createFractionHTML(num1, den1)}</div>
                        <span class="operator">+</span>
                        <div class="fraction">${this.createFractionHTML(num2, den2)}</div>
                    </div>
                </div>
                
                <div class="step">
                    <h4>Step 2: Find Common Denominator</h4>
                    <div class="lcm-explanation">
                        <p>LCM of ${den1} and ${den2} = ${lcm}</p>
                        <div class="lcm-visual">${this.createLCMVisual(den1, den2, lcm)}</div>
                    </div>
                </div>
                
                <div class="step">
                    <h4>Step 3: Convert to Common Denominator</h4>
                    <div class="fraction-display">
                        <div class="fraction">${this.createFractionHTML(newNum1, lcm)}</div>
                        <span class="operator">+</span>
                        <div class="fraction">${this.createFractionHTML(newNum2, lcm)}</div>
                    </div>
                </div>
                
                <div class="step">
                    <h4>Step 4: Add the Numerators</h4>
                    <div class="fraction-display">
                        <div class="fraction">${this.createFractionHTML(resultNum, resultDen)}</div>
                    </div>
                </div>
                
                <div class="step">
                    <h4>Final Answer</h4>
                    <div class="final-fraction">
                        <div class="fraction large">${this.createFractionHTML(resultNum, resultDen)}</div>
                        <div class="celebration">🎉</div>
                    </div>
                </div>
            </div>
        `;
    }
    
    createFractionHTML(numerator, denominator) {
        return `
            <div class="fraction-container">
                <div class="numerator">${numerator}</div>
                <div class="fraction-line"></div>
                <div class="denominator">${denominator}</div>
            </div>
        `;
    }
    
    createLCMVisual(a, b, lcm) {
        return `
            <div class="lcm-visual">
                <div class="multiples">
                    <div class="multiples-a">
                        <h5>Multiples of ${a}:</h5>
                        <div class="multiple-list">${this.getMultiples(a, lcm).map(m => `<span class="multiple">${m}</span>`).join('')}</div>
                    </div>
                    <div class="multiples-b">
                        <h5>Multiples of ${b}:</h5>
                        <div class="multiple-list">${this.getMultiples(b, lcm).map(m => `<span class="multiple">${m}</span>`).join('')}</div>
                    </div>
                </div>
                <div class="common-multiple">
                    <p>🎯 First common multiple: <strong>${lcm}</strong></p>
                </div>
            </div>
        `;
    }
    
    getMultiples(num, limit) {
        const multiples = [];
        for (let i = 1; i * num <= limit; i++) {
            multiples.push(i * num);
        }
        return multiples;
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
    
    // Create visual geometry example
    createGeometryVisual(problem, container) {
        const visual = document.createElement('div');
        visual.className = 'math-visual';
        visual.innerHTML = `
            <div class="visual-header">
                <h3>🎯 Visual Solution: ${problem}</h3>
            </div>
            <canvas id="geometry-canvas" width="400" height="300"></canvas>
            <div class="geometry-explanation" id="geometry-explanation"></div>
        `;
        
        container.appendChild(visual);
        this.drawGeometryProblem(problem);
    }
    
    drawGeometryProblem(problem) {
        const canvas = document.getElementById('geometry-canvas');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw different shapes based on problem type
        if (problem.includes('triangle')) {
            this.drawTriangle(ctx, canvas);
        } else if (problem.includes('rectangle')) {
            this.drawRectangle(ctx, canvas);
        } else if (problem.includes('circle')) {
            this.drawCircle(ctx, canvas);
        }
    }
    
    drawTriangle(ctx, canvas) {
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const size = 100;
        
        ctx.beginPath();
        ctx.moveTo(centerX, centerY - size);
        ctx.lineTo(centerX - size, centerY + size);
        ctx.lineTo(centerX + size, centerY + size);
        ctx.closePath();
        ctx.strokeStyle = '#ff6b6b';
        ctx.lineWidth = 3;
        ctx.stroke();
        
        // Add labels
        ctx.fillStyle = '#333';
        ctx.font = '16px Arial';
        ctx.fillText('A', centerX, centerY - size - 10);
        ctx.fillText('B', centerX - size - 20, centerY + size + 5);
        ctx.fillText('C', centerX + size + 5, centerY + size + 5);
    }
    
    drawRectangle(ctx, canvas) {
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const width = 150;
        const height = 100;
        
        ctx.strokeStyle = '#4ecdc4';
        ctx.lineWidth = 3;
        ctx.strokeRect(centerX - width/2, centerY - height/2, width, height);
        
        // Add labels
        ctx.fillStyle = '#333';
        ctx.font = '16px Arial';
        ctx.fillText('Length', centerX, centerY - height/2 - 10);
        ctx.fillText('Width', centerX - width/2 - 30, centerY);
    }
    
    drawCircle(ctx, canvas) {
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = 80;
        
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
        ctx.strokeStyle = '#45b7d1';
        ctx.lineWidth = 3;
        ctx.stroke();
        
        // Draw radius
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(centerX + radius, centerY);
        ctx.strokeStyle = '#feca57';
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Add labels
        ctx.fillStyle = '#333';
        ctx.font = '16px Arial';
        ctx.fillText('r', centerX + radius/2, centerY - 10);
    }
    
    // Navigation methods
    nextStep() {
        this.stepIndex++;
        this.showDivisionStep();
    }
    
    previousStep() {
        if (this.stepIndex > 0) {
            this.stepIndex--;
            this.showDivisionStep();
        }
    }
    
    resetVisual() {
        this.stepIndex = 0;
        this.showDivisionStep();
    }
    
    animateFraction() {
        const fractions = document.querySelectorAll('.fraction-container');
        fractions.forEach((fraction, index) => {
            setTimeout(() => {
                fraction.style.animation = 'bounce 0.5s ease-in-out';
            }, index * 200);
        });
    }
    
    resetFraction() {
        const fractions = document.querySelectorAll('.fraction-container');
        fractions.forEach(fraction => {
            fraction.style.animation = 'none';
        });
    }
}

// Initialize global math visualizer
window.mathVisualizer = new MathVisualizer();
