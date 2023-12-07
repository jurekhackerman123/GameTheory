from TwoPlayerClass import * 
import random


def ShowHeatMap(taxFunction, impactList, efficiencyList):

    game = tp_game(efficiencyList, impactList, 30, taxFunction)

    game.ShowHeatMap()



def sinus(action, eff, imp): 

    return np.sin(action * eff / imp)

def simple(action, eff, imp): 

    return action * eff / imp

def cutOff(action, eff, imp):

    return -10*np.heaviside(action - eff, 1)

def cutOffImp(action, eff, imp): 

    return -10*np.heaviside(action - imp, 1)



impactList = [random.random(), random.random()]
efficiencyList = [random.random(), random.random()]


# ShowHeatMap(cutOffImp, impactList, efficiencyList)

def no_tax(action,eff,imps):
    return 0

def cutoff(action,eff,imps):
    return -10*np.heaviside(action - 0.7,1)

game1 = tp_game(impactList,efficiencyList,5,cutOff)
game1.ShowHeatMap()

