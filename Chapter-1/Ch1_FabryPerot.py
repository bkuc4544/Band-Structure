# -*- coding: utf-8 -*-
"""
@author: Bharat Kuchhal

Description: The code simulates the transmission and reflection for a Fabry-Perot cavity for different values of reflectivities.
"""

import numpy as np
import matplotlib.pyplot as plt

def Trans(R, phis):
    T = (1 - R)**2
    return T/(T + 4*R* np.sin(phis/2)**2)

def Refl(R, phis):
    T = (1 - R)**2
    return (4*R* np.sin(phis/2)**2)/(T + 4*R* np.sin(phis/2)**2)

R1 = 0.1
R2 = 0.4
R3 = 0.7
R4 = 1.0
# alpha = 1  (Symmetric lossless resonator)

phis = np.linspace(0, 6*np.pi, 3001)

Trans1 = Trans(R1, phis)
Refl1 = Refl(R1, phis)

Trans2 = Trans(R2, phis)
Refl2 = Refl(R2, phis)

Trans3 = Trans(R3, phis)
Refl3 = Refl(R3, phis)

Trans4 = Trans(R4, phis)
Refl4 = Refl(R4, phis)

#%%
ticks = [0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi, 6*np.pi]
tick_labels = ["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$", r"$5\pi$", r"$6\pi$"]

fig, ax = plt.subplots(figsize=(20, 12))
ax.plot(phis, Trans1, label='$\mathcal{R}=0.1$')
ax.plot(phis, Trans2, label='$\mathcal{R}=0.4$')
ax.plot(phis, Trans3, label='$\mathcal{R}=0.7$')
ax.plot(phis, Trans4, label='$\mathcal{R}=1.0$')
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels)
ax.set_xlabel('Phase $\\varphi$')
ax.set_ylabel('Transmittance T($\\varphi$)')
plt.legend()
plt.rcParams['font.size'] = 20

#%%
fig, ax = plt.subplots(figsize=(20, 12))
ax.plot(phis, Refl1, label='$\mathcal{R}=0.1$')
ax.plot(phis, Refl2, label='$\mathcal{R}=0.4$')
ax.plot(phis, Refl3, label='$\mathcal{R}=0.7$')
ax.plot(phis, Refl4, label='$\mathcal{R}=1.0$')
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels)
ax.set_xlabel('Phase $\\varphi$')
ax.set_ylabel('Reflectance R($\\varphi$)')
plt.legend()
plt.rcParams['font.size'] = 20

