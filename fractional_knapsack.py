import numpy as np
from common import *

def read_input():
    with open('fractional_knapsack.txt') as f:
        lines = f.read().strip().split('\n')

    m = int(lines[0])
    w = [int(e) for e in lines[1].strip().split()]
    v = [int(e) for e in lines[2].strip().split()]

    return m, [(w[i], v[i], i + 1) for i in range(len(w))]


def frac_knapsack(m, a):
    a.sort(reverse=1, key=lambda x: x[1]/x[0])

    chosed = []
    val = 0
    rm = m
    for w, v, i in a:
        t = min(rm, w)
        if t == 0:
            break

        rm -= t
        val += v*t/w
        chosed.append((i, t/w))

    return val, chosed




if __name__ == '__main__':
    m, a = read_input()
    val, chosed = frac_knapsack(m, a)
    print(val)
    print(chosed)


