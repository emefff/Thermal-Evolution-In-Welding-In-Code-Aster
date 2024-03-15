#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:19:40 2024

https://www.heissbemessung.net/Infothek/Materialien_im_Brandfall/Steel-in-fire.html

@author: emefff
"""

from collections import OrderedDict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   


T1 = np.linspace(20,600,50)
heat_capa_data_temp = []
heat_capa_data_capa = []

for i,temp in enumerate(T1):
    heat_capa_600 = 425 + 7.73E-1*temp - 1.69E-3*temp**2 + 2.22E-6*temp**3    
    heat_capa_data_temp.append(temp)
    heat_capa_data_capa.append(heat_capa_600)
    
T2 = np.linspace(610,735,25)
for i,temp in enumerate(T2):
    heat_capa_735 = 666 + 13002 / (738 - temp)
    heat_capa_data_temp.append(temp)
    heat_capa_data_capa.append(heat_capa_735)

T3 = np.linspace(745,900,25)
for i,temp in enumerate(T3):
    heat_capa_900 = 545 + 17820 / (temp - 731)
    heat_capa_data_temp.append(temp)
    heat_capa_data_capa.append(heat_capa_900)

T4 = np.linspace(910,1200,25)
for i,temp in enumerate(T4):
    heat_capa_1200 = 650
    heat_capa_data_temp.append(temp)
    heat_capa_data_capa.append(heat_capa_1200)

print (heat_capa_data_capa,"\n")

# we need roh * Cp, density constant is enough Cp variation is much larger
roh = 7850 # kg/m³
heat_capa_data_capa = [1e-6 * roh * heat_capa for heat_capa in heat_capa_data_capa]

print (heat_capa_data_capa)

mapping = {'temperature':heat_capa_data_temp, 
           'RCP':heat_capa_data_capa}

df = pd.DataFrame(mapping)

# write the data to a file
filename = 'RCP_table.csv'
df.to_csv(filename, index = False, header = None)

# plot it to see if correct
plt.figure(figsize=(15,9))
plt.plot(heat_capa_data_temp,heat_capa_data_capa,'k-')
plt.show()
