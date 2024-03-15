#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:16:40 2024

https://www.heissbemessung.net/Infothek/Materialien_im_Brandfall/Steel-in-fire.html

@author: emefff

"""

from collections import OrderedDict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
 

T1 = np.linspace(20,800,60)

ther_cond_data_temp = []
ther_cond_data_cond = []

for i,temp in enumerate(T1):
    ther_cond_800 = 54 - 3.33E-2 * temp    
    ther_cond_data_temp.append(temp)
    ther_cond_data_cond.append(ther_cond_800)
    
T2 = np.linspace(810,1200,20)
for i,temp in enumerate(T2):
    ther_cond_1200 = 27.3 # wrong on the homepage!!
    ther_cond_data_temp.append(temp)
    ther_cond_data_cond.append(ther_cond_1200)

mapping = {'temperature':ther_cond_data_temp, 
           'thermal_conductivity':ther_cond_data_cond}
      
df = pd.DataFrame(mapping)

# write the data to a file
filename = 'thermal_conductivity_table.csv'
df.to_csv(filename, index = False, header = None)

# plot it to see if correct
plt.figure(figsize=(15,9))
plt.plot(ther_cond_data_temp,ther_cond_data_cond,'k-')
plt.show()
