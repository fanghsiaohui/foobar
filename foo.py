#!/usr/bin/python3
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import time
import random
import sys
n=100000
try:
    n = int(sys.argv[1])
except:
    print("invalid input")
print("n=%d" % n)
l=['a']*n
startTime = time.perf_counter()
for i in range(len(l)):
    l[i]=chr(ord(l[i]) + random.randint(0,25))
endTime = time.perf_counter()
tm = endTime - startTime
print("time = %.3f milliseconds" % (tm*1000))
print(l[-10:])
print(len(l)/10000)
