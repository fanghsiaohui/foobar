#!/usr/bin/env python3
#import pdb, sys, os, time, re, shutil, command
#pdb.set_trace()

import numpy as np
from scipy.optimize import fsolve
import time
from functools import wraps

def f1(x, mu=0, delta=1):
    return 1/(np.sqrt(2*np.pi)*delta)*np.exp(-((x-mu)**2)/(2*delta**2))

def f2(x):
    return x**2

def timer(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start = time.perf_counter()
        func(*args, **kw)
        end = time.perf_counter()
        print("time using: {} ms".format(round((end - start) * 1000, 3)))
    return wrapper

@timer
def plot_test():
    x = np.linspace(-10, 10, 201)
    plt.subplot(211)
    plt.plot(x, f1(x))
    plt.subplot(212)
    plt.plot(x, f2(x))
    plt.savefig("a.png")

@timer
def solution_test():
    a, b, c, x = symbols("a, b, c, x")
    y = a * x**2 + b * x + c
    result = solve(y, x)
    pprint(result)

@timer
def computer_test():
    random.seed(10)
    timeRandom0 = time.perf_counter()
    xRandom0 = [random.randint(1, 100) for i in range(1000000)]
    timeRandom1 = time.perf_counter()
    xRandom1 = [i**2 for i in xRandom0]
    timeRandom2 = time.perf_counter()
    print("\nrandom:")
    print("last 5 data before:\n\t{}".format(xRandom0[-5:]))
    print("last 5 data after:\n\t{}".format(xRandom1[-5:]))
    print("generate 1 millon random data, time:\n\t{} s".format(round(timeRandom1 - timeRandom0, 6)))
    print("compute 1 millon data, time:\n\t{} s".format(round(timeRandom2 - timeRandom1, 6)))

    np.random.seed(10)
    timeNumpy0 = time.perf_counter()
    xNumpy0 = np.random.randint(1, 101, 1000000)
    timeNumpy1 = time.perf_counter()
    xNumpy1 = xNumpy0 ** 2
    timeNumpy2 = time.perf_counter()
    print("\nnumpy.random:")
    print("last 5 data before:\n\t{}".format(xNumpy0[-5:]))
    print("last 5 data after:\n\t{}".format(xNumpy1[-5:]))
    print("generate 1 millon random data, time:\n\t{} s".format(round(timeNumpy1 - timeNumpy0, 6)))
    print("compute 1 millon data, time:\n\t{} s".format(round(timeNumpy2 - timeNumpy1, 6)))

if __name__ == "__main__":
    print("hello")

    #part 1: plot
    #import matplotlib.pyplot as plt
    #plot_test()
    #plt.show()

    #part 2
    #from sympy import symbols, solve, latex, pprint
    #solution_test()

    #part 3: millon data comoute speed
    #import random
    #computer_test()
