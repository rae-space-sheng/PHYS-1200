#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 13:12:05 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
Due 26 March 2025
Submitted 1 April 2025

Lab 7: Example 1: Plotting functions, alternative solution

"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define range and functions
x = np.linspace(2, 7, 400)
y1 = np.exp(x)
y2 = x**3.6

fig, axs = plt.subplots(1, 3, figsize = (12, 4))

axs[0].plot(x, y1, label = '$e^x$')
axs[0].plot(x, y2, label = '$x^{3.6}$')
axs[0].set_title('Linear Plot')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].legend()

axs[1].semilogy(x, y1, label = '$e^x$')
axs[1].semilogy(x, y2, label = '$x^{3.6}$')
axs[1].set_title('Semi-Log Plot')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].legend()

axs[2].loglog(x, y1, label = '$e^x$')
axs[2].loglog(x, y2, label = '$x^{3.6}$')
axs[2].set_title('Log-Log Plot')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].legend()

# Adjust layout and show plots
plt.tight_layout()
plt.show()