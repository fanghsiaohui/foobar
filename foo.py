#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()

import time
def f(n):
    l = range(10**n+1)
    start = time.time()
    s = sum(l)
    over = time.time()
    t = over - start
    print(t)
    print(s)
    print(type(t))
    return t

