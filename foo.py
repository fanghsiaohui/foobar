#!/usr/bin/env python
import time

def f0():
    for i in range(10):
        print(i)
        time.sleep(2)
    print(i+1)

from sympy import symbols, latex, solve, pprint
def f1():
    x, Hello, World = symbols("x, Hello, World")
    pprint(latex(solve(x**2 + Hello * x + World, x)))
    pprint(solve(x**2 + Hello * x + World, x))

if __name__ == "__main__":
    f1()
