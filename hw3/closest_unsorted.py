import random
def find(a, x, k):
    n = len(a)
    ab = [abs(y-x) for y in a]
    q = qselect(k, ab)
    array = [a[o] for (o, m) in enumerate(ab) if m <= q]
    print(array[:k])
def qselect(k, a):
    if a == []:
        return []
    else:
        rand = random.randrange(0, len(a))
        pivot = a[rand]
        left = [x for x in a[:rand] if x<= pivot] + [x for x in a[rand+1:] if x <= pivot]
        if len(left)+1 < k:
            right = [x for x in a if x > pivot]
            return qselect(k-len(left)-1, right)
        elif len(left)+1 == k:
            return pivot
        else:
            return qselect(k, left)
