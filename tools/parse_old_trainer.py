import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

old_path = 'C:/Users/popad/.gemini/antigravity/brain/0d88c693-8a20-43d6-99aa-e230eef04478/.user_uploaded/media_1790256882166.html'
with open(old_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const Q = \[(.*?)\];\s*let', text, re.DOTALL)
if not m:
    m = re.search(r'const Q = \[(.*?)\];', text, re.DOTALL)

raw_q_block = m.group(1)

# Each question starts with {id: ...
# Let's find each question block
# Let's find all objects between {id: and }
# We can find all id:"..." occurrences
id_matches = list(re.finditer(r'\{id:"([a-z0-9]+)"', raw_q_block))
print(f"Total question occurrences in file: {len(id_matches)}")

questions = []
for i in range(len(id_matches)):
    start_pos = id_matches[i].start()
    end_pos = id_matches[i+1].start() if i+1 < len(id_matches) else len(raw_q_block)
    block = raw_q_block[start_pos:end_pos].strip()
    # trim trailing comma or closing bracket
    if block.endswith(','):
        block = block[:-1].strip()
    if block.endswith(']'):
        block = block[:-1].strip()
    if block.endswith('};'):
        block = block[:-1].strip()
    
    qid = id_matches[i].group(1)
    
    # extract cat
    cat_m = re.search(r'cat:"([^"]+)"', block)
    cat = cat_m.group(1) if cat_m else "cloud"
    
    # d
    d_m = re.search(r'd:(\d+)', block)
    d = int(d_m.group(1)) if d_m else 1
    
    # q
    q_m = re.search(r'q:"(.*?)"(?=,\s*(?:opts|cat|d|a):)', block, re.DOTALL)
    if not q_m:
        q_m = re.search(r'q:"(.*?)",\s*opts:', block, re.DOTALL)
    q_text = q_m.group(1) if q_m else ""
    
    # opts
    opts_m = re.search(r'opts:(\[.*?\]),\s*a:', block, re.DOTALL)
    opts_raw = opts_m.group(1) if opts_m else "[]"
    try:
        opts = json.loads(opts_raw)
    except:
        # fallback manual parse
        opts = re.findall(r'"((?:\\.|[^"\\])*)"', opts_raw)
        
    # a
    a_m = re.search(r'a:(\[[^\]]*\])', block)
    a_raw = a_m.group(1) if a_m else "[0]"
    try:
        a = json.loads(a_raw)
    except:
        a = [int(x.strip()) for x in a_raw.strip('[]').split(',') if x.strip().isdigit()]
        
    # ex
    ex_m = re.search(r'ex:"(.*?)"\s*\}?$', block, re.DOTALL)
    if not ex_m:
        ex_m = re.search(r'ex:"(.*)', block, re.DOTALL)
    ex = ex_m.group(1).rstrip('}\n\r\t ') if ex_m else ""
    
    # clean escapes
    q_text = q_text.replace('\\"', '"').replace('\\n', '\n')
    ex = ex.replace('\\"', '"').replace('\\n', '\n')
    opts = [o.replace('\\"', '"').replace('\\n', '\n') for o in opts]
    
    questions.append({
        "id": qid,
        "cat": cat,
        "difficulty": d,
        "q": q_text,
        "opts": opts,
        "a": a,
        "ex": ex
    })

print(f"Total successfully parsed questions: {len(questions)}")
# breakdown by cat
cats = {}
for q in questions:
    cats[q['cat']] = cats.get(q['cat'], 0) + 1
print("Categories:", cats)

with open('data/old_trainer_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print("Saved data/old_trainer_parsed.json")
