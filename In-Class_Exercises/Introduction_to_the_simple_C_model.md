# Simple two pool carbon cycle model

In the in-class exercises we'll be building and analyzing results from a simple two pool carbon model (Fig 1). **The two pools correspond to the litter and soil C pools.**

![model schematic](two_Cpool_model_schematic.png)

*Figure 1: Model schematic of the two pool simple carbon cycle model.*


## Inputs to the model
Inputs to the model (model "drivers" or "forcings") are litter and soil temperature and moisture and litterfall from leaves falling off trees (as well as turnover of dead wood):
1. Litter input from leaf turnover (during senescence, as well as turnover of dead wood) (units of gC/m2/dt)
2. Temperature in the litter layer (units of degrees celcius)
3. Moisture in the litter layer (volumetric water content - unitless between 0 and 1)
4. Temperature in the soil layer (units of degrees celcius)
5. Moisture in the soil layer (volumetric water content - unitless between 0 and 1)

Input data are derived from a temperate deciduous forest site located in Denton Hill State Park in Pennsylvania (41.8N; -77.8W)

![site extended](denton_site_extend.png)

![site zoom](denton_site_zoom.png)


## Model calculations
At each timestep, we calculate the fluxes of C between the two pools (transfers of C from litter to the soil pool and vice versa). We also calculate the C lost from each pool via heterotrophic respiration (Rh). Finally, we calculate the changes in C in each C pool as a sum of the inputs minus outputs to and from each pool.

**UNITS**: Units for model simulations of Rh are kgC/m2/day (per timestep because this is a *flux* of carbon) and for the C pools kgC/m2 (not per timestep because this is a *store* of carbon). Given the litter input is in gC/m2/day, we need to convert this to kgC/m2/day. We will learn how to do this in Exercise 1.

### The general equations for this model are as follows:
![general equations](general_equations.png)


### The temperature and moisture limitation functions are as follows:
![limitation functions](limitation_functions.png)


## Model parameters
*Parameters for the environmental limitations*
- Q10: Q10 temperature limitation on heterotrophic respiration (Rh)
- Tref: reference temperature for Q10 equation (Kelvin)
- Wf_m: 'm' coefficient for the moisture limitation on Rh  
- Wf_x0: 'x0' coefficient for the moisture limitation on Rh 
- Wf_min: minimum value for moisture limitation on Rh
- Wf_max: maximum value for moisture limitation on Rh

*Parameters for the turnover time of each pool*
- tau_litter: turnover time of the litter C pool (years)
- tau_soil: turnover time of the soil C pool (years)

*Parameters for the microbial efficiency of each pool*
- Me_litter: microbial efficiency of the litter pool (fraction)
- Me_soil: microbial efficiency of the soil pool (fraction)

*Parameters for the initial carbon stock of each pool*
- C_litter_t0: initial C stock of the litter pool (kgC/m2)
- C_soil_t0: initial C stock of the soil pool (kgC/m2)


