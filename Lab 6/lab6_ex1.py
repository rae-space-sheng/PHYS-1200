#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 14:41:02 2025

@author: raesheng
"""

"""
Rae Sheng
Professor Alavi
PHYS 1200
19 March 2025

Lab 6: Example 1: Plotting Projectile Motion

Objective: Write a program to calculate the horizontal and vertical positions
           of a projectile at different time intervals,
           given its initial velocity and launch angle.
           Then make a plot of x vs t, y vs t and x vs y using subplots.
           Try different formats for your plots.

Instructions:
    • Import the NumPy library.
    • Define variables for the initial velocity (v0), launch angle (theta),
      and acceleration due to gravity (g, with a value of 9.81 m/s²).
      Convert the launch angle from degrees to radians.
    • Calculate the total time and assign it to a variable (time).
      Create a NumPy array time_intervals to represent different time intervals
      (in seconds) starting from zero to total-time .
    • Calculate the arrays for horizontal position (x_t)
      and the vertical position (y_t).
    • Plot x vs time_intervals, y vs time_intervals and x vs y using subplots.
      Make sure your axis are labeled and your plots are titled.
"""

# Import NumPy.
import numpy as np
import matplotlib.pyplot as plt

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

# Calculate total time.
# Code from Lab 5:
#    x = v0 * np.cos(theta) * time_intervals[i]
#    y = (v0 * np.sin(theta) * time_intervals[i]) - (0.5 * g * (time_intervals[i]**2))
# Deriving equation for total time.
#   y = 0
#   v0 * sin(theta) * total_time = 0.5 * g * total_time^2
#   v0 * sin(theta) = 0.5 * g * total_time (removes total_time = 0)
#   total_time = v0 * sin(theta) / 0.5 / g
time = v0 * np.sin(theta) / 0.5 / g 
time = np.ceil(time + 1) # Round up to get full graph.
# But having decimal points in total time means np.arange() will be very long.

# Start filling in variables.
t = np.arange(0, time)
x_t = np.zeros(t.size)
y_t = np.zeros(t.size)

# Use iteration to fill in x and y based on t.
i = 0
while i < t.size:
    x_t[i] = np.round(v0 * np.cos(theta) * t[i], 2)
    y_t[i] = np.round((v0 * np.sin(theta) * t[i]) - (0.5 * g * t[i]**2), 2)
    i += 1

# Variables: t, x_t, y_t

#Create a figure.
plt.figure()

"""
# SUBPLOT

# Make x(t) vs. t
plt.subplot(2, 2, 1)
plt.plot(t, x_t)
plt.title('x(t) vs. t')
plt.xlabel('t, time in seconds')
plt.ylabel('x(t), length in meters')

# Make y(t) vs. t
plt.subplot(2, 2, 2)
plt.plot(t, y_t)
plt.title('y(t) vs. t')
plt.xlabel('t, time in seconds')
plt.ylabel('y(t), height in meters')

# Make y(t) vs. x(t)
plt.subplot(2, 2, 3)
plt.plot(x_t, y_t)
plt.title('y(t) vs. x(t)')
plt.xlabel('x(t),  length in meters')
plt.ylabel('y(t), height in meters')

plt.tight_layout()
plt.show()
"""

# SUBPLOTS
fig, axes = plt.subplots(2, 2)

axes[0,0].plot(t, x_t)
axes[0, 0].set_title('x(t) vs. t')

axes[1,0].plot(t, y_t)
axes[1, 0].set_title('y(t) vs. t')

axes[0,1].plot(x_t, y_t)
axes[0,1].set_title('y(t) vs. x(t)')

plt.tight_layout()
plt.show()