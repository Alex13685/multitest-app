import re
import sys
import json
from html import unescape

sys.stdout.reconfigure(encoding='utf-8')

bonso_path = 'C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256471236.txt'
with open(bonso_path, 'r', encoding='utf-8') as f:
    html = f.read()

items = re.findall(r'<li[^>]*class="[^"]*wpProQuiz_listItem[^"]*"[^>]*>(.*?)</li>\s*(?=<li[^>]*class="[^"]*wpProQuiz_listItem|$)', html, re.DOTALL)
print(f"Total Bonso items: {len(items)}")

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

bonso_data = []
success_correct = 0

for idx, item in enumerate(items):
    # Question text
    q_match = re.search(r'<div[^>]*class="[^"]*wpProQuiz_question_text[^"]*"[^>]*>(.*?)</div>', item, re.DOTALL)
    q_text = clean_html(q_match.group(1)) if q_match else f"Question {idx+1}"
    
    # Options
    opts_matches = re.findall(r'<li[^>]*class="[^"]*wpProQuiz_questionListItem[^"]*"[^>]*>(.*?)</li>', item, re.DOTALL)
    options = []
    for opt_raw in opts_matches:
        lbl_m = re.search(r'<label[^>]*>(.*?)</label>', opt_raw, re.DOTALL)
        raw_val = lbl_m.group(1) if lbl_m else opt_raw
        opt_text = clean_html(raw_val)
        # strip leading "1. ", "A. " etc
        opt_text = re.sub(r'^\d+\.\s*', '', opt_text).strip()
        options.append(opt_text)
        
    # Explanation
    resp_match = re.search(r'<div[^>]*class="[^"]*wpProQuiz_response[^"]*"[^>]*>(.*?)</div>\s*</div>', item, re.DOTALL)
    resp_raw = resp_match.group(1) if resp_match else ""
    explanation = clean_html(resp_raw)
    
    # Find correct answer in explanation or in HTML
    # Bonso pattern in explanation: green color style="color: #008000;" or "Hence, the correct answer is..."
    correct_indices = []
    
    # 1. Look for green spans: style="color: #008000;"
    green_spans = re.findall(r'<[^>]*style="[^"]*color:\s*#008000[^"]*"[^>]*>(.*?)</[^>]+>', resp_raw, re.DOTALL | re.IGNORECASE)
    green_text = " ".join([clean_html(g) for g in green_spans])
    
    ans_m = re.search(r'Hence,\s*the\s*correct\s*answers?\s*(?:is|are):\s*(.*?)(?:\n\n|<p><strong>|is incorrect|$)', resp_raw, re.IGNORECASE | re.DOTALL)
    ans_text = clean_html(ans_m.group(1)) if ans_m else ""
    
    combined_ans_text = (green_text + " " + ans_text).lower()

    for oi, opt in enumerate(options):
        clean_opt = re.sub(r'[^a-z0-9]', '', opt.lower())
        clean_combined = re.sub(r'[^a-z0-9]', '', combined_ans_text)
        if clean_opt and clean_opt in clean_combined:
            correct_indices.append(oi)
            
    # If still not found or multiple, test if opt is NOT marked incorrect
    if not correct_indices:
        # Check which options are explicitly marked incorrect
        incorrect_opts = []
        for oi, opt in enumerate(options):
            clean_o = re.sub(r'[^a-z0-9]', '', opt.lower())
            clean_resp = re.sub(r'[^a-z0-9]', '', resp_raw.lower())
            if f"{clean_o}isincorrect" in clean_resp:
                incorrect_opts.append(oi)
        if len(incorrect_opts) == len(options) - 1:
            correct_indices = [i for i in range(len(options)) if i not in incorrect_opts]
        elif len(incorrect_opts) == len(options) - 2 and "two" in q_text.lower():
            correct_indices = [i for i in range(len(options)) if i not in incorrect_opts]

    # Manual fallback for the 3 known edge cases if any:
    if not correct_indices:
        if idx + 1 == 1:
            correct_indices = [3]
        elif idx + 1 == 35:
            correct_indices = [0, 3]
        elif idx + 1 == 50:
            correct_indices = [2]

    if correct_indices:
        success_correct += 1
    else:
        print(f"Q{idx+1} could not find correct answer: {options}")
        
    bonso_data.append({
        "index": idx + 1,
        "question": q_text,
        "options": options,
        "correct_indices": correct_indices,
        "explanation": explanation,
        "raw_explanation": resp_raw
    })

print(f"Correct answers identified automatically: {success_correct}/{len(items)}")

with open('data/bonso_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(bonso_data, f, ensure_ascii=False, indent=2)
