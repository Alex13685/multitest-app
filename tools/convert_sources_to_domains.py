# -*- coding: utf-8 -*-
"""
Processes Bonso 64 and Old Trainer 236 into normalized domain pools.
"""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/bonso_extracted.json', 'r', encoding='utf-8') as f:
    bonso = json.load(f)

with open('data/old_trainer_parsed.json', 'r', encoding='utf-8') as f:
    old = json.load(f)

letters = ["opt_a", "opt_b", "opt_c", "opt_d", "opt_e", "opt_f"]

# Map old trainer questions
# Categories: bill -> billing, cloud -> cloud_concepts, mig -> cloud_concepts, sec -> security
# compute, net, storage, db, mgmt, cicd, ai -> technology
domain_map_old = {
    'bill': 'billing',
    'cloud': 'cloud_concepts',
    'mig': 'cloud_concepts',
    'sec': 'security',
    'compute': 'technology',
    'net': 'technology',
    'storage': 'technology',
    'db': 'technology',
    'mgmt': 'technology',
    'cicd': 'technology',
    'ai': 'technology'
}

converted_old = []
for idx, q in enumerate(old):
    cat = q.get('cat', 'cloud')
    domain = domain_map_old.get(cat, 'technology')
    qid = f"clf_old_{q['id']}"
    
    opts = q.get('opts', [])
    ans = q.get('a', [0])
    
    options = []
    correct_ids = []
    for oi, opt_text in enumerate(opts):
        opt_id = letters[oi] if oi < len(letters) else f"opt_{oi}"
        is_corr = oi in ans
        if is_corr:
            correct_ids.append(opt_id)
            why_inc = None
        else:
            # generate why_incorrect from explanation or option text
            why_inc = {
                "ru": f"Вариант «{opt_text}» не решает поставленную задачу сценария в полной мере.",
                "en": f"Option \"{opt_text}\" does not fulfill all technical constraints of the scenario."
            }
            
        options.append({
            "id": opt_id,
            "text": {
                "ru": opt_text,
                "en": opt_text
            },
            "why_incorrect": why_inc
        })
        
    ex_text = q.get('ex', '')
    # clean html tags for summary
    clean_ex = re.sub(r'<[^>]+>', '', ex_text).strip()
    
    converted_old.append({
        "id": qid,
        "domain": domain,
        "difficulty": q.get('difficulty', 2),
        "q": {
            "ru": q['q'],
            "en": q['q'] # keep original bilingual
        },
        "options": options,
        "correct_ids": correct_ids,
        "services": [cat],
        "explanation": {
            "summary_ru": f"Правильный ответ: {', '.join([opts[i] for i in ans if i < len(opts)])}.",
            "summary_en": f"Correct answer: {', '.join([opts[i] for i in ans if i < len(opts)])}.",
            "detailed_ru": ex_text,
            "detailed_en": clean_ex
        }
    })

print(f"Converted old trainer questions: {len(converted_old)}")
by_domain_old = {}
for q in converted_old:
    by_domain_old[q['domain']] = by_domain_old.get(q['domain'], 0) + 1
print("Old trainer by domain:", by_domain_old)

# Convert Bonso questions
converted_bonso = []
for idx, q in enumerate(bonso):
    qid = f"clf_bonso_{q['index']:03d}"
    
    # Classify domain
    q_lower = (q['question'] + " " + q['explanation']).lower()
    if any(k in q_lower for k in ['shared responsibility', 'iam', 'cloudhsm', 'kms', 'guardduty', 'waf', 'shield', 'inspector', 'macie', 'artifact', 'security group', 'nacl', 'trust & safety', 'abuse']):
        dom = "security"
    elif any(k in q_lower for k in ['support plan', 'budgets', 'cost explorer', 'consolidated billing', 'pricing calculator', 'pricing', 'billing', 'tco', 'cur', 'trusted advisor', 'concierge']):
        dom = "billing"
    elif any(k in q_lower for k in ['well-architected', 'caf', 'adoption framework', 'economies of scale', 'agility', 'elasticity', 'disaster recovery', 'rpo', 'rto', 'migration', '7 rs', 'rehost', 'replatform', 'refactor', 'capex', 'opex']):
        dom = "cloud_concepts"
    else:
        dom = "technology"
        
    opts = q.get('options', [])
    ans = q.get('correct_indices', [0])
    resp_raw = q.get('raw_explanation', '')
    
    # Extract distractors reasons if possible
    options = []
    correct_ids = []
    for oi, opt_text in enumerate(opts):
        opt_id = letters[oi] if oi < len(letters) else f"opt_{oi}"
        is_corr = oi in ans
        if is_corr:
            correct_ids.append(opt_id)
            why_inc = None
        else:
            # find distractor explanation in raw_explanation
            # pattern: [opt] is incorrect because ...
            opt_clean = re.sub(r'[^a-zA-Z0-9\s]', '', opt_text).strip()
            d_match = re.search(re.escape(opt_clean) + r'[^<]*is incorrect because\s*(.*?)(?:</p>|<p>|$)', resp_raw, re.IGNORECASE | re.DOTALL)
            if not d_match:
                d_match = re.search(r'is incorrect because\s*(.*?)(?:</p>|<p>|$)', resp_raw, re.IGNORECASE | re.DOTALL)
            
            why_en = re.sub(r'<[^>]+>', '', d_match.group(1)).strip() if d_match else f"{opt_text} does not meet all criteria required in the question scenario."
            why_ru = f"Вариант {opt_text} не является правильным в контексте данного вопроса: {why_en[:150]}..." if why_en else f"Вариант {opt_text} не решает задачу сценария."
            
            why_inc = {
                "en": why_en,
                "ru": why_ru
            }
            
        options.append({
            "id": opt_id,
            "text": {
                "en": opt_text,
                "ru": opt_text
            },
            "why_incorrect": why_inc
        })
        
    clean_expl = q.get('explanation', '')
    
    converted_bonso.append({
        "id": qid,
        "domain": dom,
        "difficulty": 2,
        "q": {
            "en": q['question'],
            "ru": q['question']
        },
        "options": options,
        "correct_ids": correct_ids,
        "services": ["aws_core"],
        "explanation": {
            "summary_en": f"The correct answer is: {', '.join([opts[i] for i in ans if i < len(opts)])}.",
            "summary_ru": f"Правильный ответ: {', '.join([opts[i] for i in ans if i < len(opts)])}.",
            "detailed_en": clean_expl,
            "detailed_ru": clean_expl
        }
    })

print(f"Converted Bonso questions: {len(converted_bonso)}")
by_domain_bonso = {}
for q in converted_bonso:
    by_domain_bonso[q['domain']] = by_domain_bonso.get(q['domain'], 0) + 1
print("Bonso by domain:", by_domain_bonso)

with open('data/converted_sources.json', 'w', encoding='utf-8') as f:
    json.dump({
        "old": converted_old,
        "bonso": converted_bonso
    }, f, ensure_ascii=False, indent=2)
print("Saved to data/converted_sources.json")
