import matplotlib.pyplot as plt
import numpy as np
from TwoPlayerClass import * 
import copy




import numpy as np

def testPareto(matrix):
    paretoMatrix = np.ones((len(matrix), len(matrix)))

    for i in range(len(matrix)):
        for j in range(len(matrix)):

            payOffOne, payOffTwo = matrix[i, j]

            tempMatrix = copy.deepcopy(matrix)
            tempMatrix[i, j] = 0, 0


            indices = np.where(tempMatrix[:,:,0] >= payOffOne)


            # if we do not find a value that is higher than the current value, it automatically is a PO
            if np.shape(tempMatrix[indices])[0] == 0:
                paretoMatrix[i, j] = True
                continue

            # if any value is bigger or eq to payoff one *and* at the same time, bigger or eq to payoff two, 
            # it cannot be a pareto optimum 

            for k in range(len(tempMatrix[indices][:])):
                if np.any(tempMatrix[indices][k][1] >= payOffTwo):
                    if np.any(tempMatrix[indices][k][1] > payOffTwo) or np.any(tempMatrix[indices][k][0] > payOffOne):
                        paretoMatrix[i, j] = False
                    else: 
                        paretoMatrix[i, j] = True



    return paretoMatrix


def FindNash(matrix): 
    print(np.shape(matrix))
    dim = np.shape(matrix)[0]
    # iterate over columns 
    maxListCols = []

    matOne = matrix[:,:,0]
    matTwo = matrix[:,:,1]

    for i in range(dim):
        # for columns, player two maximises his payoff
        print(matrix[i])
        print(np.argmax(matOne[i]))
        maxListCols.append([i, np.argmax(matOne[i])])
    
    maxListRows = []
    for j in range(dim):
        maxListRows.append([np.argmax(matOne[:,j]), j])
    
    for k in range(dim):
        if maxListCols[k] == maxListRows[k]: 
            indexOfInterest = maxListCols[k]
            return matrix[indexOfInterest,:]

    return None


def no_tax(action,eff,imps):
    return 0

testMat = [[[1,1],[1,2],[3,3]], [[4,3],[5,5],[9,9]], [[7,7],[7,3],[1,1]]]

game2 = tp_game([1,1],[1,1],3,no_tax)
# print(game2.uti_matrix)
test = FindNash(game2.uti_matrix())