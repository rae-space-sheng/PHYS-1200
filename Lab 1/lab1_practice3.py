#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:07:17 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
29 January 2025

Lab 1: Coding practice 3

A box of mass m is sliding on a surface with a coefficient of
kinetic friction uk. Write a code that takes m and uk from the user
and prints the force of friction acting on the box. Assume acceleration
due to gravity. Make sure your code is nice and has enough comments.

"""

import numpy as np

# Get the mass of the box from the user.
print("Provide the mass (kg) of the box. Decimals accepted.")
m = float(input())
print()

# Get the coefficient of kinetic friction from the user.
print("Provide the coefficient of kinetic friction. Decimals accepted.")
uk = float(input())

# Define gravity.
g = 9.8

# Calculate the force of friction (coefficient x mass x gravity),
# then relay this information to the user.
print("The force of friction acting on the box as it slides across a flat surface is", end=" ")
print(np.round(uk*m*g, 1), end=" Newtons.")