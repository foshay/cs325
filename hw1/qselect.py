import random
def qselect(k, a):
    print(a)
    if a == []:
        return []
    else:
        rand = random.randrange(0, len(a))
        pivot = a[rand]
        #print("pivot is " + str(pivot))
        #print(a)
        left = [x for x in a[:rand] if x <= pivot] + [x for x in a[rand+1:] if x <= pivot]
        right = [x for x in a if x > pivot]
        #print("left " + str(left) + " is of len " + str(len(left)))
        #print("right " + str(right) + " is of len " + str(len(right)))
        #print("k " + str(k))
        if len(left)+1 < k:
            return qselect(k-len(left)-1 ,right)
        elif len(left)+1 == k:
            return pivot
        else:
            return qselect(k, left)
