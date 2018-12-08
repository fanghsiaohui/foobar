#!/usr/bin/env python3

def fibo(n):
    f = []
    a, b = 0, 1
    while b <= n:
        f.append(b)
        a, b = b, a+b
    return f

import sys
for i in range(1,len(sys.argv)):
    print(fibo(int(sys.argv[i])))

n = int(input('input a number: \n'))
print(fibo(n))
