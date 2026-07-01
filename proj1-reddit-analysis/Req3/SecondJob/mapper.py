#!/usr/bin/python3

import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

""" Requirement 3 : Highest/Lowest Score Topics
    Second job : End goal of this job -> To get valid topics [AKA: excludes words that
                  are just stop-words]. Then, return top and lowest scored 
                  valid topics with their score.

mapper.py
--- Input ---
Takes the output of first job [#word  #Score]. And, uses NLTK Library
    to decide which are valid topics and which words are not.

--- Output ---
Outputs : Topics and their scores.
    [#Topic  #Score]
"""
# Let these if NLTK is not downloaded.
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()         # Lemmatizer Object

stop_words = stopwords.words('english')
stop_words.extend(['would','often', 'u', 'like', 'much', 'many', 'less', 'more','very','always',\
 'yes','no', 'deleted', '[deleted]', 'wa', 'one', 'dont', 'get', 'people', 'im', 'think', 'time',\
 'ha', 'really', 'know', 'even', 'good', 'thats', 'make', 'do', 'go', 'see', 'could', 'also', 'want'])
stop_words = set(stop_words)            # Tested to have better performance than list

for line in sys.stdin:

    word, score = line.strip().split()
    topic = lemmatizer.lemmatize(word)

    if topic not in stop_words and not topic.isnumeric():   # Not a stop-word and not numeric val
      print(topic, score, sep='\t')