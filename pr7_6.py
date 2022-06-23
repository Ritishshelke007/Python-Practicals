
print("Enter values for matrix 1 : ")
matrix1 = [[int(input()) for i in range(4)] for j in range(3)]
print("Matrix 1 : ")
for i in range(3):
    for j in range(4):
        print(format(matrix1[i][j],"<3"),end=" ")
    print()

print("Enter values for matrix 2 : ")
matrix2 = [[int(input()) for i in range(4)] for j in range(3)]
print("Matrix 2 : ")
for i in range(3):
    for j in range(4):
        print(format(matrix2[i][j],"<3"),end=" ")
    print()

result_matrix = [[0 for i in range(4)]for j in range(3)]
for i in range(3):
    for j in range(4):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j] 

#print result 
print("Addition of matrix : ")
for i in range(3):
    for j in range(4):
        print(format(result_matrix[i][j],"<3"),end=" ")
    print()
