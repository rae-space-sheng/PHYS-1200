#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 13:44:05 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
Due 26 March 2025
Submitted 1 April 2025

Lab 7: Example 3: Histogram of Thermal Energy Distribution

Objective: Create a histogram showing the distribution of thermal energy
           in a system at different temperatures.

Instructions:
    • Import the necessary libraries.
    • Define a NumPy array for thermal energy values at different temperatures.
    • Use Matplotlib to create a histogram showing the distribution of
      thermal energy.
    • Label the axes and add a title to the plot.
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define Numpy array for thermal energy values (Joules)
# I came up with the numbers at random
data = np.array([12, 14, 18, 29, 49, 3, 19, 40, 39, 58, 69, 10, 57, 98, 47])

# Create histogram chart
plt.hist(data, bins = 6)
plt.xlabel('Thermal Energies (J)')
plt.ylabel('Distribution')
plt.title('Histogram of Thermal Energies Distribution')
plt.show()