#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def f1(m=3, n=1000000):
    a = np.random.randn(m, n)
    for i in range(a.shape[0]):
        plt.figure()
        plt.hist(a[i], bins=100)
        plt.xlabel("x label")
        plt.ylabel("y label")
    plt.show()
    print("the end")

if __name__ == "__main__":
    f1()
