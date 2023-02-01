import flake8
import pytest
import tracemalloc
import numpy as np
import logging
import cProfile
import re


def matMult(mat1, mat2):
    tracemalloc.start()
    logging.basicConfig(filename='matMult.log', filemode='w', format='%(asctime)s %(levelname)s - %(message)s')

    logging.info('input 1: %d',mat1)
    logging.info('input 2: %d', mat2)
    #Error code -1: Checking if mat1 input is empty
    if( mat1 == None ):
        print('Error: Matrix 1 is empty')
        logging.error('Matrix 1 is empty')
        return -1

    #Error code -2: Checking if mat2 input is empty
    if( mat2 == None ):
        print('Error: Matrix 2 is empty')
        logging.error("Matrix 2 is empty")
        return -2
    
    #Error code -3: Checking if the input datatypes are valid (both lists)
    if( type(mat1) != list or type(mat2) != list):
        print("Error: Invalid input datatype")
        logging.error("Invalid input datatype")
        return -3

    #Error code -4: Checking if mismatch in lengths of rows / columns in mat1
    for row in mat1:
        if(len(row) != len(mat1[0])):
            print("Error: Not a valid Matrix 1 (Rows / Columns of varying sizes")
            logging.error("Error: Not a valid Matrix 1 (Rows / Columns of varying sizes")
            return -4

    #Error code -5: Checking if mismatch in lengths of rows / columns in mat2
    for row in mat2:
        if(len(row) != len(mat2[0])):
            print("Error: Not a valid Matrix 2 (Rows / Columns of varying sizes")
            logging.error("Error: Not a valid Matrix 2 (Rows / Columns of varying sizes")
            return -5
    
    #Error code -6: Checking if the sizes work (if the # columns in mat1 = # rows in mat2)
    if( len(mat1[0]) != len(mat2) ):
        logging.error("Error: Invalid Matrix Size Mismatch (# columns of Matrix 1 must equal # rows of matrix 2")
        print("Error: Invalid Matrix Size Mismatch (# columns of Matrix 1 must equal # rows of matrix 2")
        return -6

    else:
        try:
            result = [0] * len(mat1)
            for i in range(len(mat1)):
                result[i] = [0] * len(mat2)
                for j in range(len(mat2)):
                    num = 0
                    for k in range(len(mat2)):
                        num += mat1[i][k] * mat2[k][j]
                    result[i][j] = num
            logging.debug("Successfully ran Matrix Multiplication")
            cProfile.run('re.compile("foo|bar")')
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            print("[ Top 10 ]")
            for stat in top_stats[:10]:
                print(stat)
            return result
        except Exception as e:
            logging.error("Exception occured", exc_info=True)
        
    
            

mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]

mat2 = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]

print(matMult(mat1, mat2))
    