def longest(a):
    r, b = _longest(a)

    return b


def _longest(t):
    if t == []:
        return 0, 0

    l, b1 = _longest(t[0])
    r, b2 = _longest(t[2])
    b3 = max(b1,b2,(l+r))
    if l >= r:
        return (l+1), b3
    else:
        return (r+1), b3
