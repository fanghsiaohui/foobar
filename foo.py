#!/usr/bin/env python3
# import pdb
# pdb.set_trace()
# import sys, re, time, os, shutil, command
# from functools import wraps
# print(*(enumerate(range(10))))

import os
def printInfo():
    print("play games")
    print("need ability of players")

def getInputs():
    a = eval(input("ability of player A (0-1): "))
    b = eval(input("ability of player B (0-1): "))
    n = eval(input("number"))
    return a, b, n

def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    pass

def gameOver():
    pass

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("summary: {}".format(n))
    print("player A win: {}, {:0.1%}".format(winsA, winsA/n))
    print("player B win: {}, {:0.1%}".format(winsB, winsB/n))

def main():
    printInfo()
    probA, probB, n = getInputs()

if __name__ == "__main__":
    main()

