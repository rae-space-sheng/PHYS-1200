#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:07:00 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
19 February 2025

EXERCISE 1: Tuple for Vector Components

Objective: Use tuples to represent 2D vector components.

Description: Ask the user to input the x and y components of a vector.
             Store these components in a tuple.
             Calculate the magnitude of the vector.
             Print the components and the magnitude.
"""

import numpy as np

# Declare and initialize variables.
x = 0
y = 0

# Welcome the user and inform them of the goal.
print("Welcome. Today, we will find the magnitude of a 2D vector.")

# Get the x-component from the user.
print("\nWhat is the x-component? Decimals accepted.")
x = float(input())

# Get the y-component from the user.
print("\nThank you. What is the y-component? Decimals accepted.")
y = float(input())
  
# Find magnitude using Numpy.
m = np.sqrt(x**2 + y**2)

# Relay information.
print("\nThe magnitude of your vector is " + str(round(m, 1)) + " units.")