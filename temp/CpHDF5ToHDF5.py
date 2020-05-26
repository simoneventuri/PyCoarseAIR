import sys
import os, errno
import os.path
from os import path
import shutil

import numpy as np
import pandas
import h5py
import csv
from   matplotlib import rc 
import matplotlib.pyplot as plt


TTra = 15000.0

PathToFile_Orig = '/home/venturi/WORKSPACE/Mars_Database/HDF5_Database_NEW/CO2_NASA_.hdf5'
PathToFile_New  = '/home/venturi/WORKSPACE/Mars_Database/HDF5_Database/CO2_NASA.hdf5'
# PathToFile_Orig = '/home/venturi/WORKSPACE/Mars_Database/HDF5_Database/CO2_NASA_PES1.hdf5'

HDF5Exist_Flg = path.exists(PathToFile_Orig)
if (HDF5Exist_Flg):
    f = h5py.File(PathToFile_Orig, 'a')
else:
    f = {'key': 'value'}

# TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra))       
# del f[TStr]
# f.close()

TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra)) + '/Rates/'       
grp  = f[TStr]

Data      = grp["Diss"]
RatesDiss = Data[...]

Data      = grp["Inel"]
RatesInel = Data[...]

iProc      = 2
ExchStr    = "Exch_" + str(iProc-1)
Data       = grp[ExchStr]
RatesExch1 = Data[...]

iProc      = 3
ExchStr    = "Exch_" + str(iProc-1)
Data       = grp[ExchStr]
RatesExch2 = Data[...]

f.close()


HDF5Exist_Flg = path.exists(PathToFile_New)
f = h5py.File(PathToFile_New, 'a')
TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra))  
del f[TStr]
TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra)) + '/Rates/'       

if TStr in f.keys():
    grp       = f[TStr]
    Data      = grp["Diss"]
    Data[...] = RatesDiss
    Data      = grp["Inel"]
    Data[...] = RatesInel
    iProc      = 2
    ExchStr    = "Exch_" + str(iProc-1)
    Data       = grp[ExchStr]
    Data[...]  = RatesExch1
    iProc      = 3
    ExchStr    = "Exch_" + str(iProc-1)
    Data       = grp[ExchStr]
    Data[...]  = RatesExch2
else:
    grp        = f.create_group(TStr)
    Proc0      = grp.create_dataset("Diss", data=RatesDiss, compression="gzip", compression_opts=9)
    Proc1      = grp.create_dataset("Inel", data=RatesInel, compression="gzip", compression_opts=9)
    iProc      = 2
    ExchStr    = "Exch_" + str(iProc-1)
    ProcExchi  = grp.create_dataset(ExchStr, data=RatesExch1, compression="gzip", compression_opts=9)
    iProc      = 3
    ExchStr    = "Exch_" + str(iProc-1)
    ProcExchi  = grp.create_dataset(ExchStr, data=RatesExch2, compression="gzip", compression_opts=9)

f.close()





f1      = h5py.File(PathToFile_Orig, 'a')

TStr    = 'T_' + str(int(TTra)) + '_' + str(int(TTra))  
TempStr = TStr + '/' + 'O2'
grp     = f1[TempStr]

Data                                 = grp["LevelQRatio"]
LevelQRatio  = Data[...]
Data                                 = grp["LevelQ"]
LevelQ       = Data[...] 
Data                                 = grp["LevelQERatio"]
LevelQERatio = Data[...]
Data                                 = grp["LevelQE"]
LevelQE      = Data[...] 

f1.close()


f2 = h5py.File(PathToFile_New, 'a')

TStr     = 'T_' + str(int(TTra)) + '_' + str(int(TTra))  
TempStr1 = TempStr  + '/'
TempStr2 = TempStr1 + '/LevelQ'     
if TempStr2 in f.keys():
    grp       = f2[TempStr1]
    Data      = grp["LevelQ"]
    Data[...] = LevelQ
    Data      = grp["LevelQRatio"]
    Data[...] = LevelQRatio
    Data      = grp["LevelQE"]
    Data[...] = LevelQE
    Data      = grp["LevelQERatio"]
    Data[...] = LevelQERatio
else:
    if (not (TempStr1 in f2.keys())):
        grp      = f2.create_group(TempStr1)
    else:
        grp      = f2[TempStr1]
    LevelQ       = grp.create_dataset("LevelQ",       data=LevelQ,       compression="gzip", compression_opts=9)
    LevelQRatio  = grp.create_dataset("LevelQRatio",  data=LevelQRatio,  compression="gzip", compression_opts=9)
    LevelQE      = grp.create_dataset("LevelQE",      data=LevelQE,      compression="gzip", compression_opts=9)
    LevelQERatio = grp.create_dataset("LevelQERatio", data=LevelQERatio, compression="gzip", compression_opts=9)

f2.close()