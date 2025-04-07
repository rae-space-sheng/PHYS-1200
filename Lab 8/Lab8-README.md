# Lab 9
Rae Sheng  
PHYS 1200  
Professor Zahra Alavi  
9 April 2025
  
**Example 1:** Taxicab distance measurement  
* **Objective:** Write a function to compute the straight-line distance between two points in 2-dimensional space.
  
**Example 2:** Vector rotation
* **Objective:** Write a function that takes a vector as (x, y) and an angle in degrees, and returns the image of the vector under rotation by theta as a numpy array. Practice calling your function and unpacking its result. Hint: Use rotation matrix and np.dot!
  
**Example 3:** Simulating coin flips
* **Objective:** Write a code that simulates coin flips and returns the total number of heads after 100 flips.
* **Instructions:**  
  * Using random.default_rng() create 100 random numbers and assign it to an array called samples.
  * Convert the numbers in samples to True or False using samples < 0.5, assign the results to an array called flips.
  * Count the number of heads by adding up the items in flips.

**Example 4:** Plot the trajectory of a 2D random walk
* **Objective:** A walker is walking on a 2D plane. At each step, he once flips a coin to determine whether to go forward or backward along the x axis, and once to determine whether to go forward or backward along the y axis. Each step size is 1. Write a code that plots his trajectory after 500 steps.
* **Instructions:**  
  * Import the NumPy library.
  * Define variables for the initial velocity (v0), launch angle (theta), and acceleration due to gravity (g, with a value of 9.81 m/s²).Convert the launch angle from degrees to radians.
  * Calculate the total time and assign it to a variable (time). Create a NumPy array time_intervals to represent different time intervals (in seconds) starting from zero to total-time.
  * Calculate the arrays for horizontal position (x_t) and the vertical position (y_t).
  * Plot x vs time_intervals, y vs time_intervals and x vs y using subplots. Make sure your axis are labeled and your plots are titled.  
  
