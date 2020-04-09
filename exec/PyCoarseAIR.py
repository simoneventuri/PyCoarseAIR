##==============================================================================================================
# 
# Coarse-Grained QCT for Atmospheric Mixtures (CoarseAIR) 
# 
# Copyright (C) 2018 Simone Venturi and Bruno Lopez (University of Illinois at Urbana-Champaign). 
#
# Based on "VVTC" (Vectorized Variable stepsize Trajectory Code) by David Schwenke (NASA Ames Research Center). 
# 
# This program is free software; you can redistribute it and/or modify it under the terms of the 
# Version 2.1 GNU Lesser General Public License as published by the Free Software Foundation. 
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Lesser General Public License for more details. 
# 
# You should have received a copy of the GNU Lesser General Public License along with this library; 
# if not, write to the Free Software Foundation, Inc. 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA 
# 
#---------------------------------------------------------------------------------------------------------------
##==============================================================================================================
import os
import sys
import numpy as np
##==============================================================================================================
print("\n[PyCoarseAIR]: Defining Paths")

WORKSPACE_PATH  = '/home/venturi/WORKSPACE/'                                                                    # It is NOT REQUIRED to change this path
#WORKSPACE_PATH  = os.environ['WORKSPACE_PATH']   
#CoarseAIRFldr   = WORKSPACE_PATH + '/CoarseAIR/coarseair/'										         	    # It is NOT REQUIRED to change this path
#CoarseAIRFldr   = os.environ['COARSEAIR_SOURCE_DIR']
PyCoarseAIRFldr = WORKSPACE_PATH  + '/PyCoarseAIR/'		                							            # <--- Please, CHANGE this path to the folder of the PyCoarseAIR Code

DtbHDF5Fldr     = WORKSPACE_PATH + '/Mars_Database/HDF5_Database/'                                              # <--- Please, CHANGE this path to the folder containing the HDF5 File

DtbWriteFldr    = WORKSPACE_PATH + '/Mars_Database/Run_0D/database/'                                            # <--- Please, CHANGE this path to the folder where you want PYCoareseAIR writing the Postprocessed Kinetics Database
OutputWriteFldr = WORKSPACE_PATH + '/Mars_Database/Results/'                                                    # <--- Please, CHANGE this path to the folder where you want PYCoareseAIR writing its Output Files and Plots
##--------------------------------------------------------------------------------------------------------------



##==============================================================================================================
print("\n[PyCoarseAIR]: Loading Files")

sys.path.insert(0, PyCoarseAIRFldr  + '/src/Objects/')
sys.path.insert(0, PyCoarseAIRFldr  + '/src/ChemicalSystems/')
sys.path.insert(0, PyCoarseAIRFldr  + '/src/MolecularProperties/')
sys.path.insert(0, PyCoarseAIRFldr  + '/src/Reading/')
sys.path.insert(0, PyCoarseAIRFldr  + '/src/Writing/')
sys.path.insert(0, PyCoarseAIRFldr  + '/src/Computing/')
sys.path.insert(0, PyCoarseAIRFldr  + '/src/Initializing/')

if (len(sys.argv) > 1):
    InputFile = sys.argv[1]
    print("[PyCoarseAIR]:   Calling PyCoarseAIR with Input File = ", InputFile)
    sys.path.insert(0, InputFile)
else:
    InputFile = PyCoarseAIRFldr + '/src/InputData/'
    print("[PyCoarseAIR]:   Calling PyCoarseAIR with the PRESET Input File Located in " + InputFile )
    sys.path.insert(0, InputFile)
##--------------------------------------------------------------------------------------------------------------



##==============================================================================================================
print("\n[PyCoarseAIR]: Loading Functions")

from Initializing      import Initialize_Data
from InputData         import inputdata
##--------------------------------------------------------------------------------------------------------------



##==============================================================================================================
print("\n[PyCoarseAIR]: Initializing Input and System Data")

InputData    = inputdata(WORKSPACE_PATH, CoarseAIRFldr, PyCoarseAIRFldr, DtbHDF5Fldr, DtbWriteFldr, OutputWriteFldr)

[Syst, Temp] = Initialize_Data(InputData)

print("[PyCoarseAIR]: Done Initializing")
##--------------------------------------------------------------------------------------------------------------



##==============================================================================================================
print("\n[PyCoarseAIR]: Uploading and Processing Rates Data")

Syst.Read_Rates( InputData, Temp )

print("[PyCoarseAIR]: Done Initializing")
##--------------------------------------------------------------------------------------------------------------