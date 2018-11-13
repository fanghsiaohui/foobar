#!/usr/bin/env python3
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1,10,100)
y1 = np.sin(x)
y2 = np.log(x)
y3 = x**2
y4 = x**3
plt.figure()
plt.subplot(221)
plt.plot(x, y1)
plt.subplot(222)
plt.plot(x, y2)
plt.subplot(223)
plt.plot(x, y3)
plt.subplot(224)
plt.plot(x, y4)
plt.show()
