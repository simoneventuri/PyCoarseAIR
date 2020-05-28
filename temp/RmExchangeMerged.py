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


TTraVec         = np.array([2500.0 5000.0, 7500.0, 10000.0, 12500, 15000.0, 20000.0])
PathToFile_Orig = '/home/venturi/WORKSPACE/Mars_Database/HDF5_Database/O2C_NASA.hdf5'
iExch           = 1


# for TTra in TTraVec:

TTra = 20000.0
f = h5py.File(PathToFile_Orig, 'a')
TStr = 'T_' + str(int(TTra)) + '_' + str(int(TTra)) + '/Rates/Exch_' + str(iExch) + '_Merged'
del f[TStr]
f.close()
