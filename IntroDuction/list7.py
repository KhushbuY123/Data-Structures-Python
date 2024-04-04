def getSecmax(l):
    if len(l)<=1:
        return None
    lar=max(l)
    slar=None
    for x in l:
        if x!=lar:
            if slar==None:
                slar=x
            else:
                slar=max(slar,x)
    return slar
l=[20,60,30,50]
print(getSecmax(l))