def find(a):
    a.sort()
    trips = []
    for z in a:
        hi = len(a)-1
        lo = 0
        while(hi>lo):
            if a[lo] + a[hi] == z:
                trips.append((a[lo],a[hi],z))
                hi-=1
            elif a[lo] + a[hi] < z:
                lo+=1
            else:
                hi-=1
            print([])
        print(trips)
    return trips
