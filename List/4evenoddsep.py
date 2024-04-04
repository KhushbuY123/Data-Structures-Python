l=[2,6,4,3,8,1,9]
even=[]
odd=[]
for i in range(len(l)):
    if l[i]%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
print(even,odd)