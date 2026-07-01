#!/usr/bin/python3

import sys
import ast
from itertools import chain
from collections import defaultdict
author_topics_dict = defaultdict(list)

for line in sys.stdin:
    author, topics = line.split('|')
    topics= ast.literal_eval(topics)
    author_topics_dict[author].extend(topics)

for auth,topics in author_topics_dict.items():
    print('AUTHOR USERNAME: ', auth, 'MOST COMMON TOPIC: ', max(set(topics), key=topics.count), sep='|')