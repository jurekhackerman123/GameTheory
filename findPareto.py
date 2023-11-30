import matplotlib.pyplot as plt
import numpy as np
from TwoPlayerClass import * 

# Generate data for the plots
x = np.linspace(0, 1, 100)
y = x
X, Y = np.meshgrid(x, y)


Z1 = X/(np.ones_like(X)+(X+Y)**2)  # Quadratic colormap 1

Z2 = Y/(1+(X+Y)**2)  # Quadratic colormap 1

# Create a figure and subplots
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))#, sharey = True)

# # Plot the first quadratic colormap
# quad1 = ax1.pcolormesh(X, Y, Z1, cmap='plasma')
# ax1.set_title('Utility Player 1')

# # Plot the second quadratic colormap
# quad2 = ax2.pcolormesh(X, Y, Z2, cmap='plasma')
# ax2.set_title('Utility Player 2')


# vmin_common = min(quad1.get_clim()[0], quad2.get_clim()[0])
# vmax_common = max(quad1.get_clim()[1], quad2.get_clim()[1])

# # Normalize the colormaps based on the common color limits
# quad1.set_clim(vmin_common, vmax_common)
# quad2.set_clim(vmin_common, vmax_common)


# cbar = fig.colorbar(quad2, ax=[ax1, ax2], orientation='vertical')
# #cbar.set_label('Utility')

# #plt.subplots_adjust(wspace=0.5)

# #plt.tight_layout()

# plt.show()
# #for i in range(10)
# plt.plot(x,x/(1+(x+x)**2))
# plt.plot(x,x/(1+((0.1+x)+x)**2))
# plt.plot(x,x/(1+((0.2+x)+x)**2))
# plt.plot(x,x/(1+((0.3+x)+x)**2))
#plt.show()


def test(a,b,c): 
    return 0


def testPareto(matrix): 


    paretoMatrix = np.ones((len(matrix), len(matrix)))

    for i in range(len(matrix)): 
        for j in range(len(matrix)): 

            if i == 0 and j == 1: 
                print('test')

            payOffOne, payOffTwo = matrix[i, j]

            for k in range(len(matrix)):
                for l in range(len(matrix)): 
                    if k == i or l == j: 
                        continue

                    otherPayOffOne, otherPayOffTwo = matrix[k, l]

                    if otherPayOffOne >= payOffOne and otherPayOffTwo >= payOffTwo: 
                        paretoMatrix[i, j] = False
                        # print(otherPayOffOne , 'bigger',  payOffOne, 'and',  otherPayOffTwo, 'beq' , otherPayOffOne)

                        continue
            

    
    return paretoMatrix


game = tp_game([1,1], [1,1], 20, test)

matrix = game.uti_matrix()

# matrix = np.array([[(3,3), (5,1)], [(1,5), (1,1)]])

testMatrix = testPareto(matrix)

print(matrix)

print(testMatrix)












# OTHER APPROACHs

def FindPareto(x): 

    step = 0.1

    test = np.arange(-0.9,1, step)

    xList = []
    yList = []


    for i in range(len(test)):
        j = test[i]

        

        y = x + j

        a = np.clip(y, 0, 1)
        

        indices = np.where(y == a)

        a = a[indices]

        xTemp = x[indices]

        # plt.plot(xTemp, a)
        
        xArray = xTemp/(1+(xTemp+j+xTemp)**2)
        xTest = x/(1+(x+j+x)**2)

        tempMax = np.max(xArray)

        tempMaxIndex = np.where(xArray == tempMax)

        tempMaxIndexOld = np.where(xTest == tempMax)

        xList.append(x[tempMaxIndexOld])
        yList.append(y[tempMaxIndexOld])

        # show funny pattern
        # plt.plot(xTemp, xArray)
        # plt.scatter(xTemp[tempMaxIndex], xArray[tempMaxIndex])

    xList2 = []
    yList2 = []

    for i in range(len(test)):
        j = test[i]

        y = x + j

        a = np.clip(y, 0, 1)

        indices = np.where(y == a)

        a = a[indices]

        xTemp = x[indices]

        yTemp = y[indices]

        xArray = a/(1+(xTemp+j+xTemp)**2)
        xTest = y/(1+(y+x)**2)

        tempMax = np.max(xArray)

        tempMaxIndex = np.where(xArray == tempMax)

        tempMaxIndexOld = np.where(xTest == tempMax)

        xList2.append(x[tempMaxIndexOld])
        yList2.append(y[tempMaxIndexOld])

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


