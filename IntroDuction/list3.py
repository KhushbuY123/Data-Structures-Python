def oddeven(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return(even,odd)
l=list(map(int,input("Entr the numbers").split()))
print(oddeven(l))