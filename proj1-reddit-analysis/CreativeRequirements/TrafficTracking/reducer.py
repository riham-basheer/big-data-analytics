#!/usr/bin/python3

import sys
from ast import literal_eval

""" Creative Requirement : Getting number of users who commented at 
        each Timestamp. 
mapper.py
--- Input ---
Takes in [#time_stamp    #username]
  and keeps track of a set containing all usernames associated with this
  timestamp. This is to avoid counting multiple comments of the same user
  as multuple users.

--- Output ---
Outputs:
    [#time_stamp    #usernames_set]
"""

time_stamp = ''
all_usrs = set()

for line in sys.stdin:
    key, usernames = line.strip().split('|')
    usernames = set(literal_eval(usernames))
    if time_stamp is '':
        time_stamp = key
    elif time_stamp != key:
        print(time_stamp, all_usrs or '{}', sep='|')
        time_stamp = key
        all_usrs = set()

    all_usrs.update(usernames)
print(time_stamp, all_usrs or '{}', sep='|')
