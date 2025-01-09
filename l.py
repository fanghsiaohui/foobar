#!/usr/bin/env python
import sys
import random
import numpy as np

mD = (35, 5, 12, 2)
mS = (33, 6, 16, 1)
m0 = (10, 3, 5, 2)

def roll_r(m):
    front = random.sample(range(1, m[0]+1), m[1])
    back = random.sample(range(1, m[2]+1), m[3])
    return (sorted(front), sorted(back))

def roll_n(m):
    front = np.random.choice(range(1, m[0]+1), m[1], replace=False)
    front.sort()
    back = np.random.choice(range(1, m[2]+1), m[3], replace=False)
    back.sort()
    return (front, back)

if __name__ == "__main__":
    try:
        i = sys.argv[1]
        m = mD if i.startswith("d") else mS if i.startswith("s") else m0
    except:
        m = m0
    print("No.1:\t", roll_r(m)[0], "\t", roll_r(m)[1])
    print("No.2:\t", roll_n(m)[0], "\t", roll_n(m)[1])
