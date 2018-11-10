#!/usr/bin/env python3
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1,10,100)
y = np.sin(x)
plt.figure()
plt.plot(x, y)
plt.show()
