import matplotlib.pyplot as plt
import numpy as np
from TwoPlayerClass import * 
import copy
# Generate data for the plots
x = np.linspace(0, 1, 100)
y = x
X, Y = np.meshgrid(x, y)


Z1 = X/(np.ones_like(X)+(X+Y)**2)  # Quadratic colormap 1

Z2 = Y/(1+(X+Y)**2)  # Quadratic colormap 1





def test(a,b,c): 
    return 0




import numpy as np

def testPareto(matrix):
    paretoMatrix = np.ones((len(matrix), len(matrix)))

    for i in range(len(matrix)):
        for j in range(len(matrix)):

            if i == 0 and j == 3: 
                print('test')

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


game = tp_game([1,1], [1,1], 20, test)

matrix = game.uti_matrix()

# matrix = np.array([[(3,3), (5,1), (2,2), (8,8)], [(2,1), (5,5), (7,3), (8,8)], [(1,5), (1,1), (2,3), (8,8)], [(4,5), (2,2), (2,5), (6,8)]])

result = testPareto(matrix)
# print(result)

result = np.flip(result, axis=1)

# testMatrix = testPareto(matrix)

# print(matrix)

# print(testMatrix)


# plt.pcolor(result)
# # plt.
# plt.show()


# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))#, sharey = True)

# # Plot the first quadratic colormap
quad1 = ax1.pcolormesh(X, Y, Z1, cmap='plasma')
ax1.set_title('Utility Player 1')

# # Plot the second quadratic colormap
quad2 = ax2.pcolormesh(X, Y, Z2, cmap='plasma')
ax2.set_title('Utility Player 2')


vmin_common = min(quad1.get_clim()[0], quad2.get_clim()[0])
vmax_common = max(quad1.get_clim()[1], quad2.get_clim()[1])

# # Normalize the colormaps based on the common color limits
quad1.set_clim(vmin_common, vmax_common)
quad2.set_clim(vmin_common, vmax_common)


cbar = fig.colorbar(quad2, ax=[ax1, ax2], orientation='vertical')

x = np.linspace(0, 1, 20)
y = x

ax2.pcolor(x, y, result, alpha = 0.2)
ax1.pcolor(x, y, result, alpha = 0.2)

plt.show()




exit()
# OTHER APPROACHs

def FindPareto(x): 

    step = 0.1

    test = np.arange(-1,1, step)

    xList = []
    yList = []


    for i in range(len(test)):
        j = test[i]

        y = x + j

        a = y#np.clip(y, 0, 1)
        

        indices = np.where(y == a)

        a = a[indices]

        xTemp = x[indices]

        print('len indices: ', (indices))
        
        print('len a: ', len(a))

        # plt.plot(xTemp, a)
        
        xArray = xTemp/(1+(a+xTemp)**2)
        xTest = x/(1+(x+j+x)**2)

        # plt.plot(xTemp, xArray)

        print('len xArray', len(xArray))

        tempMax = np.max(xArray)

        tempMaxIndex = np.argmax(xArray)

        originalIndex = indices[0][tempMaxIndex]

        # tempMaxIndex = np.where(xArray == tempMax)

        # tempMaxIndexOld = np.where(xTest == tempMax)

        xList.append(x[originalIndex])
        yList.append(y[originalIndex])

        # show funny pattern
        plt.plot(xTemp, xArray)
        plt.scatter(x[originalIndex], xTest[originalIndex])

    xList2 = []
    yList2 = []

    # for i in range(len(test)):
    #     j = test[i]

    #     y = x + j

    #     a = y#np.clip(y, 0, 1)

    #     indices = np.where(y == a)

    #     a = a[indices]

    #     xTemp = x[indices]

    #     yTemp = y[indices]

    #     xArray = a/(1+(a+xTemp)**2)
    #     xTest = y/(1+(y+x)**2)

    #     tempMax = np.max(xArray)

    #     tempMaxIndex = np.argmax(xArray)

    #     originalIndex = indices[0][tempMaxIndex]

    #     tempMaxIndexOld = np.where(xTest == tempMax)

    #     xList2.append(x[originalIndex])
    #     yList2.append(y[originalIndex])

        # plt.plot(x, arrayOfInterest[i])
        # plt.plot(x[tempMaxIndex], y[tempMaxIndex])
        # plt.plot(x, xTest)

        # show funny pattern
        # plt.plot(xTemp, xArray)
        # plt.scatter(xTemp[tempMaxIndex], xArray[tempMaxIndex])






    return xList, yList, xList2, yList2



        

X, Y, X2, Y2 = FindPareto(x)

# print(X, Y)

plt.plot(X, Y, label ='Pareto optima developement')
plt.plot(X2, Y2)
# plt.xlim(0,1)
# plt.ylim(0,1)
plt.title('Pareto Optima for fishermen')
plt.legend()
plt.show()


