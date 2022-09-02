#!/usr/bin/env python
import numpy as np

# dlt
# 35, 5, 12, 2
# ssq
# 33, 6, 16, 1

def ltr(a):
    m=list(range(1,a[0]+1))
    n1=a[1]
    back=np.arange(1,a[2]+1)
    n2=a[3]
    front=np.random.choice(front,n1)
    back=np.random.choice(back,n2)
    front=sorted(front.tolist())
    back=sorted(back.tolist())
    print(front, end=", ")
    print(back)
    return front, back

dlt=[35, 5, 12, 2]
ssq=[33, 6, 16, 1]
print("DLT:")
for i in range(2):
    ltr(dlt)
print("SSQ:")
for i in range(2):
    ltr(ssq)
