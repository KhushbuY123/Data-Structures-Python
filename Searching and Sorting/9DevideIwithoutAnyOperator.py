def devide(m,n):
    if m==0:
        return 0
    if n==0:
        return("This could generate infinite value")
    sign=-1 if (m<0) ^ (n<0) else 1
    n=abs(n)
    m=abs(m)
    start=0
    end=m
    ans=0
    while(start<=end):
        mid=(start+end)//2
        if abs(mid*n)==m:
            ans=mid
            break
        elif abs(mid*n)>m:
            end=mid-1
        else:
            ans=mid
            start=mid+1
        mid=(start+end)//2
    if sign==1:
        return min(ans,2**31-1)
    else:
        return max(-ans,-2**31)
n=-1
m=3
print(devide(m,n))
