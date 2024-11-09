def Waivy_Matrix(matrix, row, col):
    for i in range(row):
        if i % 2 == 0:
            for j in range(col):
                print(matrix[i][j], end=" ")
        else:
            for j in range(col - 1, -1, -1):
                print(matrix[i][j], end=" ")
        print()
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix = []
for i in range(row):
    sub_matrix = []
    for j in range(col):
        sub_matrix.append(int(input("Enter the elements: ")))
    matrix.append(sub_matrix)

Waivy_Matrix(matrix, row, col)
