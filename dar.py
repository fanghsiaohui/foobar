#!/usr/bin/env python
from pprint import pprint

a, b = 0, 1
for i in range(10):
    a, b = b, a + b
    print("%3d\t%3d" % (i+1, a))

with open("dar.py") as f:
    text = f.readlines()
text = [i.rstrip() for i in text]
print("\n".join(text))
