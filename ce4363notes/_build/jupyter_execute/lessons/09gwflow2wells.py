#!/usr/bin/env python
# coding: utf-8

# # Groundwater Flow to Wells - II
# 
# Leaky Confining Layer (No storage in the confining layer) A.K.A. Hantush (1956) Solution
# 
# ## Unsteady Flow Solutions
# 

# In[1]:


def wh(u, rho): # Hantush Leaky aquifer well function
    import numpy
    """Returns Hantush's well function values

    Note: works only for scalar values of u and rho

    Parameters:
    -----------
    u : scalar  (u= r^2 * S / (4 * kD * t))
    rho : sclaar (rho =r / lambda, lambda = sqrt(kD * c))
    Returns:
    --------
    Wh(u, rho) : Hantush well function value for (u, rho)
    """
    try:
        u =float(u)
        rho =float(rho)
    except:
        print("u and rho must be scalars.")
        raise ValueError()

    LOGINF = 2
    y = numpy.logspace(numpy.log10(u), LOGINF, 1000)
    ym = 0.5 * (y[:-1]+  y[1:])
    dy = numpy.diff(y)
    wh = numpy.sum(numpy.exp(-ym - (rho / 2)**2 / ym ) * dy / ym)
    return wh


# In[2]:


wh(0.4,0.06)


# In[3]:


def W(u): # Theis well function using exponential integral
    import scipy.special as sc
    w = sc.expn(1,u)
    return(w)

def s(radius,time,storage,transmissivity,discharge): # Drawdown function using exponential integral
    import math
    u = ((radius**2)*(storage))/(4*transmissivity*time)
    s = ((discharge)/(4*math.pi*transmissivity))*W(u)
    return(s)
    


# In[4]:


s(824,8/1440,2.4e-05,1400,42400)


# ## References
# 1. [Leaky Well Functions](https://transientgroundwaterflow.readthedocs.io/en/latest/WellInLeakyAquifer.html)

# In[ ]:




