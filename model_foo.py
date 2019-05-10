#!/usr/bin/env python3
#import pdb, sys, os, time, re, shutil, command
#pdb.set_trace()

import time
import numpy as np
#from scipy.optimize import fsolve

def f1(x, mu=0, delta=1):
    return 1/(np.sqrt(2*np.pi)*delta)*np.exp(-((x-mu)**2)/(2*delta**2))

def f2(x):
    return x**2

if __name__ == "__main__":
    print("hello")

    #part 1: plot
    #import matplotlib.pyplot as plt
    #x = np.linspace(-10, 10, 201)
    #plt.subplot(211)
    #plt.plot(x, f1(x))
    #plt.subplot(212)
    #plt.plot(x, f2(x))
    #plt.savefig("a.png")
    #plt.show()

    #part 2
    #from sympy import symbols, solve, latex, pprint
    #a, b, c, x = symbols("a, b, c, x")
    #y = a * x**2 + b * x + c
    #result = solve(y, x)
    #pprint(result)

    #part 3: wraps
    #from functools import wraps
    #def timer(func):
    #    @wraps(func)
    #    def wrapper(*args, **kw):
    #        start = time.perf_counter()
    #        func(*args, **kw)
    #        end = time.perf_counter()
    #        print("time using: {} ms".format(round((end - start) * 1000, 3)))
    #    return wrapper
