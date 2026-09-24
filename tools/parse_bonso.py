import re
import sys
import json
from html import unescape

sys.stdout.reconfigure(encoding='utf-8')

bonso_path = 'C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256471236.txt'
with open(bonso_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Questions in wpProQuiz are in <li class="wpProQuiz_listItem" ...>
# Let's find each item
items = re.findall(r'<li[^>]*class="[^"]*wpProQuiz_listItem[^"]*"[^>]*>(.*?)</li>\s*(?=<li[^>]*class="[^"]*wpProQuiz_listItem|$)', html, re.DOTALL)
print(f"Found {len(items)} Bonso items.")

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    # clean extra whitespace
    lines = [l.strip() for l in text.split('\n')]
    return '\n'.join([l for l in lines if l]).strip()

bonso_questions = []

for idx, item in enumerate(items):
    # Question text
    q_match = re.search(r'<div[^>]*class="[^"]*wpProQuiz_question_text[^"]*"[^>]*>(.*?)</div>\s*<ul class="wpProQuiz_questionList"', item, re.DOTALL)
    if not q_match:
        q_match = re.search(r'<div[^>]*class="[^"]*wpProQuiz_question_text[^"]*"[^>]*>(.*?)</div>', item, re.DOTALL)
    q_text = clean_html(q_match.group(1)) if q_match else f"Question {idx+1}"

    # Options: <li class="wpProQuiz_questionListItem" ...> ... <label>...</label>
    opts_matches = re.findall(r'<li[^>]*class="[^"]*wpProQuiz_questionListItem[^"]*"[^>]*>(.*?)</li>', item, re.DOTALL)
    options = []
    correct_indices = []
    for opt_idx, opt_raw in enumerate(opts_matches):
        lbl_m = re.search(r'<label[^>]*>(.*?)</label>', opt_raw, re.DOTALL)
        opt_text = clean_html(lbl_m.group(1)) if lbl_m else clean_html(opt_raw)
        options.append(opt_text)
        # Check for correct answer attributes: data-correct="1" or class wpProQuiz_answerCorrect or similar
        if 'wpProQuiz_answerCorrect' in opt_raw or 'class="wpProQuiz_answerCorrect"' in opt_raw or 'data-pos' in opt_raw or 'checked' in opt_raw:
            pass # let's debug what's in opt_raw

    # Let's inspect opt_raw in Question 1
    if idx == 0:
        print("DEBUG Question 1 opts_matches raw:")
        for oi, raw_o in enumerate(opts_matches):
            print(f"Option {oi}: {raw_o}")

    # Explanation: <div class="wpProQuiz_response" ...> or <div class="wpProQuiz_correct" ...>
    resp_match = re.search(r'<div[^>]*class="[^"]*wpProQuiz_response[^"]*"[^>]*>(.*?)</div>\s*</div>', item, re.DOTALL)
    if not resp_match:
        resp_match = re.search(r'<div[^>]*class="[^"]*wpProQuiz_response[^"]*"[^>]*>(.*?)</div>', item, re.DOTALL)
    explanation = clean_html(resp_match.group(1)) if resp_match else ""

    bonso_questions.append({
        "index": idx + 1,
        "question": q_text,
        "options": options,
        "correct_indices": correct_indices,
        "explanation": explanation
    })

print(f"Parsed {len(bonso_questions)} questions.")
if bonso_questions:
    print("\nSample Question 1:")
    print("Q:", bonso_questions[0]["question"][:150])
    print("Options:", bonso_questions[0]["options"])
    print("Correct:", bonso_questions[0]["correct_indices"])
    print("Expl:", bonso_questions[0]["explanation"][:200])

with open('data/bonso_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(bonso_questions, f, ensure_ascii=False, indent=2)
print("Saved to data/bonso_parsed.json")
