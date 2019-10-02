#!/usr/bin/env python

import time, random
import os, sys
import pdb

import numpy as np
import matplotlib.pyplot as plt

from numpy import pi, sqrt, exp
from sympy import symbols, solve, latex, pprint
from functools import wraps

#import pandas as pd
#from scipy.optimize import fsolve

def f0():
    pass

def plot(func):
    @wraps(func)
    def wrapper(*args, **kw):
        plt.plot(x, func(x))
        plt.savefig("func.png")
        plt.show()
    return wrapper

@plot
def f1(x, mu=0, delta=1):
    return 1 / (sqrt(2 * pi) * delta) * exp(-(x - mu) ** 2) / (2 * delta ** 2)

def f2():
    a, b, c, x = symbols("a, b, c, x")
    y = a * x**2 + b * x +c
    result = solve(y, x)
    pprint(result)

if __name__ == "__main__":
    #pdb.set_trace()
    x = np.linspace(-5,5,201)
    f1(x)
    f2()
