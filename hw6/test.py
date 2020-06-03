def best(W, a):
    opt={}
    back={}
    n = len(a)
    def _best(W,k,i):
        if (W, k) in opt:
            return opt[W,k]
        if W == 0 or k == 0:
            return 0
        #for j in range(a[k][2]):
        if a[k][0] > W:
            opt[W,k] = _best(W,k-1,a[k-1][2])
        else:
            notake = _best(W, k-1,a[k-1][2])
            if i > 1:
                take = _best(W-a[k][0],k,(i-1))+a[k][1]
                print("remaining items at", a[k], i)
            else:
                take = _best(W-a[k][0],k-1,a[k-1][2])+a[k][1]
            if take > notake:
                opt[W,k] = take
                back[W,k] = notake
            else:
                opt[W,k] = notake
#                print("curmax",curmax)
#                print("best",_best(W-a[i][0]))
        #opt[W,k] = curmax
        #back[W,k] = ival
#        print(a[:k+1],opt[W,k])
        print(opt[W,k])
        return opt[W,k]
    return _best(W,n-1,a[n-1][2])#, solution(W,a,back)

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
    test(3, [(2,4,2),(3,5,3)], (5, [0,1]))
    test(3, [(1,5,2),(1,5,3)], (15, [2,1]))
    test(3, [(1,5,1),(1,5,3)], (15, [1,2]))
    test(20, [(1,10,6),(3,15,4),(2,10,3)], (130, [6,4,1]))
    #test(58, [(5,9),(9,18),(6,12)], (114, [2,4,2]))
