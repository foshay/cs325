#!/usr/bin/env python3
from collections import defaultdict

def longest(n, edges):
    dic = defaultdict(int)
    back = {}
    adjlist = defaultdict(list)
    indegree = defaultdict(int)
    order = []
    for u, v in edges:
        adjlist[u].append(v)
        indegree[v] += 1

    queue = []

    for u in range(n):
        if indegree[u] == 0:
            queue.append(u)
    head = 0
    while head < len(queue):
        u = queue[head] #popping queue
        head += 1
        order.append(u) #next in topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    maxnode = 0
    maxlen = 0
    for u in order:
        for v in adjlist[u]:
            #dic[v] = max(dic[v], dic[u]+1)
            if dic[v] < dic[u] + 1:
                dic[v] = dic[u] + 1
                back[v] = u
                if maxlen < dic[v]:
                    maxlen = dic[v]
                    maxnode = v
    #print(maxlen, maxnode)
    #print(back)
    return(maxlen,solution(back,maxnode))

def solution(back,k):
    if k not in back:
        return [k]
    return solution(back,back[k]) + [k]

def test(n, e, T):
    print(order(n, e) == T, order(n,e))

if __name__ == "__main__":
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
    print(longest(8, [(2, 3), (3, 4), (4, 5)]))
    #test(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)], [0,1,2,4,3,5,6,7])
