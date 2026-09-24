/**
 * sync.js - Google Drive / Google Apps Script Sync Manager
 * AWS CLF-C02 Personal Trainer
 * Timestamp Merge Algorithm + Optimistic UI
 */

const GAS_URL_KEY = 'clf_gas_url';
const LAST_SYNC_KEY = 'clf_last_sync_time';

class SyncManager {
  constructor() {
    this.endpointUrl = localStorage.getItem(GAS_URL_KEY) || '';
    this.isSyncing = false;
    this.dirtyTimer = null;

    // DOM Elements Cache
    this.dom = {
      syncDot: document.getElementById('sync-dot'),
      syncText: document.getElementById('sync-text'),
      btnSyncHeader: document.getElementById('btn-sync'),
      gasInput: document.getElementById('gas-endpoint-input'),
      btnSaveUrl: document.getElementById('btn-save-gas-url'),
      btnTriggerSync: document.getElementById('btn-trigger-sync'),
      statusDetails: document.getElementById('sync-status-details')
    };

    this.bindEvents();
    this.initUI();
  }

  bindEvents() {
    if (this.dom.btnSaveUrl) {
      this.dom.btnSaveUrl.addEventListener('click', () => this.saveEndpointUrl());
    }
    if (this.dom.btnTriggerSync) {
      this.dom.btnTriggerSync.addEventListener('click', () => this.sync());
    }
    if (this.dom.btnSyncHeader) {
      this.dom.btnSyncHeader.addEventListener('click', () => {
        if (!this.endpointUrl) {
          // Switch to settings tab to configure URL
          window.app.switchScreen('screen-stats');
          if (this.dom.gasInput) this.dom.gasInput.focus();
        } else {
          this.sync();
        }
      });
    }
  }

  initUI() {
    if (this.dom.gasInput && this.endpointUrl) {
      this.dom.gasInput.value = this.endpointUrl;
    }
    this.updateStatusUI();
  }

  saveEndpointUrl() {
    const rawUrl = (this.dom.gasInput.value || '').trim();
    if (rawUrl && !rawUrl.startsWith('https://script.google.com/')) {
      alert('Внимание: URL должен начинаться с https://script.google.com/macros/s/.../exec');
      return;
    }

    this.endpointUrl = rawUrl;
    localStorage.setItem(GAS_URL_KEY, rawUrl);
    this.updateStatusUI();

    if (rawUrl) {
      alert('URL успешно сохранен. Запускается проверка синхронизации...');
      this.sync();
    } else {
      alert('URL синхронизации очищен.');
    }
  }

  updateStatusUI(status = 'idle', message = '') {
    if (!this.endpointUrl) {
      if (this.dom.syncDot) this.dom.syncDot.className = 'sync-indicator offline';
      if (this.dom.syncText) this.dom.syncText.textContent = 'Sync off';
      if (this.dom.statusDetails) {
        this.dom.statusDetails.textContent = 'Статус: URL не задан (оффлайн режим)';
        this.dom.statusDetails.style.color = 'var(--text-muted)';
      }
      return;
    }

    const lastSync = localStorage.getItem(LAST_SYNC_KEY);
    const lastSyncFormatted = lastSync ? new Date(parseInt(lastSync, 10)).toLocaleTimeString() : 'никогда';

    switch (status) {
      case 'syncing':
        if (this.dom.syncDot) this.dom.syncDot.className = 'sync-indicator syncing';
        if (this.dom.syncText) this.dom.syncText.textContent = 'Syncing...';
        if (this.dom.statusDetails) {
          this.dom.statusDetails.textContent = 'Статус: Синхронизация с Google Drive в процессе...';
          this.dom.statusDetails.style.color = 'var(--aws-orange)';
        }
        break;

      case 'synced':
        if (this.dom.syncDot) this.dom.syncDot.className = 'sync-indicator synced';
        if (this.dom.syncText) this.dom.syncText.textContent = 'Synced';
        if (this.dom.statusDetails) {
          this.dom.statusDetails.textContent = `Статус: Успешно синхронизировано в ${lastSyncFormatted}`;
          this.dom.statusDetails.style.color = 'var(--success-text)';
        }
        break;

      case 'error':
        if (this.dom.syncDot) this.dom.syncDot.className = 'sync-indicator error';
        if (this.dom.syncText) this.dom.syncText.textContent = 'Sync err';
        if (this.dom.statusDetails) {
          this.dom.statusDetails.textContent = `Ошибка: ${message || 'Не удалось связаться с Google Apps Script'}`;
          this.dom.statusDetails.style.color = 'var(--error-text)';
        }
        break;

      default:
        if (this.dom.syncDot) this.dom.syncDot.className = 'sync-indicator synced';
        if (this.dom.syncText) this.dom.syncText.textContent = 'Sync';
        if (this.dom.statusDetails) {
          this.dom.statusDetails.textContent = `Статус: Готов к синхронизации (последняя: ${lastSyncFormatted})`;
          this.dom.statusDetails.style.color = 'var(--text-secondary)';
        }
    }
  }

  /**
   * Called whenever user state changes locally to queue background sync
   */
  markStateDirty() {
    if (!this.endpointUrl) return;

    if (this.dirtyTimer) clearTimeout(this.dirtyTimer);
    // Debounce background sync: sync after 4 seconds of inactivity
    this.dirtyTimer = setTimeout(() => {
      this.sync({ background: true });
    }, 4000);
  }

  /**
   * Main Timestamp Merge Synchronization Flow
   */
  async sync(options = { background: false }) {
    if (!this.endpointUrl) {
      if (!options.background) {
        alert('Пожалуйста, введите URL скрипта Google Apps Script в настройках.');
      }
      return;
    }

    if (this.isSyncing) return;
    this.isSyncing = true;
    this.updateStatusUI('syncing');

    try {
      // 1. Fetch remote data (GET)
      const getResponse = await fetch(this.endpointUrl, {
        method: 'GET',
        redirect: 'follow',
        headers: { 'Accept': 'application/json' }
      });

      if (!getResponse.ok) {
        throw new Error(`HTTP ${getResponse.status} on GET: ${getResponse.statusText}`);
      }

      const rawRemoteText = await getResponse.text();
      let remotePayload = {};
      try {
        remotePayload = JSON.parse(rawRemoteText) || {};
      } catch (e) {
        console.warn('[Sync] Empty or unparsed remote payload, starting fresh');
      }

      const remoteStates = Array.isArray(remotePayload.user_states) ? remotePayload.user_states : [];
      const remoteMap = {};
      remoteStates.forEach(s => { if (s && s.id) remoteMap[s.id] = s; });

      // 2. Fetch local user states
      const localStates = await window.dbManager.getAllUserStates();
      const localMap = {};
      localStates.forEach(s => { if (s && s.id) localMap[s.id] = s; });

      // 3. Perform Timestamp Merge
      const allIds = new Set([...Object.keys(localMap), ...Object.keys(remoteMap)]);
      const mergedStates = [];
      let localUpdatesNeeded = [];

      allIds.forEach(id => {
        const local = localMap[id];
        const remote = remoteMap[id];

        if (local && remote) {
          const localTime = local.answered_at || 0;
          const remoteTime = remote.answered_at || 0;

          if (remoteTime > localTime) {
            mergedStates.push(remote);
            localUpdatesNeeded.push(remote);
          } else {
            mergedStates.push(local);
          }
        } else if (local && !remote) {
          mergedStates.push(local);
        } else if (!local && remote) {
          mergedStates.push(remote);
          localUpdatesNeeded.push(remote);
        }
      });

      // 4. Update local IndexedDB with fresher remote records
      if (localUpdatesNeeded.length > 0) {
        await window.dbManager.bulkUpdateUserStates(localUpdatesNeeded);
      }

      // 5. POST merged payload back to Google Apps Script
      // CRITICAL: Content-Type: 'text/plain;charset=utf-8' prevents preflight CORS OPTIONS failure
      const postPayload = {
        updated_at: Date.now(),
        client_version: 'CLF-C02-v1',
        user_states: mergedStates
      };

      const postResponse = await fetch(this.endpointUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'text/plain;charset=utf-8'
        },
        body: JSON.stringify(postPayload),
        redirect: 'follow'
      });

      if (!postResponse.ok) {
        throw new Error(`HTTP ${postResponse.status} on POST`);
      }

      const postResult = await postResponse.json();
      if (postResult.error) {
        throw new Error(postResult.error);
      }

      localStorage.setItem(LAST_SYNC_KEY, Date.now().toString());
      this.updateStatusUI('synced');

      // Refresh stats screen and quiz pool if needed
      if (window.app) {
        await window.app.updateProgressStats();
      }

    } catch (err) {
      console.error('[Sync] Synchronization failed:', err);
      this.updateStatusUI('error', err.message);
    } finally {
      this.isSyncing = false;
    }
  }
}

window.SyncManager = SyncManager;
