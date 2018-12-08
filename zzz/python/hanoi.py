#!/usr/bin/env python3
 
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
# print(rvs("hello"))

def f(n):
    if n ==1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n - 2)

count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        count += 1
        print("{:2d} {}: {}->{}".format(count, 1, src, dst))
    else:
        hanoi(n-1, src, mid, dst)
        count += 1
        print("{:2d} {}: {}->{}".format(count, n, src, dst))
        hanoi(n-1, mid, dst, src)

hanoi(6, 'A', 'C', 'B')
