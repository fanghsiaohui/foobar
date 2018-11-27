#!/usr/bin/env python3
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import sys
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,20,0.01)
y=np.sin(x)
plt.figure(figsize=(12,9))
plt.plot(x,y,"r-.")
plt.savefig("pic",dpi=800)
plt.show()
plt.close()
