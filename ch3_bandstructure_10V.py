# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:30:37 2024

@author: bkuch
"""

import numpy as np
import matplotlib.pyplot as plt


Omega = 17.279e6
w_L = 0.05
V1 = 10
V2 = 8
#V2 = 3*V1
Vpi = 11
#Vpref = (Omega/4j)*V0/Vpi   # For VM = V0 sin (Omega*t) modulation
Vpref1 = (Omega/4)*V1/Vpi     # For VM = V0 cos (Omega*t) modulation
#Vpref2 = 0
Vpref2 = (Omega/4)*V2/Vpi     # For VM = V0 cos (Omega*t) modulation

q1 = 1
q2 = 2
phi = np.pi/2
p_max = 20


def band(k, Omega, p_max, Vpref1, Vpref2, w_L):
    
    Hk = np.zeros((2*p_max+1, 2*p_max+1), dtype=complex)
    for p in range(-p_max, p_max+1):
        Hk[p+p_max,p+p_max] = p*Omega     # Diagonal
        for p_pr in range(-p_max, p_max+1):
            Hk[p_pr+p_max, p+p_max] += Vpref1 * (np.exp(-1j*(p_pr-p-q1)*Omega*k) * 
                np.sinc(2*w_L*np.pi*(p_pr-p-q1)))
            Hk[p_pr+p_max, p+p_max] += Vpref2 * (np.exp(-1j*(p_pr-p-q2)*Omega*k) * 
                np.sinc(2*w_L*np.pi*(p_pr-p-q2)) * np.exp(1j*phi))
            Hk[p_pr+p_max, p+p_max] += Vpref1 * (np.exp(-1j*(p_pr-p+q1)*Omega*k) * 
                np.sinc(2*w_L*np.pi*(p_pr-p+q1)))
            Hk[p_pr+p_max, p+p_max] += Vpref2 * (np.exp(-1j*(p_pr-p+q2)*Omega*k) * 
                np.sinc(2*w_L*np.pi*(p_pr-p+q2)) * np.exp(-1j*phi))

    eig_tuple = np.linalg.eigh(Hk)
    return eig_tuple[0][p_max], eig_tuple[1][:, p_max]


list_k = (np.pi/Omega)*np.linspace(-1, 1, 301)  # Sample k values
list_evals = np.zeros(len(list_k))
list_evecs = np.zeros((len(list_k), 2*p_max+1), dtype=complex)

for m_k, k in enumerate(list_k):
    list_evals[m_k], list_evecs[m_k] = band(k, Omega, p_max, Vpref1, Vpref2, w_L)
    
list_omega = (3*Omega/2)*np.linspace(-1, 1, 301)  # Frequency grid
list_transmission = np.zeros((len(list_k), len(list_omega)))
gamma = Omega/50

sout = np.zeros((len(list_k), len(list_omega)), dtype=complex)
for m_k, k in enumerate(list_k):
    for m_omega, omega in enumerate(list_omega):
        for p in range(-2, 3):
            sout[m_k, m_omega] += (1j*gamma/(omega-list_evals[m_k]-p*Omega+1j*gamma))*\
                np.abs(list_evecs[m_k, p_max])**2
            list_transmission[m_k, m_omega] += (gamma**2/((omega-list_evals[
                m_k]-p*Omega)**2+gamma**2)*np.abs(
                    list_evecs[m_k, p_max])**4)

#%%
list_transmission_trans = list_transmission.T
fig, ax = plt.subplots(figsize=(16, 16))
pc = ax.pcolormesh(*np.meshgrid(list_k/(max(list_k)), list_omega/Omega), list_transmission.T)
ax.set_xlabel('$k\omega_0/\pi$')
ax.set_ylabel('$\Delta\omega/\omega_0$')
#plt.xlim(-1, 0)
#plt.ylim(-0.5, 0.5)
fig.colorbar(pc, location='top')
fig.show()
plt.rcParams['font.size'] = 40

#%%
DOSs = list_transmission_trans.sum(axis=1)
DOSs /= max(DOSs)
fig, ax = plt.subplots(figsize=(12,8))
ax.plot(list_omega/Omega, DOSs)
ax.set_ylabel('Transmission')
ax.set_xlabel('$\Delta\omega/\omega_0$')
plt.rcParams['font.size'] = 20
#plt.ylim(-0.5, 0.5)
#ax.title('Density of States')

#%%
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(DOSs, list_omega/Omega)
ax.set_xlabel('Transmission')
ax.set_ylabel('$\Delta\omega/\omega_0$')
ax.xaxis.tick_top()
ax.yaxis.tick_right()
ax.xaxis.set_label_position("top")
ax.yaxis.set_label_position("right")
plt.rcParams['font.size'] = 10
#plt.ylim(-0.5, 0.5)
#ax.title('Density of States')

#%%
DOSs_flip = np.flip(DOSs)

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, gridspec_kw={'wspace': 0.075})
ax1.pcolormesh(*np.meshgrid(list_k/(max(list_k)), list_omega/Omega), list_transmission.T)
ax1.set_xlabel('$k\omega_0/\pi$')
ax1.set_ylabel('$\Delta\omega/\omega_0$')
#fig.colorbar(pc, location='top')
ax2.plot(DOSs_flip, list_omega/Omega)
ax2.set_xlabel('Transmission')
ax2.set_ylabel('$\Delta\omega/\omega_0$')
ax2.xaxis.tick_top()
ax2.xaxis.set_label_position("top")
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
plt.rcParams['figure.figsize'] = (40,24)
plt.rcParams['font.size'] = 45


