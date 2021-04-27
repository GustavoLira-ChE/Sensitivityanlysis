import random
import numpy as np
import math
import os
import numpy as np
import win32com.client as win32
import matplotlib.pyplot as plt

#Vincular ASPEN V11.0
aspen = win32.Dispatch('Apwn.Document')
aspen.InitFromArchive2(os.path.abspath('C:\ReacDes.bkp')) #Modificar la ruta del archivo

#Valores máximos para Ns, 
maxTotalNstage = 30
minTotalNstage = 8
refluxRatioVector = np.array([0.5, 1, 2, 5, 10])

def feedStageV(currentTotalNstage):
    
    middleStage = round(currentTotalNstage/2)
    feedStageVector = np.array([middleStage])

    indexWhileFeedStage = 1
    upValue = middleStage + 2
    lowValue = middleStage - 2

    while indexWhileFeedStage < 5:
        
        if lowValue <= 1:
            pass
        else:
            lowValueArray = np.array([lowValue])
            feedStageVector = np.append(feedStageVector,lowValueArray)
        
        if upValue >= currentTotalNstage:
            pass
        else:
            upValueArray = np.array([upValue])
            feedStageVector = np.append(feedStageVector,upValueArray)

        indexWhileFeedStage = indexWhileFeedStage + 1
        lowValue = lowValue - 2
        upValue = upValue + 2
    
    feedStageVector = np.sort(feedStageVector)
    
    return feedStageVector


def functionAspen(minTotalNstage):
    vectorOutput = np.zeros([5])
    vectorInput = np.zeros([])#Fijar número más adelante
    aspen.Reinit()

    while indexWhile < 30:
        currentTotalNstage = minTotalNstage
        Application.Tree.FindNode("\Data\Blocks\CR\Input\NSTAGE").Value = currentTotalNstage
        Application.Tree.FindNode("\Data\Blocks\CR\Input\FEED_STAGE\OXY").Value = currentTotalNstage - 1
        feedStageVector = feedStageV
        
        for indexRefluxRatio in range(refluxRatioVector):
            Application.Tree.FindNode("\Data\Blocks\CR\Input\BASIS_RR").Value = refluxRatioVector[indexRefluxRatio]
            

        Application.Tree.FindNode("\Data\Blocks\CR\Input\REAC_STAGE2\#0").Value = currentTotalNstage - 1
        
        indexWhile = indexWhile + 3