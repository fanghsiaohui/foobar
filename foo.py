#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()

# bit songtian

# example 1
TempStr = input("enter something: ")
# print(TempStr)
if TempStr[-1] in ['f', 'F']:
    C = (eval(TempStr[:-1]) - 32)/1.8
    print("convert: {:.2f}C".format(C))
elif TempStr[-1] in ['c', 'C']:
    F = 1.8*eval(TempStr[:-1]) + 32
    print("convert: {:.2f}F".format(F))
else:
    print("error input")

# example 2
