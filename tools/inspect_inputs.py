import re
import json

bonso_path = 'C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256471236.txt'
old_path = 'C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256882166.html'

print('--- Parsing Old Trainer ---')
with open(old_path, 'r', encoding='cp1251') as f:
    old_html = f.read()

# Look for QUESTIONS or const Q or similar
q_match = re.search(r'const\s+QUESTIONS\s*=\s*(\[.*?\]);', old_html, re.DOTALL)
if not q_match:
    q_match = re.search(r'const\s+Q\s*=\s*(\[.*?\]);', old_html, re.DOTALL)
if not q_match:
    # search for array of objects with 'q:' or 'topic:'
    m = re.findall(r'const\s+([A-Za-z0-9_]+)\s*=\s*\[', old_html)
    print('Found arrays:', m)
else:
    print('Found questions array match! Length:', len(q_match.group(1)))

print('\n--- Parsing Bonso ---')
with open(bonso_path, 'r', encoding='utf-8') as f:
    bonso_html = f.read()

items = re.findall(r'class="[^"]*wpProQuiz_listItem[^"]*"', bonso_html)
print('Bonso wpProQuiz_listItem count:', len(items))
