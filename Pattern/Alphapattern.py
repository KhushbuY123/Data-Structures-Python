n=int(input("Enter the number of row"))
for i in range(n+1):
    for j in range(n-1,n-i-1,-1):
        print(chr(j+65),end=" ")
    print()

    