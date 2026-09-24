import json
import re

# 1. Test services_info.json
with open('data/services_info.json', encoding='utf-8') as f:
    db = json.load(f)
print('services_info.json valid! Total keys:', len(db))

# 2. Test starter.json
with open('data/starter.json', encoding='utf-8') as f:
    qs = json.load(f)
print('starter.json valid! Total questions:', len(qs))

# 3. Test flashcards.json
with open('data/flashcards.json', encoding='utf-8') as f:
    fcs = json.load(f)
print('flashcards.json valid! Total cards:', len(fcs))

# 4. Check all tags in qs against db
unresolved = set()
for q in qs:
    for s in q.get('services', []):
        if s not in db:
            unresolved.add(s)
print('Unresolved service tags count:', len(unresolved))

# 5. Check index.html section structure
with open('index.html', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', html)
print('Sections found in order:', sections)
