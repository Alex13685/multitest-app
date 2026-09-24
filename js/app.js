/**
 * app.js - Application Controller & Coordinator
 * AWS CLF-C02 Personal Trainer (PWA)
 */

class AppController {
  constructor() {
    this.currentScreen = 'screen-trainer';
    this.servicesDb = {};
    window.appLang = localStorage.getItem('clf_lang') || 'ru';

    // DOM Elements Cache
    this.dom = {
      navTabs: document.querySelectorAll('.nav-tab'),
      screens: document.querySelectorAll('.screen-view'),
      btnLang: document.getElementById('btn-lang'),
      langEn: document.getElementById('lang-en'),
      langRu: document.getElementById('lang-ru'),
      
      // Bottom Sheet
      sheetBackdrop: document.getElementById('services-backdrop'),
      servicesSheet: document.getElementById('services-sheet'),
      sheetContent: document.getElementById('services-sheet-content'),
      btnCloseSheet: document.getElementById('btn-close-sheet'),
      btnOpenServices: document.getElementById('btn-open-services'),
      
      // Import Section
      importInput: document.getElementById('import-json-input'),
      btnRunImport: document.getElementById('btn-run-import'),
      btnLoadStarter: document.getElementById('btn-load-starter'),
      btnClearLog: document.getElementById('btn-clear-log'),
      importLog: document.getElementById('import-log'),
      btnExportJson: document.getElementById('btn-export-json'),
      btnResetLeitner: document.getElementById('btn-reset-leitner'),
      btnPurgeDb: document.getElementById('btn-purge-db'),

      // Stats Section
      statTotalQ: document.getElementById('stat-total-q'),
      statSeenQ: document.getElementById('stat-seen-q'),
      statTotalAttempts: document.getElementById('stat-total-attempts'),
      statMastered: document.getElementById('stat-mastered'),
      statAccuracy: document.getElementById('stat-accuracy'),
      domainProgressContainer: document.getElementById('domain-progress-container'),
      boxCount0: document.getElementById('box-count-0'),
      boxCount1: document.getElementById('box-count-1'),
      boxCount2: document.getElementById('box-count-2'),
      boxCount3: document.getElementById('box-count-3'),
      boxCount4: document.getElementById('box-count-4'),
      boxCount5: document.getElementById('box-count-5'),

      // Flashcards Section
      flashcardsBox: document.getElementById('flashcard-box'),
      fcName: document.getElementById('fc-name'),
      fcHint: document.getElementById('fc-hint'),
      fcDesc: document.getElementById('fc-desc'),
      fcTrap: document.getElementById('fc-trap'),
      fcGradeContainer: document.getElementById('fc-grade-container'),
      fcCategoryBadge: document.getElementById('fc-category-badge'),
      fcBoxBadge: document.getElementById('fc-box-badge'),
      fcMasteredBadge: document.getElementById('fc-mastered-badge'),
      btnFcKnow: document.getElementById('btn-fc-know'),
      btnFcGrade0: document.getElementById('btn-fc-grade-0'),
      btnFcGrade1: document.getElementById('btn-fc-grade-1'),
      btnFcGrade2: document.getElementById('btn-fc-grade-2')
    };

    this.flashcardsList = [];
    this.flashcardsState = {};
    this.currentFlashcard = null;
    this.isFlashcardRevealed = false;

    this.init();
  }

  async init() {
    this.registerServiceWorker();
    this.bindEvents();
    this.updateLanguageUI();
    await this.loadServicesData();

    // Initialize sub-engines
    window.quizEngine = new window.QuizEngine();
    window.examSimulator = new window.ExamSimulator();
    window.syncManager = new window.SyncManager();

    // Initial check & non-destructive content refresh from starter.json
    const existing = await window.dbManager.getAllQuestions();
    if (existing.length === 0) {
      await this.loadStarterQuestions(true);
    } else {
      try {
        const res = await fetch('./data/starter.json');
        if (res.ok) {
          const starter = await res.json();
          await window.dbManager.upsertQuestions(starter);
        }
      } catch (e) {
        console.warn('[App] Could not auto-refresh starter questions:', e);
      }
      await window.quizEngine.loadQuizPool();
      await window.examSimulator.updateAvailableCount();
      await this.updateProgressStats();
    }

    // Try auto-sync on launch if configured
    if (window.syncManager.endpointUrl) {
      window.syncManager.sync({ background: true });
    }
  }

  registerServiceWorker() {
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js')
          .then(reg => {
            console.log('[PWA] Service Worker registered with scope:', reg.scope);
            // Check for updates on every launch
            reg.update();
            reg.addEventListener('updatefound', () => {
              const newWorker = reg.installing;
              if (newWorker) {
                newWorker.addEventListener('statechange', () => {
                  if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                    console.log('[PWA] New version installed! Reloading...');
                    window.location.reload();
                  }
                });
              }
            });
          })
          .catch(err => console.warn('[PWA] Service Worker registration failed:', err));
      });
    }
  }

  bindEvents() {
    // Nav tabs
    this.dom.navTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const targetScreen = tab.dataset.screen;
        this.switchScreen(targetScreen);
      });
    });

    // Language Toggle
    this.dom.btnLang.addEventListener('click', () => this.toggleLanguage());

    // Services Bottom Sheet
    this.dom.btnOpenServices.addEventListener('click', () => this.openServicesSheet());
    this.dom.btnCloseSheet.addEventListener('click', () => this.closeServicesSheet());
    this.dom.sheetBackdrop.addEventListener('click', () => this.closeServicesSheet());

    // Touch swipe down on bottom sheet
    this.setupSheetSwipeToClose();

    // Flashcard Actions
    if (this.dom.flashcardsBox) {
      this.dom.flashcardsBox.addEventListener('click', () => this.revealFlashcard());
    }
    if (this.dom.btnFcGrade0) {
      this.dom.btnFcGrade0.addEventListener('click', () => this.gradeFlashcard(0));
      this.dom.btnFcGrade1.addEventListener('click', () => this.gradeFlashcard(1));
      this.dom.btnFcGrade2.addEventListener('click', () => this.gradeFlashcard(2));
    }
    if (this.dom.btnFcKnow) {
      this.dom.btnFcKnow.addEventListener('click', () => this.gradeFlashcard(5));
    }

    // Import Actions
    this.dom.btnRunImport.addEventListener('click', () => this.handleImport());
    this.dom.btnLoadStarter.addEventListener('click', () => this.loadStarterQuestions(false));
    this.dom.btnClearLog.addEventListener('click', () => { this.dom.importLog.textContent = 'Лог очищен.'; });
    this.dom.btnExportJson.addEventListener('click', () => this.exportDatabaseToJson());
    this.dom.btnResetLeitner.addEventListener('click', () => this.handleResetLeitner());
    this.dom.btnPurgeDb.addEventListener('click', () => this.handlePurgeDatabase());
  }

  switchScreen(screenId) {
    this.currentScreen = screenId;

    this.dom.navTabs.forEach(tab => {
      if (tab.dataset.screen === screenId) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });

    this.dom.screens.forEach(screen => {
      if (screen.id === screenId) {
        screen.classList.add('active');
      } else {
        screen.classList.remove('active');
      }
    });

    // Refresh specific screen contents
    if (screenId === 'screen-stats') {
      this.updateProgressStats();
    } else if (screenId === 'screen-exam') {
      window.examSimulator.updateAvailableCount();
    } else if (screenId === 'screen-cards') {
      this.renderNextFlashcard();
    }
  }

  // --- LANGUAGE SWITCHING ---

  toggleLanguage() {
    window.appLang = window.appLang === 'ru' ? 'en' : 'ru';
    localStorage.setItem('clf_lang', window.appLang);
    this.updateLanguageUI();

    // Update active question without reloading state
    if (window.quizEngine) {
      window.quizEngine.updateTextsOnLangChange(window.appLang);
    }
    if (window.examSimulator) {
      window.examSimulator.updateTextsOnLangChange();
    }
  }

  updateLanguageUI() {
    const isRu = window.appLang === 'ru';
    if (isRu) {
      this.dom.langRu.classList.add('active-lang');
      this.dom.langEn.classList.remove('active-lang');
    } else {
      this.dom.langEn.classList.add('active-lang');
      this.dom.langRu.classList.remove('active-lang');
    }

    // Static text translations across nav tabs
    const i18n = {
      nav_trainer: isRu ? 'Тренажер' : 'Practice',
      nav_exam: isRu ? 'Экзамен' : 'Exam',
      nav_import: isRu ? 'Импорт' : 'Import',
      nav_stats: isRu ? 'Прогресс' : 'Stats',
      btn_submit: isRu ? 'Ответить' : 'Check Answer',
      btn_next: isRu ? 'Следующий вопрос ➔' : 'Next Question ➔',
      btn_services: isRu ? 'Сервисы AWS' : 'AWS Services'
    };

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.dataset.i18n;
      if (i18n[key]) {
        el.textContent = i18n[key];
      }
    });
  }

  // --- AWS SERVICES DICTIONARY & BOTTOM SHEET ---

  async loadServicesData() {
    try {
      const res = await fetch('./data/services_info.json');
      if (res.ok) {
        this.servicesDb = await res.json();
      }
    } catch (e) {
      console.warn('[App] Could not load services_info.json:', e);
    }
  }

  openServicesSheet() {
    const q = window.quizEngine ? window.quizEngine.currentQuestion : null;
    if (!q) return;

    const lang = window.appLang || 'ru';
    this.dom.sheetContent.innerHTML = '';

    // Collect all unique service keys from q.services
    const serviceKeys = new Set(Array.isArray(q.services) ? q.services : []);

    // Also smartly scan option texts to auto-detect any AWS service mentioned in options
    const knownKeys = Object.keys(this.servicesDb);
    if (Array.isArray(q.options)) {
      q.options.forEach(opt => {
        const optText = ((opt.text && (opt.text.en || opt.text.ru)) || '').toLowerCase();
        knownKeys.forEach(k => {
          const sName = (this.servicesDb[k].name || '').toLowerCase();
          // Match if option text contains service name or key
          if (optText.includes(k.replace(/_/g, ' ')) || (sName && optText.includes(sName.replace(/amazon |aws /g, '')))) {
            serviceKeys.add(k);
          }
        });
      });
    }

    if (serviceKeys.size === 0) {
      this.dom.sheetContent.innerHTML = `
        <div style="color: var(--text-secondary); text-align: center; padding: 20px;">
          ${lang === 'ru' ? 'В этом вопросе нет привязанных сервисов AWS.' : 'No AWS services tagged in this question.'}
        </div>
      `;
    } else {
      serviceKeys.forEach(serviceKey => {
        const info = this.servicesDb[serviceKey] || {
          name: serviceKey.toUpperCase().replace(/_/g, ' '),
          category: 'AWS Service',
          desc_ru: 'Подробная карточка находится в процессе наполнения.',
          desc_en: 'Detailed service description coming soon.',
          key_points_ru: [],
          key_points_en: []
        };

        const card = document.createElement('div');
        card.className = 'service-card';

        const desc = lang === 'ru' ? info.desc_ru : (info.desc_en || info.desc_ru);
        const points = lang === 'ru' ? (info.key_points_ru || []) : (info.key_points_en || info.key_points_ru || []);

        let pointsHtml = '';
        if (points.length > 0) {
          pointsHtml = `<ul class="service-bullets">${points.map(p => `<li>${p}</li>`).join('')}</ul>`;
        }

        card.innerHTML = `
          <div class="service-card-header">
            <div class="service-name">${info.name}</div>
            <div class="service-category">${info.category}</div>
          </div>
          <div class="service-desc">${desc}</div>
          ${pointsHtml}
        `;

        this.dom.sheetContent.appendChild(card);
      });
    }

    this.dom.sheetBackdrop.classList.add('open');
    this.dom.servicesSheet.classList.add('open');
  }

  closeServicesSheet() {
    this.dom.sheetBackdrop.classList.remove('open');
    this.dom.servicesSheet.classList.remove('open');
  }

  setupSheetSwipeToClose() {
    let startY = 0;
    let isDraggingHandle = false;
    const handleBar = document.querySelector('.sheet-handle-bar');
    const header = document.querySelector('.sheet-header');

    const handleTouchStart = (e) => {
      startY = e.touches[0].clientY;
      isDraggingHandle = true;
    };

    const handleTouchMove = (e) => {
      if (!isDraggingHandle) return;
      const currentY = e.touches[0].clientY;
      const diffY = currentY - startY;
      // Close only if dragged downwards by more than 50px directly on handle or header
      if (diffY > 50) {
        isDraggingHandle = false;
        this.closeServicesSheet();
      }
    };

    const handleTouchEnd = () => {
      isDraggingHandle = false;
    };

    if (handleBar) {
      handleBar.addEventListener('touchstart', handleTouchStart, { passive: true });
      handleBar.addEventListener('touchmove', handleTouchMove, { passive: true });
      handleBar.addEventListener('touchend', handleTouchEnd, { passive: true });
      // Clicking the handle directly also toggles close
      handleBar.addEventListener('click', () => this.closeServicesSheet());
    }

    if (header) {
      header.addEventListener('touchstart', handleTouchStart, { passive: true });
      header.addEventListener('touchmove', handleTouchMove, { passive: true });
      header.addEventListener('touchend', handleTouchEnd, { passive: true });
    }
  }

  // --- IMPORT & MANAGEMENT ---

  async handleImport() {
    const raw = this.dom.importInput.value;
    if (!raw.trim()) {
      alert('Поле импорта пустое. Вставьте JSON-массив с вопросами.');
      return;
    }

    this.dom.importLog.textContent = 'Обработка и санитайзинг входящего JSON...';

    const result = window.DatabaseManager.sanitizeJson(raw);

    let logText = `--- РЕЗУЛЬТАТ ОБРАБОТКИ ---\n`;
    logText += `Успешно распознано валидных вопросов: ${result.validCount}\n`;

    if (result.errors && result.errors.length > 0) {
      logText += `Предупреждения / Ошибки (${result.errors.length}):\n`;
      result.errors.forEach(err => { logText += `  • ${err}\n`; });
    }

    if (result.validCount > 0) {
      const upsertResult = await window.dbManager.upsertQuestions(result.data);
      logText += `\nБаза обновлена:\n`;
      logText += `  - Новых добавлено: ${upsertResult.addedCount}\n`;
      logText += `  - Существующих обновлено: ${upsertResult.updatedCount}\n`;
      logText += `  (Пользовательская статистика и ящики Лейтнера сохранены!)\n`;

      this.dom.importInput.value = '';
      await window.quizEngine.loadQuizPool();
      await window.examSimulator.updateAvailableCount();
      await this.updateProgressStats();
    } else {
      logText += `\n❌ Ни один вопрос не прошел валидацию. Проверьте формат.`;
    }

    this.dom.importLog.textContent = logText;
  }

  async loadStarterQuestions(isAuto = false) {
    try {
      this.dom.importLog.textContent = 'Загрузка стартового пакета data/starter.json...';
      const res = await fetch('./data/starter.json');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const starterData = await res.json();

      const upsertResult = await window.dbManager.upsertQuestions(starterData);
      this.dom.importLog.textContent = `Стартовый набор успешно загружен (${starterData.length} шт).\nДобавлено: ${upsertResult.addedCount}, Обновлено: ${upsertResult.updatedCount}`;

      await window.quizEngine.loadQuizPool();
      await window.examSimulator.updateAvailableCount();
      await this.updateProgressStats();

      if (!isAuto) {
        alert(`Успешно загружено ${starterData.length} стартовых вопросов!`);
        this.switchScreen('screen-trainer');
      }
    } catch (e) {
      this.dom.importLog.textContent = `Ошибка загрузки starter.json: ${e.message}`;
    }
  }

  async exportDatabaseToJson() {
    const questions = await window.dbManager.getAllQuestions();
    if (questions.length === 0) {
      alert('База пуста, нечего экспортировать.');
      return;
    }

    const jsonString = JSON.stringify(questions, null, 2);
    const blob = new Blob([jsonString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = `aws_clf_c02_questions_${Date.now()}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  async handleResetLeitner() {
    if (confirm('Сбросить все вопросы в Box 0? Тексты вопросов сохранятся, но прогресс начнется заново.')) {
      await window.dbManager.resetAllLeitnerBoxes();
      await window.quizEngine.loadQuizPool();
      await this.updateProgressStats();
      if (window.syncManager) window.syncManager.markStateDirty();
      alert('Все ящики Лейтнера успешно сброшены в Box 0.');
    }
  }

  async handlePurgeDatabase() {
    if (confirm('ВНИМАНИЕ! Это действие полностью очистит базу вопросов и всю статистику. Продолжить?')) {
      await window.dbManager.purgeDatabase();
      await window.quizEngine.loadQuizPool();
      await window.examSimulator.updateAvailableCount();
      await this.updateProgressStats();
      alert('База данных полностью очищена.');
    }
  }

  // --- FLASHCARDS CONTROLLER ---

  async loadFlashcardsData() {
    try {
      const res = await fetch('./data/flashcards.json');
      if (res.ok) {
        this.flashcardsList = await res.json();
      }
      const saved = localStorage.getItem('clf_flashcards_state');
      if (saved) {
        this.flashcardsState = JSON.parse(saved);
      }
    } catch (e) {
      console.warn('[App] Flashcards load error:', e);
    }
  }

  saveFlashcardsState() {
    localStorage.setItem('clf_flashcards_state', JSON.stringify(this.flashcardsState));
  }

  renderNextFlashcard() {
    if (!this.flashcardsList || this.flashcardsList.length === 0) return;

    // Filter cards not yet in box 5
    const candidates = this.flashcardsList.filter(c => {
      const s = this.flashcardsState[c.id] || { b: 0 };
      return s.b < 5;
    });

    const pool = candidates.length > 0 ? candidates : this.flashcardsList;
    const nextCard = pool[Math.floor(Math.random() * pool.length)];

    this.currentFlashcard = nextCard;
    this.isFlashcardRevealed = false;

    const cardState = this.flashcardsState[nextCard.id] || { b: 0 };
    const masteredCount = this.flashcardsList.filter(c => (this.flashcardsState[c.id] && this.flashcardsState[c.id].b >= 5)).length;

    if (this.dom.fcName) this.dom.fcName.textContent = nextCard.name;
    if (this.dom.fcHint) this.dom.fcHint.style.display = 'block';
    if (this.dom.fcDesc) this.dom.fcDesc.style.display = 'none';
    if (this.dom.fcTrap) this.dom.fcTrap.style.display = 'none';
    if (this.dom.fcGradeContainer) this.dom.fcGradeContainer.style.display = 'none';

    if (this.dom.fcCategoryBadge) this.dom.fcCategoryBadge.textContent = (nextCard.cat || 'AWS').toUpperCase();
    if (this.dom.fcBoxBadge) {
      this.dom.fcBoxBadge.textContent = `Box ${cardState.b || 0}`;
      this.dom.fcBoxBadge.setAttribute('data-box', cardState.b || 0);
    }
    if (this.dom.fcMasteredBadge) {
      this.dom.fcMasteredBadge.textContent = `💡 ${masteredCount} / ${this.flashcardsList.length} освоено`;
    }
  }

  revealFlashcard() {
    if (this.isFlashcardRevealed || !this.currentFlashcard) return;
    this.isFlashcardRevealed = true;

    const c = this.currentFlashcard;
    if (this.dom.fcHint) this.dom.fcHint.style.display = 'none';
    if (this.dom.fcDesc) {
      this.dom.fcDesc.textContent = c.desc;
      this.dom.fcDesc.style.display = 'block';
    }
    if (this.dom.fcTrap && c.trap) {
      this.dom.fcTrap.innerHTML = `<strong>⚠️ ЛОВУШКА ЭКЗАМЕНА:</strong> ${c.trap}`;
      this.dom.fcTrap.style.display = 'block';
    }
    if (this.dom.fcGradeContainer) {
      this.dom.fcGradeContainer.style.display = 'grid';
    }
  }

  gradeFlashcard(grade) {
    if (!this.currentFlashcard) return;
    const id = this.currentFlashcard.id;
    const current = this.flashcardsState[id] || { b: 0, n: 0 };
    current.n++;

    if (grade === 5) {
      current.b = 5;
    } else if (grade === 2) {
      current.b = Math.min(5, (current.b || 0) + 1);
    } else if (grade === 1) {
      current.b = Math.max(0, current.b || 0);
    } else {
      current.b = 0;
    }

    this.flashcardsState[id] = current;
    this.saveFlashcardsState();
    this.renderNextFlashcard();
  }

  // --- STATS VIEW UPDATER ---

  async updateProgressStats() {
    const questions = await window.dbManager.getAllQuestions();
    const states = await window.dbManager.getAllUserStates();

    const stats = window.LeitnerEngine.computeStatistics(questions, states);

    if (this.dom.statTotalQ) this.dom.statTotalQ.textContent = stats.totalQuestions;
    if (this.dom.statSeenQ) {
      const pct = stats.totalQuestions > 0 ? Math.round((stats.seenQuestionsCount / stats.totalQuestions) * 100) : 0;
      this.dom.statSeenQ.textContent = `${stats.seenQuestionsCount} / ${stats.totalQuestions} (${pct}%)`;
    }
    if (this.dom.statTotalAttempts) this.dom.statTotalAttempts.textContent = stats.totalAttempts;
    if (this.dom.statMastered) {
      const pct = stats.totalQuestions > 0 ? Math.round((stats.mastered / stats.totalQuestions) * 100) : 0;
      this.dom.statMastered.textContent = `${stats.mastered} (${pct}%)`;
    }
    if (this.dom.statAccuracy) this.dom.statAccuracy.textContent = `${stats.accuracy}%`;

    // Render domain breakdown stacked progress bars
    if (this.dom.domainProgressContainer && stats.domainBreakdown) {
      let html = '';
      Object.keys(stats.domainBreakdown).forEach(k => {
        const d = stats.domainBreakdown[k];
        if (d.total > 0) {
          const masteredPct = Math.round((d.mastered / d.total) * 100);
          const learningPct = Math.round((d.learning / d.total) * 100);
          const weakPct = Math.round((d.weak / d.total) * 100);
          html += `
            <div class="domain-progress-row">
              <div class="domain-name" title="${d.name}">${d.name}</div>
              <div class="domain-bar-track">
                <i class="bar-segment-mastered" style="width: ${masteredPct}%;"></i>
                <i class="bar-segment-learning" style="width: ${learningPct}%;"></i>
                <i class="bar-segment-weak" style="width: ${weakPct}%;"></i>
              </div>
              <div class="domain-stats-pct">${d.mastered}/${d.total} (${masteredPct}%)</div>
            </div>
          `;
        }
      });
      this.dom.domainProgressContainer.innerHTML = html;
    }

    for (let box = 0; box <= 5; box++) {
      const boxEl = this.dom[`boxCount${box}`];
      if (boxEl) {
        boxEl.textContent = stats.boxCounts[box] || 0;
      }
    }
  }
}

// Instantiate on load
document.addEventListener('DOMContentLoaded', () => {
  window.app = new AppController();
});
