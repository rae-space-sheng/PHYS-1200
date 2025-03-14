#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:00:03 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
26 February 2025

Lab 5: In-Class Practice with Numpy Arrays
"""

#Import the Numpy library.
import numpy as np

# Create a 1D array of odd numbers.
arr1 = np.array([1, 3, 5, 7, 9])

# Create a 1D array of even numbers.
arr2 = np.array([2, 4, 6, 8, 10])

# arr*2 - Multiplies all values in the array individually by 2.

arr01 = np.zeros((2, 4))

# np.zeros - Creates a new matrix of zeroes with X rows and Y columns.

a = np.arange(1, 10)
b = np.arange(5)
c = np.arange(2.11, 5.4, 0.1)

# Creates a new array with the range described in the parameters,
# with the decimal specificity of the most precise given value.

a = np.zeros((2, 3))
b = np.ones((2, 3))
h = np.hstack([a, b])
# Stacked horizontally, next to each other.
v = np.vstack([a, b])
# Stacked vertically. Mismatch of sizes will lead to error.

A = np.array([[1,2,3], [4,5,6]])
A[1][2] = 999
A[0] = [0, 0, 0]