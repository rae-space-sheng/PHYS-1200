#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:01:17 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
9 April 2025

Lab 9, Example 2: Vector rotation

Objective: Write a function that takes a vector as (x, y) and an angle in
           degrees, and returns the image of the vector under rotation by
           theta as a numpy array. Practice calling your function and unpacking
           its result. Hint: Use rotation matrix and np.dot!
"""

import numpy as np

# This function calculates the 2D rotation matrix based on the given angle.
def rotation_matrix(t):
    matrix = [[np.cos(t), np.sin(-t)], [np.sin(t), np.cos(t)]]
    return matrix

# This function requires that the rotation angle be written in degrees.
def rotate_vector(x_component, y_component, angle):
    # Set up vector components
    old = [[x_component], [y_component]]
    
    # Set up rotation angle
    new = np.dot(rotation_matrix(np.deg2rad(angle)), old)
    vector = (np.round(new[0][0], 2), np.round(new[1][0], 2))
    return vector

# Put in the terminal to test code. Replace components and angle as needed.
vector_x, vector_y = rotate_vector(1, 5, 90)
print("The x-component of the result of the given vector rotated at the given angle is ", end="")
print(vector_x, end="")
print(" units in the x-direction and ", end="")
print(vector_y, end="")
print(" units in the y-direction. Enjoy your new vector!")