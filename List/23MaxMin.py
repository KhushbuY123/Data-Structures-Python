import numpy as np
arr=np.array([4,5,6,7,8,2,3,3,4]).reshape(3,3)
maxi=0
mini=0
for i in range(3):
    for j in range(3):
        if arr[i][j]>maxi:
            maxi=arr[i][j]
        else:
            mini=arr[i][j]
print(maxi,mini)