#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
def cheeseshop(kind, *arguments, **keywords):
    print("-- do you have any", kind, "?")
    print("-- i'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
'''

'''
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- this parrot would't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- lovely plumage, the", type)
    print("-- it's:", state, "!")
'''

'''
def ask_ok(prompt, retries=4, complaint='Yes or no, plesae!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooprative user')
        print(complaint)
'''

'''
for n in range(2,10):
    k = 0
    for x in range(2,n):
        if n % x == 0:
            print(n, 'euqals', x, '*', n//x)
            k = 1
            break
    if k == 0:
        print(n, 'is a prime number')
def fib(n):
    a, b = 0,1 
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
'''
'''
def f(a, L=[]):
    if L == []:
        L = []
    L.append(a)
    return L
'''
