#!/usr/bin/env python3
# import pdb, sys, os, time, re, shutil, command
# from functools import wraps
# pdb.set_trace()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time, random, os, sys
from pprint import pprint

s = """改革春风吹满地
中国人民真争气
这个世界太疯狂
耗子给猫当伴娘"""

def f(x, mu=0, delta=1):
    return 1/(np.sqrt(2*np.pi)*delta)*np.exp(-((x-mu)**2)/(2*delta**2))

x = np.linspace(-10,10,201)
plt.plot(x, f(x))
plt.show()
