import math
def kmergesort(k, a):
    n = len(a)
    step = n//k
    if n == 1:
        return a
    b = []
    if n >= k:
        print("SHIT")
        for i in range(k-1):
            print("FUCK")
            b[i] = kmergesort(k,a[i*step:(i+1)*step])
            print(str(i*(n//k)) + " " + str((i+1)*(n//k)) + " " + str(b[i]))
    i = [0]*k
    k = 0
    d = []
    while (True):
        k = math.inf
        for j in range(len(i)):
            if i[j] < len(i)-1:
                break

        break
    return d
