#!/usr/bin/env python3
# import pdb, sys, re, time, os, shutil, command
# from functools import wraps
# pdb.set_trace()

from scipy import *
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# sin(x) + y**2 + exp(z) = 1
# log(x) + y*4 + z =1
# tan(x) + log(y) + z = 1

def f(m):
    x, y, z = m
    return [
            sin(x) + y**2 + exp(z),
            log(x) + y*4 + z,
            tan(x) + log(y) + z]

def main():
    m = [0.0, 0.0, 0.0]
    b = [1, 1, 1]
    s = fsolve(f, b)
    print(s)
    print(f(s))

if __name__ == "__main__":
    main()
