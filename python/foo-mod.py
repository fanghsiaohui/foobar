#!/usr/bin/env python

import time, random
import os, sys
import pdb

from functools import wraps

import numpy as np
import matplotlib.pyplot as plt

from numpy import pi, sqrt, exp
from sympy import symbols, solve, latex, pprint

#import pandas as pd
#from scipy.optimize import fsolve

def f0():
    pass

def plot(func):
    @wraps(func)
    def wrapper(*args, **kw):
        plt.figure()
        plt.plot(*args, func(*args, **kw))
        plt.savefig("{}.png".format(func.__name__))
        plt.show()
    return wrapper

@plot
def f1(x, mu=0, sigma=1):
    return 1 / (sqrt(2 * pi) * sigma) * exp(-(x - mu) ** 2 / (2 * sigma ** 2))

@plot
def f2(x):
    return x**2 - x

@plot
def f3(x):
    return np.cos(x)

def f4():
    a, b, c, x = symbols("a, b, c, x")
    y = a * x**2 + b * x +c
    result = solve(y, x)
    pprint(result)

if __name__ == "__main__":
    #pdb.set_trace()
    x = np.linspace(-10, 10, 2001)
