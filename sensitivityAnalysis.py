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

def functionAspen(minTotalNstage):
    vectorOutput = np.zeros([5])
    while indexWhile < 30:
        currentTotalNstage = minTotalNstage
        Application.Tree.FindNode("\Data\Blocks\CR\Input\NSTAGE").Value = currentTotalNstage
        Application.Tree.FindNode("\Data\Blocks\CR\Input\REAC_STAGE2\#0").Value = currentTotalNstage - 1
        