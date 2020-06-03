import bisect
def find(a, x, k):
    n = len(a)
    #ab = [abs(y-x) for y in a]
    ba = bisect.bisect(a, x)
    i = ba-1
    j = ba
    q=0
    while(q<k):
        if (j>=n):
            i -= (k-q)
            break
        if (i<0):
            j += (k-q)
            break
        if(abs(a[i]-x) <= abs(a[j]-x)):
            i-=1
        else:
            j+=1
        q+=1
    return a[i+1:j]
