import json
import os

print("Compiling full 600-question dataset for AWS CLF-C02...")

DOMAINS_TARGETS = {
    'cloud_concepts': 144,
    'security': 180,
    'technology': 204,
    'billing': 72
}

# Load current 8 starter questions if present
starter_path = r'C:\Users\popad\.gemini\antigravity\scratch\clf-trainer\data\starter.json'
existing_questions = []
if os.path.exists(starter_path):
    with open(starter_path, 'r', encoding='utf-8') as f:
        existing_questions = json.load(f)

print(f"Loaded {len(existing_questions)} existing starter questions.")
