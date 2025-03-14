#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:56:19 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
29 January 2025

Lab 1: Coding practice 2

A ball is thrown upwards with an initial velocity of v. Write a code
that takes v from the user and prints the maximum height it reaches.
Assume acceleration due to gravity g is 9.8 meters per second squared
(downwards).
"""

import numpy as np

# Get the initial velocity from the user.
print('Provide the initial velocity (m/s) as a number. Decimals accepted.')
v = float(input())

# The formula for tossing something straight up in the air
# is v^2/2/g, or v^2/19.6, derived from PHYS 1100 equations.
print("The object thrown upwards reaches a maximum height of", end=" ")
print(np.round(v**2/19.6, 1), end=" meters in the air.")