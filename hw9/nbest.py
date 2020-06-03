#!/usr/bin/env python3
from heapq import heappush, heappop, heapify\
import random
def qselect(k, a):
    print(a)
    if a == []:
        return []
    else:
        rand = random.randrange(0, len(a))
        pivot = a[rand]
        #print("pivot is " + str(pivot))
        #print(a)
        left = [x for x in a[:rand] if x <= pivot] + [x for x in a[rand+1:] if x <= pivot]
        right = [x for x in a if x > pivot]
        #print("left " + str(left) + " is of len " + str(len(left)))
        #print("right " + str(right) + " is of len " + str(len(right)))
        #print("k " + str(k))
        if len(left)+1 < k:
            return qselect(k-len(left)-1 ,right)
        elif len(left)+1 == k:
            return pivot
        else:
            return qselect(k, left)

def nbest(ABs):    # no need to pass in k or n
    k = len(ABs)
    n = len(ABs[0][0])
    def trypush(i, p, q):  # push pair (A_i,p, B_i,q) if possible
        A, B = ABs[i] # A_i, B_i
        if p < n and q < n and (i,p, q) not in used:
            heappush(h, ((A[p] + B[q],A[p]),i, p, q, (A[p],B[q])))
            used.add((i, p, q))
    h, used = [], set()                 # initialize
    for i in range(k):  # NEED TO OPTIMIZE
        A, B = ABs[i]
        h.append(((A[0] + B[0],A[0]),i, 0, 0, (A[0],B[0])))
        used.add((i, 0, 0))
    heapify(h)
    for _ in range(n):
        _, i, p, q, pair = heappop(h)
        yield pair     # return the next pair (in a lazy list)
        trypush(i, p+1, q)
        trypush(i, p, q+1)
if __name__ == "__main__":
    print(list(nbest([([1,2,4], [2,3,5]), ([0,2,4], [3,4,5])])))
    print(list(nbest([([-1,2],[1,4]), ([0,2],[3,4]), ([0,1],[4,6]), ([-1,2],[1,5])])))
    print(list(nbest([([5,6,10,14],[3,5,10,14]),([2,7,9,11],[3,8,12,16]),([1,3,8,10],[5,9,10,11]),([1,2,3,5],[3,4,9,10]),([4,5,9,10],[2,4,6,11]),([4,6,10,13],[2,3,5,9]),([3,7,10,12],[1,2,5,10]),([5,9,14,15],[4,8,13,14])])))
    print(list(nbest([([1,6,8,13],[5,8,11,12]),([1,2,3,5],[5,9,11,13]),([3,5,7,10],[4,6,7,11]),([1,4,7,8],[4,9,11,15]),([4,8,10,13],[4,6,10,11]),([4,8,12,15],[5,10,11,13]),([2,3,4,8],[4,7,11,15]),([4,5,10,15],[5,6,7,8])])))
