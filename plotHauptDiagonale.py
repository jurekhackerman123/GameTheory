import matplotlib.pyplot as plt
import numpy as np

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


def FindPareto(x): 

    step = 0.01

    arrayOfInterest = np.zeros((int(2/(step)), len(x)))


    test = np.arange(-0.9,1, step)

    maxList = []

    xMaxList = []
    xList = []
    yList = []

    # y = x/(1+((x)+x)**2)

    for i in range(len(test)):
        j = test[i]

        

        y = x + j

        a = np.clip(y, 0, 1)

        indices = np.where(y == a)

        xTemp = x[indices]

        print(np.shape(a))

        # tempArray = x/(1+(a+x)**2)
        xArray = xTemp/(1+(xTemp+j+xTemp)**2)
        xTest = x/(1+(x+j+x)**2)

        # arrayOfInterest[i, :] = x/(1+(x+j+x)**2)

        # tempMaxIndex = np.argmax(arrayOfInterest[i])

        tempMax = np.max(xArray)

        # tempMaxIndex = np.where(xTest == tempMax)
        tempMaxIndex = np.where(xArray == tempMax)
        # xMaxList.append(tempMax)

        tempMaxIndexOld = np.where(xTest == tempMax)

        xList.append(x[tempMaxIndexOld])
        yList.append(y[tempMaxIndexOld])

        # plt.plot(x, arrayOfInterest[i])
        # plt.plot(x[tempMaxIndex], y[tempMaxIndex])
        # plt.plot(x, xTest)

        # show funny pattern
        plt.plot(xTemp, xArray)
        plt.scatter(xTemp[tempMaxIndex], xArray[tempMaxIndex])

    return xList, yList



def PlotStuff(x): 
    test = [2,3,5,8]
    for n in test:
        y = x/(1+(n*x)**2)

        plt.plot(x, y, label = str(n) + ' player')
    plt.title('Utility vs. Action for varying number of players')
    plt.xlabel('Action')
    plt.ylabel('Utility')
    plt.legend()
    plt.show()

PlotStuff(x)
    

        
exit()
X, Y = FindPareto(x)

# print(X, Y)

plt.plot(X, Y, label ='Pareto optima developement')
plt.xlim(0,1)
plt.ylim(0,1)
plt.title('Pareto Optima for fishermen')
plt.legend()
plt.show()

