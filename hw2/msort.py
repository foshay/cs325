def mergesort(a):
    n = len(a)
    if n == 1:
        return a
    if n >= 2:
        b = mergesort(a[:n//2])
        c = mergesort(a[n//2:])
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
        if b[i] < c[j]:
            d.append(b[i])
            i += 1
        elif b[i] > c[j]:
            d.append(c[j])
            j += 1
        else:
            d.append(b[i]+c[j])
            i += 1
            j += 1
    return d
