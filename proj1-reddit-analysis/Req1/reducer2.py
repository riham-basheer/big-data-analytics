#!/usr/bin/python3

import sys
import ast
from itertools import chain
from collections import defaultdict
authors = defaultdict(list)
timer =0

for line in sys.stdin:
    if timer <1000:
        timer +=1
        rank, key_subred, author_topic = line.split('|')
        author_topic= ast.literal_eval(author_topic)
        topics =list(chain.from_iterable(author_topic.values()))
        most_common_per_subred = max(set(topics), key=topics.count)
        #print (key_subred, most_common_per_subred, author_topic, sep='|' )
        print ('SUBREDDIT: '+key_subred, 'MOST COMMON TOPIC: '+most_common_per_subred,"|",author_topic, sep='\t' )
