for i in range(1,5+1):
    for j in range(1,5-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(5-1,0,-1):
    for j in range(1,5-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
