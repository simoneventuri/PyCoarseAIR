import h5py
import numpy as np

TVec     	      = np.array([1500.0, 2500.0, 5000.0, 6000.0, 8000.0, 10000.0, 12000.0, 14000.0, 15000.0, 20000.0])
FromPath 	      = '/home/venturi/WORKSPACE/Air_Database/HDF5_Database/O3_UMN.hdf5' 
ToPath   	      = '/home/venturi/WORKSPACE/Air_Database/HDF5_Database/O3_UMN_Cleaned.hdf5'

Molecule 	      = 'O2'
MoleculeDescr     = 'Contains Properties of O2 Rovibrational Levels. Diatomic Potentials from Varga et al. (J. Chem. Phys. 147, 154312 (2017))'

MoleculeList      = ['LevelEEh', 
					 'LevelEeV', 
					 #'LevelEgam', 
					 'LevelTau', 
					 'LevelVMax', 
					 'LevelVMin', 
					 'Levelg', 
					 'Leveljqn', 
					 'LevelrIn', 
					 'LevelrMax', 
					 'LevelrMin', 
					 'LevelrOut', 
					 'Levelvqn', 
					 'NLevels']
MoleculeListDescr = ['Rovibrational Energy [Eh]',
					 'Rovibrational Energy [eV]',
					 #'Lifetime [a.u.]',
					 'Vibrational Time Constant [a.u.]',
					 'Maximum of the Effective Diatomic Potential [Eh]',
					 'Minimum of the Effective Diatomic Potential [Eh]',
					 'Degeneracy',
					 'Rotational Q.N.',
					 'Inner Turning Point [a0]',
					 'Location of the Maximum of the Effective Diatomic Potential [a0]',
					 'Location of the Minimum of the Effective Diatomic Potential [a0]',
					 'Outer Turning Point [a0]',
					 'Vibrational Q.N.',
					 'Nb of Rovibrational Levels']

RatesDescr        = 'Contains Ab Initio Rate Coefficients for Dissociation, Inelastic and Exchange Reactions from QCT Calculations of Venturi et al. (J. Phys. Chem. A, Just Accepted). PESs from Varga et al. (J. Chem. Phys. 147, 154312 (2017))'

arrList           = ['Diss', 
					 'Inel', 
					 'Exch_1']
arrListDescr      = ['Dissociation Rate Coefficients, BEFORE 16/3 CORRECTION',
					 'Exothermic Inelastic Rate Coefficients',
					 'Exothermic Exchange Reaction Rate Coefficients']


fr       = h5py.File(FromPath, 'r')
fw       = h5py.File(ToPath,   'w')

gw = fw.create_group(Molecule)
gw.attrs['Description'] = MoleculeDescr
for i, var in enumerate(MoleculeList):
	print('Reading Group: ' + Molecule + '/' + var)
	arr = fr.get(Molecule + '/' + var)
	arr = np.array(arr)
	print('Values = ', arr[...])
	###
	dw = gw.create_dataset(var, data=arr, compression="gzip", compression_opts=9)
	dw.attrs['Description'] = MoleculeListDescr[i]


for var in TVec:
	print('Reading T = ' + str(int(var)))
	gw  = fw.create_group('T' + str(int(var)) + 'K')
	gww = fw.create_group('T' + str(int(var)) + 'K/Rates')
	gww.attrs['Description'] = RatesDescr

	varvar = arrList[0]
	print('  Reading group: ' + varvar)
	arr = fr.get('T_' + str(int(var)) + '_' + str(int(var)) + '/Rates/' + varvar)
	print('Values = ', arr[...])
	###
	dw = gww.create_dataset(varvar, data=arr[:,0], compression="gzip", compression_opts=9)
	dw.attrs['Description'] = arrListDescr[0]

	varvar = arrList[1]
	print('  Reading group: ' + varvar)
	arr = fr.get('T_' + str(int(var)) + '_' + str(int(var)) + '/Rates/' + varvar)
	print('Values = ', arr[...])
	###
	dw = gww.create_dataset(varvar, data=np.tril(arr, 0), compression="gzip", compression_opts=9)
	dw.attrs['Description'] = arrListDescr[1]

	varvar = arrList[2]
	print('  Reading group: ' + varvar)
	arr = fr.get('T_' + str(int(var)) + '_' + str(int(var)) + '/Rates/' + varvar)
	print('Values = ', arr[...])
	###
	dw = gww.create_dataset(varvar, data=np.tril(arr, 0), compression="gzip", compression_opts=9)
	dw.attrs['Description'] = arrListDescr[2]

fr.close()
fw.close()