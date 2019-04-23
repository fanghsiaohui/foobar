#!/usr/bin/env python3
# import pdb, sys, os, time, re, shutil, command
# from functools import wraps
# pdb.set_trace()

import numpy as np
import matplotlib.pyplot as plt

def f1(x, mu=0, delta=1):
    return 1/(np.sqrt(2*np.pi)*delta)*np.exp(-((x-mu)**2)/(2*delta**2))

def f2(x):
    return x**2
x = np.linspace(-10,10,201)
plt.subplot(211)
plt.plot(x, f1(x))
plt.subplot(212)
plt.plot(x, f2(x))
#plt.show()
plt.savefig("a.png")
