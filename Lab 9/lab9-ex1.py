#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 13:45:26 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
9 April 2025

Lab 9, Example 1: Taxicab distance measurement

Objective: Write a function to compute the straight-line distance between two
           points in 2-dimensional space.
"""

import numpy as np

def distance(initial_point, final_point = (0, 0), metric = 'taxi'):

    # Define and explain function
    """
    PARAMETERS
        initial_point: list/tuple, coordinates of initial point (x1, y1)
        final_point: list/tuple, coordinates of final point (x2, y2)
    
    RETURNS:
        straight_line_distance: float
    """
    
    # Calculate and return distance
    if metric == 'taxi':
        distance = abs(initial_point[0] - final_point[0]) + abs(initial_point[1] - final_point[1])
    else: # Euclidean
        distance = np.sqrt( (initial_point[0] - final_point[0])**2 + (initial_point[1] - final_point[1])**2 )
    return distance