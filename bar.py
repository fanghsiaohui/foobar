#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from pprint import pprint

def f(t):
    x, y = t
    f1 = x**2 + y**2 - 16
    f2 = x - y - 4
    return f1,f2

solve = fsolve(f, [1, 1])
