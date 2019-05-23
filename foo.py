#!/data/data/com.termux/files/usr/bin/env python
a, b = 0, 1
for i in range(30):
    a, b = b, a + b
    print("{:3d}: {:8d}, {:8x}, {:20b}".format(i + 1, a, a, a))
