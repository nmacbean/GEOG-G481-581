"""
Simple two pool C model

Author: N. MacBean
Date: 02/15/2020
"""

import numpy as np


class model:

	"""
	Sets up model and runs simulations for the 2 pool C model defined here:
	https://github.com/nmacbean/GEOG-G440-540/blob/master/In-Class%20Exercises/Introduction%20to%20the%20simple%20C%20model.md
	"""
	@classmethod
	def run(self, params=None, input_data=None):
		
		"""
		The model needs two inputs:
		1. Parameters (as dictionary)
		2. Input data/climate forcing drivers (as pandas dataframe)
		
		Note that the rest of the code remains the same as we had in the Jupyter Notebooks for Exercises 1 and 2.
		"""
		
		
		# - calculate the number of timesteps from the input data
		ntsteps = len(input_data.index)



		# -
		# - initialize model variables
		# -

		# - litter and soil C pools (want to save time series)
		Cpools = np.zeros((ntsteps+1, params['npools']))
		Cpools[0,0] = params['C_litter_t0']
		Cpools[0,1] = params['C_soil_t0']

		# - litter and soil Rh (want to save timeseries)
		Rh = np.zeros((ntsteps, params['npools']))

		# - total C decomp each tstep
		Cdecomp = np.zeros(params['npools'])

		# - total C transferred
		Ctrans = np.zeros(params['npools'])
		
		
		
		# -
		# - temperature function for litter and soil
		# -
		ftemp_litter = params['Q10']**((input_data.LITTER_TEMP - params['Tref'])/10.)
		ftemp_soil = params['Q10']**((input_data.SOIL_TEMP - params['Tref'])/10.)
		
		
		
		# -
		# - moisture function
		# -
		fmoist_litter = np.maximum(params['Wf_min'], params['Wf_max'] + params['Wf_m'] * ( (input_data.LITTER_MOIST - params['Wf_x0'])**2 ))
		fmoist_soil = np.maximum(params['Wf_min'], params['Wf_max'] + params['Wf_m'] * ( (input_data.SOIL_MOIST - params['Wf_x0'])**2 ))
		
		
		
		# -
		# - begin model simulations
		# -

		# - set up for loop over total number of timesteps in input data
		for nt in np.arange(ntsteps):

		    # - calculate the total amount of C decomposed in each pool (prior to splitting between C transferred and Rh) (Eq. 1)
		    Cdecomp[0] = Cpools[nt,0] * (params['dt']/params['tau_litter']) * ftemp_litter[nt] * fmoist_litter[nt]
		    Cdecomp[1] = Cpools[nt,1] * (params['dt']/params['tau_soil']) * ftemp_soil[nt] * fmoist_soil[nt]

		    # - calculate the fraction of C transferred from one pool to the other (Eqns. 2 and 4)
		    Ctrans[0] = Cdecomp[0] * params['Me_litter']
		    Ctrans[1] = Cdecomp[1] * params['Me_soil']

		    # - calculate the heterotrophic respiration in each pool (Eqns. 3 and 5)
		    Rh[nt,0] = Cdecomp[0] * (1. - params['Me_litter'])
		    Rh[nt,1] = Cdecomp[1] * (1. - params['Me_soil'])

		    # - calculate evolution of C pools (Eqns. 6 and 7) --> NOTE: updating C pool from current to next tstep
		    Cpools[nt+1,0] = Cpools[nt,0] + input_data.LITTER_INPUT[nt] - Cdecomp[0] + Ctrans[1]
		    Cpools[nt+1,1] = Cpools[nt,1] + Ctrans[0] - Cdecomp[1]

		# -
		# - end of the model
		# -

		# -
		# - return variables we want to assess:
		# - heterotrophic respiration (Rh) and soil C pools (Cpools) for both litter and soil layers
		# -
		return Rh, Cpools
