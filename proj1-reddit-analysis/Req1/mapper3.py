#!/usr/bin/python3
import json
import ast
import sys

for line in sys.stdin:
    subred_info, author_topic = line.split('|')
    author_topic= ast.literal_eval(author_topic.strip())
    for key,val in author_topic.items():
        print(key, val,sep='|')
