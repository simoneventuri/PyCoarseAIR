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


#TTraVec         = np.array([1500.0, 2500.0, 5000.0, 6000.0, 8000.0, 10000.0, 12000.0, 14000.0, 15000.0, 20000.0]) #np.array([1000.0, 2500.0, 3500.0, 7500.0, 10000.0, 12500.0, 15000.0, 20000.0, 25000.0, 30000.0, 40000.0, 50000.0])
TTraVec         = np.array([10000.0, 5000.0, 20000.0]) #np.array([1000.0, 2500.0, 3500.0, 7500.0, 10000.0, 12500.0, 15000.0, 20000.0, 25000.0, 30000.0, 40000.0, 50000.0])
#TTraVec         = np.array([10000.0]) #np.array([1000.0, 2500.0, 3500.0, 7500.0, 10000.0, 12500.0, 15000.0, 20000.0, 25000.0, 30000.0, 40000.0, 50000.0])
#TTraVec         = np.array([1000.0, 2500.0, 3500.0, 7500.0, 10000.0, 12500.0, 15000.0, 20000.0, 25000.0, 30000.0, 40000.0, 50000.0])
#TTraVec         = np.array([10000.0, 3500.0, 20000.0]) #np.array([1000.0, 2500.0, 3500.0, 7500.0, 10000.0, 12500.0, 15000.0, 20000.0, 25000.0, 30000.0, 40000.0, 50000.0])
PathToFile_Orig = '/home/venturi/WORKSPACE/Air_Database/HDF5_Database/CO2_NASA.hdf5'
iExch           = 1


# for TTra in TTraVec:

# TTra = 20000.0
# f = h5py.File(PathToFile_Orig, 'a')
# TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra)) + '/Rates/Exch_' + str(iExch) + '_Merged'
# del f[TStr]
# f.close()

# StrVec = ['/O2_30p15']
# for StrStr in StrVec:
# 	for TTra in TTraVec:
# 		print(TTra, StrStr)
# 		f = h5py.File(PathToFile_Orig, 'a')
# 		TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra)) + StrStr 
# 		del f[TStr]
# 		f.close()

StrVec = ['/RatesMicroRev', '/O2_VSM', '/CO_VSM', '/O2_DP20', '/CO_DP20', '/O2_DP83', '/CO_DP83']
for StrStr in StrVec:
	for TTra in TTraVec:
		print(TTra, StrStr)
		f = h5py.File(PathToFile_Orig, 'a')
		TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra)) + StrStr 
		del f[TStr]
		f.close()
