"""
Simple environment check script for the Frameworks_Assignment starter repo.
Run this in your virtual environment to verify required packages are importable and the sample data loads.
"""

import importlib
import sys
import os

reqs = ['pandas', 'matplotlib', 'seaborn', 'streamlit', 'wordcloud', 'nltk']
missing = []
for r in reqs:
    try:
        importlib.import_module(r)
    except Exception as e:
        missing.append(r)

print('Python executable:', sys.executable)
if missing:
    print('\nMissing packages:')
    for m in missing:
        print(' -', m)
    print('\nInstall requirements with: pip install -r requirements.txt')
else:
    print('\nAll required packages appear to be importable.')

# Check sample data file
base = os.path.join(os.path.dirname(__file__), '..')
paths = [
    os.path.join(base, 'data', 'metadata.csv'),
    os.path.join(base, 'data', 'metadata_sample.csv')
]
for p in paths:
    if os.path.exists(p):
        print('\nFound data file:', p)
        break
else:
    print('\nNo data file found in data/. Add metadata.csv or metadata_sample.csv in the data/ folder')
