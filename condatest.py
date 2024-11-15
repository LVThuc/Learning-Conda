# 16/11/2024

import matplotlib.pyplot as plt

def sqr(x):
    return x**2

def double(x):
    return x*2

def doublesquare(x=sqr, y=None):
    return x(double(y))

print(doublesquare(,3))