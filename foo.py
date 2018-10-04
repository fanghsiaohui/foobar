#!/usr/bin/env python3
# coding: utf-8
 
import sys, time
import re
# import pdb
# pdb.set_trace()

def deco(func):
    print("before")
    def wrapper(*args, **kw):
        print("after")
        func(*args, **kw)
    return wrapper

@deco
def add(alist, x):
    s = sum(alist)
    print("sum = {}, and 2nd = {}".format(s, x))
    return s

l = [1,2,3]
add(l, 5)

if __name__ == "__main__":
    print("run as main")
else:
    print("run as module")

