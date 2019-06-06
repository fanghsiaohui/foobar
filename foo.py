#!/usr/bin/env python
import random, pdb, time
import numpy as np

with open("weight") as f:
    text = f.readlines()
text.pop(0)
start = time.time()
text = [[eval(j) for j in i.split()] for i in text]
elapse = time.time() - start
print(elapse, "s")
