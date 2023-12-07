class n_player_steps(): #n player game with heaviside as tax
    
    def __init__(self, eff_list, imp_list, grating, subtax):
        self.n = len(eff_list) #amount of players
        self.eff_list = np.array(eff_list) #list of efficiency values of players
        self.imp_list = np.array(imp_list) #list of impact values of players
        self.action_space = np.linspace(0,1,grating,endpoint = True)    
        self.subtax = subtax #must be a function subtax(efficiency, impact)
        
    def uti_null_single(self,i,action):
        return self.eff_list[i]*action/(1+(self.imp_list[i]*action)**2)-2*np.heaviside(action-self.subtax(self.eff_list[i],self.imp_list[i]),0)
        
        
    def best_response(self,i):
        res = np.array([self.uti_null_single(i,a) for a in self.action_space]) #np.array([self.uti_single(i,action) for action in self.action_space()])
        return self.action_space[np.argmax(res)]
    
    def nash_eqs(self): #returns array of actions that are a NE of the game
        return np.array([self.best_response(i) for i in range(self.n)])
    
    def total_usage(self):
        return np.sum(self.imp_list * self.nash_eqs())/np.sum(self.imp_list)
    
    def total_outcome(self):
        return np.sum(self.nash_utis())
        
    
    def nash_utis(self): #returns array of utilities at the NE
        actions = self.nash_eqs()
        usage = actions * self.imp_list
        taxes = [2*np.heaviside(actions[i]-self.subtax(self.eff_list[i],self.imp_list[i]),0) for i in range(self.n)]
        
        return self.eff_list*actions/(1+np.sum(usage)**2) - taxes
    

        
        
        
