from TwoPlayerClass import * 

import numpy as np
import matplotlib.pyplot as plt 
import nashpy as nash 
from matplotlib.colors import ListedColormap
import copy

class tp_game: #two player game
    
    def __init__(self,efficiency_list, impact_list, grating, tax):
        self.effs = np.array(efficiency_list)
        self.imps = np.array(impact_list)
        self.tax = tax #must be a function tax(action,efficiency,impact)
        self.action_space = np.linspace(0,1,grating,endpoint = True)    
        self.full_action_space = np.moveaxis(np.swapaxes(np.array(np.meshgrid(self.action_space,self.action_space)),1,2),0,-1)
            #full_action_space[:,i,j,k,...] gives an action profile where player 1 takes ith action, player 2 the jth action, player 3 the kth action etc.
        
    def uti_matrix_2(self): #same output as uti_matrix but scalabe
        new_matrix = np.empty_like(self.full_action_space)
               
        ais = range(np.shape(self.full_action_space)[0]) #action indices
        index_space = np.moveaxis(np.array(np.meshgrid(ais,ais)),0,-1)
        
        for i in index_space:
            for j in i:
                new_matrix[j[0],j[1]] = np.array([self.uti_all(np.array([self.action_space[k] for k in j]))])
        return new_matrix
            
    
    def uti_all(self,action_profile): #array of utility for all players at given action profile 
        return np.array([self.uti_single(i,action_profile) for i in range(2)])
            
    def uti_single(self,i,action_profile): #utility for player i at given action profile
        impact_profile = self.imps * action_profile
        return self.effs[i]*action_profile[i]/(1+sum(impact_profile)**2) + self.tax(action_profile[i],self.effs[i],self.imps[i])
    
        
    def uti_matrix(self):
        temp = []
        for i in self.action_space:
            temp2 = []
            for j in self.action_space:
                temp2.append(self.uti_all(np.array([i,j])))
            temp.append(temp2)
        return np.array(temp)
    
    def create_Nash_game(self):
        um = self.uti_matrix()
        return nash.Game(um[:,:,0],um[:,:,1])

    def GetNashEquilibriumStupid(self): 
        tempGame = self.create_Nash_game()
        nashEquilibrium = tempGame.support_enumeration()
        nashEqList = list(nashEquilibrium)
        print(np.where(nashEqList[0][1] == True)[0][0])
        x = nashEqList[0][0][np.where(nashEqList[0][0] == True)[0][0]]
        y = nashEqList[0][1][np.where(nashEqList[0][1] == True)[0][0]]
        return x, y


        

    def FindNash(self): 
        matrix = self.uti_matrix()
        dim = np.shape(matrix)[0]

        # iterate over columns 
        maxListCols = []

        matOne = matrix[:,:,0]
        matTwo = matrix[:,:,1]

        for i in range(dim):
            # for columns, player two maximises his payoff
            maxListCols.append([i, np.argmax(matTwo[i])])
        
        maxListRows = []
        for j in range(dim):
            # for rows, player one maximises her payoff
            maxListRows.append([np.argmax(matOne[:,j]), j])
        
        for k in range(dim):
            if maxListCols[k] == maxListRows[k]: 
                
                indexOfInterest = maxListCols[k]
                
                return self.action_space[indexOfInterest]

        print('No Nash Equilibrium found!')
        return None




    def FindPareto(self):
        # paretoMatrix = np.ones((len(matrix), len(matrix)))
        matrix = self.uti_matrix()
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

    def ShowHeatMap(self): 
        utiMatrixCombined = self.uti_matrix()
        utiMatrixOne = utiMatrixCombined[:,:,0]
        utiMatrixTwo = utiMatrixCombined[:,:,1]

        # cols correspond to dim, because nxn matrix 
        grating = np.shape(utiMatrixOne)[0]

        x = np.linspace(0, 1, grating)
        y = x
        # X, Y = np.meshgrid(x, y)

        # Create a figure and subplots
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))#, sharey = True)

        # Plot the first quadratic colormap
        quad1 = ax1.pcolormesh(x, y, utiMatrixOne, cmap='plasma')
        ax1.set_title('Utility Player 1')

        # Plot the second quadratic colormap
        quad2 = ax2.pcolormesh(x, y, utiMatrixTwo, cmap='plasma')
        ax2.set_title('Utility Player 2')


        vmin_common = min(quad1.get_clim()[0], quad2.get_clim()[0])
        vmax_common = max(quad1.get_clim()[1], quad2.get_clim()[1])

        # Normalize the colormaps based on the common color limits
        quad1.set_clim(vmin_common, vmax_common)
        quad2.set_clim(vmin_common, vmax_common)


        cbar = fig.colorbar(quad2, ax=[ax1, ax2], orientation='vertical')

        x = np.linspace(0, 1, grating)
        y = x

        result = self.FindPareto()

        ax3.pcolor(x, y, result, alpha = 1, cmap='binary')

        # Plot Nash eq
        [nashEqX, nashEqY] = self.FindNash()
        ax3.scatter(nashEqX, nashEqY, s = 150, color = 'red', marker='s')

        ax3.text(nashEqX, nashEqY, 'NE', fontsize=8, ha='center', va='center')

        plt.show()



