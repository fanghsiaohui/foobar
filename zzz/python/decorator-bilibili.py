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
