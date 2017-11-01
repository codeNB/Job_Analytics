"""run third, calculate the term frequency from retrieved documents"""
import json
import re
from collections import defaultdict

FREQ = defaultdict(int)

DATA = open('data/post_data.txt')

def strip_punct(text: str) -> str:
    """remove punctuation from string"""
    pat = re.compile(['^a-zA-Z ']) # match all a-z A-Z and space
    return pat.sub('', text) 

for line in DATA:
    # TODO add some text cleaning code here to strip away punct and change all to a single case.
    line = strip_punct(line)
    line = line.strip().lower()
    for word in line.split():
        freq[word] += 1

with open('data/word_freq.json', 'w') as f:
    json.dump(FREQ, f, ensure_ascii=False)
