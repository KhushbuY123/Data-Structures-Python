def Solve(arr, target):
    if target == 0:
        return 0
    if target < 0:
        return float('inf')  # Using infinity as a substitute for maxint
    mini = float('inf')
    for i in range(len(arr)):
        target= target - arr[i]
        minim = Solve(arr, target)
        mini = min(mini, minim)
    return mini+1

arr = [1,0,3,2]
target = 5
ans = Solve(arr, target)
print(ans)

