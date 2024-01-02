from TwoPlayerClass import * 
import random


def ShowHeatMap(taxFunction, impactList, efficiencyList):

    game = tp_game(efficiencyList, impactList, 30, taxFunction)

    game.ShowHeatMap()



def sinus(action, eff, imp): 

    return -np.sin(10*action * eff / imp)

def quadratic(action, eff, imp): 
    '''
    interesting, for 0.5 * ..., we have two pareto optima 
    '''
    return -(0.5 * action * imp / eff)**2


def simple(action, eff, imp): 

    return -0.1 * action * eff / imp

def simple2(action, eff, imp): 
    '''
    for 0.18*... we get two NE!!
    '''
    return -0.2 * action * eff / imp

def cutOff(action, eff, imp):

    return -10*np.heaviside(action - 0.55 * eff / (imp), 1)



def ExpFct(action, eff, imp):
    '''
    for different impact, well visible! 
    '''
    return -0.05 * np.exp(action * eff / imp)


# ShowHeatMap(cutOffImp, impactList, efficiencyList)

def no_tax(action,eff,imps):
    return 0

# indep of eff and imp
def cutoff(action,eff,imps):
    return -10*np.heaviside(action - 0.5,1)


# same eff and imp
game1 = tp_game([1,0.5],[1,1],30,no_tax)
game1.ShowHeatMap()

# # diff efficiency
# game2 = tp_game([1,0.5],[1,1],30,cutOff)
# game2.ShowHeatMap()

# # diff impact 
# game3 = tp_game([1,1],[1,0.5],30,cutOff)
# game3.ShowHeatMap()


# vary functions: 
# game = tp_game([1,1],[1,0.5],20,simple)
# game.ShowHeatMap()

# game = tp_game([1,1],[1,0.5],20,simple)
# game.ShowHeatMap()

# game = tp_game([1,1],[1,0.5],20,simple2)
# game.ShowHeatMap()

