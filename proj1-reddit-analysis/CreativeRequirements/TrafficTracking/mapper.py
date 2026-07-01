#!/usr/bin/python3
import sys
import json

""" Creative Requirement : Getting number of users who commented at 
        each Timestamp. 
mapper.py
--- Input ---
Takes the json file line by line. Gets the username and timestamp.

--- Output ---
Outputs:
    [#time_stamp    #username]
"""

for line in sys.stdin:
    content = json.loads(line)
    # read author of this comment and its timestamp
    usrname = content["author"]
    time_stamp = content["created_utc"]
    if usrname != '[deleted]':
      print(time_stamp, set((usrname, )), sep="|")