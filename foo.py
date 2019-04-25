#!/usr/bin/env python3
# import pdb, sys, os, time, re, shutil, command
# from functools import wraps
# pdb.set_trace()

import numpy as np
from scipy.optimize import fsolve

def f1(x, mu=0, delta=1):
    return 1/(np.sqrt(2*np.pi)*delta)*np.exp(-((x-mu)**2)/(2*delta**2))

def f2(x):
    return x**2

if __name__ == "__main__":
    print("hello")

    '''
    # part 1: plot
    import matplotlib.pyplot as plt
    x = np.linspace(-10,10,201)
    plt.subplot(211)
    plt.plot(x, f1(x))
    plt.subplot(212)
    plt.plot(x, f2(x))
    plt.savefig("a.png")
    plt.show()
    '''

    '''
    # part 2
    from sympy import symbols, solve, latex, pprint
    a, b, c = symbols('a, b, c')
    x, y = symbols('x, y')
    '''

    '''
    # part 3: millon data comoute speed
    import random, time

    random.seed(10)
    t0 = time.perf_counter()
    x1 = [random.randrange(1,101) for i in range(1000000)]
    t1 = time.perf_counter()
    x2 = [i**2 for i in x1]
    t2 = time.perf_counter()
    print("random:")
    print("last 5 item of x1:\n\t{}".format(x1[-5:]))
    print("gen 1 millon random data, time:\n\t{}".format(t1-t0))
    print("last 5 item of x2:\n\t{}".format(x2[-5:]))
    print("compute 1 millon data, time:\n\t{}".format(t2-t1))

    np.random.seed(10)
    m0 = time.perf_counter()
    n1 = np.random.randint(1,101,1000000)
    m1 = time.perf_counter()
    n2 = n1**2
    m2 = time.perf_counter()
    print("\nnumpy.random:")
    print("last 5 item of n1:\n\t{}".format(n1[-5:]))
    print("gen 1 millon random data, time:\n\t{}".format(m1-m0))
    print("last 5 item of n2:\n\t{}".format(n2[-5:]))
    print("compute 1 millon data, time:\n\t{}".format(m2-m1))
    '''
