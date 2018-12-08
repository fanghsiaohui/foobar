#!/usr/bin/env python3

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(func.__name__, "time: = {:.3f} ms".format((end - start)*1000))
        return result
    return wrapper

@timethis
def f(arg1, arg2):
    print(arg1, arg2)
    r1 = sum(arg1)
    r2 = arg2**2
    print("test function result: {}, {}".format(r1, r2))
    return r1, r2

if __name__ == "__main__":
    a = [4,5,6]
    b = 8
    f(a, b)
