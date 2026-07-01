#!/usr/bin/python3

import sys
from collections import defaultdict
import ast
authors = defaultdict(list)
subred = None
count = 0

for line in sys.stdin:
    #try: 
    key_subred, body_author, value = line.strip().split('|')
    body_author=list(ast.literal_eval(body_author).items())
    author,body = body_author[0][0],body_author[0][1]
    #except: print(line)
    if subred is None:
        subred = key_subred
    elif subred != key_subred:
        print(subred, dict(authors), count,sep='|')
        subred = key_subred
        count = 0
        authors = defaultdict(list)

    count += int(value)
    authors[author].append(body)

print( subred,dict(authors), count, sep='|')