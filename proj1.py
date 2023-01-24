import flake8
import pytest
import numpy as np

def matMult(mat1, mat2):
    if( mat1 == None ):
        print("Error: Matrix 1 is empty")
        return
    if( mat2 == None ):
        print("Error: Matrix 2 is empty")
        return
    for row in mat1:
        if(len(row) != len(mat1[0])):
            print("Error: Not a valid Matrix 1 (Rows / Columns of varying sizes")
    for row in mat2:
        if(len(row) != len(mat2[0])):
            print("Error: Not a valid Matrix 2 (Rows / Columns of varying sizes")
    if( len(mat1[0]) != len(mat2) ):
        print("Error: Invalid Matrix Size Mismatch (# columns of Matrix 1 must equal # rows of matrix 2")
        return
    else:
        result = [0] * len(mat1[0])
        for i in range(len(mat1[0])):
            result[i] = [0] * len(mat2)
            for j in range(len(mat2)):
                num = 0
                for k in range(len(mat2)):
                    num += mat1[i][k] * mat2[k][j]
                result[i][j] = num
        print(result)
            

mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]

mat2 = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]

matMult(mat1, mat2)
    