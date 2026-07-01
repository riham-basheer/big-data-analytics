#!/usr/bin/python3
import sys
import heapq as hq

""" Requirement 3 : Highest/Lowest Score Topics
    Second job : End goal of this job -> To get valid topics [AKA: excludes words that
                  are just stop-words]. Then, return top and lowest scored 
                  valid topics with their score.

mapper.py
--- Input ---
Takes a topic with its score [#Topic  #Score].

--- Output ---
Outputs : Top 600 and Lowest 10 scored topics in the form:
    [#Topic  #Score]
"""

# Keeping Track of top and down x topics in terms of score
x = 10

# Top was increased as it contained a lot of stop-words that weren't removed.
top_x = [(-99999999, '') for _ in range(600)]
down_x = [(-99999999, '') for _ in range(x)]
hq.heapify(top_x)
hq.heapify(down_x)

# A heap queue is used because of its efficient sorted insertion
#   It keeps track of this by using a binary tree.
for line in sys.stdin:

    topic, score = line.strip().split()
    hq.heappushpop(top_x, (int(score), topic))
    hq.heappushpop(down_x, (-1*int(score), topic))      # (-1) To push the largest out instead of the smallest

# Print Top 600
top_lst =[hq.heappop(top_x) for i in range(len(top_x))]
for score, topic in reversed(top_lst):
    print(topic, score, sep='\t')

# Print Lowest 10
down_lst =[hq.heappop(down_x) for i in range(len(down_x))]
for score, topic in reversed(down_lst):
    print(topic, -1*score, sep='\t')
