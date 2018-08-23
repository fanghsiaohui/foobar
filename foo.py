#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def fibo(n):
    print("hello, python")
    f = []
    a, b = 0, 1
    while b <= n:
        print(b, end=' ')
        f.append(b)
        a, b = b, a+b
    print()
    return f

y1 = fibo(60)
print("add a number")
y1.append(100)
print(y1)
