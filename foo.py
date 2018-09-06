#!/usr/bin/env python3
'''
for n in range(2,10):
    k = 0
    for x in range(2,n):
        if n % x == 0:
            print(n, 'euqals', x, '*', n//x)
            k = 1
            break
    if k == 0:
        print(n, 'is a prime number')
def fib(n):
    a, b = 0,1 
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
'''
def f(a, L=[]):
    if L == []:
        L = []
    L.append(a)
    return L

