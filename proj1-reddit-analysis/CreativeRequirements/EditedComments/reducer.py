#!/usr/bin/python3
import sys

""" reducer.py
--- Input ---
Will be getting:
    [#username  #edited_comments   #1 [for the current comment]]

--- Output ---
Sums the number of edited comments and total number of comments 
    for each user.
Final Output in the form:
    [#username  #count_of_edited_comments   #count_of_total_comments]
"""

comments_count = edited_comments_count = 0
username = ""

for line in sys.stdin:
    myLine = line.strip().split()
    if username is "": 
        username = myLine[0]
    elif username != myLine[0]:
        print(username, edited_comments_count, comments_count, sep='\t')
        username = myLine[0]
        comments_count = edited_comments_count = 0
  
    edited_comments_count += int(myLine[1])
    comments_count += int(myLine[2])
    
print(username, edited_comments_count, comments_count, sep='\t')
