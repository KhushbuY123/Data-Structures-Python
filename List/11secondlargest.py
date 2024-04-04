l=[70,50,30,80,90,20]
ans=l[0]
for i in range(len(l)):
    if ans<l[i]:
        ans=l[i]
        break
print(ans)
       