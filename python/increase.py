#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt

def traes(n=100, prob=0.8, perc=0.1):
    fund = [1]
    for i in range(n):
        if random.random() < prob:
            fund.append(fund[i] * (1 + perc))
        else:
            fund.append(fund[i] * (1 - perc))
    return fund
 
def more(m = 1000, n=100, prob=0.8, perc=0.1):
    endOutput = []
    for i in range(m):
        endOutput.append(traes(n, prob, perc))
    return endOutput

def plot(endOutput, m=1000, n=100, prob=0.8, perc=0.1):
    plt.subplot(211)
    plt.title("fund-times")
    plt.plot(endOutput)
    plt.subplot(212)
    plt.hist(endOutput, bins=100)
    plt.grid()
    plt.show()

def getInput():
    try:
        prob = eval(input("enter prob (default 0.8): "))
    except:
        prob = 0.8
    try:
        n = eval(input("trade times (default 100): ")) 
    except:
        n = 100
    try:
        perc = eval(input("partial (default 0.1): ")) 
    except:
        perc = 0.1 
    try:
        m = eval(input("moni times (default 1000): ")) 
    except:
        m = 1000
    return n, prob, perc, m

def main():
    n, prob, perc, m = getInput()
    endMore = more(m, n, prob, perc)
    end = [i[-1] for i in endMore]
    plot(end)

if __name__ == "__main__":
    main()
