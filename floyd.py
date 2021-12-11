import numpy as np
from common import *
from math import sqrt


MAXW = int(1e18)


def read_input():
    with open('floyd.txt') as f:
        nums = lmap(int, f.read().strip().split())
        nums = lmap(lambda x: MAXW if x < 0 else x, nums)

    n = int(sqrt(len(nums)))
    a = np.array(nums).reshape(n, n)
    for i in range(n):
        a[i][i] = 0
    return a



def floyd(a: np.ndarray):
    d = a.copy()
    n = len(a)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d

def print_res(d):
    for row in d:
        for cell in row:
            print('{0: <4}'.format('x' if cell == MAXW else cell), end='')
        print()
    print()




if __name__ == '__main__':
    a = read_input()
    print_res(a)
    d = floyd(a)
    print_res(d)
