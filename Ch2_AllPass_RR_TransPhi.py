# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:49:49 2024

@author: Bharat Kuchhal

Description: This code plots the transmission spectrum via the Through port and the overall Phase Shift for an All-Pass Ring Resonator 
             for different cavity Finesse values.
"""

import numpy as np
import matplotlib.pyplot as plt

alpha = 0.95                                # Amplitude Transmission Factor
phis = np.linspace(-0.3*np.pi, 0.3*np.pi, 1001)

F = 10 * np.linspace(1, 6, 6)                # Finesses

# Rearranging F = pi sqrt(r1 alpha) / (1 - r1 alpha)
pi_by_2F = np.pi/2/F
r1 = ((-pi_by_2F + np.sqrt(1 + pi_by_2F**2)) ** 2) / alpha

num = np.zeros((np.size(F), np.size(phis)), dtype=complex)
den = np.zeros((np.size(F), np.size(phis)), dtype = complex)
st_s = np.zeros((np.size(F), np.size(phis)), dtype=complex)
T = np.zeros((np.size(F), np.size(phis)))
Phi = np.zeros((np.size(F), np.size(phis)))

# Transmission and Phase
for idx in range(len(F)):
    num[idx, :] = alpha - r1[idx]*np.exp(-1j*phis)
    den[idx, :] = 1 - r1[idx]*alpha*np.exp(1j*phis)
    st_s[idx, :] = np.exp(1j*(np.pi + phis)) * num[idx]/den[idx]
    T[idx, :] = np.abs(st_s[idx]) ** 2                      # Cavity Transmission
    Phi[idx, :] = np.angle(st_s[idx])                       # Phase of cavity transmission


#Plots
ticks_x = [-0.3*np.pi, -0.2*np.pi, -0.1*np.pi, 0, 0.1*np.pi, 0.2*np.pi, 0.3*np.pi]
tick_labels_x = [r"$-0.3\pi$", r"$-0.2\pi$", r"$-0.1\pi$", "0", r"$0.1\pi$", r"$0.2\pi$", r"$0.3\pi$"]
ticks_Phis_y = [-np.pi, 0, np.pi]
tick_labels_Phis_y = [r"$-\pi$", "0", r"$\pi$"]

fig, ax = plt.subplots(figsize=(20, 12))
for idx in range(len(F)):
#    string = 'F = '+str(F[idx])
    ax.plot(phis, T[idx], label='$\mathcal{F}$ = '+str(F[idx]))
ax.set_xlabel('$\\varphi$')
ax.set_ylabel('Transmission $T_t$')
ax.set_xticks(ticks_x)
ax.set_xticklabels(tick_labels_x)
plt.ylim(0, 1)
plt.legend()
plt.rcParams['font.size'] = 30

fig, ax = plt.subplots(figsize=(20, 12))
for idx in range(len(F)):
#    string = 'F = '+str(F[idx])
    ax.plot(phis, Phi[idx], label='$\mathcal{F}$ = '+str(F[idx]))
ax.set_xlabel('$\\varphi$')
ax.set_ylabel('Phase $\Phi$')
ax.set_xticks(ticks_x)
ax.set_xticklabels(tick_labels_x)
ax.set_yticks(ticks_Phis_y)
ax.set_yticklabels(tick_labels_Phis_y)
plt.legend()
plt.rcParams['font.size'] = 30
