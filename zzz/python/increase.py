#!/usr/bin/env python3
# import pdb, sys, re, time, os, shutil, command
# pdb.set_trace()
# from functools import wraps
# print(*(enumerate(range(10))))

import random
import matplotlib.pyplot as plt

def games(n, perc, prob):
    out = 1
    for i in range(n):
        if random.random() < prob:
            out *= (1 + perc)
        else:
            out *= (1 - perc)
    return out
 
def main():
    try:
        prob = eval(input("enter prob: "))
        n = eval(input("times: ")) 
    except:
        prob = 0.9
        n = 100
    perc = 0.1
    end = []
    t = 10000
    for i in range(t):
        end.append(games(n, perc, prob))

    plt.subplot(211)
    plt.title("prob = 0.9, after 100 times")
    plt.plot(end)
    plt.subplot(212)
    plt.hist(end, bins = 100)
    plt.show()

if __name__ == "__main__":
    main()
