#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 14:02:56 2025

@author: raesheng
"""

# Import MATPLOTLIB
import matplotlib.pyplot as plt

# Create basic line plot.
x = [0,1,2,3]
y = [2,4,6,8]

# Create the plot.
plt.plot(x,y)

# Label the axes.
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Title the plot.
plt.title('Basic line plot')

# Show the plot. Shows up in Plots pane, to the right of Variable Explorer.
plt.show()

# Can have multiple plots in the same graph. Consult handouts.

# matplotlib.pyplot.subplot