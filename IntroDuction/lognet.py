def longest(a):
    res=count=0
    for i in a:
        if i==1:
            count+=1
            res=max(count,res)
        else:
            count=0
    return res
a=[1,0,0,1,1,1,0,0]
print(longest(a))