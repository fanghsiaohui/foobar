#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os, math
from matplotlib.pyplot import plot, show
from random import random

def pi(n):
    m = 0
    for i in range(n):
        x, y = random(), random()
        if (x*2 - 1)**2 + (y*2 - 1)**2 <=1:
            m += 1
    return 4*m/n #m/n = pi/4

for i in sys.argv[1:]:
    print('pi equals {0:.20f}.'.format(pi(int(i))))
