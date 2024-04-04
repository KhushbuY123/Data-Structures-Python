l=[2,5,8,7,4,2]
m=[2,6,8,1]
res=[]
for i in range(len(l)):
    ans=l[i]
    for j in range(len(m)):
        if ans==m[j]:
            res.append(ans)
print(res)
