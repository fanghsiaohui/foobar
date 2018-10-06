#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time
import numpy as np
import matplotlib.pyplot as plt

# code below
x = np.linspace(1,10,1000)
y = np.sin(x)
plt.figure()
plt.plot(x, y, label="中文chinese", color="red")
plt.ylim(-2,2)
plt.ylabel("哈哈haha")
plt.legend()
plt.show()
