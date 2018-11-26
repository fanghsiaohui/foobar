#!/usr/bin/env python3
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import sys
print("system standard input: ", end="")
sys.stdout.flush()
a=sys.stdin.read()
print("a=", a.strip())
