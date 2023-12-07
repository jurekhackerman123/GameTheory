from TwoPlayerClass import * 
import random


def ShowHeatMap(taxFunction, impactList, efficiencyList):

    game = tp_game(efficiencyList, impactList, 30, taxFunction)

    game.ShowHeatMap()


def sinusImp(eff, imp):

    return np.sin(imp)

def sinusEff(eff, imp): 

    return np.sin(eff)

def simple(eff, imp): 

    return eff / imp

def cutOff(eff, imp):

    return -10*np.heaviside(0.5 - eff, 1)

def cutOffImp(eff, imp): 

    return -10*np.heaviside(imp - 0.5, 1)



impactList = [random.random(), random.random()]
efficiencyList = [random.random(), random.random()]


# ShowHeatMap(cutOffImp, impactList, efficiencyList)

def no_tax(action,eff,imps):
    return 0

def cutoff(action,eff,imps):
    return -10*np.heaviside(action - 0.7,1)

game1 = tp_game([1,1],[1,1],5,no_tax)
game1.ShowHeatMap()

