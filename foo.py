#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
import sys, re, time
import numpy as np
# import matplotlib.pyplot as plt

# code below
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]], dtype = np.complex)

r1 = np.arange(0,1,0.1)
r2 = np.linspace(0,1,12)
r3 = np.logspace(0,2,20)

def func(i):
    return i%4+1

r4 = np.fromfunction(func, (10,))
print("{}\n{}\n{}\n{}".format(r1,r2,r3,r4))
0 1
1 2
2 3
3 4
4 1
:wq

