def lessthan(l,x):
    # res=[]
    # for i in l:
    #     if i<=x:
    #         res.append(i)
    # return res
    res=[i for i in l if i<=x]
    return res
l=[10,2,1,4,80,30,6,50]
x=8
print(lessthan(l,x))
