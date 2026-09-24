# Архитектура и ТЗ: AWS CLF-C02 Personal Trainer (PWA)

## 1. Концепция и цель
Персональное оффлайн-приложение (PWA) для подготовки к сертификации AWS Certified Cloud Practitioner (CLF-C02).
- **Стек:** Чистый Vanilla JS, HTML5, CSS3 (без внешних фреймворков и сборщиков).
- **Автономность:** Полный Offline-First через Service Worker и IndexedDB.
- **Двуязычие (EN ↔ RU):** Переключение языка одной кнопкой на лету без потери состояния. Названия сервисов AWS (Amazon S3, AWS KMS, IAM), параметры инстансов и ключевые термины сохраняются на английском в обоих режимах.
- **Разбор Bonso-style:** Детальное объяснение правильного варианта и отдельное объяснение для каждого неверного.
- **Синхронизация:** Через Google Apps Script прямо в личный Google Диск пользователя (JSON-файл `trainer_state.json`, Timestamp Merge).
- **Интервальное повторение:** Система Лейтнера (ящики 0–5).
- **Симулятор экзамена:** 65 вопросов / 90 минут, пропорции доменов CLF-C02, шкала 100–1000 (проходной 700).

---

## 2. Структура проекта
```text
clf-trainer/
├── index.html            # Единый интерфейс (Тренажер, Экзамен, Импорт, Статистика)
├── manifest.json         # PWA Manifest (dark mode, standalone, icons)
├── sw.js                 # Service Worker (кэширование файлов и оффлайн-режим)
├── css/
│   └── style.css         # Темная тема (GitHub/AWS Dark), min touch-target 50px
├── js/
│   ├── app.js            # Навигация экранов, переключение языка EN/RU, шторка сервисов
│   ├── db.js             # IndexedDB (хранилища questions и user_state, upsert, автолечение JSON)
│   ├── engine.js         # Логика квиза, перемешивание вариантов (Fisher-Yates) по opt_id
│   ├── leitner.js        # Интервальное повторение (ящики 0-5)
│   ├── exam.js           # Режим симулятора (65 вопросов / 90 минут) с sessionStorage
│   └── sync.js           # Синхронизация с Google Apps Script (Timestamp Merge, Optimistic UI)
├── server/
│   └── google_sync.js    # Код для редактора Google Apps Script
├── data/
│   ├── starter.json      # Стартовые вопросы для проверки из коробки
│   └── services_info.json # Справочник сервисов AWS для шторки (BottomSheet)
└── SPEC.md
```

---

## 3. Точный контракт данных вопроса (question_schema.json)

```json
{
  "id": "clf_sec_005",
  "domain": "security",
  "difficulty": 2,
  "q": {
    "en": "Which AWS service enables automated security assessments to improve the security and compliance of applications deployed on Amazon EC2?",
    "ru": "Какой сервис AWS обеспечивает автоматическую оценку безопасности для улучшения защиты и соответствия приложений, развернутых на Amazon EC2?"
  },
  "options": [
    {
      "id": "opt_a",
      "text": { "en": "Amazon Inspector", "ru": "Amazon Inspector" },
      "why_incorrect": null
    },
    {
      "id": "opt_b",
      "text": { "en": "AWS Shield", "ru": "AWS Shield" },
      "why_incorrect": {
        "ru": "AWS Shield предназначен исключительно для защиты от DDoS-атак, а не для поиска уязвимостей в ОС.",
        "en": "AWS Shield is solely designed for DDoS protection, not for scanning operating systems for vulnerabilities."
      }
    }
  ],
  "correct_ids": ["opt_a"],
  "services": ["amazon_inspector", "aws_shield"],
  "explanation": {
    "summary_ru": "Amazon Inspector автоматически сканирует рабочие нагрузки на наличие уязвимостей ПО и непреднамеренного сетевого доступа.",
    "summary_en": "Amazon Inspector automatically scans workloads for software vulnerabilities and unintended network exposure.",
    "detailed_ru": "Amazon Inspector проводит аудит безопасности инстансов Amazon EC2, образов контейнеров в Amazon ECR и функций AWS Lambda на соответствие нормам и наличие уязвимостей (CVE).",
    "detailed_en": "Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure."
  }
}
```

---

## 4. Логика ядра и защита от сбоев

### 4.1. База данных (db.js)
- **Инициализация:** База `clf_trainer_db` (версия 1) с двумя изолированными хранилищами:
  1. `questions` (keyPath: `id`) — хранит только текст, варианты, домен и пояснения.
  2. `user_state` (keyPath: `id`) — хранит `{ id, box, answered_at, correct_count, error_count }`.
- **Защита от сброса кэша iOS Safari:** Вызов `navigator.storage.persist()`.
- **Изолированный Upsert:** Повторный импорт вопроса с тем же `id` обновляет текст в `questions`, но оставляет без изменений ящик Лейтнера и статистику в `user_state`.
- **Лечащий санитайзер импорта (`sanitizeJson`):**
  - Автоматически срезает обёртки \`\`\`json ... \`\`\`.
  - Удаляет висячие запятые перед `}` и `]`.
  - Если строка оборвана на полуслове, находит последнюю закрытую фигурную скобку `}` и дописывает `]`, сохраняя все валидно переданные вопросы.
  - Поэлементная валидация: битые вопросы отсеиваются в лог ошибок, валидные добавляются в базу.

### 4.2. Механика ответов и вариантов (engine.js)
- **Определение типа ввода:**
  - `correct_ids.length === 1` → Радиокнопки (одиночный выбор).
  - `correct_ids.length > 1` → Чекбоксы (множественный выбор). Кнопка «Ответить» активируется только при выборе нужного числа чекбоксов.
- **Безопасное перемешивание (Fisher-Yates):** Варианты перемешиваются перед рендерингом. Проверка ответа идет сравнением выбранных `option.id` с массивом `correct_ids`.
- **Двуязычие на лету:** При переключении языка обновляются тексты без сброса выбранных чекбоксов/радиокнопок.
- **Шторка сервисов (BottomSheet):** Вытягивается снизу по свайпу или клику, отображает карточки сервисов из поля `services` текущего вопроса.

### 4.3. Интервальное повторение (leitner.js)
- Ящики от 0 до 5.
- Ошибка сбрасывает вопрос в `box = 0`. Правильный ответ увеличивает ящик `box = Math.min(5, box + 1)`.
- Выбор следующего вопроса: взвешенный выбор с приоритетом ящиков 0–1, вопросов с частыми ошибками и слабо усвоенных тем.

### 4.4. Симулятор экзамена (exam.js)
- Ровно 65 вопросов, обратный таймер 90:00.
- Разбивка по доменам CLF-C02:
  - Cloud Concepts: ~24% (15-16 вопросов)
  - Security and Compliance: ~30% (19-20 вопросов)
  - Technology: ~34% (22 вопроса)
  - Billing and Pricing: ~12% (8 вопросов)
- Формула AWS Scaled Score:
  $$\text{Score} = 100 + \text{Math.round}\left(\frac{\text{correct}}{65} \times 900\right)$$
  Проходной балл: 700 / 1000.
- Защита от сброса: состояние экзамена пишется в `sessionStorage` при каждом действии.

---

## 5. Синхронизация (sync.js и google_sync.js)
- Google Apps Script Web App («Execute as: Me», «Who has access: Anyone»).
- Запрос с заголовком `'Content-Type': 'text/plain;charset=utf-8'` (предотвращает preflight CORS OPTIONS) и `redirect: 'follow'`.
- **Timestamp Merge:** Сравнение поля `answered_at` для каждого вопроса. Побеждает более свежая запись.
- **Optimistic UI:** Синхронизация выполняется в фоне с индикатором статуса в шапке (Synced / Syncing / Offline / Error).
