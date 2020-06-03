#!/usr/bin/env python3
from collections import defaultdict
from heapdict import heapdict
import random

def qselect(k, a):
    print(a)
    if a == []:
        return []
    else:
        rand = random.randrange(0, len(a))
        pivot = a[rand]
        left = [x for x in a[:rand] if x <= pivot] + [x for x in a[rand+1:] if x <= pivot]
        right = [x for x in a if x > pivot]
        if len(left)+1 < k:
            return qselect(k-len(left)-1 ,right)
        elif len(left)+1 == k:
            return pivot
        else:
            return qselect(k, left)


def shortest(n, edges):
    back = {}
    done = set()
    adjlist = defaultdict(list)
    Q = heapdict()
    Q[0] = 0
    for u, v, w in edges:
        adjlist[u].append((v,w))
        adjlist[v].append((u,w))

    while len(Q) > 0:
        u, d = Q.popitem()
        done.add(u)
        if u == (n-1):
            break
        for v, w in adjlist[u]:
            if v in done: continue
            #Q[v] = d+w
            if v not in Q or w+d < Q[v]:
                Q[v] = w+d
                back[v] = u
    if u != (n-1): return None
    return(d, solution(back,u))

def solution(back,k):
    if k not in back:
        return [k]
    return solution(back,back[k]) + [k]

def test(n, e, T):
    print(order(n, e) == T, order(n,e))

if __name__ == "__main__":
    print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print(shortest(8, [(0,2,4), (1,2,2), (2,3,3), (2,4,6), (4,3,7), (3,5,1), (4,5,4), (5,6,3), (5,7,2)]))
