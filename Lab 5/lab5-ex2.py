#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 12:52:39 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
12 March 2025

Lab 5: Example 2: Analyzing Projectile Motion

Objective: Write a program to calculate the horizontal and vertical positions
           of a projectile at different time intervals, given its initial
           velocity and launch angle.

Instructions:
    • Import the NumPy library.
    • Define variables for the initial velocity (v0), launch angle (theta),
      and acceleration due to gravity (g, with a value of 9.81 m/s²).
    • Convert the launch angle from degrees to radians.
    • Create a NumPy array time_intervals to represent different time intervals
      (in seconds) after the launch.
    • Use a loop to iterate over the time_intervals array.
    • For each time interval, calculate the horizontal position
      (x = v0 * cos(theta) * t) and the vertical position
      (y = v0 * sin(theta) * t - 0.5 * g * t²).
    • Print the time interval along with the corresponding
      horizontal and vertical positions.
"""

# Import NumPy.
import numpy as np

# Get and define variables.
print("Enter a positive number for the initial velocity (m/s). Decimals accepted.")
v0 = float(input())
print("")

print("Enter a number between 0 and 90 for the launch angle (degrees) above the x-axis. Decimals accepted.")
theta = float(input())
print("That's ", end = " ")
# Convert theta into radians.
theta = theta * np.pi / 180
print(np.round(theta, 2), end = " ")
print("in radians.")
print("")

g = 9.81

# Create time_intervals array.
print("Enter how many seconds after launch you would like to calculate the position for. Whole numbers greater than 0 only.")
time_intervals = np.arange(0, int(input()))
print("")

i = 0
while i < time_intervals.size:
    # Calculate the horizontal and vertical positions.
    x = v0 * np.cos(theta) * time_intervals[i]
    y = (v0 * np.sin(theta) * time_intervals[i]) - (0.5 * g * (time_intervals[i]**2))
    
    # Convey the information to the user.
    print(time_intervals[i], end=" ")
    print("seconds after launch,")
    print("the horizontal position is", end=" ")
    print(np.round(x, 2), end=" ")
    print("meters;")
    print("the vertical position is", end=" ")
    print(np.round(y, 2), end=" ")
    print("meters.")
    print("")
    
    # Increment.
    i += 1
