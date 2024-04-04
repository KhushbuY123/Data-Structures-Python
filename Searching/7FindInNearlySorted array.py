def fin_ele(l,k):
    start=0
    end=len(l)-1
    while(start<=end):
        mid=(start+end)//2
        if l[mid]==k:
            return mid
        if (mid-1>0 and l[mid-1]==k):
            return mid-1
        if (mid+1<len(l) and l[mid+1]==k):
            return mid+1
        if l[mid]<k:
            start=mid+2
        else:
            end=mid-2
        mid=start+end//2
l=[2,3,4,5,8,1,34,36]
k=36
ans=fin_ele(l,k)
print(ans)

