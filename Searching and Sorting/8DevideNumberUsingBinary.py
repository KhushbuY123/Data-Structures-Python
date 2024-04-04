def devide(n,m):
    start=0
    end=abs(m)
    ans=1
    while(start<=end):
        mid=(start+end)/2
        if abs(mid*n)==abs(m):
            return mid
        if abs(mid*n)>abs(m):
            end=mid-1
        else:
            ans=mid
            start=mid+1
        mid=(start+end)/2
    if ((n<0 and m<0) or (n>0 and m>0)):
        return ans
    else:
        return -ans
    # return ans
m=22
n=-6
ans=devide(n,m)
print(ans)