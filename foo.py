#!/data/data/com.termux/files/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 10, 101)
b = np.cos(a)
c = np.sin(a)

plt.grid(True)
plt.plot(a, b, a, c)
plt.legend(["cosine", "sine"])
plt.savefig("tri", dpi=1200)
