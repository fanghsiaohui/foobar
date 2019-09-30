#!/usr/bin/env python

import time, random
import pdb
def pi(n):
    m = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1:
            m += 1
    return m/n*4

n = 100
for i in range(3):
    pdb.set_trace()
    n *= 10
    start = time.time()
    p = pi(n)
    end = time.time()
    print("%.2e, %.8f, %.6f" % (n, p, end-start))
