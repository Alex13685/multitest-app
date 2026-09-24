/**
 * engine.js - Quiz Rendering & Interactive Engine
 * AWS CLF-C02 Personal Trainer
 */

class QuizEngine {
  constructor() {
    this.currentQuestion = null;
    this.currentUserState = null;
    this.shuffledOptions = [];
    this.selectedOptionIds = new Set();
    this.isAnswered = false;
    this.allQuestions = [];
    this.userStatesMap = {};

    this.activeMode = 'all';

    // DOM Elements Cache
    this.dom = {
      domainBadge: document.getElementById('badge-domain'),
      boxBadge: document.getElementById('badge-box'),
      statsBadge: document.getElementById('badge-stats'),
      btnServices: document.getElementById('btn-open-services'),
      questionText: document.getElementById('question-text'),
      questionHint: document.getElementById('question-hint'),
      optionsContainer: document.getElementById('options-container'),
      btnSubmit: document.getElementById('btn-submit-answer'),
      btnKnow100: document.getElementById('btn-know-100'),
      btnNext: document.getElementById('btn-next-question'),
      modeChips: document.querySelectorAll('.mode-chip'),
      explanationContainer: document.getElementById('explanation-container'),
      explanationHeader: document.getElementById('explanation-header'),
      leitnerFeedback: document.getElementById('leitner-feedback'),
      explanationSummary: document.getElementById('explanation-summary'),
      explanationDetailed: document.getElementById('explanation-detailed')
    };

    this.bindEvents();
  }

  bindEvents() {
    this.dom.btnSubmit.addEventListener('click', () => this.submitAnswer());
    this.dom.btnNext.addEventListener('click', () => this.loadNextQuestion());

    if (this.dom.btnKnow100) {
      this.dom.btnKnow100.addEventListener('click', () => this.markKnow100());
    }

    if (this.dom.modeChips) {
      this.dom.modeChips.forEach(chip => {
        chip.addEventListener('click', () => {
          this.setMode(chip.dataset.mode);
        });
      });
    }
  }

  setMode(mode) {
    this.activeMode = mode || 'all';
    this.dom.modeChips.forEach(c => {
      c.classList.toggle('active', c.dataset.mode === this.activeMode);
    });
    this.loadNextQuestion();
  }

  async markKnow100() {
    if (!this.currentQuestion) return;
    const q = this.currentQuestion;

    this.currentUserState.box = 5;
    this.currentUserState.answered_at = Date.now();
    this.currentUserState.correct_count = (this.currentUserState.correct_count || 0) + 1;
    this.userStatesMap[q.id] = this.currentUserState;

    await window.dbManager.updateUserState(q.id, {
      box: 5,
      answered_at: Date.now(),
      correct_count: this.currentUserState.correct_count
    });

    if (window.syncManager) window.syncManager.markStateDirty();
    if (window.app) window.app.updateProgressStats();

    await this.loadNextQuestion();
  }

  /**
   * Fisher-Yates In-Place Shuffle (Returns a copy)
   */
  static shuffleArray(array) {
    const copy = [...array];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  /**
   * Initializes quiz with full question pool
   */
  async loadQuizPool() {
    this.allQuestions = await window.dbManager.getAllQuestions();
    const states = await window.dbManager.getAllUserStates();
    this.userStatesMap = {};
    states.forEach(s => { this.userStatesMap[s.id] = s; });

    if (this.allQuestions.length === 0) {
      this.renderEmptyState();
      return;
    }

    await this.loadNextQuestion();
  }

  renderEmptyState() {
    const lang = window.appLang || 'ru';
    this.dom.questionText.innerHTML = lang === 'ru'
      ? 'База вопросов пуста.<br><span style="font-size: 14px; color: var(--text-secondary);">Перейдите на вкладку <strong>Импорт</strong> и нажмите «Загрузить базу (600 вопросов)».</span>'
      : 'Question database is empty.<br><span style="font-size: 14px; color: var(--text-secondary);">Go to the <strong>Import</strong> tab and click "Load database (600 questions)".</span>';
    
    this.dom.optionsContainer.innerHTML = '';
    this.dom.questionHint.textContent = '';
    this.dom.btnSubmit.style.display = 'none';
    this.dom.btnNext.style.display = 'none';
    this.dom.explanationContainer.style.display = 'none';
    this.dom.btnServices.style.display = 'none';
  }

  /**
   * Picks and renders the next question via LeitnerEngine
   */
  async loadNextQuestion() {
    let pool = this.allQuestions;
    if (this.activeMode === 'weak') {
      const weakList = this.allQuestions.filter(q => {
        const s = this.userStatesMap[q.id];
        return !s || !s.answered_at || s.error_count > s.correct_count || s.box <= 1;
      });
      if (weakList.length > 0) pool = weakList;
    } else if (this.activeMode === 'traps') {
      const trapList = this.allQuestions.filter(q => q.trap);
      if (trapList.length > 0) pool = trapList;
    } else if (this.activeMode === 'hard') {
      const hardList = this.allQuestions.filter(q => q.difficulty === 3);
      if (hardList.length > 0) pool = hardList;
    }

    const lastId = this.currentQuestion ? this.currentQuestion.id : null;
    const nextQ = window.LeitnerEngine.pickNextQuestion(pool, this.userStatesMap, lastId);

    if (!nextQ) {
      this.renderEmptyState();
      return;
    }

    this.currentQuestion = nextQ;
    this.currentUserState = await window.dbManager.getUserState(nextQ.id);
    this.userStatesMap[nextQ.id] = this.currentUserState;

    this.isAnswered = false;
    this.selectedOptionIds.clear();

    // Fisher-Yates shuffle of options
    this.shuffledOptions = QuizEngine.shuffleArray(nextQ.options);

    this.renderQuestion();
  }

  /**
   * Renders the current question and options
   */
  renderQuestion() {
    if (!this.currentQuestion) return;

    const q = this.currentQuestion;
    const state = this.currentUserState;
    const lang = window.appLang || 'ru';
    const isMulti = q.correct_ids.length > 1;

    // Reset UI visibility
    this.dom.explanationContainer.style.display = 'none';
    this.dom.btnSubmit.style.display = 'flex';
    this.dom.btnSubmit.disabled = true;
    this.dom.btnNext.style.display = 'none';

    // Meta bar
    this.dom.domainBadge.textContent = this.formatDomain(q.domain, lang);
    this.dom.boxBadge.textContent = `Box ${state.box || 0}`;
    this.dom.boxBadge.setAttribute('data-box', state.box || 0);

    const totalAns = (state.correct_count || 0) + (state.error_count || 0);
    this.dom.statsBadge.textContent = `🔥 ${state.correct_count || 0} / ${totalAns}`;

    // Services toggle button
    if (q.services && q.services.length > 0) {
      this.dom.btnServices.style.display = 'inline-flex';
      this.dom.btnServices.querySelector('span:last-child').textContent =
        lang === 'ru' ? `Сервисы AWS (${q.services.length})` : `AWS Services (${q.services.length})`;
    } else {
      this.dom.btnServices.style.display = 'none';
    }

    // Question text
    const qText = q.q[lang] || q.q.ru || q.q.en || '';
    this.dom.questionText.textContent = qText;

    // Hint text
    if (isMulti) {
      this.dom.questionHint.textContent = lang === 'ru'
        ? `⚠️ Выберите ${q.correct_ids.length} правильных ответа`
        : `⚠️ Select ${q.correct_ids.length} correct answers`;
    } else {
      this.dom.questionHint.textContent = lang === 'ru'
        ? 'ℹ️ Выберите 1 правильный ответ'
        : 'ℹ️ Select 1 correct answer';
    }

    // Render Options
    this.dom.optionsContainer.innerHTML = '';
    this.shuffledOptions.forEach((opt) => {
      const optEl = document.createElement('div');
      optEl.className = `option-item ${isMulti ? 'is-checkbox' : 'is-radio'}`;
      optEl.dataset.optId = opt.id;

      const optText = opt.text[lang] || opt.text.ru || opt.text.en || '';

      optEl.innerHTML = `
        <div class="option-indicator">${this.getOptionLetter(opt.id)}</div>
        <div class="option-text-wrap">
          <div class="option-text">${this.escapeHtml(optText)}</div>
          <div class="option-why-incorrect" style="display: none;"></div>
        </div>
      `;

      optEl.addEventListener('click', () => this.handleOptionClick(opt.id));
      this.dom.optionsContainer.appendChild(optEl);
    });
  }

  handleOptionClick(optId) {
    if (this.isAnswered) return;

    const q = this.currentQuestion;
    const isMulti = q.correct_ids.length > 1;

    if (isMulti) {
      if (this.selectedOptionIds.has(optId)) {
        this.selectedOptionIds.delete(optId);
      } else {
        if (this.selectedOptionIds.size < q.correct_ids.length) {
          this.selectedOptionIds.add(optId);
        } else {
          // If already reached limit, replace oldest or ignore
          return;
        }
      }
    } else {
      this.selectedOptionIds.clear();
      this.selectedOptionIds.add(optId);
    }

    this.updateOptionsSelectionState();

    // Enable submit button only if exact required number of options selected
    this.dom.btnSubmit.disabled = this.selectedOptionIds.size !== q.correct_ids.length;
  }

  updateOptionsSelectionState() {
    const items = this.dom.optionsContainer.querySelectorAll('.option-item');
    items.forEach(el => {
      const id = el.dataset.optId;
      if (this.selectedOptionIds.has(id)) {
        el.classList.add('selected');
      } else {
        el.classList.remove('selected');
      }
    });
  }

  /**
   * User submits an answer
   */
  async submitAnswer() {
    if (this.isAnswered || !this.currentQuestion) return;

    const q = this.currentQuestion;
    if (this.selectedOptionIds.size !== q.correct_ids.length) return;

    this.isAnswered = true;
    this.dom.btnSubmit.style.display = 'none';
    this.dom.btnNext.style.display = 'flex';

    // Verify answer
    const correctSet = new Set(q.correct_ids);
    let isCorrect = this.selectedOptionIds.size === correctSet.size;
    if (isCorrect) {
      for (const id of this.selectedOptionIds) {
        if (!correctSet.has(id)) {
          isCorrect = false;
          break;
        }
      }
    }

    // Process Leitner Box update
    const leitnerResult = window.LeitnerEngine.processAnswer(this.currentUserState, isCorrect);
    this.currentUserState = leitnerResult.newState;
    this.userStatesMap[q.id] = leitnerResult.newState;

    // Save to IndexedDB
    await window.dbManager.updateUserState(q.id, {
      box: leitnerResult.newBox,
      answered_at: leitnerResult.newState.answered_at,
      correct_count: leitnerResult.newState.correct_count,
      error_count: leitnerResult.newState.error_count
    });

    // Notify sync manager that local state changed
    if (window.syncManager) {
      window.syncManager.markStateDirty();
    }

    // Render Answer State & Bonso breakdown
    this.renderAnswerState(isCorrect, leitnerResult);
  }

  renderAnswerState(isCorrect, leitnerResult) {
    const q = this.currentQuestion;
    const lang = window.appLang || 'ru';
    const correctSet = new Set(q.correct_ids);

    // Style options list
    const items = this.dom.optionsContainer.querySelectorAll('.option-item');
    items.forEach(el => {
      el.classList.add('locked');
      const optId = el.dataset.optId;
      const isSelected = this.selectedOptionIds.has(optId);
      const isActuallyCorrect = correctSet.has(optId);

      const whyIncorrectEl = el.querySelector('.option-why-incorrect');
      const optData = this.shuffledOptions.find(o => o.id === optId);

      if (isActuallyCorrect) {
        el.classList.add('is-correct');
      } else if (isSelected && !isActuallyCorrect) {
        el.classList.add('is-incorrect');
      }

      // Display why_incorrect for wrong options
      if (!isActuallyCorrect && optData && optData.why_incorrect) {
        const whyText = optData.why_incorrect[lang] || optData.why_incorrect.ru || optData.why_incorrect.en;
        if (whyText) {
          whyIncorrectEl.textContent = `❌ ${whyText}`;
          whyIncorrectEl.style.display = 'block';
        }
      }
    });

    // Render Explanation Card (Bonso style)
    this.dom.explanationContainer.style.display = 'flex';

    if (isCorrect) {
      this.dom.explanationHeader.className = 'explanation-header success';
      this.dom.explanationHeader.innerHTML = lang === 'ru'
        ? '<span>🎉</span> <span>Правильно!</span>'
        : '<span>🎉</span> <span>Correct!</span>';
      
      this.dom.leitnerFeedback.style.borderColor = 'var(--success-border)';
      this.dom.leitnerFeedback.innerHTML = `
        <span style="color: var(--success-text);">Box ${leitnerResult.oldBox} ➔ Box ${leitnerResult.newBox} (+1)</span>
      `;
    } else {
      this.dom.explanationHeader.className = 'explanation-header error';
      this.dom.explanationHeader.innerHTML = lang === 'ru'
        ? '<span>❌</span> <span>Неверно!</span>'
        : '<span>❌</span> <span>Incorrect!</span>';
      
      this.dom.leitnerFeedback.style.borderColor = 'var(--error-border)';
      this.dom.leitnerFeedback.innerHTML = `
        <span style="color: var(--error-text);">Сброшен в Box 0 (было Box ${leitnerResult.oldBox})</span>
      `;
    }

    // Explanation Summary & Detailed
    this.updateExplanationTexts(lang);

    // Update meta bar badges
    this.dom.boxBadge.textContent = `Box ${leitnerResult.newBox}`;
    this.dom.boxBadge.setAttribute('data-box', leitnerResult.newBox);
    const totalAns = this.currentUserState.correct_count + this.currentUserState.error_count;
    this.dom.statsBadge.textContent = `🔥 ${this.currentUserState.correct_count} / ${totalAns}`;

    // Scroll to explanation smoothly if on mobile
    if (window.innerWidth < 768) {
      this.dom.explanationContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  updateExplanationTexts(lang) {
    const q = this.currentQuestion;
    if (!q || !q.explanation) return;

    const summaryText = q.explanation[`summary_${lang}`] ||
      (q.explanation.summary && (q.explanation.summary[lang] || q.explanation.summary.ru || q.explanation.summary.en)) ||
      q.explanation.summary_ru || q.explanation.summary_en || '';

    const detailedText = q.explanation[`detailed_${lang}`] ||
      (q.explanation.detailed && (q.explanation.detailed[lang] || q.explanation.detailed.ru || q.explanation.detailed.en)) ||
      q.explanation.detailed_ru || q.explanation.detailed_en || '';

    this.dom.explanationSummary.innerHTML = `<strong>💡 Разбор:</strong> ${this.escapeHtml(summaryText)}`;
    this.dom.explanationDetailed.innerHTML = this.escapeHtml(detailedText);
  }

  /**
   * On-the-fly language update without losing current state or selections
   */
  updateTextsOnLangChange(newLang) {
    if (!this.currentQuestion) return;

    const q = this.currentQuestion;

    // Update domain badge
    this.dom.domainBadge.textContent = this.formatDomain(q.domain, newLang);

    // Update services button label
    if (q.services && q.services.length > 0) {
      this.dom.btnServices.querySelector('span:last-child').textContent =
        newLang === 'ru' ? `Сервисы AWS (${q.services.length})` : `AWS Services (${q.services.length})`;
    }

    // Update Question text
    const qText = q.q[newLang] || q.q.ru || q.q.en || '';
    this.dom.questionText.textContent = qText;

    // Update Hint text
    const isMulti = q.correct_ids.length > 1;
    if (isMulti) {
      this.dom.questionHint.textContent = newLang === 'ru'
        ? `⚠️ Выберите ${q.correct_ids.length} правильных ответа`
        : `⚠️ Select ${q.correct_ids.length} correct answers`;
    } else {
      this.dom.questionHint.textContent = newLang === 'ru'
        ? 'ℹ️ Выберите 1 правильный ответ'
        : 'ℹ️ Select 1 correct answer';
    }

    // Update Options text and why_incorrect without re-creating DOM
    const items = this.dom.optionsContainer.querySelectorAll('.option-item');
    items.forEach(el => {
      const optId = el.dataset.optId;
      const optData = this.shuffledOptions.find(o => o.id === optId);
      if (optData) {
        const textEl = el.querySelector('.option-text');
        textEl.textContent = optData.text[newLang] || optData.text.ru || optData.text.en || '';

        const whyEl = el.querySelector('.option-why-incorrect');
        if (optData.why_incorrect && whyEl.style.display !== 'none') {
          const whyText = optData.why_incorrect[newLang] || optData.why_incorrect.ru || optData.why_incorrect.en;
          if (whyText) {
            whyEl.textContent = `❌ ${whyText}`;
          }
        }
      }
    });

    // Update Bonso explanations if already displayed
    if (this.isAnswered) {
      this.updateExplanationTexts(newLang);
    }
  }

  formatDomain(domain, lang) {
    const map = {
      cloud_concepts: { en: 'Cloud Concepts', ru: 'Концепции облака' },
      security: { en: 'Security & Compliance', ru: 'Безопасность и комплаенс' },
      technology: { en: 'Technology & Services', ru: 'Технологии и сервисы' },
      billing: { en: 'Billing & Pricing', ru: 'Биллинг и ценообразование' }
    };
    const key = (domain || '').toLowerCase();
    if (map[key]) {
      return map[key][lang] || map[key].en;
    }
    return domain || 'General';
  }

  getOptionLetter(id) {
    const match = id.match(/opt_([a-z0-9]+)/i);
    if (match) return match[1].toUpperCase();
    return '•';
  }

  escapeHtml(text) {
    if (!text) return '';
    return text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }
}

window.QuizEngine = QuizEngine;
