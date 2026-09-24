/**
 * leitner.js - Leitner Spaced Repetition Engine (Boxes 0-5)
 * AWS CLF-C02 Personal Trainer
 */

class LeitnerEngine {
  /**
   * Weights for choosing questions based on box level.
   * Lower boxes (0 and 1) have dramatically higher probability of appearing.
   */
  static BOX_WEIGHTS = {
    0: 12.0, // High priority (unlearned / recent mistakes)
    1: 7.0,  // Fragile knowledge
    2: 3.5,  // Developing retention
    3: 1.8,  // Moderate retention
    4: 1.0,  // Good retention
    5: 0.5   // Mastered (infrequent review)
  };

  /**
   * Updates state after user answers a question.
   * @param {Object} currentState - { id, box, answered_at, correct_count, error_count }
   * @param {boolean} isCorrect - whether user got all correct_ids
   * @returns {Object} { newState, oldBox, newBox, delta }
   */
  static processAnswer(currentState, isCorrect) {
    const oldBox = currentState.box || 0;
    let newBox;
    let delta = 0;

    const now = Date.now();
    let correctCount = currentState.correct_count || 0;
    let errorCount = currentState.error_count || 0;

    if (isCorrect) {
      newBox = Math.min(5, oldBox + 1);
      delta = newBox - oldBox;
      correctCount++;
    } else {
      newBox = 0; // Reset directly to Box 0 on error
      delta = 0 - oldBox;
      errorCount++;
    }

    const newState = {
      ...currentState,
      box: newBox,
      answered_at: now,
      correct_count: correctCount,
      error_count: errorCount
    };

    return {
      newState,
      oldBox,
      newBox,
      delta
    };
  }

  /**
   * Weighted random selection of the next question from available pool.
   * Prioritizes:
   * 1. Low Leitner boxes (0 and 1)
   * 2. High error rates
   * 3. Avoids immediate consecutive repeat if pool > 1
   */
  static pickNextQuestion(allQuestions, userStatesMap, lastQuestionId = null) {
    if (!allQuestions || allQuestions.length === 0) return null;
    if (allQuestions.length === 1) return allQuestions[0];

    // Filter out last question if possible to prevent immediate repeat
    const candidates = allQuestions.filter(q => q.id !== lastQuestionId);
    const pool = candidates.length > 0 ? candidates : allQuestions;

    // Compute weights
    const weightedPool = pool.map(q => {
      const state = userStatesMap[q.id] || { box: 0, correct_count: 0, error_count: 0 };
      const box = state.box !== undefined ? state.box : 0;
      let baseWeight = LeitnerEngine.BOX_WEIGHTS[box] || 1.0;

      // Extra weight for questions with high error history
      if (state.error_count > state.correct_count) {
        baseWeight *= 1.5;
      }

      // Bonus weight for questions never answered yet
      if (!state.answered_at) {
        baseWeight *= 1.3;
      }

      return { question: q, weight: baseWeight };
    });

    const totalWeight = weightedPool.reduce((sum, item) => sum + item.weight, 0);
    let randomThreshold = Math.random() * totalWeight;

    for (const item of weightedPool) {
      if (randomThreshold <= item.weight) {
        return item.question;
      }
      randomThreshold -= item.weight;
    }

    return weightedPool[0].question;
  }

  /**
   * Computes summary metrics across all questions
   */
  static computeStatistics(allQuestions, userStates) {
    const statesMap = {};
    (userStates || []).forEach(s => { statesMap[s.id] = s; });

    const totalQuestions = allQuestions.length;
    const boxCounts = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };

    let totalCorrectAnswers = 0;
    let totalErrorAnswers = 0;

    let seenQuestionsCount = 0;
    const domainBreakdown = {
      cloud_concepts: { name: 'Cloud Concepts (24%)', total: 0, mastered: 0, learning: 0, weak: 0, ok: 0, n: 0 },
      security: { name: 'Security & Compliance (30%)', total: 0, mastered: 0, learning: 0, weak: 0, ok: 0, n: 0 },
      technology: { name: 'Technology & Services (34%)', total: 0, mastered: 0, learning: 0, weak: 0, ok: 0, n: 0 },
      billing: { name: 'Billing & Pricing (12%)', total: 0, mastered: 0, learning: 0, weak: 0, ok: 0, n: 0 }
    };

    allQuestions.forEach(q => {
      const st = statesMap[q.id];
      const box = (st && st.box !== undefined) ? st.box : 0;
      boxCounts[box] = (boxCounts[box] || 0) + 1;

      const dom = q.domain || 'technology';
      if (!domainBreakdown[dom]) {
        domainBreakdown[dom] = { name: dom, total: 0, mastered: 0, learning: 0, weak: 0, ok: 0, n: 0 };
      }
      domainBreakdown[dom].total++;

      if (st) {
        const correct = st.correct_count || 0;
        const err = st.error_count || 0;
        const totalAns = correct + err;
        totalCorrectAnswers += correct;
        totalErrorAnswers += err;

        if (totalAns > 0 || st.answered_at > 0 || box > 0) {
          seenQuestionsCount++;
        }

        domainBreakdown[dom].ok += correct;
        domainBreakdown[dom].n += totalAns;

        if (box >= 4) {
          domainBreakdown[dom].mastered++;
        } else if (box >= 1) {
          domainBreakdown[dom].learning++;
        } else if (totalAns > 0) {
          domainBreakdown[dom].weak++;
        }
      }
    });

    const totalAnswers = totalCorrectAnswers + totalErrorAnswers;
    const accuracy = totalAnswers > 0 ? Math.round((totalCorrectAnswers / totalAnswers) * 100) : 0;
    const mastered = (boxCounts[4] || 0) + (boxCounts[5] || 0);
    const inProgress = totalQuestions - mastered;

    return {
      totalQuestions,
      seenQuestionsCount,
      totalAttempts: totalAnswers,
      mastered,
      inProgress,
      accuracy,
      boxCounts,
      domainBreakdown
    };
  }
}

window.LeitnerEngine = LeitnerEngine;
