# Print Array
def Print_arr(arr,n,i):
    if i>=n:
        return
    print(arr[i])
    Print_arr(arr,n,i+1)
    # Reverse Array
    print(arr[i])
arr=[29,30,50,12,45]
n=5
i=0
Print_arr(arr,n,i)

