#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:07:17 2025

@author: raesheng
"""

"""
Rae Sheng
PHYS 1200
Professor Zahra Alavi
19 February 2025

EXERCISE 2: List of Prime Numbers

Objective:  Create a list of prime numbers and
            perform various operations on it.

Scenario:   Let's say we want to create a list
            of the first few prime numbers and then
            perform some basic operations like
            adding new primes, accessing elements, and
            combining with another list:

1- Create a list of the first 5 prime numbers.
2- Add a few more.
3- Access the first and last prime numbers of the list.
4- Create a new list containing only the first three prime numbers.
5- Combine the list of prime numbers with another list of primes.
6- Reversing the List.
"""

# Part 1 - Create a list of the first 5 prime numbers
prime = [2, 3, 5, 7, 11]

# Part 2 - Add a few more
prime.append(13)
prime.append(17)
prime.append(19)
print(prime)

# Part 3 - Access the first and last prime numbers of the list
print(prime[0])
print(prime[-1])

# Part 4 - Create a new list containing only the first three prime numbers
prime_3 = [prime[0], prime[1], prime[2]]
print(prime_3)

# Part 5 - Combine the list of prime numbers with another list of primes
prime_add = prime_3 + prime
print(prime_add)

# Part 6 - Reversing the List
prime_reversed = prime[::-1]
print (prime_reversed)