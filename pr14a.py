import numpy as np  
mat1 = np.array([[7, 8, 9], [3, -1, 17], [15, 10, 21]])  
mat2 = np.array([[9, -18, 27], [11, 22, 33], [13, -26, 39]])  
mat3 = mat1 + mat2
print("The matrix addition is : \n",mat3)  
mat4 = mat1  - mat2   
print("The matrix subtraction is : \n",mat4)  
mat5 = mat1.dot(mat2)
print("The matrix multiplication is: \n",mat5)  
mat6 = mat1 / mat2
print("The matrix division is: \n",mat6)  
