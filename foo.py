#!/usr/bin/env python3
# coding: utf-8
 
import sys, time
import re
# import pdb
# pdb.set_trace()

s = "life is short, i use python"
r = re.findall("life(.*)python", s)
#print(r.group(1))
#print(type(r.group(1)))
print(r)
print(type(r))
