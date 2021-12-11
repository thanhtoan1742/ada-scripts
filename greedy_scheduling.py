import numpy as np
from common import *
from math import sqrt


def read_input():
    with open('greedy_scheduling.txt') as f:
        lines = f.read().strip().split('\n')

    s = [int(e) for e in lines[0].strip().split()]
    f = [int(e) for e in lines[1].strip().split()]

    return [(s[i], f[i], i + 1) for i in range(len(s))]


def schedule(a):
    a.sort(key=lambda x: x[1])
    ff = -1

    res = []
    for s, f, i in a:
        if s >= ff:
            res.append(i)
            ff = f

    return res


if __name__ == '__main__':
    a = read_input()
    res = schedule(a)
    print(res)

