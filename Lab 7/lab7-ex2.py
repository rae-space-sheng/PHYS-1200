#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 13:13:25 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
Due 26 March 2025
Submitted 1 April 2025

Lab 7: Example 2: Bar Chart of Kinetic Energy of Different Objects

Objective: Create a bar chart showing the kinetic energy of different objects
           with varying masses and constant velocity.

Instructions:
    • Import the necessary libraries: NumPy for calculations and Matplotlib
      for plotting.
    • Define a NumPy array for the masses of different objects.
    • Assume a constant velocity for all objects.
    • Calculate the kinetic energy for each object using the formula
      kinetic_energy = 0.5 * mass * velocity**2.
    • Use Matplotlib to create a bar chart showing the kinetic energy
        of each object.
    • Label the axes and add a title to the plot.
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define Numpy array for masses of different objects
mass = np.array([0.9, 2, 3.1, 4.5, 6.2])

# Assume and define constant velocity
velocity = 5

# Understanding bar charts
"""
categories = ['A', 'B', 'C', 'D'] # Define categories for x-axis
values = [10, 25, 15, 5] # Define values for y-axis
plt.bar(categories, values) # Create bar chart
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()
"""

# Calculate kinetic energy
ke = 0.5 * mass * velocity**2

# Create bar chart
plt.bar(mass, ke)
plt.xlabel('Masses (kg)')
plt.ylabel('Kinetic Energy (J)')
plt.title('Kinetic Energy (Velocity = 5)')
plt.show()
