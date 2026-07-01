#!/usr/bin/python3
import json
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
lemmatizer = WordNetLemmatizer()

stop_words = stopwords.words('english')
stop_words.extend([re.sub(r'[^\w\s]', '', w.lower()) for w in  stop_words])
stop_words.extend(['like', 'much', 'many', 'less', 'more','very','always','yes','no'] )
stop_words = set(stop_words)


for line in sys.stdin:

    content= json.loads(line.strip())
    word_tokens =re.sub(r'[^\w\s]', '',  x['body'].lower()).split()
    filtered_sentence = [lemmatizer.lemmatize(w) for w in word_tokens if w not in stop_words]
    if filtered_sentence:
        topic = max(set(filtered_sentence), key=filtered_sentence.count)
    else:
        topic =None


    if x['author'] and topic and x['author'] not in ['deleted', '[deleted]'] and :
        print(x["subreddit"],{x['author']:topic},1,sep='|')

