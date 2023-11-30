import numpy as np


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