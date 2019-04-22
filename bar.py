#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

a = np.arange(1,10).reshape(3,3)
pprint(a)
plt.plot(range(3), a)
plt.show()
