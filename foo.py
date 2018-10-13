#!/usr/bin/env python3
# coding: utf-8

"makeTextFile.py -- create text file"
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
import os
ls = os.linesep

# get filename
while True:
    fname = input("enter filename:\n")
    if os.path.exists(fname):
        print("Erroe: {} already exists.".format(fname))
    else:
        break

# get file content (text) lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

# loop until user terminates input
while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(["{}{}".format(x, ls) for x in all])
fobj.close()
print("DONE")

