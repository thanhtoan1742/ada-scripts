import numpy as np
from math import sqrt
from queue import PriorityQueue
from common import *

MAX_COST = int(1e18)

def read_input():
    with open('TSP.txt') as f:
        nums = lmap(int, f.read().split())

    n = int(sqrt(len(nums)))
    return np.array(nums).reshape((n, n))




def tsp(a, start=0):
    prunned = 0
    tsp_cycles = []
    best = MAX_COST

    def tsp_rec(a, u, path, cost):
        nonlocal prunned
        nonlocal tsp_cycles
        nonlocal best
        # print(path)

        n = len(a)
        if len(path) == n:
            w = a[path[-1]][path[0]]
            if w == 0:
                return

            path.append(path[0])
            # print(cost + w, path, sep=': ')
            if best == cost + w:
                tsp_cycles.append(path)
            elif best > cost + w:
                best = cost + w
                tsp_cycles = [path]
            return

        for v in range(n):
            if a[u][v] != 0 and (not v in path):
                if cost + a[u][v] >= best:
                    # print(path, v, 'x')
                    prunned += 1
                    continue

                tsp_rec(a, v, path + [v], cost + a[u][v])

    tsp_rec(a, start, [start], 0)
    return tsp_cycles



def cost(a, cycle):
    n = len(cycle) - 1
    res = 0
    for i in range(n):
        res += a[cycle[i]][cycle[i + 1]]
    return res



def prim(a, root=0):
    n = len(a)
    included = [0 for i in range(n)]
    par = [-1 for i in range(n)]
    key = [MAX_COST for i in range(n)]
    key[root] = 0
    q = PriorityQueue()
    for u in range(n):
        q.put((key[u], u))

    while not q.empty():
        k, u = q.get()
        if k != key[u]:
            continue

        included[u] = 1
        for v in range(n):
            if not included[v] and a[u][v] != 0 and a[u][v] < key[v]:
                key[v] = a[u][v]
                par[v] = u
                q.put((key[v], v))

    return par



def visit_tree(u, children, path):
    path.append(u)

    for v in children[u]:
        visit_tree(v, children, path)



def tsp_from_par(par):
    n = len(par)
    children = {i:[] for i in range(n)}
    root = 0
    for v in range(n):
        if par[v] >= 0:
            children[par[v]].append(v)
        else:
            root = v

    path = []
    visit_tree(root, children, path)
    return path


def approx_tsp(a):
    par = prim(a)
    cycle = tsp_from_par(par)
    return cycle + [cycle[0]]


if __name__ == '__main__':
    a = read_input()
    tsp_cycles = tsp(a)
    for cycle in tsp_cycles:
        print(cycle)
    print(cost(a, tsp_cycles[0]))

    approx_cycle = approx_tsp(a)
    print(approx_cycle)
    print(cost(a, approx_cycle))
