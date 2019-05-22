#/usr/bin/env python
a, b = 0, 1
for i in range(10000):
    a, b = b, a + b
print(len(str(a)))
