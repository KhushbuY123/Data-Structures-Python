from sys import maxsize

def Max_Sum(arr, sum, i, maxi):
    if i >= len(arr):
        maxi = max(sum, maxi)
        return maxi
    maxi = Max_Sum(arr, sum + arr[i], i + 2, maxi)
    maxi = Max_Sum(arr, sum, i + 1, maxi)
    return maxi

arr = [2, 1, 4,9]
i = 0
sum_val = 0
maxi = -maxsize - 1
maxi = Max_Sum(arr, sum_val, i, maxi)
print(maxi)
