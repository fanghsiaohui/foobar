#!/usr/bin/env python3
# coding: utf-8
 
import sys, time, re
# import pdb
# pdb.set_trace()

def deco(func):
    def wrapper(*args, **kw):
        print("wrapper")
        func(*args, **kw)
    return wrapper

@deco
def add(alist, x):
    s = sum(alist)
    print("{}, and {}".format(s, x))
    return s

l = [1,2,3]
add(l, 5)

if __name__ == "__main__":
    print("run as main")
else:
    print("run as module")

