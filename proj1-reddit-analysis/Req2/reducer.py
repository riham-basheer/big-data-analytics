#!/usr/bin/python3
import sys
import ast

for line in sys.stdin:
  if len(line.strip()) != 0:
    contr, rep, score = line.strip().split("|")
    
    if rep != '0':
        rep = len(ast.literal_eval(rep))
    
    print("CONTRAVERSIALITY:  "+contr, " NUM REPLIES: "+rep, " SCORE: "+score, sep = "|" )