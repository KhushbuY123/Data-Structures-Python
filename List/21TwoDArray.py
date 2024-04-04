# Using Naive method
# row,col=(3,4)
# arr=[[0]*col]*row
# print(arr)
#but this will behave unexpectedly sometimes..................

# arr=[]
# rows, cols=5,5
# for i in range(rows):
#     brr=[]
#     for j in range(cols):
#         brr.append(0)
#     arr.append(brr)
# print(arr)

# numpy
import numpy as np
arr=np.array((0,0,1,0,0,0,0,0,0,0,0,0)).reshape(3,4)
print(arr[0][2])

