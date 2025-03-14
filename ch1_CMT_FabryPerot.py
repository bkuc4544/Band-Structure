# -*- coding: utf-8 -*-
"""
@author: Bharat Kuchhal

Description: The code uses coupled-mode theory to determine the transmission and reflection results for a Fabry-Perot cavity.
"""

import numpy as np
import matplotlib.pyplot as plt

Q1 = 1000
Q2 = 1000

domegas = np.linspace(-0.01, 0.01, 1001)

one_tau1 = 1/2/Q1
one_tau2 = 1/2/Q2

# Transmissivity
t = -(2*np.sqrt(one_tau1*one_tau2)) / (1j*domegas - one_tau1 - one_tau2)
Trans = np.abs(t) ** 2    # Steady-state Transmission

# Reflectivity
r = -(1 + (2*one_tau1)/(1j*domegas - one_tau1 - one_tau2))
Refl = np.abs(r) ** 2     # Steady-state Reflection

fig, ax = plt.subplots(figsize=(20, 12))
ax.plot(domegas, Trans, 'r', label='T($\omega$)')
ax.plot(domegas, Refl, 'b', label='R($\omega$)')
ax.set_xlabel('$\Delta\omega / \omega_0$')
ax.set_ylabel('$Intensity$')
plt.legend()
plt.rcParams['font.size'] = 23
