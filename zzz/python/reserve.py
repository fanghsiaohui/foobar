#!/usr/bin/env python3
 
x = int(input("enter a number: "))
s = 0
while x != 0:
    s = s*10 + x % 10
    x //= 10
print("reversed: %d" % s)
