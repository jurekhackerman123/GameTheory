from TwoPlayerClass import * 
import random


def ShowHeatMap(taxFunction, impactList, efficiencyList):

    game = tp_game(efficiencyList, impactList, 30, taxFunction)

    game.ShowHeatMap()



def sinus(action, eff, imp): 

    return np.sin(10*action * eff / imp)

def simple(action, eff, imp): 

    return action * eff / imp

def cutOff(action, eff, imp):

    return -10*np.heaviside(action - 2 * eff / imp, 1)

def cutOffImp(action, eff, imp): 

    return -10*np.heaviside(action - 0.2 * eff / imp, 1)

def ExpFct(action, eff, imp):

    return np.exp(action)





impactList = [random.uniform(0.8, 1), random.uniform(0.8, 1)]
efficiencyList = [random.uniform(0.8, 1),random.uniform(0.8, 1)]


# ShowHeatMap(cutOffImp, impactList, efficiencyList)

def no_tax(action,eff,imps):
    return 0

def cutoff(action,eff,imps):
    return -10*np.heaviside(action - 0.5,1)

game1 = tp_game([1,1],[1,0.5],18,cutOff)
game1.ShowHeatMap()

