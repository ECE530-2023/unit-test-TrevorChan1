Trevor Chan U94717228

# EC530 Project 1

matMult.py is the file that contains the matMult function that takes in two lists as inputs and outputs their matrix multiplication result, or an error code otherwise.

test_sample.py contains the python tests that tests each of the error cases as well as a successful run of the matrix multiplication, checking that the output is what it should be.

actions.yaml contains the Github Actions automation of the project. In it, I have made it so that Github Actions will run pytest and flake8 on any Git push. The actions will fail if any of the pytest test cases have not succeeded, and it will give a success if flake8 flags any bad syntax although it will print out the messages on what should be changed.