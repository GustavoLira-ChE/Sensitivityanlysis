#%%
import numpy as np

def feedStageV(currentTotalNstage):
    
    middleStage = round(currentTotalNstage/2)
    feedStageVector = np.array([middleStage])

    indexWhileFeedStage = 1
    upValue = middleStage + 2
    lowValue = middleStage - 2

    while indexWhileFeedStage < 5: #5 número de vueltas del ciclo while para generar los números de entrada de alimentación
        
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

a = feedStageV(30)
print(a)
# %%
