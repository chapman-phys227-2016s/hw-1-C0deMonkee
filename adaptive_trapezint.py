#! /usr/bin/env python

"""
File: adaptive_trapezint.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 3.8
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Adaptive trapezoidal rule that decides how many trapezoids to use in order to achieve a desierd accuracy
"""
import numpy as np

def II_derivative_max(f, a, b, n=654321):
    """
    Calculates the maximum of the second derivative using many points: 654,321 of them to find the max of those points.
    """
    delta = (b - a) / float(n)
    max = abs(II_derivative(f, a))
    for i in range(n):
        current = abs(II_derivative(f, a + delta * (i + 1)))
        if current > max:
            max = current
    return max

def II_derivative(f, x, h=1e-6):
    return (f(x - h) - 2 * f(x) + f(x + h)) / float(h**2)

def trapezint(f, a, b, n):
    """
    Function from excercise 3.6
    """
    h = (b-a) / float(n)
    sum = 0
    for i in range(int(n)):
        sum = sum + (1/2.0)*h*(f(a + h*i) + f(a + h*(i + 1)))
    return sum

def adaptive_trapezint(f, a, b, eps=1E-5):
    """
    Adaptive trapezoidal rule that decides how many trapezoids to use in order to achieve a desierd accuracy
    """
    h = np.sqrt(12*eps)*(((b-a)*II_derivative_max(f, a, b))**(-1/2.0))
    n = (b-a)/float(h)
    return (trapezint(f, a, b, n), n)

def outputInformation():
    """
    Outputs the information of the exact error and estimated n for each case of adaptive_trapezint(f, a, b, eps=1E-5)
    """
    cos1 = adaptive_trapezint(cos, 0, np.pi)
    sin1 = adaptive_trapezint(sin, 0, np.pi)
    sin2 = adaptive_trapezint(sin, 0, np.pi/2)

    error1 = abs(cos1[0]-0)
    error2 = abs(sin1[0]-2)
    error3 = abs(sin2[0]-1)

    print("Function\tError\t\t\tEstimated n")
    print("Cos [0,Pi]\t" + str(error1) + "\t" + str(cos1[1]))
    print("Sin [0,Pi]\t" + str(error2) + "\t" + str(sin1[1]))
    print("Sin [0,Pi/2]\t" + str(error3) + "\t" + str(sin1[1]))
def line(x):
    return 2*x + 2
def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)

def test_trap_rule():
    """
    Area of a triangle = 1/2*b*h = 8 for the line 2x+2 integrated from 0 to 2
    """
    print(abs(trapezint(line, 0, 2, 100)))
    assert (abs(trapezint(line, 0, 2, 100) - 8) < 1E-5)
