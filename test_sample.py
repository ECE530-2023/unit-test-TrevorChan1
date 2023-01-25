import matMult
import pytest

mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]

mat2 = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]

def test_empty1():
    result = matMult.matMult(None,mat2)
    #Test if captures an empty mat1
    assert result == -1

def test_empty2():
    result = matMult.matMult(mat1,None)
    #Test if captures an empty mat2
    assert result == -2

def test_invalidType():
    input1 = 5
    input2 = 4
    result = matMult.matMult(input1,input2)
    #Test if captures non-list datatype inputs
    assert result == -3

def test_mismatch1():
    mat3 = [
    [1, 2, 3],
    [4, 5, 6, 7]
    ]
    result = matMult.matMult(mat3,mat2)
    #Test if captures a matrix with non-uniform length
    assert result == -4


def test_mismatch2():
    mat4 = [
    [1, 3, 5],
    [2, 4, 6, 7],
    [7, 8, 9]
    ]
    result = matMult.matMult(mat1,mat4)
    #Test if captures a matrix with non-uniform length
    assert result == -5

def test_invalidMult():
    mat5 = [
        [1, 2],
        [3, 5]
    ]
    result = matMult.matMult(mat5,mat2)
    #Test if captures a non-valid matrix multiplication operation
    assert result == -6

def test_validMult():
    result = matMult.matMult(mat1,mat2)
    #Test if computes proper result
    assert result == [[26, 35, 44], [56, 80, 104]]
