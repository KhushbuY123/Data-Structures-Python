import numpy as np
arr=np.array([2,3,4,5,6,7,8,10,1]).reshape(3,3)
print(arr)
for i in range(3):
    ans=0
    maxi=0
    for j in range(3):
        ans+=arr[i][j]
        if ans>maxi:
            maxi=ans
print(maxi)
