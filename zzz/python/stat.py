#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

def getNum():
    nums = []
    iNumStr = input("enter number: ")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("enter number: ")
    return nums

def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers) - 1), 0.5)

def median(numbers):
    numbers2 = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers2[size//2 - 1] + numbers2[size//2]) / 2
    else:
        med = (numbers2[size//2])
    return med

n = getNum()
m = mean(n)
d = dev(n, m)
med = median(n)
print("mean = {}, dev = {:.2f}, med = {}.".format(m, d, med))
