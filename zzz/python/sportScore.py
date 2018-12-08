#!/usr/bin/env python3

from random import random

def printInfo():
    print("play games")
    print("need ability of players")

def getInputs():
    a = eval(input("ability of player A (0-1): "))
    b = eval(input("ability of player B (0-1): "))
    n = eval(input("number: "))
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
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    return a==15 or b==15

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("summary: {}".format(n))
    print("player A win: {}, {:0.1%}".format(winsA, winsA/n))
    print("player B win: {}, {:0.1%}".format(winsB, winsB/n))

def main():
    printInfo()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

if __name__ == "__main__":
    main()

