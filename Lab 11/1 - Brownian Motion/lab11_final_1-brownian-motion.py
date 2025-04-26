#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 14:05:16 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
11 May 2025

Lab 11, Problem 1: Brownian Motion

Objective: In this lab, you'll use Python to generate two-dimensional random
walks, plot their trajectories, and look at the distribution of end points for
a large number of random walkers.
           
Sections:

    1.1 - Generating and plotting trajectories

        A. Make a random walk trajectory, and then plot it. To remove any
        distortion, use the command plt. axis ('square') or plt.axis ('equal')
        after making the plot.
    
        B. Now make four such trajectories, and look at all four side by side.
        Use plt.figure() to create a new figure window. You can access the
        individual subplots by using commands like plt.subplot (2, 2, 1) before
        the first pIt.plot command, plt.subplot (2, 2, 2) before the second
        plt.plot command, and so on. Python may give each plot a diﬀerent
        magnification. Consult help(plt.xlim) and help(pIt.axis) to find out
        how to give each of your plots the same x and y limits.

    1.2 - Plotting the displacement distribution
    
        A. Once you have a code that works, increase the number of random walks
        from 100 to 1000. Make a scatter plot of the end points.
      
        B. Use plt.hist to make a histogram of the displacement values.
        
        C. Make a histogram of the quantity displacement**2.
        
        D. Your result from C may inspire a guess as to the mathematical form
        of the histogram. Use semilog and log-log axes to test for exponential
        or power law relationships.
        
        E. Use np.mean to find the average value of displacement**2 (the
        mean-square displacement) for a random walk of 1000 steps.
        
        F. Find the mean-square displacement of a 4000-step walk. If you wish
        to carry the analysis further, see if you can determine how the
        mean-square displacement depends on the number of steps in a random
        walk.
"""

import numpy as np
import matplotlib.pyplot as plt



""" SECTION 1-1, PART A """

# Set the number of steps taken using only one line.
num_steps = 1000

# This function returns two arrays: x-steps and y-steps.
def walker_2d(steps):
    # Use a random number generator to get our random -1's and 1's.
    # Insert a number into the parentheses after rng for the seed.
    rng = np.random.default_rng()
    x_rand = rng.random(steps)
    y_rand = rng.random(steps)
    
    # Setting up x_step and y_step with random -1's and 1's.
    x_step = np.full(steps, 1)
    y_step = np.full(steps, 1)
    
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
    
    return x, y
    
x, y = walker_2d(num_steps)
plt.plot(x, y)
plt.title("Walker trajectory (square)")
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.tight_layout()
plt.axis('equal')
plt.show()



""" SECTION 1-1, PART B """

# Create a new figure and subplot.
plt.figure()
axes = [-40, 40, -30, 30]

# Trajectory 1 out of 4.
plt.subplot(2, 2, 1)
x1, y1 = walker_2d(num_steps)
plt.plot(x1, y1)
plt.title("Walker trajectory 1")
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.tight_layout()
plt.axis(axes)

# Trajectory 2 out of 4.
plt.subplot(2, 2, 2)
x2, y2 = walker_2d(num_steps)
plt.plot(x2, y2)
plt.title("Walker trajectory 2")
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.tight_layout()
plt.axis(axes)

# Trajectory 3 out of 4.
plt.subplot(2, 2, 3)
x3, y3 = walker_2d(num_steps)
plt.plot(x3, y3)
plt.title("Walker trajectory 3")
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.tight_layout()
plt.axis(axes)

# Trajectory 4 out of 4.
plt.subplot(2, 2, 4)
x4, y4 = walker_2d(num_steps)
plt.plot(x4, y4)
plt.title("Walker trajectory 4")
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.tight_layout()
plt.axis(axes)
plt.show()



""" SECTION 1-2, PART A """

# Set the number of walks to observe data from.
num_walks = 1000

x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)

i = 0
while i < num_walks:
    x, y = walker_2d(num_steps)
    x_final[i] = x[-1]
    y_final[i] = y[-1]
    displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)
    i+=1
    
plt.scatter(x_final, y_final, 3)
plt.title("Scatterplot of endpoints")
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.axis('square')
plt.show()



""" SECTION 1-2, PART B """

# Create histogram chart.
plt.hist(displacement, bins = 50)
plt.title('Histogram of displacement from origin')
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.show()



""" SECTION 1-2, PART C """

# Create histogram chart.
count, bins, patches = plt.hist(displacement**2, bins = 50)
plt.title('Histogram of displacement**2 from origin')
plt.xlabel('x-axis, units of 1')
plt.ylabel('y-axis, units of 1')
plt.show()



""" SECTION 1-2, PART D """

bins = bins[1:]

fig, axs = plt.subplots(1, 3, figsize = (12, 4))

axs[0].plot(bins, count, label = 'Linear')
axs[0].set_title('Linear Plot')
axs[0].set_xlabel('Bins')
axs[0].set_ylabel('Count')
axs[0].legend()

axs[1].semilogy(bins, count, label = 'Exponential Log')
axs[1].set_title('Semi-Log Plot')
axs[0].set_xlabel('Bins')
axs[0].set_ylabel('Count')
axs[1].legend()

axs[2].loglog(bins, count, label = 'Power Log')
axs[2].set_title('Log-Log Plot')
axs[0].set_xlabel('Bins')
axs[0].set_ylabel('Count')
axs[2].legend()

plt.tight_layout()
plt.show()

print("SECTION 1-2, PART D:")
print("Based on the subplot with linear, semi-log, and log-log plots, we can see that the mathematical relationship for the quantity displacement^2 is most likely that of an exponential log.")


""" SECTION 1-2, PART E """

print("The average displacement for ", end="")
print(num_steps, end="")
print(" steps is ", end="")
print(np.round(np.mean(displacement), 3), end="")
print(" units.")


""" SECTION 1-2, PART F """
num_steps = 4000

num_walks = 1000

x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)

i = 0
while i < num_walks:
    x, y = walker_2d(num_steps)
    x_final[i] = x[-1]
    y_final[i] = y[-1]
    displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)
    i+=1

print("SECTION 1-2, PART F:")
print("The average displacement for ", end="")
print(num_steps, end="")
print(" steps is ", end="")
print(np.round(np.mean(displacement), 3), end="")
print(" units.")

""" FURTHER ANALYSIS (INCOMPLETE) """

num_analysis = 9
steps = np.zeros(num_analysis)
mean_displacement = np.zeros(num_analysis)

# Start at 1000 steps and increment to 10000 steps, then plot.

num_steps = 1000

x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)

j = 0
while j < num_analysis:

    i = 0
    while i < num_walks:
        x, y = walker_2d(num_steps)
        x_final[i] = x[-1]
        y_final[i] = y[-1]
        displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)
        i+=1
    
    steps[j] = num_steps
    mean_displacement[j] = np.mean(displacement)
    num_steps+=1000
    j+=1

plt.plot(steps, mean_displacement)
plt.title("Mean displacement vs. number of steps")
plt.xlabel('Number of steps')
plt.ylabel('Mean displacement (units of 1')
plt.tight_layout()
plt.show()

print()
print("FURTHER ANALYSIS: From the plot \"Mean displacement vs. number of steps,\" we can conclude that the relationship between the walker's mean displacement and the number of steps taken is linear.")
