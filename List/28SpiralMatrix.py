def SpiralMatrix(matrix,row,col):
row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))
matrix=[]
for i in range(row):
    sub_matrix=[]
    for j in range(col):
        sub_matrix.append(int(input("Enter the elements: ")))
    matrix.append(sub_matrix)
SpiralMatrix(matrix,row,col)