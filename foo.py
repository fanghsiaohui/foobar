#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
#print(*(enumerate(range(10))))

import time, sys
def timer(n):
    for i in range(n,0,-1):
        print("{:02d}s".format(i))
        time.sleep(1)
    print("00s")

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except (ValueError, IndexError):
        n = 3
    timer(n)
