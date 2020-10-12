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
        self.TranVec                   = np.array([10000.0])
        self.T0                        = 300.0
        self.iPES                      = 0

        self.DelRateMat_Flg            = True

        self.PlotShow_Flg              = False


        ### CHEMICAL SYSTEM SPECIFIC
        self.SystNameLong              = 'OaObOcOd_UMN'
        self.OldVersion_IntFlg         = 0
        self.DtbReadFldr               = self.WORKSPACE_PATH + '/CoarseAIR/O4_UMN_StS/Test/'
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

        self.ThCollPart                 = True

        ## Writing Kinetics Data
        self.Write_Flg                  = True
        self.WriteFldr                  = DtbWriteFldr
        self.WriteDiss_Flg              = True 
        self.CorrFactor                 = 1.0
        self.WriteDissInel_Flg          = True 
        self.WriteInel_Flg              = True
        self.WriteExch_Flg              = True

        self.WriteExoth_Flg             = True
        self.WriteQB_IntFlg             = 2
        self.WriteFormat                = 'PLATO'

        self.WriteMicroRevCorrection    = False
        #self.SytOfComplemExch           = 'O3_UMN'
        #self.ProcOfComplemExch          = np.array([2], dtype=np.int64)



        ## Resolution of the Kinetics Data in Input? Array of 'StS' / 'VSM' / 'CGM' of size Syst.NMolecules
        self.MinStateIn                 = np.array([     0,     0,     0,     0], dtype=np.int64)
        self.MaxStateIn                 = np.array([100000,100000,100000,100000], dtype=np.int64)
        ###
        self.MolResolutionIn            = ['StS','StS','StS','CGM','CGM','CGM']
        self.NGroupsIn                  = np.array([6115,6115,6115,1,1,1], dtype=np.int64)
        self.GroupsInPathsToMapping     = ['','','','/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/O3_UMN/O2/LevelsMap_RVE1.csv','/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/O3_UMN/O2/LevelsMap_RVE1.csv','/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/O3_UMN/O2/LevelsMap_RVE1.csv']
        self.GroupsInSuffix             = '_StS'
        ### 
        # self.MolResolutionIn            = ['VSM']
        # self.NGroupsIn                  = np.array([45], dtype=np.int64)
        # self.GroupsInPathsToMapping     = ['']
        # self.GroupsInSuffix             = '_VSM'

        ## Resolution of the Kinetics Data in Output? Array of 'StS' / 'VSM' / 'CGM' of size Syst.NMolecules
        self.MinStateOut                = np.array([     0,     0,     0,     0], dtype=np.int64)
        self.MaxStateOut                = np.array([100000,100000,100000,100000], dtype=np.int64)
        self.GroupsOut_Flg              = False
        self.GroupsOutWrite_Flg         = False 
        ###
        self.MolResolutionOut           = ['StS','StS','StS','CGM','CGM','CGM']
        self.NGroupsOut                 = np.array([6115,6115,6115,1,1,1], dtype=np.int64)
        self.GroupsOutPathsToMapping    = ['','','','/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/O3_UMN/O2/LevelsMap_RVE1.csv','/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/O3_UMN/O2/LevelsMap_RVE1.csv','/home/venturi/WORKSPACE/Air_Database/Run_0D/database/grouping/O3_UMN/O2/LevelsMap_RVE1.csv']
        self.GroupsOutSuffix            = '_StS'
        # ###
        # self.MolResolutionOut           = ['VSM']
        # self.NGroupsOut                 = np.array([45], dtype=np.int64)
        # self.GroupsOutPathsToMapping    = ['']
        # self.GroupsOutSuffix            = '_VSM'



        ## Packing + Unpacking Dissocation Rates:
        self.PackUnpackDiss_Flg         = False
        self.PackUnpackType             = ['VSM']
        self.PackUnpackPathsToMapping   = ['']
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

    def __init__( self, WORKSPACE_PATH ):

        self.Read_Flg                   = False
        self.ReadFldr                   = WORKSPACE_PATH + '/Mars_Database/Run_0D/'
        self.WriteFolder                = ''
        self.ProcCode                   = '0_1_1_1'
        self.TimeVec                    = np.array([1.e-10, 1.e-8, 1.e-6, 1.e-4])
