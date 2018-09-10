#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import sys, os, math
from random import random
from matplotlib.pyplot import plot, show
def pi(n):
    m = 0
    for i in range(n):
        x, y = random(), random()
        if (x*2 - 1)**2 + (y*2 - 1)**2 <=1:
            m += 1
    return 4*m/n

# m/n = pi/4
