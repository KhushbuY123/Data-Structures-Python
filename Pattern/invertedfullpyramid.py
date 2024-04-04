n=5
k=0
for i in range(n):
    for j in range(k):
        print("",end=" ")
    k=k+1
    for j in range(n-i):
        print("*",end=" ")
    print()

