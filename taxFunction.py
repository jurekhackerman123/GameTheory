from TwoPlayerClass import * 
from FindParetoAndNash import *

import numpy as np
import matplotlib.pyplot as plt 
import nashpy as nash 

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

    def GetNashEquilibrium(self): 
        tempGame = self.create_Nash_game()
        nashEquilibrium = tempGame.support_enumeration()
        nashEqList = list(nashEquilibrium)
        print(np.where(nashEqList[0][1] == True)[0][0])
        x = nashEqList[0][0][np.where(nashEqList[0][0] == True)[0][0]]
        y = nashEqList[0][1][np.where(nashEqList[0][1] == True)[0][0]]
        return x, y

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

        # # Plot the first quadratic colormap
        quad1 = ax1.pcolormesh(x, y, utiMatrixOne, cmap='plasma')
        ax1.set_title('Utility Player 1')

        # # Plot the second quadratic colormap
        quad2 = ax2.pcolormesh(x, y, utiMatrixTwo, cmap='plasma')
        ax2.set_title('Utility Player 2')


        vmin_common = min(quad1.get_clim()[0], quad2.get_clim()[0])
        vmax_common = max(quad1.get_clim()[1], quad2.get_clim()[1])

        # # Normalize the colormaps based on the common color limits
        quad1.set_clim(vmin_common, vmax_common)
        quad2.set_clim(vmin_common, vmax_common)


        cbar = fig.colorbar(quad2, ax=[ax1, ax2], orientation='vertical')

        x = np.linspace(0, 1, grating)
        y = x

        result = testPareto(utiMatrixCombined)

        ax3.pcolor(x, y, result, alpha = 1)
        # ax1.pcolor(x, y, result, alpha = 0.2)

        # Plot Nash eq
        # nashEqX, nashEqY = self.GetNashEquilibrium()
        # ax3.scatter(nashEqX, nashEqY, s = 100, color = 'red')

        plt.show()


def no_tax(action,eff,imps):
    return 0

def cutoff(action,eff,imps):
    return -10*np.heaviside(action - 0.7,1)


def simpleTry(action, eff, imp): 
    return -(eff/imp) * action


game1 = tp_game([1,1],[1,1],20,no_tax)
game2 = tp_game([1,1],[1,1],5,cutoff)
game3 = tp_game([1,1],[1,1],5,simpleTry)

game1.ShowHeatMap()
# x, y = game1.GetNashEquilibrium()
# print(x,y)


# ng1 = game1.create_Nash_game()
# ng2 = game2.create_Nash_game()
# ng3 = game3.create_Nash_game()


