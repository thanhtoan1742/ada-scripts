import numpy as np
from common import *

MAXF = int(1e18)

def read_input():
    with open('matrix_chain.txt') as f:
        lines = f.read().strip().split('\n')

    return lmap(int, lines[0].strip().split())


def best_chain(a):
    n = len(a) - 1
    f = np.zeros((n, n), dtype=int)
    trace = np.zeros((n, n), dtype=int)

    for j in range(n):
        for i in reversed(range(n)):
            f[i][j] = MAXF
            if i == j:
                f[i][j] = 0

            if i >= j:
                continue

            for k in range(i, j):
                t = f[i][k] + f[k + 1][j] + a[i]*a[k + 1]*a[j + 1]
                if t < f[i][j]:
                    f[i][j] = t
                    trace[i][j] = k

    return f, trace



def retrace(trace, l, r):
    if l == r:
        return [], str(l)

    m = trace[l][r]

    lres, ls = retrace(trace, l, m)
    rres, rs = retrace(trace, m + 1, r)

    return [(l, r)] + lres + rres, '(' + ls + rs + ')'


def print_table(table):
    n = len(table)
    for j in reversed(range(n)):
        for i in range(n):
            val = '{0: <4}'.format('.' if i >= j else table[i][j])
            print(val, end='')
        print()
    print()


def print_res(f, trace):
    n = len(f)
    print(f[0][n - 1])
    print_table(f)
    print_table(trace + 1)

    tr, s = retrace(trace, 0, n - 1)
    print(tr)
    print(s)




if __name__ == '__main__':
    a = read_input()
    table, trace = best_chain(a)
    print_res(table, trace)
