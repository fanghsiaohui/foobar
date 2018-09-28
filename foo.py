#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()

# bit songtian

# example 1
# TempStr = input("enter something: ")
# # print(TempStr)
# if TempStr[-1] in ['f', 'F']:
#     C = (eval(TempStr[:-1]) - 32)/1.8
#     print("convert: {:.2f}C".format(C))
# elif TempStr[-1] in ['c', 'C']:
#     F = 1.8*eval(TempStr[:-1]) + 32
#     print("convert: {:.2f}F".format(F))
# else:
#     print("error input")

# example 2
import turtle
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("purple")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.circle(40, 80/2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40 * 2/3)
# # turtle.done()

import time, sys
def f(n):
    starttime = time.time()
    for i in range(n):
        m = (i+1)**2
        if m == n*n:
            print(i+1,m)
    endtime = time.time()
    lasttime = (endtime - starttime)*1000
    print(lasttime)

# n = int(sys.argv[1])
for i in range(8):
    print(i+1)
    n = 10**(i+1)
    f(n)
    print("=========")

