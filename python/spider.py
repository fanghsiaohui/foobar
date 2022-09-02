#!/usr/bin/env python3
import requests, os

savepath = "../Downloads"
url = "http://127.0.0.1"
path = "/pics/bbb/27/001.jpg"
filename = os.path.split(path)[-1]
#kv = {"user-agent":"mozilla/63.0.3"}
#params = {"wd":"julia"}
try:
    #r = requests.get(url, headers = kv, params = params)
    r = requests.get(url+path)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("fail")
with open(os.path.join(savepath, filename), "wb") as f:
    f.write(r.content)
