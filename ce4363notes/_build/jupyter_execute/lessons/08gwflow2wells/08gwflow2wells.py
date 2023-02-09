#!/usr/bin/env python
# coding: utf-8

# # Groundwater Flow to Wells - I (pp. 156-162)
# 
# ## Terminology
# 
# - Drawdown
# - Cone of Depression
# - Well interference
# 
# Have already examined steady flow solutions.
# 
# ## Unsteady Flow Solutions
# 
# There are two ways to proceede - just apply the groundwater flow equatrions or use a plasuibility argument to infer what solutions might look like.
# 
# **Infer Structure**
# 
# ![](f2w-001.png)
# 
# ![](f2w-002.png)
# 
# ![](f2w-003.png)
# 
# ![](f2w-004.png)
# 
# ![](f2w-005.png)
# 
# ![](f2w-006.png)
# 
# ![](f2w-007.png)
# 
# ![](f2w-008.png)
# 
# ![](f2w-009.png)
# 
# ![](f2w-010.png)
# 
# **Apply Groundwater Flow Equations**
# 
# ![](cf2well001.png)
# 
# ![](cf2well002.png)
# 
# ![](cf2well003.png)
# 
# ![](cf2well004.png)
# 
# ![](cf2well005.png)
# 
# ![](cf2well006.png)
# 
# ![](cf2well007.png)
# 

# ## Implementing Solutions
# 
# In the olden days, one would look up well function values in tabulations such as [TWRI BOOK 3 Chapter B3 TYPE CURVES FOR SELECTED PROBLEMS OF FLOW TO WELLS IN CONFINED AQUIFERS](https://pubs.usgs.gov/twri/twri3-b3/pdf/TWRI_3-B3.pdf)
# 
# Many of the special functions were leter embedded in the analysis packages for spreadsheets.
# 
# Or one can simply program themselves as shown below:

# In[1]:


def W(u): # Theis well function using exponential integral
    import scipy.special as sc
    w = sc.expn(1,u)
    return(w)

def s(radius,time,storage,transmissivity,discharge): # Drawdown function using exponential integral
    import math
    u = ((radius**2)*(storage))/(4*transmissivity*time)
    s = ((discharge)/(4*math.pi*transmissivity))*W(u)
    return(s)


# Lets choose an the example from the book on pg. 162 to illustrate the homebrew script.  The relevant problem parametrs are:
# 
# - $K = 14.9 m/d$
# - $b = 20.1 m$
# - $T = Kb = 299 m^2/d$
# - $S = 0.0051$
# - $Q_w = 2725 m^3/d$
# - $r = 7.0 m $
# - $t = 1 d$

# In[2]:


radius=7.0
time=1.0
storage=0.0051
transmissivity=299
discharge=2725

print("Drawdown is ",round(s(radius,time,storage,transmissivity,discharge),2)," meters")


# ## References
# 
# 1.  [Cleveland, T.G., (2001) *Groundwater Hydrology - Lecture 009* Lecture Notes to accompany CE 6361 at the University of Houston](http://54.243.252.9/ce-4363-webroot/ce4363notes/lessons/08gwflow2wells/Lecture009.PDF)
# 
# 2. [TWRI BOOK 3 Chapter B3 TYPE CURVES FOR SELECTED PROBLEMS OF FLOW TO WELLS IN CONFINED AQUIFERS](https://pubs.usgs.gov/twri/twri3-b3/pdf/TWRI_3-B3.pdf)

# In[ ]:




