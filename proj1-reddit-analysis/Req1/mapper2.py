#!/usr/bin/python3
import json
import sys
x = {}
#will be sys.stdin
for line in sys.stdin:
    key_subred, author_topic, rank = line.split('|')
    print(-int(rank), key_subred,author_topic,sep='|')
