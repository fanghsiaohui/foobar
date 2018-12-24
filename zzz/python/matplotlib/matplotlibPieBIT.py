#!/usr/bin/env python3
import time
import numpy as np
import matplotlib.pyplot as plt

labels = "frogs", "hogs", "dogs", "logs"
sizes = [15, 20, 45, 10]
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct="%.1f%%", shadow=False, startangle=90)
plt.grid(True)
plt.show()
