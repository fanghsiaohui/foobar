import matplotlib.pyplot as plt
from random import random

def oneturn(x, y, ratio):
    bet = ratio * min(x,y)
    if random() <0.5:
        return x + bet, y - bet
    else:
        return x - bet, y + bet

def stoppingtime(x=1.0, y=1.0, turns=0, ratio=0):
    if x/y +y/x > 100:
        return turns
    x_, y_ = oneturn(x, y, ratio)
    return stoppingtime(x_, y_, turns+1, ratio)

def plot_N(ratio, N=10000):
    results = [0]
    for i in range(N):
        results.append(stoppingtime(ratio=ratio))
    plt.hist(results, bins=30)
    plt.show()
