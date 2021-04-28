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


def functionAspen(TotalNstage):
    vectorOutput = np.zeros([5])
    vectorInput = np.zeros([])#Fijar número más adelante

    while indexWhile < 30:
        currentNstage = TotalNstage
        feedStageVector = feedStageV(currentNstage)
        
        for indexRefluxRatio in range(refluxRatioVector):
            for indexFeedStage in range(feedStageVector):



            

        Application.Tree.FindNode("\Data\Blocks\CR\Input\REAC_STAGE2\#0").Value = currentNstage - 1
        
        indexWhile = indexWhile + 3