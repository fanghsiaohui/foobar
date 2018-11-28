#!/usr/bin/env python3
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import requests, bs4, scrapy
from bs4 import BeautifulSoup

url = "http://127.0.0.1"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
