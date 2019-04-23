#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from pprint import pprint

A = np.array([[8, 2, 9], 
        [9, 7, 8],
        [4, 6, 6]])
b = np.array([67, 79, 56])
x0 = np.array([2, 3, 5])
Ainv = np.linalg.inv(A)

