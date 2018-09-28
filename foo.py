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

# something
x = int(input("enter a number: "))
s = 0
while x != 0:
    s = s*10 + x % 10
    x //= 10
print("reversed: %d" % s)
