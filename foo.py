#!/usr/bin/env python3
# import pdb, sys, os, time, re, shutil, command
# from functools import wraps
# pdb.set_trace()

import time
i = 0
while True:
    print(i, end='')
    print('\a')
    if i < 5:
        time.sleep(1)
        i += 1
    else:
        break
