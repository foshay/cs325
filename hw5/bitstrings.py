def num_no(k):
    dic = {0:1,
            1:1,
            2:3,
            3:5}
    def _num_no(k):
        if k in dic: return dic[k]
        dic[k] = _num_no(k-1) + _num_no(k-2)
        return dic[k]

    return _num_no(k)
def num_yes(k):
    dic = {0:0,
            1:0,
            2:1,
            3:3}
    def _num_yes(k):
        if k in dic: return dic[k]
        dic[k] = _num_yes(k-1) + _num_yes(k-2)
        return dic[k]
    return _num_yes(k)

if __name__ == "__main__":
    print(num_yes(3) == 3)
    print(num_yes(3))
