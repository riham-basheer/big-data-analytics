#!/usr/bin/python3
import sys
import json

""" Creative Requirement : % of edited comments per user
mapper.py
--- Input ---
Takes the json file line by line. Gets the username and if their comment is edited.

--- Output ---
Outputs:
    [#username  #edited_comments   #1 [for the current comment]]
"""

for line in sys.stdin:
    content = json.loads(line)
    # read author of this comment and if it's edited
    usrname = content["author"]
    edited = int(content["edited"] == True)
    if usrname != "[deleted]":
      print(usrname, edited, 1, sep="\t")
    
