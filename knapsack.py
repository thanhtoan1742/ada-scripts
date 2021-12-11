import numpy as np
from common import *

def read_input():
    with open('knapsack.txt') as f:
        lines = f.read().strip().split('\n')

    m = int(lines[0])
    w = [int(e) for e in lines[1].strip().split()]
    v = [int(e) for e in lines[2].strip().split()]

    return m, [(w[i], v[i]) for i in range(len(w))]



def bin_knapsack(m ,a):
    f = np.zeros(m + 1, dtype=int)
    trace = np.zeros(m + 1, dtype=int)

    for i, (w, v) in enumerate(a):
        for bw in reversed(range(m + 1)):
            if bw - w < 0:
                break

            if f[bw] < f[bw - w] + v:
                f[bw] = f[bw- w] + v
                trace[bw] = i

    return f, trace


def inf_knapsack(m ,a):
    f = np.zeros(m + 1, dtype=int)
    trace = np.zeros(m + 1, dtype=int)

    for i, (w, v) in enumerate(a):
        for bw in range(m + 1):
            if bw - w < 0:
                continue

            if f[bw] < f[bw - w] + v:
                f[bw] = f[bw- w] + v
                trace[bw] = i

    return f, trace



def print_res(a, f, trace):
    n = len(f)
    for v in f:
        print('{0: <4}'.format(v), end='')
    print()
    for tr in trace:
        print('{0: <4}'.format(tr + 1), end='')
    print()

    w = n - 1
    while w > 0:
        print(f'weight {w}, item {trace[w] + 1}: {a[trace[w]]}')
        w -= a[trace[w]][0]



if __name__ == '__main__':
    m, a = read_input()
    f, trace = inf_knapsack(m, a)
    print_res(a, f, trace)


