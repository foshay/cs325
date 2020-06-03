def nbesta(a, b):
    c = []
    for i in a:
        for j in b:
            c.append((i,j))
    d = sorted(c, key=lambda tup: tup[0]+tup[1])
    return d[:len(a)]

def nbestb(a, b):
    return b
def nbestc(a, b):
    return a+b
