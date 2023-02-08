#!/usr/bin/env python
# coding: utf-8

# # Groundwater Flow Equations (pp. 130-135; 
# 
# ## Confined Aquifer
# 
# $$S \frac{\partial h}{\partial t} = \frac{\partial}{\partial x}(T_x\frac{\partial h}{\partial x}) 
# + \frac{\partial}{\partial y}(T_y\frac{\partial h}{\partial y}) \pm source/sink $$
# 
# ## Unconfined Aquifer
# 
# $$S_y \frac{\partial h}{\partial t} = \frac{\partial}{\partial x}(K_x h \frac{\partial h}{\partial x}) 
# + \frac{\partial}{\partial y}(K_y h \frac{\partial h}{\partial y}) \pm source/sink $$
# 
# ## Solutions (p. 134)
# 
# Solved by a model that consists of the governing flow equation (one of the above), boundary conditions, and initial conditions.  Generally the goal is a description of the head at any location and time.  
# 
# Solution methods:
# 
# - Analysis.  Some geometries are suitable for analysis (using calculus), other complex geometries are solved using computer programs implementing numerical methods.
# - Computer Programs
# 

# ## References 
# 
# 1. [Cleveland, T.G., (2001) *Groundwater Hydrology - Lecture 008* Lecture Notes to accompany CE 6361 at the University of Houston](http://54.243.252.9/ce-4363-webroot/ce4363notes/lessons/06gwflowequations/Lecture_008.PDF)

# In[ ]:




