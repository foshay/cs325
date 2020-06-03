#!/usr/bin/python3
import sys
sys.path.append(".")
from dijkstra import shortest
from collections import defaultdict
from heapdict import heapdict

def judge(num, tuples, tgt):
    print(tuples)
    edge_dict = defaultdict(int)
    for i,j,v in tuples:
        edge_dict[(i,j)] = v
        edge_dict[(j,i)] = v

    result = shortest(num, tuples)
    if result[0] != tgt:
        return False
    total_length = 0
    for idx in range(len(result[1])-1):
        l,r = result[1][idx], result[1][idx+1]
        total_length += edge_dict[(l,r)]
    if total_length != tgt:
        return False

    return True
