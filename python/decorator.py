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
#!/usr/bin/env python3
import time

def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def f1(func_name):
    print("this is a function named " + func_name)

@decorator
def f2(func_name1, func_name2):
    print("this is a function named " + func_name1)
    print("this is a function named " + func_name2)

@decorator
def f3(func_name1, func_name2, **kw):
    print("this is a function named " + func_name1)
    print("this is a function named " + func_name2)
    print(kw)

f1("test func")
f2("test func1", "test func2")
f3("test func1", "test_func2", a=1, b=2, c="1.2.3")
