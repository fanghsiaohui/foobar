#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time
# import numpy as np
# import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from math import sin, cos

# code below
def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
            5*x1 + 3,
            4*x0**2 - 2*sin(x1*x2),
            x1*x2 -1.5
            ]

result = fsolve(f, [1,1,1])
print(result)
print(f(result))

