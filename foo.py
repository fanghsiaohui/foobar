#!/data/data/com.termux/files/usr/bin/env python
def f():
    a, b = 0, 1
    c, d = "hello", "world"
    return a, b, c, d

*t, a, b = f()
print(t)
print(a, b)
print(hex(id(a)), hex(id(b)))
