i=1;j=0
while(i<=5):
    while(j<=i-1):
        print(i,"*",end="")
        j+=1
    print("\r")
    j=0;i+=1