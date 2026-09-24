import json
import re

# Domain mappings from old categories
CAT_TO_DOMAIN = {
    'bill': 'billing',
    'cloud': 'cloud_concepts',
    'sec': 'security',
    'compute': 'technology',
    'net': 'technology',
    'storage': 'technology',
    'db': 'technology',
    'mgmt': 'technology',
    'cicd': 'technology',
    'ai': 'technology',
    'mig': 'technology'
}

# Domain weights for blueprint
DOMAINS = ['cloud_concepts', 'security', 'technology', 'billing']

print("bank_builder initialized")
