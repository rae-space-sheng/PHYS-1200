#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:59:55 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
9 April 2025

Lab 7, Example 4: Plot the trajectory of a 2D random walk

Objective: A walker is walking on a 2D plane. At each step he once flips a coin
          to determine wether to go forward or backward along the x axis, and
          once to determine wether to go forward or backward along the y axis.
          Each step size is 1. Write a code that plots his trajectory after
          500 steps.

Instructions:
    1. Create two arrays like the one from Ex. 1 with 500 random True and
       False, one for x axis (x_step) and one for y axis (y_step).
    2. Convert your two arrays so they include +1 and -1 s instead of True
       and False.
    3. Operate a cumulative sum on your arrays to get the coordinate at each
       step. Hint: look up np.cumsum
    4. Plot your coordinates. Label everything.
    5. Run your code a bunch of times and compare the results.
    6. Now when you define rng give it a seed value. Then run your code a
       bunch of times and compare the results.
"""

import numpy as np
import matplotlib.pyplot as plt

# Use a random number generator to get our random -1's and 1's.
# Insert a number into the parentheses after rng for the seed.
rng = np.random.default_rng(32)
x_rand = rng.random((500))
y_rand = rng.random((500))

# Setting up x_step and y_step with random -1's and 1's.
x_step = np.full(500, 1)
y_step = np.full(500, 1)

# If random < 0.5, then step = -1.
i = 0
while i < x_step.size:
    if x_rand[i] < 0.5:
        x_step[i] = -1
    if y_rand[i] < 0.5:
        y_step[i] = -1
    i += 1

# Set up steps.
x = np.cumsum(x_step)
y = np.cumsum(y_step)

plt.plot(x, y)
plt.title("Walker progression over 500 steps")
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.tight_layout()
plt.show()