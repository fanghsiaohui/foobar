#!/usr/bin/env python3
import scipy.signal as signal
import numpy as np
import pylab as pl

a = np.array([1.0, -1.947463016918843, 0.9555873701383931])
b = np.array([0.9833716591860479, -1.947463016918843, 0.9722157109523452])
t = np.arange(0, 0.5, 1/44100.0)
x = signal.chirp(t, f0 = 10, t1 = 0.5, f1 = 1000.0)
y = signal.lfilter(b, a, x)
x2 = x.reshape((-1,50))
z = np.zeros(max(len(a), len(b)) -1, dtype = np.float)
y2 = []

for tx in x2:
    ty, z = signal.lfilter(b, a, tx, zi=z)
    y2.append(ty)

y2 = np.array(y2)
y2 = y2.reshape((-1,))

y3 = np.sum((y-y2)**2)

print(y3)
pl.plot(t, y, t, y2)
pl.show()
