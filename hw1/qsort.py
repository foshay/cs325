def sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]
def sorted(t):
    if t == []:
        return []
    else:
        return sorted(t[0]) + [t[1]] + sorted(t[2])
    return
def search(t, x):
    if _search(t, x):
        return True
    else:
        return False
def insert(t, x):
    q = _search(t, x)
    print(id(t)-id(_search(t,x)))
    return
def _search(t, x):
    if t == []:
        return t
    if t[1] == x:
        return t
    else:
        return _search(t[0], x) + _search(t[2], x)
