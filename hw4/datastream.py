import heapq
import math
def ksmallest(k, a):
    if (k < len(a)):
        h = [float("-inf")]*k
    else:
        h = [float("-inf")]*len(a)
    #print(h)
    heapq.heapify(h)
    for x in a:
        x=x*-1
        #print(str(h) + " " + str(x))
        if (x >= h[0]):
            heapq.heappushpop(h,x)
        #print(h)

    h.sort(reverse=True)
    return [abs(x) for x in h]
