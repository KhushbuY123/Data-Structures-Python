def Is_Sorted(arr,n,i):
    if i==n-1:
        return True
    if(arr[i+1]<arr[i]):
        return False
    return Is_Sorted(arr,n,i+1)
arr=[4,3,1,2,4,4]
n=len(arr)
i=0
isSorted=Is_Sorted(arr,n,i)
if(isSorted):
    print("Array is sorted")
else:
    print("Array is not sorted")
