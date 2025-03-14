#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 12:27:27 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
12 March 2025

Lab 5: Example 1: Calculating Gravitational Force between Planets

Objective: Write a program to calculate the gravitational force
           between two planets given their masses
           and the distance between them.

Instructions:
    • Import the NumPy library.
    • Define a variable for the gravitational constant, G,
      with a value of 6.674e-11 (N m²/kg²).
    • Create two NumPy arrays, masses and distances, to store
      the masses of the planets (in kilograms) and
      the distances between them (in meters), respectively.
    • Use a loop to iterate over the elements of the masses and distances arrays.
    • For each pair of planets, calculate the gravitational force
      using the formula: F = G * (m1 * m2) / d²,
      where m1 and m2 are the masses of the planets,
      and d is the distance between them.
    • Print the gravitational force for each pair of planets.
"""

# Import the NumPy library.
import numpy as np

# Define gravitational constant.
g = 6.674e-11

# Create list of planet names. 8 entries.
name = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Create NumPy array for masses of planets (kg). 8 entries.
mass = np.array([0.33e24, 4.87e24, 5.97e24, 0.64e24, 1900e24, 568e24, 86.8e24, 102e24])

# Create NumPy array for distance between planets (m). 7 entries.
dist = np.array([5.03e10, 4.14e10, 7.83e10, 5.50e11, 6.46e11, 1.45e12, 1.63e12])

# Go through arrays/lists and calculate the
# gravitational force using F = g * (m1 * m2) / d^2.

i = 0
while i < 7: # Count of 7 to avoid error for dist[i].
    # Calculate f while looping through planets.
    m1 = mass[i]
    m2 = mass[i + 1]
    d = dist[i]
    f = g * (m1 * m1) / (d**2)
    
    # Print the planet names and gravitational force.
    print("The gravitational force between ", end="")
    print(name[i], end=" ")
    print(" and ", end=" ")
    print(name[i + 1], end=" ")
    print(" is ", end=" ")
    print(np.format_float_scientific(f, 3), end=" ")
    print(" Newtons.")
    

    # Increase the count.
    i += 1