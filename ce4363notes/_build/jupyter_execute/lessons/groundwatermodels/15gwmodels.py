#!/usr/bin/env python
# coding: utf-8

# # MODFLOW Program

# ## Introduction

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

# In[1]:


get_ipython().system(' pwd')


# ## References
# 
# 1. [Groundwater Modeling Exercise (used in video)](http://54.243.252.9/ce-4363-webroot/3-Readings/Groundwater_modelling_exercise.pdf)

# In[ ]:




