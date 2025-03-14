# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
19 February 2025

EXERCISE 3: Weight on a Planet

Objective: Use a dictionary to store “g” for each planet,
           then calculate the weight on a given planet.

Description: Create a dictionary including the eight planets
                 as keys and their value for gas values.
             Get the mass of the user in kg and their desired planet.
             Use the planet the user enters to extract the value
                 of its g from the dictionary and return the weight
                 of the user on that planet.
"""

# Getting weight in pounds.
print("How many kilograms do you weigh on Earth?\n")
w = float(input())
a = 0
answered = False

# Informing user of available planets.
print("\nChoose a planet to find out how much\nyou would weigh on it. Case sensitive.\n")
print("Mercury\nVenus\nEarth\nMars\nJupiter\nSaturn\nUranus\nNeptune\n")
p = str(input())

# Make sure the user enters the name of a valid planet.
while answered == False:

    # Dictionary of gravitational forces.
    gravity = {"Mercury": 3.7, "Venus": 8.9, "Earth": 9.8, "Mars": 3.7, "Jupiter": 23.1, "Saturn": 9.0, "Uranus": 8.7, "Neptune": 11.0}
    if p in gravity:
        answered = True
        a = w / gravity["Earth"] * gravity[p]
    if p not in gravity:
        print("/nSorry, please enter a valid planet.")

# Calculate and relay information to user.
print("\nOn " + p + ", you would weigh " + str(round(a)) + " kilograms,")
print("as opposed to " + str(round(w)) + " kilograms on Earth. Thanks!")
