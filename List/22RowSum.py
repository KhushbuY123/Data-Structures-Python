a=[]
for i in range(3):
    b=[]
    for j in range(4):
        b.append(int(input("")))
    a.append(b)
print(a)
for i in range(3):
    ans=0
    for j in range(4):
        ans+=a[i][j]
    print(ans)