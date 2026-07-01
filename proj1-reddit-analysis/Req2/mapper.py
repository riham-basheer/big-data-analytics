#!/usr/bin/python3
import json
import sys
x = {}

for line in sys.stdin:
    line = json.loads(line)
    replies = 0
    try: 
        replies = line['replies']
    except KeyError: 
        pass
    if line["score"]:
        sc = line["score"]
    else:
        sc = 0
    if int(line['controversiality']) != 0:
      print(line["controversiality"], replies, sc, sep='|')
    
