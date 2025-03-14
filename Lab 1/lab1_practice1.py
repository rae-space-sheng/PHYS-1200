# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
29 January 2025

Lab 1: Coding practice 1

Suppose an object starts from rest and accelerates uniformly. If
the acceleration is a and the time for which this acceleration is
applied is t , write a code that takes a and t from the user and
prints the final position s of the object.

"""

import numpy as np

# Get the acceleration from the user.
print('Type the acceleration (m/s) as a number. Decimals accepted.')
a = float(input())

# Get the time elapsed from the user.
print('Type the time elapsed (s) as a number. Decimals accepted.')
t = float(input())

# Equation for distance traveled is
# acceleration times time elapsed squared divided by 2.
print("The final position of the object is", end=" ")
print(np.round(a*(t**2)/2, 1), end=" meters.")