#!/usr/bin/env python
import os, sys, time
import numpy as np
import matplotlib.pyplot as plt

def f0(m=8):
    x = np.linspace(-m, m, 101)
    y = np.cos(x)
    y2 = np.tan(x)
    plt.subplot(211)
    plt.plot(x, y)
    plt.subplot(212)
    plt.plot(x, y2)
    plt.savefig(f"{m}.png")
    return m

if __name__ == "__main__":
    t = time.perf_counter()
    f0(10)
    print(time.perf_counter() - t)
