def Count_prime(n):
    if n<=1:
        return 0
    prime=[0]*(n+1)
    prime[0],prime[1]=1,1
    for i in range(2,n+1):
        if prime[i]==0:
            for j in range(i*i,n+1,i):
                prime[j]=1
    for i in range(2,n+1):
        if prime[i]==0:
            print(i,end=" ")
Count_prime(10)