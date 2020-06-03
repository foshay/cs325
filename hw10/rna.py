#!/usr/bin/env python3
allowed = set(['AU','UA','CG','GC','GU','UG'])
from collections import defaultdict
from heapq import heappush, heappop, heapify
#----------------------------------------------------------
def best(x):
#-----------------------------
    def _best(i, j):
        if (i, j) in opt:
            return opt[i, j]
        if i < 0 or j <= 0:
            return 0
        curr = 0
        for k in range(i, j):
            if x[k] + x[j] in allowed:
                if _best(i,k-1) + _best(k+1,j-1)+1 > curr: #If xj and xk can pair
                    curr = _best(i,k-1) + _best(k+1,j-1)+1
                    back[i, j] = k
        if _best(i, j-1) > curr:
            curr = _best(i, j-1)
            back[i, j] = -1
        opt[i, j] = curr
        return curr
#-----------------------------
#-----------------------------
    def solution(i, j):
        if (i,j) not in back:
            return "."*(j-i+1)
        k = back[i, j]
        if k == -1:
            return "%s." % solution(i, j-1)
        else:
            return "%s(%s)" % (solution(i, k-1), solution(k+1,j-1))
    opt = defaultdict(int)
    back = {}
    n = len(x)
    for i in range(n):
        opt[i,i] = 0
        opt[i, i-1] = 0
    return _best(0, n-1), solution(0, n-1)
#-----------------------------
#----------------------------------------------------------
#----------------------------------------------------------
def total(x):
#-----------------------------
    def _total(i, j):
        if (i, j) in opt:
            return opt[i, j]
        if i < 0 or j <= 0:
            return 0
        curr = 0
        for k in range(i, j):
            if x[k] + x[j] in allowed:
                curr += _total(i,k-1) * _total(k+1,j-1)
        curr += _total(i, j-1)
        opt[i, j] = curr
        return curr
    opt = defaultdict(int)
    n = len(x)
    for i in range(n):
        opt[i,i] = 1
        opt[i, i-1] = 1
    total = _total(0, n-1)
    return total
#-----------------------------
#----------------------------------------------------------
#----------------------------------------------------------
#-----------------------------
def kbest(x,k):
    def _kbest(i, j):
        def trypush_a(s,p,q):
            if p < len(topk[i,s-1]) and q < len(topk[s+1,j-1]) and (s,p,q) not in visited:
                heappush(h, (- (topk[i, s-1][p][0] + topk[s+1, j-1][q][0]+1),(s,p,q)))
                visited.add((s,p,q))
        def trypush_b(p):
            if p < len(topk[i,j-1]):
                heappush(h, (-(topk[i, j-1][p][0]),(p,)))
        if (i, j) in topk:
            return topk[i, j]
        h = []
        visited = set()
        for s in range(i, j):
            if x[s]+x[j] in allowed:
                _kbest(i, s-1)
                _kbest(s+1, j-1)
                trypush_a(s,0,0)
        _kbest(i, j-1)
        trypush_b(0)
        for _ in range(k):
            if h == []:
                break
            score, indices = heappop(h)
            try:
                s, p, q = indices
                topk[i, j].append((-score, "%s(%s)" % (topk[i, s-1][p][1],
                                                        topk[s+1,j-1][q][1])))
                trypush_a(s, p+1, q)
                trypush_a(s,p,q+1)
            except ValueError as e:
                p = indices[0]
                topk[i,j].append((-score, "%s." % topk[i,j-1][p][1]))
                trypush_b((p+1))
    topk = defaultdict(list)
    n = len(x)
    for i in range(n):
        topk[i,i] = [(0,'.')]
        topk[i,i-1] = [(0,'')]
    _kbest(0,n-1)
    return topk[0,n-1]
def test(s):
    print("---------\n",s)
    #print(best(s))
    #print(total(s),"\n---------")
    print(kbest(10,s))
if __name__ == "__main__":
    test("ACAGU")
    test("AC")
    test("GUAC")
    test("GCACG")
    test("CCGG")
    test("CCCGGG")
    test("UUCAGGA")
    #test("AUAACCUA")
    #test("UUGGACUUG")
    #test("UUUGGCACUA")
    #test("GAUGCCGUGUAGUCCAAAGACUUC")
