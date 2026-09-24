import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/old_trainer_parsed.json', 'r', encoding='utf-8') as f:
    old = json.load(f)

for i in [0, 25, 50, 100, 150, 200]:
    q = old[i]
    print(f"\n=== ID: {q['id']} | Cat: {q['cat']} | Diff: {q['difficulty']} ===")
    print("Q:", q['q'])
    print("Opts:", q['opts'])
    print("Ans:", q['a'])
    print("Ex:", q['ex'])
