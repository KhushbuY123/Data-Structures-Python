a=[2,3,4,5,2,2,3,2]
l=[]
for i in range(len(a)):
    if a[i] not in l:
        l.append(a[i])
print(l)