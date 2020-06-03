def num_inversions(a):
    r = 0
    t, r = _mergesort(a)
    print(t)
    return r


def _mergesort(a):
    n = len(a)
    if n == 1:
        return a, 0
    else:
        b, r1 = _mergesort(a[:n//2])
        c, r2 = _mergesort(a[n//2:])
        r = r1+r2
    i = 0
    j = 0
    d = []
    while (True):
        if (i >= len(b)):
            d += c[j:]
            break
        if (j >= len(c)):
            d += b[i:]
            break
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            print("c[j] " + str(c[j]) + " is less than " + str(b[i]))
            print("adding " + str(len(b[i:])) + " to r's " + str(r))
            r+=len(c[i:])
            j += 1
    print("returning r = " + str(r))
    return d, r
