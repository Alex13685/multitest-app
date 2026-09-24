# -*- coding: utf-8 -*-
"""
Master Dataset Builder: Combines all questions into data/starter.json
Target: Exactly 600 authentic CLF-C02 questions.
- Domain 1: Cloud Concepts -> 144
- Domain 2: Security & Compliance -> 180
- Domain 3: Cloud Technology & Services -> 204
- Domain 4: Billing, Pricing, and Support -> 72
Total = 600
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load files
with open('data/converted_sources.json', 'r', encoding='utf-8') as f:
    sources = json.load(f)
old_qs = sources['old']
bonso_qs = sources['bonso']

with open('data/domain1_supplementary_107.json', 'r', encoding='utf-8') as f:
    d1_supp = json.load(f)

with open('data/domain2_supplementary_115.json', 'r', encoding='utf-8') as f:
    d2_supp = json.load(f)

with open('data/domain3_supplementary_50.json', 'r', encoding='utf-8') as f:
    d3_supp = json.load(f)

with open('data/domain4_72.json', 'r', encoding='utf-8') as f:
    d4_curated = json.load(f)

# Sort source questions by domain
d1_pool = []
d2_pool = []
d3_pool = []

for q in old_qs:
    dom = q['domain']
    if dom == 'cloud_concepts':
        d1_pool.append(q)
    elif dom == 'security':
        d2_pool.append(q)
    elif dom == 'technology':
        d3_pool.append(q)

for q in bonso_qs:
    dom = q['domain']
    if dom == 'cloud_concepts':
        d1_pool.append(q)
    elif dom == 'security':
        d2_pool.append(q)
    elif dom == 'technology':
        d3_pool.append(q)

# Add supplementary questions
d1_pool.extend(d1_supp)
d2_pool.extend(d2_supp)
d3_pool.extend(d3_supp)

# Final target slices
final_d1 = d1_pool[:144]
final_d2 = d2_pool[:180]
final_d3 = d3_pool[:204]
final_d4 = d4_curated[:72]

print(f"Final domain counts:")
print(f"  Cloud Concepts (Domain 1): {len(final_d1)} / 144")
print(f"  Security (Domain 2):       {len(final_d2)} / 180")
print(f"  Technology (Domain 3):     {len(final_d3)} / 204")
print(f"  Billing (Domain 4):        {len(final_d4)} / 72")

master_list = []
seen_ids = set()

def add_clean_questions(q_list, prefix):
    for i, q in enumerate(q_list):
        # generate clean consistent ID
        clean_id = f"clf_{prefix}_{i+1:03d}"
        q_copy = dict(q)
        q_copy['id'] = clean_id
        
        # Verify options
        assert len(q_copy['options']) >= 4, f"{clean_id} has less than 4 options"
        assert len(q_copy['correct_ids']) >= 1, f"{clean_id} has no correct_ids"
        
        # Check that all correct_ids exist in options
        opt_ids = set(o['id'] for o in q_copy['options'])
        for cid in q_copy['correct_ids']:
            assert cid in opt_ids, f"{clean_id}: correct_id {cid} not in options {opt_ids}"
            
        seen_ids.add(clean_id)
        master_list.append(q_copy)

add_clean_questions(final_d1, "cloud")
add_clean_questions(final_d2, "sec")
add_clean_questions(final_d3, "tech")
add_clean_questions(final_d4, "bill")

print(f"\nTotal questions assembled: {len(master_list)}")
assert len(master_list) == 600, f"Expected 600 questions, got {len(master_list)}"
assert len(seen_ids) == 600, "Duplicate question IDs detected!"

# Save to data/starter.json
with open('data/starter.json', 'w', encoding='utf-8') as f:
    json.dump(master_list, f, ensure_ascii=False, indent=2)

print("\nSuccessfully written master database to data/starter.json!")
