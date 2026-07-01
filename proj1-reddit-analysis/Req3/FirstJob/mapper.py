#!/usr/bin/python3

import sys
import json
import re

""" Requirement 3 : Highest/Lowest Score Topics
    First job : End goal of this job -> to get words and their collective score.
        Works same as word count but instead of just counting, it sums their scores.

mapper.py
--- Input ---
Takes the json file line by line. Takes the comment's body,
    cleans it a bit, and returns the word and its score.

--- Output ---
Outputs :
    [#word  #Score]
    Eg : "love  5"
"""

for line in sys.stdin:
    content = json.loads(line)                       # Read json line
    body = content["body"].lower()                   # lower-case comment's body
    body = re.sub(r'https?:\/\/.*[\r\n]*', '', body) # Remove links  
    body = re.sub(r'[^\w\s]', '',  body).split()     # Remove alphanumeric/whitespace  

    for word in body:
        print(word, content["score"], sep='\t')      # Print word and its score [the comment's]
