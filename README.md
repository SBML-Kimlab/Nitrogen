In this repository, you will find the constraint-based model of E. coli K-12 MG1655 (iML1515 model of metabolism) under different nitrogen sources (ammonia, cytidine, and cytosine).

FBA analysis and MCMC sampling were performed with the iML1515 E. coli metabolic model and COBRApy. For a parameter of nitrogen uptake rate, uptake rate the glucose and export rate for pyrimidine measured by HPLC were used to constrain the model. 

The distribution of feasible fluxes for each reaction in the iML1515 model was determined using MCMC sampling. The biomass objective function was provided a lower bound of 95% of the optimal growth rate as computed by FBA. Thus, the sample flux distributions by MCMC sampling method represented sub-optimal flux distributions. MCMC sampling was used to obtain 10,000 feasible flux distributions, and the average of flux samples for each reaction was used.


![Synopsis Figure](https://user-images.githubusercontent.com/42198206/205002221-6eafcaf5-bdb3-49ba-856a-d83bae25682f.png)
