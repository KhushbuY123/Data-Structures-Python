def binary_search(arr,k,start,end):
    if(start>end):
        return -1
    mid=(start+end)//2
    if(k==arr[mid]):
        return mid
    elif(k>arr[mid]):
        return binary_search(arr,k,mid+1,end)
    else:
        return binary_search(arr,k,start,mid-1)
arr=[9,11,12,13,45,67,89]
start=0
end=len(arr)
k=12
ans=binary_search(arr,k,start,end)
print(ans)
