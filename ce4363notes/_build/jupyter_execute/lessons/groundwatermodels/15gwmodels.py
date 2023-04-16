#!/usr/bin/env python
# coding: utf-8

# # MODFLOW Program

# ## Introduction
# 
# *Adapted from [https://pubs.usgs.gov/fs/FS-121-97/](https://pubs.usgs.gov/fs/FS-121-97/)*
# 
# The modular finite-difference groundwater flow model (MODFLOW) developed by the U.S. Geological Survey (USGS) is a computer program for simulating common features in groundwater systems (McDonald and Har- baugh, 1988; Harbaugh and McDonald, 1996). The program was constructed in the ear- ly 1980s and has continually evolved since then with development of many new packages and related programs for groundwater studies. Currently MODFLOW is the most widely used program in the world for simulating ground- water flow. The popularity of the program is attributed to the following factors:
# - The finite-difference method used by MODFLOW is relatively easy to understand and apply to a wide variety of real-world conditions.
# - MODDFLOW works on many different computer systems ranging from personal computers to super computers.
# - MODFLOW can be applied as a one- dimensional, two-dimensional, or quasi- or full three-dimensional model.
# - Each simulation feature of MODFLOW has been evensively tested.
# - Data input instructions and theory are well documented.
# - The modular program design of MODFLOW allows for new simulation features to be added with relative ease.
# - A wide variety of computer programs written by the USGS, other federal agencies, and private companies are available to analyze field data and con- struct input data sets for MODFLOW.
# - A wide variety of programs are available to read output from MODFLOW and graphically present model results in ways that are easily understood.
# - MODFLOW has been accepted in many court cases in the United States as a legitimate approach to analysis of groundwater systems.
# 
# ### Modeling
# 
# Modeling is a tool used by engineers to make decisions regarding design and operation of an environmental system.  Models can be used to forecast future conditions in response to those decisions, select a best set of decisions based on some desired criterion, or determine the most likely physical values that explain an observed condition.
# 
# Because most real systems are far too complicated to model as they are, a set of simplifying assumptions is posed to make the modeling problem tractable - this is often called the "conceptual model".  
# 
# On the basis of these simplifying assumptions a "mathematical model" (usually balance equations) is created.  The solution of the mathematical model yields the behavior of the system being studied.
# 
# After the model is created, it is "calibrated".  This is the process of adjusting model parameters (transmissivity, storativity, etc.), forcing inputs, and geometry until the model response is identical (within some tolerance) to the observed historical response of the real system.  Multiple calibrations can produce identical responses, so great care must be taken in calibrating and testing a model before using it  - once acceptably calibrated the model can be used for forecasting.
# 
# **Classification of Environmental Models:**
# 1. Physical models (experimentation) - usually impractical for groundwater 'systems'.
# 2. Analog Models
# 3. Mathematical Models
#   - Analytical solutions - application of calculus to achieve closed-form equations (some of which can be very difficult to evaluate).
#   - Numerical solutions - application of numerical methods to achieve accurate approximations to the governing equations.

# ## MODFLOW 6 (Using your own computer)
# 
# This would be the preferred way to use MODFLOW for this class.  The install is not that hard, but alos not point and click.  A video showing an installation is available for viewing at:
# 
# - [Installing ModelMuse and MODFLOW 6 on a local computer](https://www.youtube.com/watch?v=x_D_rvsQ-tI&feature=youtu.be)
# 
# The installation process is:
# 
# 1. GOOGLE "modflow 6"  and/or select: [https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model) Download the MODFLOW 6 program (choose windows installer)
# 
# 2. GOOGLE "ModelMuse" and/or select: [https://www.usgs.gov/software/modelmuse-a-graphical-user-interface-groundwater-models](https://www.usgs.gov/software/modelmuse-a-graphical-user-interface-groundwater-models)  Download the interface program (installer for 32/64 bit.  Do not commit to 64 bit only (it might not work well).  When you get a real job, have an IT professional do the install and testing)
# 
# 3. Create C:/WRDAPP folder to house modflow binaries - note the folder attaches at C:/  any other path will probably mess things up later on.
# 
# 4. Install ModelMuse using installer (double click, accept defaults)
# 
# 5. Move the modflow package into C:/WRDAPP folder, extract package, put into folder root.
# 
# 6. Start ModelMuse
#   - create MODFLOW
#   - next
#   - next
#   - Model/MODFLOW Program Locations
#   - set the directory path (may need to edit names a bit)
#   
# 7. Restart ModelMuse and run tutorial.
#   - Pray for smiley faces!
#   - Yay! Install complete.

# ## MODFLOW 6 (Using Shared On-Line Windows Server 2019 on AWS)
# 
# A fully provisioned implementation of ModelMuse and MODFLOW 6 is available for use at:
# 
# - **server name** kittyinthewindow.ddns.net
# - **user name** ce3372-share
# - **passwort** modflow63\$hare
# 
# You must access using a **Remote Desktop Protocol** client application, it is built-in to Windows
# 
# - Windows Support Pages: [https://support.microsoft.com/en-us/windows/how-to-use-remote-desktop-5fe128d5-8fb1-7a23-3b8a-41e636865e8c](https://support.microsoft.com/en-us/windows/how-to-use-remote-desktop-5fe128d5-8fb1-7a23-3b8a-41e636865e8c)
# - Windows 10 Client: [https://apps.microsoft.com/store/detail/microsoft-remote-desktop/9WZDNCRFJ3PS?hl=en-au&gl=au&rtc=1&activetab=pivot%3Aoverviewtab](https://apps.microsoft.com/store/detail/microsoft-remote-desktop/9WZDNCRFJ3PS?hl=en-au&gl=au&rtc=1&activetab=pivot%3Aoverviewtab)
# - Mac OS Users: [https://apps.apple.com/app/microsoft-remote-desktop/id1295203466?mt=12](https://apps.apple.com/app/microsoft-remote-desktop/id1295203466?mt=12)
# - iOS Users: [https://apps.apple.com/app/microsoft-remote-desktop/id714464092](https://apps.apple.com/app/microsoft-remote-desktop/id714464092) **This would be really stupid to try to operate on a phone** but you could.  I think for iPad access this might make sense.
# - Other Drug Users (Android/Linux):[https://play.google.com/store/apps/details?id=com.microsoft.rdc.android](https://play.google.com/store/apps/details?id=com.microsoft.rdc.android)
# 
# ### Video Demonstrating Remote Connection
# 
# A video demonstrating remote connection is available at [Login to shared server running ModelMuse and MODFLOW 6](https://youtu.be/3Rv6e61FBYk)

# ## MODFLOW 1988 (On-Line Structured Input Files)
# 
# A functioning web-accessible implementation of MODFLOW88 is available at [54.243.252.9](http://54.243.252.9/toolbox/gwhydraulics/modflow/).  This is the hardest to use in terms of file management and error interpretation, but is reasonably easy to employ if using legacy files and the older documentation.
# 
# - **server name** http://54.243.252.9/toolbox/gwhydraulics/modflow/
# - **user name** MODFLOW99
# - **passwort** On-Line
# 
# A video demonstrating the creation and running of a model using this implementation is available at [YouTube](https://youtu.be/ZxFDEgkOkzU).

# ## MODFLOW Python Interfaces
# 
# A way to access MODFLOW using Python and Jupyter Notebooks is avaliable at 
# 
# [FloPy: Python Package for Creating, Running, and Post-Processing MODFLOW-Based Models ](https://www.usgs.gov/software/flopy-python-package-creating-running-and-post-processing-modflow-based-models)
# 
# The PDF link below shows the installation and an example run on the AWS server.
# 
# [MODFLOW on a Jupyter Server - notes](http://54.243.252.9/ce-4363-webroot/ce4363notes/lessons/groundwatermodels/installing.pdf)
# 

# ## References
# 
# 1. [Groundwater Modeling Exercise (used in video)](http://54.243.252.9/ce-4363-webroot/3-Readings/Groundwater_modelling_exercise.pdf)
# 2. [MODFLOW Notes (Cleveland circa 1992)](http://54.243.252.9/ce-4363-webroot/3-Readings/modflowNotes01.pdf)  The Obleo Aquifer simulation in the MODFLOW88 video is described in these notes.
# 3. [MODFLOW Manual (US EPA)](http://54.243.252.9/ce-4363-webroot/3-Readings/modflmn.pdf) An EPA training document on the use of MODFLOW

# In[ ]:




