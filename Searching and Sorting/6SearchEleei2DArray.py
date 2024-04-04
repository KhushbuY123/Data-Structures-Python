n=int(input("Enter row number"))
m=int(input("Enter columun number"))
arr=[]
k=9
for i in range(n):
    l=[]
    for j in range(m):
        l.append(int(input("Enter the numbers")))
    arr.append(l)
print(arr)
def Find_ArrayEle(arr,k):
    s=0
    e=(n*m)-1
    while(s<=e):
        mid=(s+e)//2
        rowindex=mid//m
        colindex=mid//n
        res=arr[rowindex][colindex]
        if k==res:
            return(rowindex,colindex)
        elif res>k:
            end=mid-1
        else:
            start=mid+1
    return False
print(Find_ArrayEle(arr,k))
