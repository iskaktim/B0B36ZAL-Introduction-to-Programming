import math

def newtonPi(init: float)->float:
    x = init
    while True:
        x_new = x - math.sin(x) / math.cos(x) 
        if x_new == x:
            return x
        x = x_new 


def leibnizPi(iterations: int)->float:
    pi = 0
    for i in range(iterations):
        pi += ((-1) ** i) * (4/(i*2+1)) 
    return float(pi)


def nilakanthaPi(iterations:int)->float:
    pi = 3
    for i in range(iterations - 1):
        x = i * 2 + 2
        pi += ((-1) ** i) * (4 / (x * (x + 1) * (x + 2)))
    return pi