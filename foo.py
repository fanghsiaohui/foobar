#!/usr/bin/python3
# import pdb, sys, re, time, os, shutil, command
# pdb.set_trace()
# from functools import wraps
# print(*(enumerate(range(10))))

import sys, time, pprint
from math import pi

def main():
    for i in range(11):
        print("{:2d}, {}".format(i, round(pi, i)))

if __name__ == "__main__":
    main()
