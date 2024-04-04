def subset_sum(sm,arr,n):
    subset=[[-1 for i in range(sm+1)] for j in range(n+1)]
    for i in range(n+1):
        subset[i][0]=1
    for j in range(1,sm+1):
        subset[0][j]=
    for i in range(1,n+1):
        for j in range(1,sm+1):
            if(arr[i-1]<=j):
                subset[i][j]=subset[i-1][j] or subset[i-1][j-arr[i-1]]
            if(arr[i-1]>j):
                subset[i][j]=subset[i-1][j]
    return subset[n][sm]
def FindSubset(n):
    a=[]
    for i in range(1,n):
        a.append(i)
    return a 
n=7
arr=FindSubset(n)
print(subset_sum(n,arr,len(arr)))



