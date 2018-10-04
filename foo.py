#!/usr/bin/env python3
# coding: utf-8
 
# import sys, time
# import pdb
# pdb.set_trace()

def deco(func):
    print("before")
    def func():
        print("after")
    return func

def add(args):
    s = sum(args)
    print("sum = {}".format(s))
    return s

x = [1,2,3]

@deco
add(x)
