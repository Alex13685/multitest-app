import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

bonso_path = 'C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256471236.txt'
with open(bonso_path, 'r', encoding='utf-8') as f:
    text = f.read()

items = re.findall(r'<li[^>]*class="[^"]*wpProQuiz_listItem[^"]*"[^>]*>(.*?)</li>\s*(?=<li[^>]*class="[^"]*wpProQuiz_listItem|$)', text, re.DOTALL)
print('Items count:', len(items))

# Let's inspect the first 3 items: their options and explanations
for i in range(min(3, len(items))):
    item = items[i]
    q_m = re.search(r'<div[^>]*class="[^"]*wpProQuiz_question_text[^"]*"[^>]*>(.*?)</div>', item, re.DOTALL)
    q_text = re.sub(r'<[^>]+>', ' ', q_m.group(1)).strip() if q_m else ""
    opts = re.findall(r'<li[^>]*class="[^"]*wpProQuiz_questionListItem[^"]*"[^>]*>(.*?)</li>', item, re.DOTALL)
    print(f"\n=== Q{i+1}: {q_text[:80]}... ===")
    for oi, opt in enumerate(opts):
        classes = re.findall(r'class="([^"]*)"', opt)
        opt_text = re.sub(r'<[^>]+>', ' ', opt).strip()
        print(f"  Opt {oi}: class={classes} text={opt_text}")
    resp_m = re.search(r'<div[^>]*class="[^"]*wpProQuiz_response[^"]*"[^>]*>(.*?)</div>\s*</div>', item, re.DOTALL)
    if resp_m:
        print(f"\n--- RESP Q{i+1} full ---")
        print(resp_m.group(1))
