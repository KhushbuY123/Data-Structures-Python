def Find_Sqrt(l,k):
    start=0
    end=len(l)-1
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        if l[-1]*l[-1]<k:
            return ("There is no sqrt present in this array")
        if l[mid]*l[mid]==k:
            return mid
        elif l[mid]*l[mid]>k:
            end=mid-1
        else:
            ans=l[mid]
            start=mid+1
    return ans
l=[2,4,5,6,7,8,9,10]
k=70
print(Find_Sqrt(l,k))
