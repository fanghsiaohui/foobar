#!/usr/bin/env python3
import time, sys

def timer2():
    i = 0
    while True:
        print("{:02d}s".format(i))
        time.sleep(1)
        i += 1
if __name__ == "__main__":
    timer2()
