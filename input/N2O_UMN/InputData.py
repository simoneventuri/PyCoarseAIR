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
import numpy as np


class inputdata(object):

    def __init__( self, WORKSPACE_PATH, CoarseAIRFldr, PyCoarseAIRFldr, DtbHDF5Fldr, DtbWriteFldr, OutputWriteFldr ):
        self.WORKSPACE_PATH            = WORKSPACE_PATH
        self.CoarseAIRFldr             = CoarseAIRFldr
        self.PyCoarseAIRFldr           = PyCoarseAIRFldr

        ### CASE SPECIFIC
        self.TranVec                   = np.array([2500.0, 5000.0, 7500.0, 10000.0, 15000.0, 20000.0]) # np.array([5000.0, 10000.0, 20000.0]) #
        self.T0                        = 300.0
        self.iPES                      = 0

        self.DelRateMat_Flg            = True

        self.PlotShow_Flg              = False


        ### CHEMICAL SYSTEM SPECIFIC
        self.SystNameLong              = 'N2O_UMN'
        self.OldVersion_IntFlg         = 1
        self.DtbReadFldr               = self.WORKSPACE_PATH + '/CG-QCT/run_N2O_UMN/Test/'
        self.OutputWriteFldr           = OutputWriteFldr 
        self.SuffixName                = ''


        ### DO NOT CHANGE
        self.NTran                     = np.size(   self.TranVec )
        self.iTVec                     = np.arange( self.NTran   ) + 1

        self.Kin                       = kinetics( self.WORKSPACE_PATH, DtbWriteFldr )
        self.HDF5                      = hdf5(     self.WORKSPACE_PATH, DtbHDF5Fldr )
        self.ME                        = ME(       self.WORKSPACE_PATH )



class kinetics(object):

    def __init__( self, WORKSPACE_PATH, DtbWriteFldr ):

        ### Reading Kinetics Data
        self.Read_Flg                   = True
        #self.ReadFldr                   = WORKSPACE_PATH + '/Mars_Database/Run_0D/database/'                      # To be used Only when Required to read a Database in PLATO's Format


        ## Writing Kinetics Data
        self.Write_Flg                  = True
        self.WriteFldr                  = DtbWriteFldr
        self.WriteDiss_Flg              = True
        self.CorrFactor                 = 1.0
        self.DissTypes                  = np.array([0, 1, 2])
        self.WriteInel_Flg              = True
        self.WriteExch_Flg              = True

        self.WriteExoth_Flg             = True
        self.WriteQB_IntFlg             = 2
        self.WriteFormat                = 'PLATO'

        self.WriteMicroRevCorrection    = True
        self.SytOfComplemExch           = ['NON_UMN']
        self.ProcOfComplemExch          = np.array([2], dtype=np.int64)


        ## Resolution of the Kinetics Data in Input? Array of 'StS' / 'VSM' / 'CGM' of size Syst.NMolecules
        self.MolResolutionIn            = ['StS', 'StS']
        self.MinStateIn                 = np.array([     0], dtype=np.int64)
        self.MaxStateIn                 = np.array([100000], dtype=np.int64)
        self.NGroupsIn                  = []
        self.GroupsInPathsToMapping     = ['']
        self.GroupsInSuffix             = ''


        ## Resolution of the Kinetics Data in Output? Array of 'StS' / 'VSM' / 'CGM' of size Syst.NMolecules
        self.MinStateOut                = np.array([     0,      0], dtype=np.int64)
        self.MaxStateOut                = np.array([100000, 100000], dtype=np.int64)
        #### StS
        self.MolResolutionOut           = ['StS', 'StS']
        self.GroupsOut_Flg              = False
        self.GroupsOutWrite_Flg         = False
        self.GroupsOutPathsToMapping    = ['']
        self.NGroupsOut                 = np.array([45], dtype=np.int64)
        self.GroupsOutSuffix            = ''
        # ### CGM DP
        # self.MolResolutionOut           = ['CGM', 'CGM']
        # self.GroupsOut_Flg              = True
        # self.GroupsOutWrite_Flg         = True
        # self.GroupsOutPathsToMapping    = ['/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/N2O_UMN/N2/LevelsMap_DPM10.csv', '/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/N2O_UMN/NO/LevelsMap_DPM10.csv']
        # self.NGroupsOut                 = np.array([10,10], dtype=np.int64)
        # self.GroupsOutSuffix            = '_DP10' #_Phys_45Bins
        # ### CGM DP Inel
        # self.MolResolutionOut           = ['CGM', 'CGM']
        # self.GroupsOut_Flg              = True
        # self.GroupsOutWrite_Flg         = True
        # self.GroupsOutPathsToMapping    = ['/home/venturi/WORKSPACE/CoarseAIR/coarseair/dtb/Molecules/N2/UMN_ForN2O2/Bins_54/LevelsMap_InelDP54.csv', '/home/venturi/WORKSPACE/CoarseAIR/coarseair/dtb/Molecules/NO/UMN/Bins_46/LevelsMap_InelDP46.csv',]
        # self.NGroupsOut                 = np.array([54,46], dtype=np.int64)
        # self.GroupsOutSuffix            = '_DPI54' #_Phys_45Bins
        # ### CGM Amal
        # self.MolResolutionOut           = ['CGM', 'CGM']
        # self.GroupsOut_Flg              = True
        # self.GroupsOutWrite_Flg         = True
        # self.GroupsOutPathsToMapping    = ['/home/venturi/WORKSPACE/CoarseAIR/coarseair/dtb/Molecules/N2/UMN_ForN2O2/Bins_54/LevelsMap_InelAmal54.csv', '/home/venturi/WORKSPACE/CoarseAIR/coarseair/dtb/Molecules/NO/UMN/Bins_46/LevelsMap_InelAmal46.csv',]
        # self.NGroupsOut                 = np.array([54,46], dtype=np.int64)
        # self.GroupsOutSuffix            = '_ADA54' #_Phys_45Bins
        # ### CGM RVE
        # self.MolResolutionOut           = ['CGM', 'CGM']
        # self.GroupsOut_Flg              = True
        # self.GroupsOutWrite_Flg         = True
        # self.GroupsOutPathsToMapping    = ['/home/venturi/WORKSPACE/CoarseAIR/coarseair/dtb/Molecules/N2/UMN_ForN2O2/Bins_54/LevelsMap_RVE54.csv', '/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/N2O_UMN/NO/LevelsMap_RVE46.csv']
        # self.NGroupsOut                 = np.array([54,46], dtype=np.int64)
        # self.GroupsOutSuffix            = '_RVE54' #_Phys_45Bins
        # ### VSM
        # self.MolResolutionOut           = ['VSM', 'VSM']
        # self.GroupsOut_Flg              = True
        # self.GroupsOutWrite_Flg         = True
        # self.GroupsOutPathsToMapping    = ['','']
        # self.NGroupsOut                 = np.array([54,46], dtype=np.int64)
        # self.GroupsOutSuffix            = '_VSM' #_Phys_45Bins

        ## Packing + Unpacking Dissocation Rates:
        self.PackUnpackDiss_Flg         = False
        self.PackUnpackType             = ['VSM', 'VSM']
        self.PackUnpackPathsToMapping   = ['', '']
        self.PackUnpackSuffix           = '_VS' #_Phys_45Bins


        ## Correcting Kinetics Based on Window-Averaging
        self.WindAvrg_Flg               = False
        self.WindAvrgJs                 = 3
        self.WindAvrgVs                 = 2

        ## Writing Arrhenius Files
        self.MaxEntOrPlato              = 1
        self.MinRate                    = 1.e-15
        self.MinNbTs                    = 4
        self.MaxErrArr                  = 1.e-7        


        ## Analyzig the Preferential Jumps between Levels
        self.RatesPrefJumps_Flg         = False
        self.RatesNPrefJumps            = 5



class hdf5(object):

    def __init__( self, WORKSPACE_PATH, DtbHDF5Fldr ):

        self.DtbFldr                    = DtbHDF5Fldr
        self.ForceReadDat_Flg           = False
        self.Save_Flg                   = True



class ME(object):

    def __init__(self, WORKSPACE_PATH):

        self.Read_Flg                   = False
        self.ReadFldr                   = WORKSPACE_PATH + '/Mars_Database/Run_0D/'
        self.WriteFolder                = ''
        self.ProcCode                   = '0_1_1_1'
        self.TimeVec                    = np.array([1.e-10, 1.e-8, 1.e-6, 1.e-4])
