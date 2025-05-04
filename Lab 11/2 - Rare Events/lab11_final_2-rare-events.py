#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 01:23:30 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
11 May 2025

Lab 11, Problem 2: Rare Events

Objective: In this lab, you'll use Python to visualize and plot Poisson
distribution using the example of a coin that unfairly lands on tails more
often.  

Sections:
    
    2.1 - Generating and plotting trajectories

        A. Before you start flipping coins, plot this function for some
        interesting range of l values. You may find the following helpful:
            
            • The factorial function can be imported from scipy. special.
            
            • You need not take l ρ(l) all the way out to infinity. You'll see
            that quickly gets negligibly small.
            
            • In Python, the elements of a vector are always numbered 0, 1, 2,
            3, ..., and l is also an integer starting from zero, so l is a good
            array index.
            
            • The value of 8^l can get very large- larger than the largest
            integer NumPy can store. (By default NumPy uses 64-bit integers,
            so the largest number it can store is 2^63 − 1.) To avoid numerical
            over flow - and erroneous results - use an array of floats instead
            of integers. Consult help(np.arange), and read about the dtype
            keyword argument.
    
        B. Perform N coin flip trials, each consisting of 100 flips of a coin
        that lands heads only 8% of the time. [Good practice: Eventually you
        may want to take N to be a huge number. While developing your code,
        make it not so huge, say, N = 1000, so that your code will run fast.]
        
        C. Get Python to count the number of heads, M, for each trial. Then,
        use plt.hist to create a histogram of the frequency of getting M heads
        in N trials. If you don't like what you see, consult help(plt. hist).
        (For example, plt.hist may make a poor choice about how to bin the
        data.)
        
        D. Make a graph of the Poisson distribution (Equation 11.2 above)
        multiplied by N. What's the most probable outcome? Graph this plot on
        the same axes as the histogram in C.
        
        E. Repeat (B-D) for N = 1000,000, and comment. This may take a while.

    2.2 - Plotting the displacement distribution
    
        A. Construct a random string of 1's and 0's representing 1000 flips of
        the unfair coin. Then, plot the frequencies of waiting times of length
        0, 1, 2, ..., as outlined above. Also make semilog and log-log plots
        of these frequencies. Is this distribution a familiar-looking function?
        
        B. What is the average waiting time between heads?
        
        C. Repeat A and B for 1000,000 flips of the coin.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import special as sp

""" SECTION 2.1, PART A """

# Using capital L for lambda.
L = 0.08
l = np.arange(10, dtype = "float")

# The probability that heads (L% chance) comes up l times in 100 flips.
def poisson():
    return np.exp(-L) * np.power(L, l) / sp.factorial(l)

p = poisson()

# Plot the "interesting range" of l.
plt.plot(l, p)
plt.title("Poisson function from 0 to 10 occurrences")
plt.xlabel('l (lowercase L, # of times unfair coin lands on heads)')
plt.ylabel('p (probability of occurence)')
plt.tight_layout()
plt.show()


""" SECTION 2.1, PART B AND C """
# Difficult to separate Part B and C
# due to the way I set up my code.

# Set up RNG and variables for coin flip trials.
N = 1000
num_flips = 100

rng = np.random.default_rng()
samples = rng.random((num_flips))

flips = np.full(num_flips, True)

# Head count.
M = np.zeros(N)

j = 0
while j < N:
    samples = rng.random((num_flips))
    # Heads = True, Tails = False.
    i = 0
    while i < samples.size:
        if samples[i] <= 0.08:
            flips[i] = False
            M[j] += 1
        i += 1
    j += 1


""" SECTION 2.1, PART C """

# Create histogram chart.
plt.hist(M, bins = np.arange(0, 27, 1))
plt.title('Frequency of M heads in N trials')
plt.xlabel('Number of Heads')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


""" SECTION 2.1, PART D """

# Create histogram chart.
plt.hist(M * N, bins = 15)
plt.title('Poisson distribution multiplied by N')
plt.xlabel('Number of Heads')
plt.ylabel('Distribution * N')
plt.tight_layout()
plt.show()



""" SECTION 2.1, PART E """

# Changed N = 1000 to N = 1,000,000.
# Changed back to 1000 to speed up debugging for 2.2.



""" SECTION 2.2, PART A """

# Creating array of 0 (tails) and 1 (heads).

num_flips = 1000
num_flips = 1000000

samples = rng.random((num_flips))
binary_flips = np.full(num_flips, 0)

m = 0
while m < samples.size:
    if samples[m] <= 0.08:
        binary_flips[m] = 1
    m += 1

nonzero = np.nonzero(binary_flips)
waiting_time = np.diff(nonzero)
waiting_time = waiting_time.flatten()
waiting_time += 1

# Regular histogram.
plt.hist(waiting_time)
plt.title('Waiting times between heads (regular)')
plt.xlabel('Number of seconds (1 flip/second)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Semi-log histogram.
plt.hist(waiting_time)
plt.title('Waiting times between heads (semi-log)')
plt.yscale('log')
plt.xlabel('Number of seconds (1 flip/second)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Log-log histogram.
plt.hist(waiting_time)
plt.title('Waiting times between heads (log-log)')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of seconds (1 flip/second)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

print("SECTION 2.2, PART A: We have a similar distribution to Part 1 of the final.")
print()



""" SECTION 2.2, PART B """

average = np.average(waiting_time)
print("SECTION 2.2, PART B: The average waiting time between the occurrence of heads for ", end = "")
print(num_flips, end = "")
print(" flips of a coin is ", end = "")
print(np.round(average, 2), end = "")
print(" seconds, assuming one flip per second and an 8% chance of the coin landing on heads.", end = "")


""" SECTION 2.2, PART C """

# Set num_flips = 1,000,000 in 2.2 as needed.