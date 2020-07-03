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


TTra = 20000.0

PathToFile_Orig = '/home/venturi/WORKSPACE/Mars_Database/HDF5_Database/O2C_NASA.hdf5'

HDF5Exist_Flg = path.exists(PathToFile_Orig)

f    = h5py.File(PathToFile_Orig, 'a')
TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra))       
del f[TStr]
f.close()

# f       = h5py.File(PathToFile_Orig, 'a')
# TStr    = 'T_' + str(int(TTra)) + '_' + str(int(TTra))  
# TempStr = TStr + '/' + 'CO'
# del f[TempStr]
# f.close()

# f       = h5py.File(PathToFile_Orig, 'a')
# TStr    = 'T_' + str(int(TTra)) + '_' + str(int(TTra))  
# TempStr = TStr + '/' + 'O2'
# del f[TempStr]
# f.close()
