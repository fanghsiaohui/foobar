#!/usr/bin/env python3
import time
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0., 5., 0.02)
plt.plot(a, np.cos(2*np.pi*a), "r--")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("$y=cos(2\pi x)$")
plt.text(2,1,"$\mu = 100$")
plt.annotate(r"$\mu=100$", xy=(0.5,-1), xytext=(2,-1.5), arrowprops=dict(facecolor="blue", shrink=0.1, width=2))
plt.savefig("test", dpi=600)
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show()
