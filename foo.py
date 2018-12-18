#!/usr/bin/env python3
# import pdb, sys, re, time, os, shutil, command
# from functools import wraps
# pdb.set_trace()

def f(m):
    m = m
    def g(n):
        return m*n
    return g
