import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

dom_ids = [
    'services-backdrop', 'services-sheet', 'services-sheet-content', 'btn-close-sheet', 'btn-open-services',
    'import-json-input', 'btn-run-import', 'btn-load-starter', 'btn-clear-log', 'import-log',
    'btn-export-json', 'btn-reset-leitner', 'btn-purge-db',
    'stat-total-q', 'stat-seen-q', 'stat-total-attempts', 'stat-mastered', 'stat-accuracy',
    'domain-progress-container', 'box-count-0', 'box-count-1', 'box-count-2', 'box-count-3', 'box-count-4', 'box-count-5',
    'flashcard-box', 'fc-name', 'fc-hint', 'fc-desc', 'fc-trap', 'fc-grade-container',
    'fc-category-badge', 'fc-box-badge', 'fc-mastered-badge', 'btn-fc-know', 'btn-fc-grade-0', 'btn-fc-grade-1', 'btn-fc-grade-2'
]

print("--- Checking HTML IDs ---")
for did in dom_ids:
    if f'id="{did}"' not in html and f"id='{did}'" not in html:
        print("MISSING ID IN HTML:", did)

# Check screens
screens = ['screen-trainer', 'screen-cards', 'screen-exam', 'screen-import', 'screen-stats']
for s in screens:
    if f'id="{s}"' not in html:
        print("MISSING SCREEN ID IN HTML:", s)
