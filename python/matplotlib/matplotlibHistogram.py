#!/usr/bin/env python3
import time
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
mu, sigma = 100, 20
a = np.random.normal(mu, sigma, size=100)
plt.hist(a, 40, density=1, histtype="stepfilled", facecolor="blue", alpha=0.75)
plt.title("histogram")
plt.show()
