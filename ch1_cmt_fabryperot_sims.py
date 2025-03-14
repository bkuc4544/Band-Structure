# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:37:46 2024

@author: bkuch

Ch1, Eqs. (1.42)
"""

import numpy as np
import matplotlib.pyplot as plt

Q1 = 1000
Q2 = 1000

domegas = np.linspace(-0.01, 0.01, 1001)    #domega = omega/omega0

#%%
# T = (4/tau1/tau2) / ((omega - omega0)^2 + (1/tau1 + 1/tau2)^2)

# Let domega = omega/omega0 - 1
# one_tau1 = 1/tau1 = w0/2Q_1, i.e., 1/tau1 = 1/2Q_1 normalized by w0
# one_tau2 = 1/tau2 = w0/2Q_2, i.e., 1/tau2 = 1/2Q_2 normalized by w0

# t = s2-/s1+ = -(2 * sqrt(one_tau1*one_tau2)) / (1j*domegas - one_tau1 - one_tau2)
# Trans = abs(t) ** 2
 
# and
# r = - (1 + (2*one_tau1)/(1j*domegas - one_tau1 - one_tau2))
# Refl = abs(r) ** 2

#%%

one_tau1 = 1/2/Q1
one_tau2 = 1/2/Q2

t = -(2*np.sqrt(one_tau1*one_tau2)) / (1j*domegas - one_tau1 - one_tau2)
Trans = np.abs(t) ** 2    # Steady-state Transmission

r = -(1 + (2*one_tau1)/(1j*domegas - one_tau1 - one_tau2))
Refl = np.abs(r) ** 2     # Steady-state Reflection

fig, ax = plt.subplots(figsize=(20, 12))
ax.plot(domegas, Trans, 'r', label='T($\omega$)')
ax.plot(domegas, Refl, 'b', label='R($\omega$)')
ax.set_xlabel('$\Delta\omega / \omega_0$')
ax.set_ylabel('$Intensity$')
plt.legend()
plt.rcParams['font.size'] = 23
