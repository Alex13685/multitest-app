import json
import random
import os

print("Building 600-question master bank...")

# We will read starter.json, segment_bill.py, flashcards.json and our master topic catalogs
from segment_bill import OLD_Q

print(f"Loaded {len(OLD_Q)} old trainer questions from segment_bill.")
