#!/usr/bin/env python
import time, sys, random

def test(r=0.2):
    rdm = random.random()
    flag = 1 if rdm < r else 0
    return flag

def timer(m):
    flag = 0
    while m > 0:
        print(m)
        time.sleep(1)
        if test():
            print("\tABORT")
            break
        m -= 1
    else:
        print(f"{m}\n\tFIRE")
        flag = 1
    return flag

if __name__ == "__main__":
    try:
        m = int(sys.argv[1])
    except:
        m = 3

    timer(m)
