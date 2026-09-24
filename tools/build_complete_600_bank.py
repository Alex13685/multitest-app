# -*- coding: utf-8 -*-
"""
Master CLF-C02 Bank Generator (600 Questions)
Combines:
1. 64 Authentic Tutorials Dojo (Jon Bonso) questions
2. 236 Authentic questions from the previous trainer
3. 300 Complementary high-yield authentic CLF-C02 exam questions
Strictly balanced across the official AWS exam domains:
- Domain 1: Cloud Concepts (24% = 144 questions)
- Domain 2: Security & Compliance (30% = 180 questions)
- Domain 3: Cloud Technology & Services (34% = 204 questions)
- Domain 4: Billing, Pricing, and Support (12% = 72 questions)
Total = 600 questions.
"""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load raw inputs
with open('data/bonso_extracted.json', 'r', encoding='utf-8') as f:
    bonso_raw = json.load(f)

with open('data/old_trainer_parsed.json', 'r', encoding='utf-8') as f:
    old_raw = json.load(f)

with open('data/domain4_72.json', 'r', encoding='utf-8') as f:
    domain4_curated = json.load(f)

print(f"Loaded bonso: {len(bonso_raw)}, old: {len(old_raw)}, domain4: {len(domain4_curated)}")
