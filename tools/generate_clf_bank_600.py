# -*- coding: utf-8 -*-
"""
Master Builder for 600 Authentic CLF-C02 Questions
Balances:
- Domain 1: Cloud Concepts -> exactly 144 questions
- Domain 2: Security & Compliance -> exactly 180 questions
- Domain 3: Cloud Technology & Services -> exactly 204 questions
- Domain 4: Billing, Pricing, and Support -> exactly 72 questions
Total = 600 questions.
"""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load curated sources
with open('data/converted_sources.json', 'r', encoding='utf-8') as f:
    sources = json.load(f)

old_qs = sources['old']
bonso_qs = sources['bonso']

with open('data/domain4_72.json', 'r', encoding='utf-8') as f:
    domain4_qs = json.load(f)

print(f"Loaded: old={len(old_qs)}, bonso={len(bonso_qs)}, domain4={len(domain4_qs)}")

# Group sources by domain
pool = {
    'cloud_concepts': [],
    'security': [],
    'technology': [],
    'billing': []
}

# Add old questions
for q in old_qs:
    if q['domain'] in pool:
        pool[q['domain']].append(q)

# Add bonso questions
for q in bonso_qs:
    if q['domain'] in pool:
        pool[q['domain']].append(q)

print("Current counts from sources:")
for k, v in pool.items():
    print(f"  {k}: {len(v)}")

# Targets
# cloud_concepts: 144
# security: 180
# technology: 204
# billing: 72 (we will use domain4_qs directly)
TARGETS = {
    'cloud_concepts': 144,
    'security': 180,
    'technology': 204,
    'billing': 72
}

# Domain 1 generator: we need (144 - len(pool['cloud_concepts'])) = 144 - 37 = 107 questions
# Domain 2 generator: we need (180 - len(pool['security'])) = 180 - 65 = 115 questions
# Domain 3 generator: we need (204 - len(pool['technology'])) = 204 - 154 = 50 questions

print(f"Need to generate: cloud_concepts={TARGETS['cloud_concepts'] - len(pool['cloud_concepts'])}, security={TARGETS['security'] - len(pool['security'])}, technology={TARGETS['technology'] - len(pool['technology'])}")
