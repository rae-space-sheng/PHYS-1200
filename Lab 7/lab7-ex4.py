#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 13:44:06 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
Due 26 March 2025
Submitted 1 April 2025

Lab 7: Example 4: Pie Chart of Relative Abundances of Elements in the Universe

Objective: Create a pie chart showing the relative abundances of different
           elements in the universe.

Instructions:
    • Import the necessary libraries.
    • Define a list of element names and a corresponding list of their
      relative abundances.
    • Use Matplotlib to create a pie chart showing the relative abundances
      of the elements.
    • Add a legend to the plot.
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Source: Abundance of elements in Earth's crust by percentage, Wikipedia
# https://en.wikipedia.org/wiki/Abundance_of_elements_in_Earth%27s_crust

# Define list of element names
names = ['oxygen', 'silicon', 'aluminium', 'iron', 'calcium', 'sodium', 'magnesium', 'potassium']

# Define list of abundances by percentage
abundances = [46.1, 28.2, 8.23, 5.63, 4.15, 2.36, 2.33, 2.09]

# Create pie chart
plt.pie(abundances, labels = names, autopct = '%1.1f%%')
plt.title('Abundance of elements in Earth\'s crust')
plt.legend()
plt.show()