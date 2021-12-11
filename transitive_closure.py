import numpy as np
from common import *
from math import sqrt


def read_input():
    with open('transitive_closure.txt') as f:
        nums = lmap(int, f.read().strip().split())

    n = int(sqrt(len(nums)))
    return np.array(nums).reshape(n, n)

def transitive_closure(a: np.ndarray):
    tc = a.copy()
    n = len(a)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                tc[i][j] |= tc[i][k] and tc[k][j]

    return tc

def print_res(tc):
    print(tc)

    n = len(tc)
    for i in range(n):
        reachable = [str(j) for j in range(n) if tc[i][j]]
        print(f'{i}:', ', '.join(reachable))



if __name__ == '__main__':
    a = read_input()
    tc = transitive_closure(a)
    print_res(tc)
