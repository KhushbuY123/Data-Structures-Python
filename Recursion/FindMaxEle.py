# Find maximum Element in the given array....
def find_max(arr,n,i,maxi):
    if i>=n:
        return maxi
    maxi=max(maxi,arr[i])
    return find_max(arr,n,i+1,maxi)
arr=[20,50,12,50,345]
n=5
i=0
maxi=0
max_element = find_max(arr, n, i, maxi)
print("Maximum element in the array:", max_element)


