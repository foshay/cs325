def max_wis(a):
    dic = {}
    k = len(a)
    def _max_wis(k):
        if k< 0:
            dic[k] = 0, []
            return dic[k]
        if k in dic: return dic[k]
        v1, l1 = _max_wis(k-1)
        v2, l2 = _max_wis(k-2)
        if v2+a[k]>v1:
            dic[k] = (v2+a[k]), l2+[a[k]]
        else:
            dic[k] = v1, l1
        return dic[k]

    return _max_wis(k-1)

def max_wis2(a):
    return max_wis(a)
def das():
    print('-'*80)
if __name__ == "__main__":
    print(str(max_wis([7,8,5]) == (12, [7,5]))+str(max_wis([7,8,5])))
    print(str(max_wis([7,8,5,6]) == (14, [8,6]))+str(max_wis([7,8,5,6])))
    print(str(max_wis([-1,8,10]) == (10, [10]))+str(max_wis([-1,8,10])))
    print(str(max_wis([10,10,10]) == (20, [10,10])))
    print(str(max_wis([-1,-8,-10]) == (0, [])))
    print(str(max_wis([0,0,0]) == (0, []))+str(max_wis([0,0,0])))
    print(str(max_wis([40,-10,45,100,-10,10]) == (150, [40,100,10])))



