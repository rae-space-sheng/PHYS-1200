#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 13:55:15 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
12 March 2025

Lab 5: Example 3: Calculating Resistance in Series and Parallel Circuits

Objective: Write a program to calculate the total resistance
           of a circuit with resistors in series and in parallel.

Instructions:
    • Import the NumPy library.
    • Create two NumPy arrays, resistors_series and resistors_parallel,
      to store the resistance values (in Ohms) of resistors in series
      and parallel configurations, respectively.
    • Use a loop to iterate over the resistors_series array
      and calculate the total resistance in series
      by summing up all the resistance values.
    • Use a loop to iterate over the resistors_parallel array
      and calculate the total resistance in parallel
      using the formula: 1 / R_total = 1 / R1 + 1 / R2 + ... + 1 / Rn,
      where Rn is the resistance of each resistor in parallel.
    • Print the total resistance for both series and parallel configurations.

"""

# Import NumPy.
import numpy as np

# Create resistors_series
resistors_series = np.array([1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9])

# Create resistors_parallel
resistors_parallel = np.array([5.0, 5.2, 5.3, 5.7, 6.2, 6.8, 7.0, 7.1])

# Calculate total resistance in series using iteration
i = 0
total_series = 0
while i < resistors_series.size:
    total_series += resistors_series[i]
    i += 1

# Calculate total resistance in parallel using iteration, remember formula
i = 0
total_parallel = 0
while i < resistors_parallel.size:
    total_parallel += 1/resistors_parallel[i]
    i += 1

# Print the total resistance for both
print("Total resistance in series configuration:", end=" ")
print(np.round(total_series, 1))

print("Total resistance in parallel configuration:", end=" ")
print(np.round(total_parallel, 2))
print("")