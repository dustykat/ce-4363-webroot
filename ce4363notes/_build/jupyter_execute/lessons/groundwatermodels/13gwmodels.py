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
# - The cross-sectional flow area, $A$, is the product of height of the aquifer block and its width (in this case the width is into the plane of the paper). 
# - The distance between two measurement points is $L$. The head at the two points is $h_1$ and $h_2$.
# - The gradient of head, $\frac{\partial h}{\partial x}$, is $\frac{h_2 - h_1}{L}$.
# - The hydraulic gradient is  $- \frac{\partial h}{\partial x}$, is $\frac{h_1 - h_2}{L}$.
# 
# Finally Darcy's law (for the drawing) is $Q = K A \frac{h_1 - h_2}{L}$.
# 
# 
# ## Confined Aquifer Flow Modeling Theory 
# 
# Using Figure {numref}`1D-aquifer-flow` as a starting point, one can develop a computational model of flow in a confined aquifer.
# Let's decide that the distance $L$ in the figure is going to be divided into a series of connected, small blocks.
# The flow direction in the figure will be declared  the $x$ direction, the depth into the drawing is declared the $y$ direction, and the height of the block is declared the $z$ direction.
# 
# {numref}`single-computational-cell` is a diagram of one such small block.
# 
# ```{figure} single-computational-cell.png
# ---
# width: 400px
# name: single-computational-cell
# ---
# Single computational cell definition sketch
# ```
# 
# Using this diagram we can now develop a set of expressions for the cell volume, solids volume in the cell,  pore volume in the cell (where water actually can flow), and solids mass.
# 
# First some definitional expressions for each cell:
# 
# > - Cell Volume: $V_{cell} = \Delta x \times \Delta y \times \Delta z$
# > - Solids Volume: $V_{solid} =(1-\omega) \Delta x \times \Delta y \times \Delta z$
# > - Void (Pore) Volume: $V_{pore} = \omega \Delta x \times \Delta y \times \Delta z$
# > - Solids Mass: $M_{solid} = \rho_{s} (1-\omega) \Delta x \times \Delta y \times \Delta z$
# 
# Next write a mass balance for water in the cell;
# 
# $$
# \frac{d M_{water}}{dt} = M_{Inflow} - M_{Outlfow}
# $$
# 
# The left side of the expression is simply the storage term, and in the context of storage coefficients and aquifer head is replaced by
# 
# $$
# {\frac{d M_{water}}{dt}\mid}_{cell} =\rho_{w} S_{s} \Delta x \Delta y \Delta z \frac{\partial h_i}{\partial t}
# $$
# 
# where $h_i$ is the head in the $i-$th cell.  
#  
# The right hand side of the expression is based on writing Darcy's law for the cell, and using values in adjacent (hydraulically connected) cells.
# 
# {numref}`multiple-computational-cell` is a diagram of three such connected blocks.
# 
# ```{figure} multiple-computational-cell.png
# ---
# width: 400px
# name: multiple-computational-cell
# ---
# Multiple computational cell definition sketch
# ```
# 
# The $i-$th cell is the cell of interest, the cell to the left is cell ID $i-1$, and the cell to the right is cell ID $i+1$.  
# 
# We now write Darcy's law for each face of cell $i$, treating the head in each of the cell centers as if they were the sampling wells of {numref}`1D-aquifer-flow` (In the context of {numref}`1D-aquifer-flow`, the cell face is halfway between the two wells; the cell centers are at the wells.)
# 
# Darcy's law for the left face is 
# 
# $$
# M_{Inflow} = Q_{left} =\rho_{w} K \Delta y \Delta z \frac{h_{i-1} - h_{i}}{\Delta x}
# $$
#  
# Similarly for the right face, 
# 
# $$
# M_{Outflow} = Q_{right} =\rho_{w} K \Delta y \Delta z \frac{h_{i} - h_{i+1}}{\Delta x}
# $$
# 
# Now combine these together in the mass balance
# 
# $$
# \rho_{w} S_{s} \Delta x \Delta y \Delta z \frac{\partial h_i}{\partial t} = 
# (\rho_{w} K \Delta y \Delta z \frac{h_{i-1} - h_{i}}{\Delta x}) - 
# (\rho_{w} K \Delta y \Delta z \frac{h_{i} - h_{i+1}}{\Delta x})
# $$
# 
# Next divide by the water density $\rho_{w}$,
# 
# $$
# S_{s} \Delta x \Delta y \Delta z \frac{\partial h_i}{\partial t} = 
# (K \Delta y \Delta z \frac{h_{i-1} - h_{i}}{\Delta x}) - 
# (K \Delta y \Delta z \frac{h_{i} - h_{i+1}}{\Delta x})  
# $$
# 
# Then divide by cell width $\Delta y $,
# 
# $$
# S_{s} \Delta x \Delta z \frac{\partial h_i}{\partial t} = 
# (K  \Delta z \frac{h_{i-1} - h_{i}}{\Delta x}) - 
# (K  \Delta z \frac{h_{i} - h_{i+1}}{\Delta x})
# $$
# 
# Rewrite the right hand side into gradient of head form
# 
# $$
# S_{s} \Delta x \Delta z \frac{\partial h_i}{\partial t} = 
# (K \Delta z \frac{h_{i+1} - h_{i}}{\Delta x}) - 
# (K \Delta z \frac{h_{i} - h_{i-1}}{\Delta x})
# = 
# {K \Delta z \frac{\partial h}{\partial x}}\mid_{i~\rightarrow i+1} -
# {K \Delta z \frac{\partial h}{\partial x}}\mid_{i-1~\rightarrow i}
# $$
# 
# Divide by cell distance, $\Delta x$,
# 
# $$
# S_{s}  \Delta z \frac{\partial h_i}{\partial t} = 
# \frac{{K \Delta z \frac{\partial h}{\partial x}}\mid_{i~\rightarrow i+1} -
# {K \Delta z\frac{\partial h}{\partial x}}\mid_{i-1~\rightarrow i}}{\Delta x}
# $$
# 
# Take limit as $\Delta x~\rightarrow0$, 
# 
# $$
# S_{s} \Delta z  \frac{\partial h}{\partial t} = 
# \frac{\partial}{\partial x}({K \Delta z \frac{\partial h}{\partial x}})
# $$
# 
# Finally, stipulate that $S_{s} \Delta z = S$, the storage coefficient (for confined aquifer), and define the aquifer transmissivity as $K \Delta z = T$ and we have performed a nicely back-handed way to get the partial differential equation of aquifer flow.  
# 
# $$
# S \frac{\partial h}{\partial t} = 
# \frac{\partial}{\partial x}({T \frac{\partial h}{\partial x}})
# $$
# 
# ## Solution Methods
# 
# Ironically, the analysis actually provides an algorithm to approximate head in the aquifer 
# 
# ### Finite-Difference Methods -- 1 Spatial Dimension
# Here we will use the equation obtained after dividing by the water density as a starting point for simulating aquifer behavior.   
# 
# As a first model, lets consider the steady flow situation, in which case the left hand side vanishes (there is no change in storage).
# 
# $$
# 0 = 
# (K \Delta y \Delta z \frac{h_{i-1} - h_{i}}{\Delta x}) - 
# (K \Delta y \Delta z \frac{h_{i} - h_{i+1}}{\Delta x})
# $$
# 
# Next we will use the arithmetic mean values of the material properties ($K$) at the cell interfaces, so the difference equation becomes
# 
# :::{note}
# Other spatial averaging formulas are employed, but the arithmetic mean is quite common
# :::
# 
# $$
# 0 = 
# (\frac{1}{2}(K_{i-1}+K_{i}) \Delta y \Delta z \frac{h_{i-1} - h_{i}}{\Delta x}) - 
# (\frac{1}{2}(K_{i}+K_{i-1}) \Delta y \Delta z \frac{h_{i} - h_{i+1}}{\Delta x})
# $$
# 
# Now lets group some constants:
# 
# $$
# \begin{matrix}
# A_{i} = \frac{1}{2 \Delta x}(K_{i-1}+K_{i}) \Delta y \Delta z \\
# B_{i} = \frac{1}{2 \Delta x}(K_{i}+K_{i+1}) \Delta y \Delta z
# \end{matrix}
# $$
# 
# Now substitute into the difference equation
# 
# $$
# 0 = A_{i}(h_{i-1}) -(A_{i}+B_{i})(h_{i}) + B_{i}(h_{i+1})
# $$
# 
# Now all that remains is to specify boundary conditions, and then implement an algorithm to solve the resulting system of algebraic equations.
# 
# :::{note}
# I have assumed that the spatial step, $\Delta x$ is the same for each cell -- it doesn't have to be, but relaxing that assumption complicates the specifications of the constants $A$ and $B$.
# :::
# 
# Some of the plausible boundary conditions are:
# 1. Specified head boundary (pretty easy to specify in a computer representation).
# 2. Zero-flux boundary (also easy to specify using the cell-centered formulation herein).
# 3. Specified flux boundary (using a modeling trick not too hard to specify).
# 
# These three types of conditions should handle the majority of practical situations where one would need to model an aquifer system.
# 
# Lets examine the difference equation a little bit -- assume we have the correct values then
# 
# $$
# h_{i} = \frac{A_{i}(h_{i-1}) + B_{i}(h_{i+1})}{(A_{i}+B_{i})}
# $$
# 
# which suggests a nice algorithm. 
# 
# We will simply apply boundary conditions, then evaluate the expression for each cell, and after we compute the expression for all the cells, we will repeat the process until the solution stops changing.  
# 
# Computationally, we are employing a Jacobi iteration scheme, which will work nicely for this particular problem structure.  
# An alternative, equally valid, would be to construct the linear system of equations (in this case it will be a three-banded matrix), and apply an appropriate row reduction technique to find the solution. 
# 
# ### Homebrew - Example 1
# 
# ### Homebrew - Example 2
# 
# ### Finite-Difference Methods -- 2 Spatial Dimensions

# In[ ]:




