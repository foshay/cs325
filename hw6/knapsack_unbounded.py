def best(W, a):
    opt={}
    back={}
    n = len(a)
    def _best(W):
        if W in opt:
            return opt[W]
        curmax = 0
        ival = 0
        for i in range(n):
#            print(a[i][0])
            if a[i][0] <= W:
                #curmax = max(_best(W-a[i][0])+a[i][1],curmax)
                temp = _best(W-a[i][0])+a[i][1]
                if (temp > curmax):
                    curmax = temp
                    ival = i
#                print("curmax",curmax)
#                print("best",_best(W-a[i][0]))
        opt[W] = curmax
        back[W] = ival
        return opt[W]
    return _best(W), solution(W,a,back)

def solution(W, a, back):
    b = [0]*len(a)
    while W>0:
#        print(a[back[W]][1])
        b[back[W]]+=1
        W-=a[back[W]][0]
    return b

def test(W, a, T):
    print(a,best(W, a) == T, best(W,a))

if __name__ == "__main__":
    test(3, [(2,4),(3,5)], (5, [0,1]))
    test(3, [(1,5),(1,5)], (15, [3,0]))
    test(3, [(1,2),(1,5)], (15, [0,3]))
    test(3, [(1,2),(2,5)], (7, [1,1]))
    test(58, [(5,9),(9,18),(6,12)], (114, [2,4,2]))
    test(92, [(8,9),(9,10),(10,12),(5,6)], (109, [1,1,7,1]))
