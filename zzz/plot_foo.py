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

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(1,11,11)
plt.figure()
plt.plot(y1)

y2 = np.random.random(11)
plt.scatter(x,y2,color="red")
plt.show()
