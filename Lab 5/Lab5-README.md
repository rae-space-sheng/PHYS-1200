# Lab5
Rae Sheng  
PHYS 1200: Computational Lab  
Professor Zahra Alavi  
Wednesday, 12 March 2025  

**Exercise 1:** Calculating Gravitational Force Between Planets  
* **Objective:** Write a program to calculate the gravitational force between two planets given their massesand the distance between them.  
* **Instructions:**
  * Import the NumPy library.
  * Define a variable for the gravitational constant, G, with a value of 6.674e-11 (N m²/kg²).
  * Create two NumPy arrays, masses and distances, to store the masses of the planets (in kilograms) and the distances between them (in meters), respectively.
  * Use a loop to iterate over the elements of the masses and distances arrays.
  * For each pair of planets, calculate the gravitational force using the formula: F = G * (m1 * m2) / d², where m1 and m2 are the masses of the planets, and d is the distance between them.
  * Print the gravitational force for each pair of planets.  
  
**Exercise 2:** Analyzing Projectile Motion  
* **Objective:** Write a program to calculate the horizontal and vertical positions of a projectile at different time intervals, given its initial velocity and launch angle.  
* **Instructions:**  
  * Import the NumPy library.
  * Define variables for the initial velocity (v0), launch angle (theta), and acceleration due to gravity (g, with a value of 9.81 m/s²).
  * Convert the launch angle from degrees to radians.
  * Create a NumPy array time_intervals to represent different time intervals (in seconds) after the launch.
  * Use a loop to iterate over the time_intervals array.
  * For each time interval, calculate the horizontal position (x = v0 * cos(theta) * t) and the vertical position (y = v0 * sin(theta) * t - 0.5 * g * t²).
  * Print the time interval along with the corresponding horizontal and vertical positions.  
  
**Exercise 3:** Calculating Resistance in Series and Parallel Circuits  
* **Objective:** Write a program to calculate the total resistance of a circuit with resistors in series and in parallel.
* **Instructions:**
  * Import the NumPy library.
  * Create two NumPy arrays, resistors_series and resistors_parallel, to store the resistance values (in ohms) of resistors in series and parallel configurations, respectively.
  * Use a loop to iterate over the resistors_series array and calculate the total resistance in series by summing up all the resistance values.
  * Use a loop to iterate over the resistors_parallel array and calculate the total resistance in parallel using the formula: 1 / R_total = 1 / R1 + 1 / R2 + ... + 1 / Rn, where Rn is the resistance of each resistor in parallel.
  * Print the total resistance for both series and parallel configurations.  
