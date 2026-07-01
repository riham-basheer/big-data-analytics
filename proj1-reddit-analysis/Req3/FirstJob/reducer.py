#!/usr/bin/python3

import sys

""" Requirement 3 : Highest/Lowest Score Topics
    First job : End goal of this job -> to get words and their collective score.
        Works same as word count but instead of just counting, it sums their scores.

reducer.py
--- Input ---
Takes a word and its score : [#word  #Score]
    Treats word as a key and sums its scores.
--- Output ---
Outputs :
    [#word  #Total_Score]
"""

# Simple word count but now, summing scores

word = None
count = 0

for line in sys.stdin:
    key, value = line.strip().split()
    if word is None:
        word = key
    elif word != key:
        print(word, count, sep='\t')
        word = key
        count = 0
    count += int(value)

print(word, count, sep='\t')
