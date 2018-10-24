#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in """!"#$%&()*+,-./:;<=>?@[\\]^_{|}`~'""":
        txt = txt.replace(ch, " ")
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    count[word] = counts.get(word, 0) + 1
items = list(count.items())
items.sort(key = lambda x:x[1], reverse = True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
