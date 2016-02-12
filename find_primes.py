#! /usr/bin/env python

"""
File: find_primes.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 3.34
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implementing a prime sieve
"""

def find_primes(n):
    """
    Creates a generator that outputs prime numbers between 1 and n
    """
    nums = [True] * n
    nums[0] = nums[1] = False
    for i, isPrime in enumerate(nums):
        if isPrime:
            yield i
            for j in range(i*i, n, i):
                nums[j] = False
    return

def test_primse():
    nums = find_primes(100)
    assert(next(nums) == 2 and next(nums) == 3 and next(nums) == 5 and next(nums) == 7 and next(nums) == 11)