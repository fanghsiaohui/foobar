#!/usr/bin/env python3
# coding: utf-8
 
import sys, time
import re
# import pdb
# pdb.set_trace()

def deco(func):
    print("before")
    def wrapper(args):
        print("after")
        func(args)
    return wrapper

@deco
def add(args):
    s = sum(args)
    print("sum = {}".format(s))
    return s

x = [1,2,3]
add(x)
