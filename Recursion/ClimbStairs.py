def climb(n):
    if n==0 or n==1:
        return 1
    else:
        return climb(n-1)+climb(n-2)
print(climb(2))   # Leetcode 70 TLE