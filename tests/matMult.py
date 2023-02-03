import tracemalloc
import logging
import cProfile


# Flake8 used in Github Actions
def matMult(mat1, mat2):
#test
#fuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcslafuckjahcusahcsla
    tracemalloc.start()

    # Set logging to log any errors/warnings to matMult.log
    logging.basicConfig(filename='matMult.log',
                        filemode='w',
                        format='%(asctime)s %(levelname)s - %(message)s')

    # Log basic info about inputs
    logging.info('input 1: %d', mat1)
    logging.info('input 2: %d', mat2)

    # Error -1: Checking if mat1 input is empty
    if (mat1 is None):
        print('Error: Matrix 1 is empty')
        logging.error('Matrix 1 is empty')
        return -1

    # Error -2: Checking if mat2 input is empty
    if (mat2 is None):
        print('Error: Matrix 2 is empty')
        logging.error("Matrix 2 is empty")
        return -2

    # Error -3: Checking if the input datatypes are valid (both lists)
    if (type(mat1) != list or type(mat2) != list):
        print("Error: Invalid input datatype")
        logging.error("Invalid input datatype")
        return -3

    # Error -4: Checking if mismatch in lengths of rows / columns in mat1
    for row in mat1:
        if (len(row) != len(mat1[0])):
            print("Error: Input 1 has varying row sizes")
            logging.error("Error: Input 1 has varying row sizes")
            return -4

    # Error -5: Checking if mismatch in lengths of rows / columns in mat2
    for row in mat2:
        if (len(row) != len(mat2[0])):
            print("Error: Input 2 has varying row sizes")
            logging.error("Error: Input 2 has varying row sizes")
            return -5

    # Error -6: Checking if the # columns in mat1 = # rows in mat2
    if (len(mat1[0]) != len(mat2)):
        logging.error("Error: Matrix Size Mismatch")
        print("Error: Matrix Size Mismatch")
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
            print("Exception %s", e)


mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]

mat2 = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]

print(matMult(None, mat2))
