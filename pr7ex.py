from turtle import end_fill


matrix1 = [[1,2,3,4],
            [5,6,7,8],
            [1,2,3,4]]

matrix2 = [[1,2,3,4],
            [5,6,7,8],
            [1,2,3,4]]

result = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(3):
    for j in range(4):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Print addition")
for i in range(3):
    for j in range(4):
        print(format(result[i][j],"<4"),end='')
    print()