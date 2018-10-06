#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
import scipy, sympy
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,10,1000)
y = np.sin(x)
plt.figure()
plt.plot(x, y, label="chinese", color="red")
plt.ylim(-2,2)
plt.ylabel("haha")
plt.legend()
plt.show()

