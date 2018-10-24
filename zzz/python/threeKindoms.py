#!/usr/bin/env python3
# coding: utf-8
 
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import jieba
txt = open("threekingdoms.txt", "r", encoding = "utf-8").read()
words
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
