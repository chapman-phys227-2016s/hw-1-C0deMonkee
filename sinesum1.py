#! /usr/bin/env python

"""
File: sinsum1.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 3.15
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Compares two functions, one to approximate the other
"""

import numpy as np

def S(t, n, T):
    """
    Returns the value of function S(t;n)
    """
    sum = []
    for i in range(1,n+1):
        sum.append(((2 * (i + 1) - 1)**-1) * np.sin((2 * (2 * (i + 1) - 1) \
        * np.pi * t) / float(T)))
    return np.sum(sum) * 4 / np.pi

def f(t, T):
    """
    Returns the value of the piecewise function f(t)
    """
    if(t < T/2.0):
        return 1
    elif(t == T/2.0):
        return 0
    return -1

def outputTable():
    """
    Outputs a table of errors of ranging values of n and t
    """
    table = [["\nn", "alpha", "\tValue of S", "\tValue of f", "Value of f - S\n"]]
    T = 2 * np.pi
    n = [1, 3, 5, 10, 30, 100]
    t = [0.01 * T, 0.25 * T, 0.49 * T]

    for elem_n in n:
        for elem_t in t:
            S_val = S(elem_t, elem_n, T)
            f_val = f(elem_t, T)
            table.append([elem_n, elem_t/T, S_val, f_val, f_val - S_val])
    print(str(table[0][0]) + "\t" + str(table[0][1]) + "\t" + str(table[0][2]) + "\t" + str(table[0][3]) + "\t" + str(table[0][4]))
    for num, j in enumerate(table):
        if(num == 0):
            continue
        if(num%3 == 1):
            print("\n")
        print(str(j[0]) + "\t" + str(j[1]) + "\t" + str(j[2]) + "\t\t" + str(j[3]) + "\t\t" + str(j[4]))

def test_sum():
    sum = S(.49, 1, 2 * np.pi)
    assert(sum - (4/np.pi)*(1)*np.sin((.49*2*np.pi)/(2*np.pi)) < .001)