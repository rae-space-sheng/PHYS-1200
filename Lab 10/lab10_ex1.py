#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 15:17:52 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
23 April 2025

Lab 10, Example 1: Numerical Integration
           
Instructions:
    1. Integrate f(x) = x^2 from x = 0 to x = 2 and check the results.
    2. Evaluate the integral from 0 to x-max with an integrand of e^(-x^2/2)dx 
       from x = 0 to x = 5 and plot the results.
    3. Can quad handle infinite limits? Use -np.inf and np.inf as limits to
       evaluate the integral from -infinity to infinity with an integrand of
       e^(-x^2/2)dx. Compare to the exact result: sqrt(2pi).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

""" PART 1 """

# This is the function to be integrated.
def f(x):
    return (x**2)

# Integrate f(x) from 0 to 2.
result, error = quad(f, 0, 2)

print("*** RESULTS FOR PART 1: ***")
print()
print("Integral: ", np.round(result, 2))
print("Estimated error: ", np.format_float_scientific(error, 2))
print()



""" PART 2 """

def g(x):
    return (np.exp((-x**2)/2))

upper_limit = np.linspace(0, 5, 100)
results = np.zeros(upper_limit.size)

for i in range(upper_limit.size):
    results[i], error = quad(g, 0, upper_limit[i])
    
x = upper_limit
y = results
plt.plot(x, y)
plt.title('Part 2: Results for x=0 to x=5')
plt.xlabel('x-value from 0 to 5')
plt.ylabel('Value of integral from 0 to x')
plt.tight_layout()
plt.show()

print("*** RESULTS FOR PART 2: ***")
print()
print("Please refer to the Plots viewing screen.")
print()



""" PART 3 """

# Integrate f(x) from -infinity to infinity.
result, error = quad(g, -np.inf, np.inf)

print("*** RESULTS FOR PART 3: ***")
print()
print("Integral: ", np.round(result, 5))
print("Estimated error: ", np.format_float_scientific(error, 2))
print("Result is exactly equal to sqrt(2pi): ", result == np.sqrt(2*np.pi))
print()
print("As long as the integral converges, quad can handle infinite limits. I tested this with x^2, which is divergent.")