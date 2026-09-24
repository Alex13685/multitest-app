import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/bonso_extracted.json', 'r', encoding='utf-8') as f:
    bonso = json.load(f)

# Keywords for domain classification
def classify_domain(q_text, expl):
    combined = (q_text + " " + expl).lower()
    
    # Billing & Support
    if any(k in combined for k in ['support plan', 'cost explorer', 'budgets', 'consolidated billing', 'pricing calculator', 'total cost of ownership', 'tco', 'billing dashboard', 'cur', 'cost and usage report', 'trusted advisor', 'concierge', 'enterprise support', 'business support']):
        return "billing"
        
    # Security & Compliance
    if any(k in combined for k in ['shared responsibility', 'iam', 'guardduty', 'cloudhsm', 'kms', 'security group', 'nacl', 'waf', 'shield', 'inspector', 'macie', 'artifact', 'audit manager', 'compliance', 'encryption', 'pci dss', 'hipaa', 'root user', 'mfa', 'trust & safety', 'abuse']):
        return "security"
        
    # Cloud Concepts
    if any(k in combined for k in ['well-architected', 'caf', 'cloud adoption framework', 'agility', 'elasticity', 'fault tolerance', 'high availability', 'reliability pillar', 'capex', 'opex', 'economies of scale', 'disaster recovery', 'rpo', 'rto', 'migration strategy', '7 rs', 'rehost', 'replatform', 'refactor']):
        return "cloud_concepts"
        
    # Default to technology
    return "technology"

counts = {}
for q in bonso:
    dom = classify_domain(q['question'], q['explanation'])
    q['domain'] = dom
    counts[dom] = counts.get(dom, 0) + 1

print("Bonso Domain Breakdown:", counts)
