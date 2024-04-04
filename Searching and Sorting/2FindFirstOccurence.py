def binary_seacrh(l,k):
    start=0
    end=len(l)-1
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        if l[mid]==k:
            ans=mid
            end=mid-1
        elif(l[mid]<k):
            start=mid+1
        elif(k<l[mid]):
            end=mid-1
        mid=(start+end)/2
    return ans
l=[2,3,4,4,4,4,4,4,6,7]
k=4
print(binary_seacrh(l,k))



