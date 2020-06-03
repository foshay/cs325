def best(W, a):
    opt={(0,0):(0,0)}
    n = len(a)
    def _best(W,k):
        if (W, k) in opt:
            return opt[W,k][0]
        if W <= 0 or k < 0 or a[k][1] <= 0:
            opt[W,k] = (0,0)
            return opt[W,k][0]
        curmax=0
        curbak=0
        for j in range(a[k][2],-1,-1):
            if a[k][0]*j <= W:
                take = _best(W-(a[k][0]*j),k-1)+(a[k][1]*j)
                if take >= curmax:
                    curmax = take
                    curbak = j
            else:
                j-= (a[k][0]*j - W)//a[k][0]
        opt[W,k] = (curmax,curbak)
        return opt[W,k][0]
    return _best(W,n-1), solution(W,a,opt,n-1)

def solution(W,a,opt,k):
    if k <= -1:
        return []
    return solution(W-a[k][0]*opt[W,k][1], a, opt, k-1) + [opt[W,k][1]]

def test(W, a, T):
    print(a,best(W, a) == T, best(W,a))

if __name__ == "__main__":
    test(3, [(2,4,2),(3,5,3)], (5, [0,1]))
    test(3, [(1,5,2),(1,5,3)], (15, [2,1]))
    test(3, [(1,5,1),(1,5,3)], (15, [1,2]))
    test(20, [(1,10,6),(3,15,4),(2,10,3)], (130, [6,4,1]))
    test(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)], (236, [6,7,3,7,2]))
