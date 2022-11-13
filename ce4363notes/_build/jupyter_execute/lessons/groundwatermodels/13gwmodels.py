#!/usr/bin/env python
# coding: utf-8

# # Groundwater Models
# 
# Flow in porous media is a topic that appears in many branches of engineering and science, e.g., ground water hydrology, reservoir engineering, soil science, soil mechanics, and chemical engineering (filtration).
# The aquifer, which is the porous medium domain of the hydrologist, or the oil reservoir, which is the porous medium of the petroleum engineer are typical examples. {numref}`aquifers` is a sketch of different aquifer classifications. 
# 
# ```{figure} aquifers.png
# ---
# width: 400px
# name: aquifers
# ---
# Aquifer Schematic
# ```
# A confined aquifer (pressure aquifer) is one bounded above and below by impermeable formations.
# In a well penetrating such an aquifer, the water level will rise above the base of the confining formation.
# Water levels in wells that sample a certain aquifer define an imaginary surface called the piezometric surface.
# 
# An unconfined aquifer (water table aquifer; phreatic aquifer) is one with the water table as its upper boundary.
# The classifications are important because the equations of motion are different in different kinds of aquifers.
# 
# ## Storativity
# 
# Storativity of an aquifer is the relationship between changes in head within the aquifer and the quantity of water stored in the aquifer.  The dominant mechanism of storage is different for confined and unconfined aquifers. {numref}`storage` is a sketch depicting the storage process in a confined, and an unconfined aquifer.
# 
# ```{figure} storage.png
# ---
# width: 400px
# name: storage
# ---
# Storage Mechanisms 
# ```
# 
# In a confined aquifer the water is stored or released by compression and decompression of water and the solid matrix (like a sponge squeezed while wrapped in plastic wrap).  In an unconfined aquifer the water is stored or released from the pore space when the water table elevation changes.
# 
# The storage coefficient (confined) or specific yield (unconfined) is the volume of water added to (or removed from) storage per unit area of aquifer per unit change in head.  The usual symbols are $S$, and $S_y$.
# 
# ## Permeability
# Permeability is the material property that relates the resistance of flow through the porous medium to the hydraulic gradient.
# 
# ## Head Loss Models
# 
# Darcy's law (a linear flux model) is the head loss model used for porous media flow.   
# 
# Darcy's law is usually presented as a discharge model
# 
# $$Q = -KA\frac{\Delta h}{\Delta x}$$
# 
# Expressed as a head loss model it is rearranged as
# 
# $$
# h_L = \frac{QL}{KA}
# $$
# where $Q$ is the discharge in the aquifer, $L$ is the length in the flow direction, $A$ is the cross sectional area of aquifer (pore space and solid phase), $K$ is the hydraulic conductivity (sometimes called the permeability).
# 
# A more useful (for computation) form of the head loss model, is to express it (the loss equation) as an equation of motion as in 
# 
# $$Q = -KA\frac{\partial h}{\partial x}$$
# 
# where $- \frac{\partial h}{\partial x}$ is the hydraulic gradient (slope of the hydraulic grade line) in the aquifer.
# 
# {numref}`1D-aquifer-flow` is a diagram that illustrates the relationships expressed by Darcy's law.  
# 
# 
# ```{figure} 1D-aquifer-flow.png
# ---
# width: 400px
# name: 1D-aquifer-flow
# ---
# Schematic diagram of unidirectional flow in a generic aquifer, showing heads in two measuring wells located distance $L$ apart
# ```
# ## Theory
# ## Solution Methods
# 
# ## Homebrew
# 

# In[ ]:




