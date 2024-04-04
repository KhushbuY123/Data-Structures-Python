l=[20,50,47,21]
ans=l[0]
for i in range(len(l)):
    if ans>l[i]:
        ans=l[i]
print(ans)