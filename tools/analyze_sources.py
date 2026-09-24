import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/bonso_extracted.json', 'r', encoding='utf-8') as f:
    bonso = json.load(f)

with open('data/old_trainer_parsed.json', 'r', encoding='utf-8') as f:
    old = json.load(f)

print(f"Bonso count: {len(bonso)}")
print(f"Old trainer count: {len(old)}")

# Old trainer categories:
# bill, cloud, compute, net, storage, db, mgmt, cicd, ai, sec, mig
# In CLF-C02:
# Domain 1 (Cloud Concepts): cloud (20), mig (13), some mgmt -> ~40
# Domain 2 (Security & Compliance): sec (40), some net (security groups/nacl) -> ~45
# Domain 3 (Technology & Services): compute (22), net (23), storage (20), db (21), mgmt (21), cicd (15), ai (22) -> ~130
# Domain 4 (Billing & Support): bill (19)

cat_counts = {}
for q in old:
    cat_counts[q['cat']] = cat_counts.get(q['cat'], 0) + 1
print("Old trainer by category:", cat_counts)
