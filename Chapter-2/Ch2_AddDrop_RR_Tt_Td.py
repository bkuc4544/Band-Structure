# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:48:42 2024

@author: Bharat Kuchhal
"""

"""
Description: This code plots the transmission spectrum via the Through and Drop ports for an Add-Drop Ring Resonator for different
             beam-splitter configurations. 
"""

import numpy as np
import matplotlib.pyplot as plt


phis = np.linspace(-np.pi/2, np.pi/2, 1001)

def trans(alpha, r1, r2):
    
    Den = 1 - 2*r1*r2*alpha*np.cos(phis) + (r1*r2*alpha)**2

    # Transmission via Through Port
    Num_through = r2**2 * alpha**2 - 2*r1*r2*alpha*np.cos(phis) + r1**2
    through = Num_through/Den
    
    #Transmission via Drop Port
    Num_drop = alpha * (1 - r1**2) * (1 - r2**2)
    drop = Num_drop/Den
    
    return [through, drop]

alpha = 0.95             # Round-trip loss
r1 = [0.95, 0.995]       # Reflectivity of BS 1
r2 = [0.95, 0.995]       # Reflectivity of BS 2


# %%
ticks_x = [-np.pi/2, 0, np.pi/2]
tick_labels_x = [r"$\pi/2$", "0", r"$\pi/2$"]

fig, ax = plt.subplots(figsize=(20, 12))
for idx in range(len(r1)):
    string = '$r_1 = r_2$ = '+str(r1[idx])
    ax.plot(phis, trans(alpha, r1[idx], r2[idx])[0], label='$T_t$ ('+string+')')
    ax.plot(phis, trans(alpha, r1[idx], r2[idx])[1], label='$T_d$ ('+string+')')
ax.set_xlabel('$\\varphi$')
ax.set_ylabel('Transmission')
ax.set_xticks(ticks_x)
ax.set_xticklabels(tick_labels_x)
plt.legend()
plt.ylim(0,1)
plt.rcParams['font.size'] = 30
