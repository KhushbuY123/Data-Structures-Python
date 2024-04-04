def onlyodd(l):
    a=0
    i=0
    while(i<len(l)):
        b=l.count(i)
        if b%2!=0:
            a=i
        i=i+1
    return a
l=[2,4,6,6,2,5,5,4]
print(onlyodd(l))

def findodd(l):
    res=0
    for x in l:
     res=res^x
    return res
l=[2,2,4,5,4,5,6]
print(findodd(l))

        