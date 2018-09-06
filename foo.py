#!/usr/bin/env python3
for n in range(2,10):
    k = 0
    for x in range(2,n):
        if n % x == 0:
            print(n, 'euqals', x, '*', n//x)
            k = 1
            break
    if k == 0:
        print(n, 'is a prime number')