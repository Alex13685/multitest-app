import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/bonso_extracted.json', 'r', encoding='utf-8') as f:
    bonso = json.load(f)

print("Inspecting first 5 Bonso questions...")
for i in range(5):
    q = bonso[i]
    print(f"\nQ{i+1}: {q['question']}")
    print(f"Options: {q['options']}")
    print(f"Correct indices: {q['correct_indices']}")
    print(f"Explanation snippet: {q['explanation'][:250]}...")
