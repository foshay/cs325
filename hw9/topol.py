#!/usr/bin/env python3

from collections import defaultdict

def _order(n, edges):

    adjlist = defaultdict(list)
    indegree = defaultdict(int)

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
        yield u #next in topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

def order(n, edges):
    return list(_order(n, edges))

def test(n, e, T):
    print(order(n, e) == T, order(n,e))

if __name__ == "__main__":
    test(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)], [0,1,2,4,3,5,6,7])
