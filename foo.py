#!/usr/bin/python3
# import pdb, sys, re, time, os, shutil, command
# pdb.set_trace()
# from functools import wraps
# print(*(enumerate(range(10))))

import random

def main():
    cnt = 0
    for i in range(1000):
        j = random.randrange(2)
        if j: cnt += 1
        print("{:3d}: nu = {}, cnt = {}, {:.6%}".\
                format(i+1, j, cnt, cnt/(i+1)))
        a = input()
        try:
            if a[0] in ['q', 'Q']: break
        except:
            pass

if __name__ == "__main__":
    main()
