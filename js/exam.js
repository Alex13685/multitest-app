/**
 * exam.js - AWS CLF-C02 Exam Simulator (65 Questions / 90 Minutes)
 * Scaled Score 100-1000 (Passing: 700) + sessionStorage crash recovery
 */

const EXAM_SESSION_KEY = 'clf_active_exam_session';
const EXAM_TOTAL_QUESTIONS = 65;
const EXAM_DURATION_SECONDS = 90 * 60; // 90 minutes = 5400 seconds
const PASSING_SCORE = 700;

class ExamSimulator {
  constructor() {
    this.session = null;
    this.timerInterval = null;

    // DOM Elements Cache
    this.dom = {
      welcomeView: document.getElementById('exam-welcome'),
      activeContainer: document.getElementById('exam-active-container'),
      resultsContainer: document.getElementById('exam-results-container'),
      dbCount: document.getElementById('exam-db-count'),
      btnStart: document.getElementById('btn-start-exam'),
      timerDisplay: document.getElementById('timer-display'),
      examTimerBox: document.getElementById('exam-timer'),
      progressCounter: document.getElementById('exam-progress-counter'),
      examMap: document.getElementById('exam-map'),
      questionDomain: document.getElementById('exam-question-domain'),
      questionText: document.getElementById('exam-question-text'),
      questionHint: document.getElementById('exam-question-hint'),
      optionsContainer: document.getElementById('exam-options-container'),
      btnPrev: document.getElementById('btn-exam-prev'),
      btnNext: document.getElementById('btn-exam-next'),
      btnFinishEarly: document.getElementById('btn-finish-exam-early'),
      resultScore: document.getElementById('exam-result-score'),
      resultStatus: document.getElementById('exam-result-status'),
      domainBreakdown: document.getElementById('exam-domain-breakdown'),
      btnRestart: document.getElementById('btn-restart-exam')
    };

    this.bindEvents();
    this.checkExistingSession();
  }

  bindEvents() {
    this.dom.btnStart.addEventListener('click', () => this.startNewExam());
    this.dom.btnPrev.addEventListener('click', () => this.navigateQuestion(-1));
    this.dom.btnNext.addEventListener('click', () => this.navigateQuestion(1));
    this.dom.btnFinishEarly.addEventListener('click', () => this.confirmFinishEarly());
    this.dom.btnRestart.addEventListener('click', () => this.resetExamToWelcome());
  }

  async updateAvailableCount() {
    const all = await window.dbManager.getAllQuestions();
    if (this.dom.dbCount) {
      this.dom.dbCount.textContent = all.length;
    }
  }

  checkExistingSession() {
    try {
      const saved = sessionStorage.getItem(EXAM_SESSION_KEY);
      if (saved) {
        this.session = JSON.parse(saved);
        if (this.session && this.session.questions && !this.session.isFinished) {
          console.log('[Exam] Resuming active exam from sessionStorage');
          this.resumeExam();
        }
      }
    } catch (e) {
      console.warn('[Exam] Error loading session:', e);
    }
  }

  saveSession() {
    if (this.session) {
      try {
        sessionStorage.setItem(EXAM_SESSION_KEY, JSON.stringify(this.session));
      } catch (e) {
        console.warn('[Exam] Storage save error:', e);
      }
    }
  }

  clearSession() {
    this.session = null;
    sessionStorage.removeItem(EXAM_SESSION_KEY);
  }

  async startNewExam() {
    const allQuestions = await window.dbManager.getAllQuestions();
    if (!allQuestions || allQuestions.length === 0) {
      alert('В базе нет вопросов! Сначала импортируйте вопросы во вкладке "Импорт".');
      return;
    }

    const examQuestions = this.selectExamQuestions(allQuestions);

    this.session = {
      questions: examQuestions,
      answers: {}, // questionId -> array of selected optionIds
      currentIndex: 0,
      timeRemaining: EXAM_DURATION_SECONDS,
      startTime: Date.now(),
      isFinished: false
    };

    this.saveSession();
    this.resumeExam();
  }

  /**
   * Distributes questions matching the official AWS CLF-C02 domain blueprint weights
   */
  selectExamQuestions(allQuestions) {
    const targetTotal = Math.min(EXAM_TOTAL_QUESTIONS, allQuestions.length);

    // Group by domain
    const domains = {
      cloud_concepts: allQuestions.filter(q => q.domain === 'cloud_concepts'),
      security: allQuestions.filter(q => q.domain === 'security'),
      technology: allQuestions.filter(q => q.domain === 'technology'),
      billing: allQuestions.filter(q => q.domain === 'billing')
    };

    // If pool is small (< 65), just shuffle all available
    if (allQuestions.length <= EXAM_TOTAL_QUESTIONS) {
      return QuizEngine.shuffleArray(allQuestions);
    }

    // Blueprint targets: Cloud 24%, Security 30%, Tech 34%, Billing 12%
    const targets = {
      cloud_concepts: Math.round(targetTotal * 0.24), // ~16
      security: Math.round(targetTotal * 0.30),       // ~20
      technology: Math.round(targetTotal * 0.34),     // ~22
      billing: Math.round(targetTotal * 0.12)        // ~8
    };

    const selected = [];
    Object.keys(targets).forEach(domKey => {
      const pool = QuizEngine.shuffleArray(domains[domKey] || []);
      const count = Math.min(targets[domKey], pool.length);
      selected.push(...pool.slice(0, count));
    });

    // Fill remaining up to targetTotal if any domain was short
    if (selected.length < targetTotal) {
      const selectedIds = new Set(selected.map(q => q.id));
      const remaining = allQuestions.filter(q => !selectedIds.has(q.id));
      const shuffledRemaining = QuizEngine.shuffleArray(remaining);
      selected.push(...shuffledRemaining.slice(0, targetTotal - selected.length));
    }

    return QuizEngine.shuffleArray(selected);
  }

  resumeExam() {
    this.dom.welcomeView.style.display = 'none';
    this.dom.resultsContainer.style.display = 'none';
    this.dom.activeContainer.style.display = 'flex';

    this.startTimer();
    this.renderQuestionMap();
    this.renderCurrentQuestion();
  }

  startTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);

    this.updateTimerDisplay();

    this.timerInterval = setInterval(() => {
      if (!this.session || this.session.isFinished) {
        clearInterval(this.timerInterval);
        return;
      }

      this.session.timeRemaining--;
      this.updateTimerDisplay();

      if (this.session.timeRemaining <= 0) {
        clearInterval(this.timerInterval);
        this.finishExam();
      }

      // Periodically persist timer
      if (this.session.timeRemaining % 10 === 0) {
        this.saveSession();
      }
    }, 1000);
  }

  updateTimerDisplay() {
    if (!this.session) return;
    const remaining = Math.max(0, this.session.timeRemaining);
    const mins = Math.floor(remaining / 60);
    const secs = remaining % 60;
    this.dom.timerDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

    if (remaining < 300) { // < 5 minutes
      this.dom.examTimerBox.classList.add('urgent');
    } else {
      this.dom.examTimerBox.classList.remove('urgent');
    }
  }

  renderQuestionMap() {
    if (!this.session) return;
    this.dom.examMap.innerHTML = '';

    this.session.questions.forEach((q, index) => {
      const btn = document.createElement('button');
      btn.className = 'exam-map-btn';
      btn.textContent = index + 1;
      
      const isAnswered = this.session.answers[q.id] && this.session.answers[q.id].length > 0;
      if (isAnswered) btn.classList.add('answered');
      if (index === this.session.currentIndex) btn.classList.add('current');

      btn.addEventListener('click', () => {
        this.session.currentIndex = index;
        this.saveSession();
        this.renderQuestionMap();
        this.renderCurrentQuestion();
      });

      this.dom.examMap.appendChild(btn);
    });
  }

  renderCurrentQuestion() {
    if (!this.session) return;

    const q = this.session.questions[this.session.currentIndex];
    const total = this.session.questions.length;
    const lang = window.appLang || 'ru';
    const isMulti = q.correct_ids.length > 1;

    // Header progress
    this.dom.progressCounter.textContent = lang === 'ru'
      ? `Вопрос ${this.session.currentIndex + 1} из ${total}`
      : `Question ${this.session.currentIndex + 1} of ${total}`;

    // Domain & texts
    this.dom.questionDomain.textContent = (q.domain || '').toUpperCase();
    this.dom.questionText.textContent = q.q[lang] || q.q.ru || q.q.en || '';

    if (isMulti) {
      this.dom.questionHint.textContent = lang === 'ru'
        ? `⚠️ Выберите ${q.correct_ids.length} варианта`
        : `⚠️ Select ${q.correct_ids.length} options`;
    } else {
      this.dom.questionHint.textContent = lang === 'ru'
        ? 'ℹ️ Выберите 1 вариант'
        : 'ℹ️ Select 1 option';
    }

    // Prev / Next button state
    this.dom.btnPrev.disabled = this.session.currentIndex === 0;
    this.dom.btnNext.textContent = this.session.currentIndex === total - 1
      ? (lang === 'ru' ? 'Завершить экзамен ✔' : 'Finish Exam ✔')
      : (lang === 'ru' ? 'Вперед ➔' : 'Next ➔');

    // Selected answers for this question
    const currentSelections = new Set(this.session.answers[q.id] || []);

    // Render options
    this.dom.optionsContainer.innerHTML = '';
    q.options.forEach((opt, idx) => {
      const optEl = document.createElement('div');
      optEl.className = `option-item ${isMulti ? 'is-checkbox' : 'is-radio'}`;
      if (currentSelections.has(opt.id)) optEl.classList.add('selected');

      const optText = opt.text[lang] || opt.text.ru || opt.text.en || '';

      optEl.innerHTML = `
        <div class="option-indicator">${String.fromCharCode(65 + idx)}</div>
        <div class="option-text-wrap">
          <div class="option-text">${optText}</div>
        </div>
      `;

      optEl.addEventListener('click', () => {
        if (isMulti) {
          if (currentSelections.has(opt.id)) {
            currentSelections.delete(opt.id);
          } else {
            if (currentSelections.size < q.correct_ids.length) {
              currentSelections.add(opt.id);
            }
          }
        } else {
          currentSelections.clear();
          currentSelections.add(opt.id);
        }

        this.session.answers[q.id] = Array.from(currentSelections);
        this.saveSession();
        this.renderQuestionMap();
        this.renderCurrentQuestion();
      });

      this.dom.optionsContainer.appendChild(optEl);
    });
  }

  navigateQuestion(delta) {
    if (!this.session) return;
    const newIdx = this.session.currentIndex + delta;
    const total = this.session.questions.length;

    if (newIdx >= total) {
      this.confirmFinishEarly();
      return;
    }

    if (newIdx >= 0 && newIdx < total) {
      this.session.currentIndex = newIdx;
      this.saveSession();
      this.renderQuestionMap();
      this.renderCurrentQuestion();
    }
  }

  confirmFinishEarly() {
    if (!this.session) return;
    const answeredCount = Object.keys(this.session.answers).filter(k => this.session.answers[k].length > 0).length;
    const total = this.session.questions.length;

    const lang = window.appLang || 'ru';
    const message = lang === 'ru'
      ? `Вы ответили на ${answeredCount} из ${total} вопросов. Завершить экзамен и рассчитать балл?`
      : `You answered ${answeredCount} of ${total} questions. Finish exam and calculate score?`;

    if (confirm(message)) {
      this.finishExam();
    }
  }

  finishExam() {
    if (!this.session) return;
    if (this.timerInterval) clearInterval(this.timerInterval);

    this.session.isFinished = true;
    const total = this.session.questions.length;
    let correctCount = 0;

    const domainStats = {
      cloud_concepts: { total: 0, correct: 0 },
      security: { total: 0, correct: 0 },
      technology: { total: 0, correct: 0 },
      billing: { total: 0, correct: 0 }
    };

    this.session.questions.forEach((q) => {
      const dom = q.domain || 'technology';
      if (!domainStats[dom]) domainStats[dom] = { total: 0, correct: 0 };
      domainStats[dom].total++;

      const selected = new Set(this.session.answers[q.id] || []);
      const correctSet = new Set(q.correct_ids);

      let isCorrect = selected.size === correctSet.size;
      if (isCorrect) {
        for (const id of selected) {
          if (!correctSet.has(id)) {
            isCorrect = false;
            break;
          }
        }
      }

      if (isCorrect) {
        correctCount++;
        domainStats[dom].correct++;
      }
    });

    // AWS Scaled score: 100 + round((correct / total) * 900)
    const scaledScore = total > 0 ? (100 + Math.round((correctCount / total) * 900)) : 100;
    const isPassed = scaledScore >= PASSING_SCORE;

    this.clearSession();

    // Render results view
    this.dom.activeContainer.style.display = 'none';
    this.dom.resultsContainer.style.display = 'block';

    this.dom.resultScore.textContent = `${scaledScore} / 1000`;
    this.dom.resultScore.style.color = isPassed ? 'var(--success-text)' : 'var(--error-text)';

    this.dom.resultStatus.textContent = isPassed ? 'PASSED / СДАН' : 'FAILED / НЕ СДАН';
    this.dom.resultStatus.className = `badge ${isPassed ? 'badge-box' : ''}`;
    this.dom.resultStatus.style.background = isPassed ? 'var(--success-bg)' : 'var(--error-bg)';
    this.dom.resultStatus.style.borderColor = isPassed ? 'var(--success-border)' : 'var(--error-border)';
    this.dom.resultStatus.style.color = isPassed ? 'var(--success-text)' : 'var(--error-text)';

    // Domain Breakdown HTML
    let domainHtml = `<h4 style="margin-top: 10px; margin-bottom: 6px;">Точность по доменам:</h4>`;
    Object.keys(domainStats).forEach(key => {
      const d = domainStats[key];
      if (d.total > 0) {
        const pct = Math.round((d.correct / d.total) * 100);
        domainHtml += `
          <div style="background: var(--bg-secondary); padding: 8px 12px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); display: flex; justify-content: space-between;">
            <span>${key.toUpperCase().replace('_', ' ')}</span>
            <strong>${d.correct} / ${d.total} (${pct}%)</strong>
          </div>
        `;
      }
    });

    this.dom.domainBreakdown.innerHTML = domainHtml;
  }

  resetExamToWelcome() {
    this.clearSession();
    this.dom.resultsContainer.style.display = 'none';
    this.dom.activeContainer.style.display = 'none';
    this.dom.welcomeView.style.display = 'block';
    this.updateAvailableCount();
  }

  updateTextsOnLangChange() {
    if (this.session && !this.session.isFinished) {
      this.renderCurrentQuestion();
    }
  }
}

window.ExamSimulator = ExamSimulator;
