#%%
import random
import numpy as np
import math
import os
import numpy as np
import win32com.client as win32
import matplotlib.pyplot as plt
import pyswarm as pso

def feedStageV(currentNstage):
    
    middleStage = round(currentNstage/2)
    feedStageVec = np.array([middleStage])

    indexWhileFeedStage = 1
    upValue = middleStage + 2
    lowValue = middleStage - 2

    while indexWhileFeedStage < 5:
        
        if lowValue <= 1:
            pass
        else:
            lowValueArray = np.array([lowValue])
            feedStageVec = np.append(feedStageVec,lowValueArray)
        
        if upValue >= currentNstage:
            pass
        else:
            upValueArray = np.array([upValue])
            feedStageVec = np.append(feedStageVec,upValueArray)

        indexWhileFeedStage = indexWhileFeedStage + 1
        lowValue = lowValue - 2
        upValue = upValue + 2
    
    feedStageVec = np.sort(feedStageVec)
    
    return feedStageVec

def reactiveStageBoundary(currentNstage):
    middleStage = round(currentNstage/2)
    ub = [middleStage, currentNstage -1]
    lb = [2, middleStage + 1]
    return lb, ub

def funcAspen(x, *agrs):

    currentNstage, refluxRatioVector[indexRefluxRatio], feedStageVector[indexFeedStage] = args
    reactiveStage1, reactiveStage2 = x

    #Star ASPEN simulation
    aspen.Reinit()

    #Args value
    #Number of stage in column
    #aspen.Tree.FindNode('\Data\Blocks\CR\Input\NSTAGE').Value = currentNstage
    #Number of feed stage of oxygen 
    aspen.Tree.FindNode('\Data\Blocks\CR\Input\FEED_STAGE\OXY').Value = currentNstage - 1
    #Number of reflux ratio
    aspen.Tree.FindNode('\Data\Blocks\CR\Input\BASIS_RR').Value = refluxRatioVector[indexRefluxRatio]
    #Numeber of feed stage of glycerin
    aspen.Tree.FindNode('\Data\Blocks\CR\Input\FEED_STAGE\FEED').Value = feedStageVector[indexFeedStage]

    #Variable value
    aspen.Tree.FindNode('\Data\Blocks\CR\Input\REAC_STAGE1\#0').Value = reactiveStage1
    aspen.Tree.FindNode('\Data\Blocks\CR\Input\REAC_STAGE2\#0').Value = reactiveStage2

    #Run simulation
    aspen.Engine.Run2()

    reboilerHeatDuty = aspen.Tree.FindNode('\Data\Blocks\CR\Output\REB_DUTY').Value
    aspen.Close()

    return reboilerHeatDuty

#Vincular ASPEN V11.0
aspen = win32.Dispatch('Apwn.Document')
aspen.InitFromArchive2(os.path.abspath('C:\SimulationCR-C1.bkp')) #Modificar la ruta del archivo

#Valores máximos para Ns
maxTotalNstage = 30
minTotalNstage = 8
refluxRatioVector = np.array([0.5, 1, 2, 5, 10])

def functionAspen(minTotalNstage):
    #vectorOutput = np.zeros([5])
    #vectorInput = np.zeros([])#Fijar número más adelante

    while minTotalNstage < maxTotalNstage:
        currentNstage = minTotalNstage
        feedStageVector = feedStageV(currentNstage)
        lbyub = reactiveStageBoundary(currentNstage)
        lb = lbyub[0]
        ub = lbyub[1]
        for indexRefluxRatio in range(len(refluxRatioVector)):
            for indexFeedStage in range(len(feedStageVector)):
                args = [currentNstage, refluxRatioVector[indexRefluxRatio], feedStageVector[indexFeedStage]]
                xopt, fopt = pso(funcAspen, lb, ub,args=args)

        minTotalNstage = minTotalNstage + 3
    
    return xopt, fopt

correr = functionAspen(minTotalNstage)
# %%
