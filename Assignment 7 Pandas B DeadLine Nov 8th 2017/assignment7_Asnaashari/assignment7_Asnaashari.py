import os
import pandas as pd
import numpy as np

os.chdir("D:/polimi note books/energy and enviromnetal technologies for building systems/assignments/Assignment 7 Pandas B DeadLine Nov 8th 2017/__Guidelines__")

windows_DF = pd.read_csv("windows_completed1.csv",sep=';',index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=';',index_col=0)
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=';',index_col=0)


Tx = 1
Fshade = 0
latitude = "45"


BeamIrreastPC = BeamIrradiance_DF.loc["E",latitude]
DiffIrreastPC = DiffuseIrradiance_DF.loc["E",latitude]

PXI = Tx*(DiffIrreastPC + (1-Fshade)*BeamIrreastPC)

windows_DF ["PXI"] = np.array([PXI,0,0,0])

windows_DF.to_csv("windows_completed_withPXI.csv", sep=';')