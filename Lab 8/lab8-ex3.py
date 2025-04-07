#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:55:59 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
9 April 2025

Lab 7, Example 3: Simulating coin flips

Objective: Write a code that simulates coin flips and returns the total number
           of heads after 100 flips.
           
Instructions:
    1. Using random.default_rng() create 100 random numbers and assign it to
       an array called samples
    2. Convert the numbers in samples to True or False using samples < 0.5,
       sign the results to an array called flips.
    3. Count the number of heads by adding up the items in flips.
"""

# Import library and set up rng
import numpy as np
rng = np.random.default_rng()
samples = rng.random((100))

# Create array full of True
flips = np.full(100, True)

i = 0

# If < 0.5, then false
while i < samples.size:
    if samples[i] < 0.5:
        flips[i] = False
    i += 1
    
# Therefore, all Trues mean >= 0.5

# Heads = True, Tails = False

print("The coin landed on heads ", end = "")
print(np.count_nonzero(flips), end = "")
print(" out of 100 times.")