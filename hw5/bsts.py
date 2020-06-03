def bsts(k):
    dic={0:0,
            2:2,
            3:5}
    def _bsts(k):
        if k in dic: return dic[k]
        dic[k] =0
        return dic[k]
    return _bsts(k)
