#!/usr/bin/env python
# coding: utf-8

# # Aquifer Properties - II
# 
# ## Aquifers
# 
# **Water Table**
# 
# Before our journey into the fascinating world of aquifers and their kin, we need to define a water table, which is the the locus of points in a porous medium where the pore water pressure is equal to the atmospheric pressure (pg. 98).  One particularly important type of aquifer is a water table aquifer. 
# 
# Some useful heuristic guidelines regarding water table behavior are:
# 
# 1. In the absence of groundwater flow (discharge, recharge, reversed charge), the water table will be flat (no meaningful gardient)
# 2. A sloped water table indicates that groundwater is flowing
# 3. Groundwater discharge zones tends to be in topographic low spots
# 4. The water table shape often mimics the surface topography (unless engineers have their way!)
# 5. Groundwater tends to flow away from topographic high spots and towards topographic low spots, but not always
# 
# **Aquifer**
# 
# Water-bearing geologic unit, tends to be of large areal extent.  Will have many different point values of $K$, for engineering usually need to express some "average" value.  The arithmetic mean is not usually useful, in part because $K$ is not normally distributed (or even symmetrically distributed; negative values are meaningless), typically the median and geometric mean are used.
# 
# :::{note}
# Geometric mean is determined by logartihmic transformation of the inputs:
# 
# $$ y_i = log(K_i) $$
# 
# such that the geometric mean is 
# 
# $$e^{\bar y}$$
# :::
# 
# **Confining Layer**
# 
# **Aquifuge**
# 
# **Aquitard**
# 
# **Unconfined Aquifer**
# 
# Aquifers close to the surface with materials of high intrinsic permeability extending downward from the surface to the base of the aquifer are called unconfined (or water table aquifers)
# 
# **Confined Aquifer**
# 
# Aquifers overlain by a confining layer or formation are called confined aquifers. Confined aquifers are called [artesian](https://www.youtube.com/watch?v=lgn0NXckqQs) aquifers when the piezometric head (pressure head) in the aquifer is sufficient to lift water to the surface without addidional inputs of energy (a flowing well).
# 
# 

# ## Storage
# 
# Storage is the term used to describe how much water is contained in an aquifer.  
# 
# There are three principal mechanisms of storage always present, but of differing relative contribution:
# 
# 1. draining/filling of the pore space, and
# 2. compression/decompression of the water, and
# 3. compression/expansion of the solids structure.
# 
# Three terms related to these mechanisms are:
# 
# 1. porosity (specific yield), and
# 2. bulk compressibility of water, and
# 3. bulk compressibility of the solid structure.
# 
# **Unconfined Aquifers** primary storage mechanism is draining/filling of the pore space in the vicinity of the free surface.  The other two mechanisms are relatively insignificant, even at large scales.
# 
# **Confined Aquifers** primary storage mechanisms are compression/expansion of the solids structure and compression/decompression of the water.
# 
# The term matrix compressibility refers to the phenomenon where the solids rearrange so that matrix porosity changes with changes in head.  Draining/filling of pore space is insignificant (as long as the aquifer remains confined the same volume of aquifer is saturated)
# 
# ![](wspstorage1.png)
# 
# ![](wspstorage2.png)
# 
# ### Storage Mechanism Algebra
# 
# ![](storativity1.png)
# ![](storativity2.png)
# ![](storativity3.png)
# ![](storativity4.png)
# ![](storativity5.png)
# ![](storativity6.png)
# ![](storativity7.png)
# ![](storativity8.png)
# ![](storativity9.png)
# ![](storativity10.png)
# ![](storativity11.png)
# ![](storativity12.png)

# ## Effective Stress and Compressibility
# 
# Effective stress (solids pressure) is a term used to describe the load per unit area carred by the solids matrix in a porous medium.
# 
# ![](effectivestress.png)
# 
# Consider a unit block of aquifer as above.  The total load on top of the block is supported in part by the solids structure and in part by the water (bouyancy).  From a static force balance we have:
# 
# $$p_T = p_l + p_s$$
# 
# where $p_T$, $p_l$, and $p_s$ are the total, liquid, and solids pressures (normal stresses).
# 
# When water is removed or added to the blaock the total pressure (overburden) is unchanged so the variation in the liquid pressure is equal and opposite to the variation in solids pressure (effective stress).
# 
# $$ dp_l = - dp_s$$
# 
# The variation in head in the block is directly related to variation of liquid pressure as the block is assumed to be fixed in space so we have:
# 
# $$ dh = \frac{dp_l}{\rho g}$$
# 
# From this concept we can define matrix and water compressibility terms.
# 
# Typically;
# 
# $$ dp_l = \rho g dh$$
# 
# $$ dp_s = -\rho g dh$$
# 
# Matrix compressibility is
# 
# $$\alpha = \frac{-\frac{db}{b}}{dp_s}$$
# 
# where $b$ is the unit thickness.  Combining this concept with water compressibility defines the confined aquifer specific storage coefficient as 
# 
# $$S_s = \rho_w g (\alpha + n \beta)$$
# 
# where 
# 
# $$\beta = \frac{\frac{d\rho}{\rho}}{dp_l}$$

# ## Transmissivity
# 
# The ability of an entire thickness of an aquifer to convey water is called the transmissivity and is usually just the product of storage coefficient and hydraulic conductivity. 
# 
# $$T = K b$$
# 
# 
# 

# ## Water Table & Potentiometric Maps
# 
# Elevation of water level in wells or piezometers is the pressure head.  The sum of the pressure and elevation head (well screen levels are known) is the hydraulic head.
# 
# These maps have maps have many uses
# 
# - determine regional flow direction and magnitude
# - estimate storativity
# - estimate pollutant transport 
# 
# ### Map Application Determine Storativity
# 
# ![](mapstor1.png)
# ![](mapstor2.png)
# ![](mapstor3.png)
# ![](mapstor4.png)
# ![](mapstor5.png)
# 
# ### Map Application Determine Gradient and Flow
# 
# ![](headmap1.png)
# ![](headmap2.png)
# 
# ![](3well1.png)
# ![](3well2.png)
# ![](3well3.png)
# ![](3well4.png)
# ![](3well5.png)
# ![](3well6.png)
# ![](3well7.png)
# 
# Link to [MODEL1.XLS](http://54.243.252.9/ce-4363-webroot/ce4363notes/lessons/04aquiferproperties/MODEL1.XLS) gradient calculator spreadsheet.
# 
# ### Map Application Determine Regional Flow
# 
# ![](mapflow1.png)
# 
# ![](mapflow2.png)
# 
# ![](mapflow3.png)
# 
# ![](mapflow4.png)
# 
# ![](mapflow5.png)
# 
# ![](mapflow6.png)
# 
# ![](mapflow7.png)

# ## Homogeneity and Isotropy (pg 108)
# 

# ## References
# 
# 1. [Cleveland, T.G., R. Bravo, and J.R. Rogers, 1992. Specific Storage and Hydraulic Conductivities Using Extensometer and Hydrograph Data, Ground Water, Vol. 30, No. 5, pp 701-708.](http://54.243.252.9/about-me-webroot/about-me/MyWebPapers/journal_papers/specific_storage_jawa_1992/specific_storage_jawa_1992.pdf)

# In[ ]:




