/**
 * db.js - IndexedDB Manager & JSON Import Sanitizer
 * AWS CLF-C02 Personal Trainer
 */

const DB_NAME = 'clf_trainer_db';
const DB_VERSION = 1;
const STORE_QUESTIONS = 'questions';
const STORE_USER_STATE = 'user_state';

class DatabaseManager {
  constructor() {
    this.db = null;
    this.initPromise = this.init();
  }

  async init() {
    // Request persistent storage (critical for iOS Safari cache retention)
    if (typeof navigator !== 'undefined' && navigator.storage && navigator.storage.persist) {
      try {
        const isPersisted = await navigator.storage.persist();
        console.log(`[DB] Storage persistence: ${isPersisted ? 'granted' : 'default'}`);
      } catch (err) {
        console.warn('[DB] Storage persistence check failed:', err);
      }
    }

    return new Promise((resolve, reject) => {
      const request = indexedDB.open(DB_NAME, DB_VERSION);

      request.onupgradeneeded = (event) => {
        const db = event.target.result;

        // Store 1: questions - static question contents, bilingual texts, explanations
        if (!db.objectStoreNames.contains(STORE_QUESTIONS)) {
          const qStore = db.createObjectStore(STORE_QUESTIONS, { keyPath: 'id' });
          qStore.createIndex('domain', 'domain', { unique: false });
        }

        // Store 2: user_state - box (0-5), correct_count, error_count, answered_at
        if (!db.objectStoreNames.contains(STORE_USER_STATE)) {
          const sStore = db.createObjectStore(STORE_USER_STATE, { keyPath: 'id' });
          sStore.createIndex('box', 'box', { unique: false });
          sStore.createIndex('answered_at', 'answered_at', { unique: false });
        }
      };

      request.onsuccess = (event) => {
        this.db = event.target.result;
        console.log('[DB] IndexedDB connected successfully');
        resolve(this.db);
      };

      request.onerror = (event) => {
        console.error('[DB] IndexedDB error:', event.target.error);
        reject(event.target.error);
      };
    });
  }

  async ensureDb() {
    if (!this.db) {
      await this.initPromise;
    }
    return this.db;
  }

  // --- QUESTIONS STORE OPERATIONS ---

  /**
   * Upserts questions into `questions` store WITHOUT touching existing `user_state`.
   * If a question is new, initializes user_state to Box 0.
   */
  async upsertQuestions(questionsArray) {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORE_QUESTIONS, STORE_USER_STATE], 'readwrite');
      const qStore = tx.objectStore(STORE_QUESTIONS);
      const sStore = tx.objectStore(STORE_USER_STATE);

      let addedCount = 0;
      let updatedCount = 0;

      tx.oncomplete = () => {
        resolve({ addedCount, updatedCount, totalProcessed: questionsArray.length });
      };

      tx.onerror = (e) => reject(e.target.error);

      questionsArray.forEach((q) => {
        if (!q.id) return;

        // Upsert into questions store
        qStore.put(q);

        // Check if user state exists; if not, initialize Box 0
        const stateReq = sStore.get(q.id);
        stateReq.onsuccess = (e) => {
          const existingState = e.target.result;
          if (!existingState) {
            sStore.put({
              id: q.id,
              box: 0,
              answered_at: 0,
              correct_count: 0,
              error_count: 0
            });
            addedCount++;
          } else {
            updatedCount++;
          }
        };
      });
    });
  }

  async getAllQuestions() {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_QUESTIONS, 'readonly');
      const store = tx.objectStore(STORE_QUESTIONS);
      const req = store.getAll();
      req.onsuccess = () => resolve(req.result || []);
      req.onerror = () => reject(req.error);
    });
  }

  async getQuestion(id) {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_QUESTIONS, 'readonly');
      const store = tx.objectStore(STORE_QUESTIONS);
      const req = store.get(id);
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
  }

  // --- USER STATE STORE OPERATIONS ---

  async getUserState(id) {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_USER_STATE, 'readonly');
      const store = tx.objectStore(STORE_USER_STATE);
      const req = store.get(id);
      req.onsuccess = () => {
        resolve(req.result || {
          id,
          box: 0,
          answered_at: 0,
          correct_count: 0,
          error_count: 0
        });
      };
      req.onerror = () => reject(req.error);
    });
  }

  async getAllUserStates() {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_USER_STATE, 'readonly');
      const store = tx.objectStore(STORE_USER_STATE);
      const req = store.getAll();
      req.onsuccess = () => resolve(req.result || []);
      req.onerror = () => reject(req.error);
    });
  }

  async updateUserState(id, updates) {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_USER_STATE, 'readwrite');
      const store = tx.objectStore(STORE_USER_STATE);
      const getReq = store.get(id);

      getReq.onsuccess = () => {
        const current = getReq.result || {
          id,
          box: 0,
          answered_at: 0,
          correct_count: 0,
          error_count: 0
        };

        const updated = {
          ...current,
          ...updates,
          id // enforce id invariant
        };

        const putReq = store.put(updated);
        putReq.onsuccess = () => resolve(updated);
        putReq.onerror = () => reject(putReq.error);
      };

      getReq.onerror = () => reject(getReq.error);
    });
  }

  /**
   * Bulk merge states (used by sync.js during timestamp merge)
   */
  async bulkUpdateUserStates(statesArray) {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_USER_STATE, 'readwrite');
      const store = tx.objectStore(STORE_USER_STATE);

      tx.oncomplete = () => resolve(statesArray.length);
      tx.onerror = (e) => reject(e.target.error);

      statesArray.forEach((state) => {
        if (state && state.id) {
          store.put(state);
        }
      });
    });
  }

  /**
   * Resets all question boxes to 0 without deleting question text
   */
  async resetAllLeitnerBoxes() {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(STORE_USER_STATE, 'readwrite');
      const store = tx.objectStore(STORE_USER_STATE);
      const req = store.getAll();

      req.onsuccess = () => {
        const states = req.result || [];
        states.forEach((s) => {
          s.box = 0;
          store.put(s);
        });
      };

      tx.oncomplete = () => resolve(true);
      tx.onerror = (e) => reject(e.target.error);
    });
  }

  /**
   * Completely clears both stores
   */
  async purgeDatabase() {
    const db = await this.ensureDb();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORE_QUESTIONS, STORE_USER_STATE], 'readwrite');
      tx.objectStore(STORE_QUESTIONS).clear();
      tx.objectStore(STORE_USER_STATE).clear();
      tx.oncomplete = () => resolve(true);
      tx.onerror = (e) => reject(e.target.error);
    });
  }

  // --- SANITIZER & IMPORTER ---

  /**
   * Auto-healing JSON sanitizer for LLM outputs.
   * Handles markdown code blocks, comments, trailing commas, and incomplete truncated outputs.
   */
  static sanitizeJson(rawText) {
    if (!rawText || typeof rawText !== 'string') {
      return { success: false, data: [], errors: ['Пустой ввод'] };
    }

    let cleaned = rawText.trim();

    // 1. Remove markdown backtick blocks (```json ... ``` or ``` ...)
    cleaned = cleaned.replace(/^```(?:json)?\s*/i, '');
    cleaned = cleaned.replace(/\s*```$/i, '');
    cleaned = cleaned.trim();

    // 2. Find the start of the JSON array '[' or single object '{'
    const firstBracket = cleaned.indexOf('[');
    const firstBrace = cleaned.indexOf('{');

    if (firstBracket === -1 && firstBrace === -1) {
      return { success: false, data: [], errors: ['Не найден начальный символ JSON ("[" или "{")'] };
    }

    // If starts with '{', wrap in array brackets
    if (firstBracket === -1 || (firstBrace !== -1 && firstBrace < firstBracket)) {
      cleaned = '[' + cleaned + ']';
    } else {
      // Slice from the first '['
      cleaned = cleaned.slice(firstBracket);
    }

    // 3. Auto-heal cut off string: if trailing without ']', find last complete object '}'
    cleaned = cleaned.trim();
    if (!cleaned.endsWith(']')) {
      const lastClosingBrace = cleaned.lastIndexOf('}');
      if (lastClosingBrace !== -1) {
        cleaned = cleaned.slice(0, lastClosingBrace + 1) + ']';
      }
    }

    // 4. Remove trailing commas before } or ] (e.g. `,\s*}` -> `}`)
    cleaned = cleaned.replace(/,\s*([}\]])/g, '$1');

    // 5. Try parsing
    let parsedArray = [];
    try {
      const parsed = JSON.parse(cleaned);
      parsedArray = Array.isArray(parsed) ? parsed : [parsed];
    } catch (parseErr) {
      // Secondary emergency recovery: regex-based extraction of valid { ... } chunks
      const recovered = DatabaseManager.extractObjectsRegex(cleaned);
      if (recovered.length > 0) {
        parsedArray = recovered;
      } else {
        return {
          success: false,
          data: [],
          errors: [`Ошибка парсинга JSON: ${parseErr.message}`]
        };
      }
    }

    // 6. Item-by-item schema validation
    const validQuestions = [];
    const validationErrors = [];

    parsedArray.forEach((item, index) => {
      const val = DatabaseManager.validateQuestionItem(item, index);
      if (val.isValid) {
        validQuestions.push(val.sanitizedItem);
      } else {
        validationErrors.push(`Элемент #${index + 1} (${item.id || 'без ID'}): ${val.reason}`);
      }
    });

    return {
      success: validQuestions.length > 0,
      data: validQuestions,
      errors: validationErrors,
      totalParsed: parsedArray.length,
      validCount: validQuestions.length
    };
  }

  /**
   * Fallback regex chunk extractor for broken JSON streams
   */
  static extractObjectsRegex(text) {
    const results = [];
    let depth = 0;
    let startIdx = -1;

    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      if (char === '{') {
        if (depth === 0) startIdx = i;
        depth++;
      } else if (char === '}') {
        depth--;
        if (depth === 0 && startIdx !== -1) {
          const chunk = text.slice(startIdx, i + 1);
          try {
            const cleanChunk = chunk.replace(/,\s*([}\]])/g, '$1');
            results.push(JSON.parse(cleanChunk));
          } catch (e) {
            // skip malformed chunk
          }
          startIdx = -1;
        }
      }
    }
    return results;
  }

  /**
   * Validates and normalizes single question item against schema
   */
  static validateQuestionItem(item, index) {
    if (!item || typeof item !== 'object') {
      return { isValid: false, reason: 'Не является объектом' };
    }

    // Required fields: id, q, options, correct_ids
    const id = item.id || `clf_gen_${Date.now()}_${index}`;

    if (!item.q) {
      return { isValid: false, reason: 'Отсутствует поле "q" (текст вопроса)' };
    }

    // Ensure bilingual question text
    const q = typeof item.q === 'string'
      ? { en: item.q, ru: item.q }
      : {
          en: item.q.en || item.q.ru || 'Missing question text',
          ru: item.q.ru || item.q.en || 'Отсутствует текст вопроса'
        };

    if (!Array.isArray(item.options) || item.options.length < 2) {
      return { isValid: false, reason: 'Поле "options" должно быть массивом минимум из 2 вариантов' };
    }

    if (!Array.isArray(item.correct_ids) || item.correct_ids.length === 0) {
      return { isValid: false, reason: 'Поле "correct_ids" должно быть непустым массивом' };
    }

    // Normalize options
    const normalizedOptions = item.options.map((opt, optIdx) => {
      const optId = opt.id || `opt_${String.fromCharCode(97 + optIdx)}`;
      const optText = typeof opt.text === 'string'
        ? { en: opt.text, ru: opt.text }
        : {
            en: (opt.text && opt.text.en) || (opt.text && opt.text.ru) || `Option ${optId}`,
            ru: (opt.text && opt.text.ru) || (opt.text && opt.text.en) || `Вариант ${optId}`
          };

      let whyInc = null;
      if (opt.why_incorrect) {
        if (typeof opt.why_incorrect === 'string') {
          whyInc = { ru: opt.why_incorrect, en: opt.why_incorrect };
        } else {
          whyInc = {
            ru: opt.why_incorrect.ru || opt.why_incorrect.en || null,
            en: opt.why_incorrect.en || opt.why_incorrect.ru || null
          };
        }
      }

      return {
        id: optId,
        text: optText,
        why_incorrect: whyInc
      };
    });

    // Normalize explanation
    let explanation = {
      summary_ru: 'Разбор ответа готов.',
      summary_en: 'Answer explanation ready.',
      detailed_ru: '',
      detailed_en: ''
    };

    if (item.explanation) {
      if (typeof item.explanation === 'string') {
        explanation.summary_ru = item.explanation;
        explanation.summary_en = item.explanation;
      } else {
        explanation.summary_ru = item.explanation.summary_ru || item.explanation.summary_en || (item.explanation.summary && item.explanation.summary.ru) || '';
        explanation.summary_en = item.explanation.summary_en || item.explanation.summary_ru || (item.explanation.summary && item.explanation.summary.en) || '';
        explanation.detailed_ru = item.explanation.detailed_ru || item.explanation.detailed_en || (item.explanation.detailed && item.explanation.detailed.ru) || '';
        explanation.detailed_en = item.explanation.detailed_en || item.explanation.detailed_ru || (item.explanation.detailed && item.explanation.detailed.en) || '';
      }
    }

    const domain = (item.domain && typeof item.domain === 'string')
      ? item.domain.toLowerCase()
      : 'technology';

    const difficulty = typeof item.difficulty === 'number' ? item.difficulty : 2;
    const services = Array.isArray(item.services) ? item.services : [];

    const sanitizedItem = {
      id,
      domain,
      difficulty,
      q,
      options: normalizedOptions,
      correct_ids: item.correct_ids,
      services,
      explanation
    };

    return { isValid: true, sanitizedItem };
  }
}

// Global instance
window.dbManager = new DatabaseManager();
