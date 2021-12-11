import numpy as np
from common import *

def read_input():
    with open('lcs.txt') as f:
        lines = f.read().strip().split('\n')

    a = [e.strip() for e in lines[0].strip().split(',')]
    b = [e.strip() for e in lines[1].strip().split(',')]
    return a, b


def lcs(a, b):
    n = len(a)
    m = len(b)
    f = np.zeros((n, m), dtype=int)
    trace = np.zeros((n, m, 2), dtype=int)

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                f[i][j] = (0 if i == 0 or j == 0 else f[i - 1][j - 1]) + 1
                trace[i][j] = (i, j)

            if i > 0 and f[i - 1][j] > f[i][j]:
                f[i][j] = f[i - 1][j]
                trace[i][j] = (i - 1, j)

            if j > 0 and f[i][j - 1] > f[i][j]:
                f[i][j] = f[i][j - 1]
                trace[i][j] = (i, j - 1)

    return f, trace


def arrow_print(x, y, val):
    if x == val[0] and y - 1 == val[1]:
        return '← '
    if x - 1 == val[0] and y == val[1]:
        return '↑ '
    return '↖ '


def print_table(table, fmt = None):
    if fmt == None:
        fmt = lambda x, y, val: '{0: <4}'.format(val)

    n = len(table)
    m = len(table[0])
    for i in range(n):
        for j in range(m):
            print(fmt(i, j, table[i][j]), end='')
        print()
    print()



def retrace(trace, a, b):
    x = len(trace) - 1
    y = len(trace[0]) - 1

    res = ''
    while x >= 0 and y >= 0:
        if x == trace[x][y][0] and y == trace[x][y][1]:
            res += a[x]
            x -= 1
            y -= 1
        else:
            x, y = trace[x][y]
    return res[::-1]

def print_res(f, trace, a, b):
    print_table(f)
    print_table(trace, fmt=arrow_print)

    res = retrace(trace, a, b)
    print(res)



if __name__ == '__main__':
    a, b = read_input()
    print(a)
    print(b)

    f, trace = lcs(a, b)
    print(f[len(a) - 1][len(b) - 1])
    print_res(f, trace, a, b)

