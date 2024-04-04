import numpy as np
arr=np.array([2,3,4,5]).reshape(2,2)
print(arr)
for i in range(2):
    for j in range(i+1):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
print(arr)