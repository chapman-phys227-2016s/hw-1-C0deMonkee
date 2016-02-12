#! /usr/bin/env python

"""
File: centered_diff.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 3.18
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Approxiates many derivatives
"""

import sympy as sp

def quad(x):
    return (x**2)
def exp(x):
    return exp(x)
def exp2(x):
    return exp(-2*x**2)
def cos(x):
    return np.cos(x)
def ln(x):
    return np.log(x)

def diff(f,x, h=1E-5):
    """
    Approximates a derivative of a function at a point
    """
    return ((f(x+h)-f(x-h))/(2*float(h)))
def test_diff():
    print(diff(quad, 5))
    assert(diff(quad, 5) - 10 < 0.00001)

def application():
    print("error of e^x @ (x=0): " + abs(diff(exp, 0, .01) - 1))
    print("error of e^(-2x^2) @ (x=0): " + abs(diff(exp, 0, .01)))
    print("error of cos(x) @ (x=2pi): " + abs(diff(cos, 2*np.pi, .01)))
    print("error of ln(x) @ (x=1): " + abs(diff(ln, 1, .01)))