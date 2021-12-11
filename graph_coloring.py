import numpy as np
from common import *


def read_input():
    with open('graph_coloring.txt') as f:
        lines = f.read().strip().split('\n')

    adj = {}
    for line in lines:
        u, vs = [e.strip() for e in line.split(':')]
        vs = [v.strip() for v in vs.split(' ')]
        adj[u] = sorted(vs)

    return adj



def color_graph(adj, ordering="vertex"):
    us = list(adj.keys())
    if ordering == "vertex":
        us.sort()
    if ordering == "degree":
        us.sort(key=lambda u: (-len(adj[u]), u))

    colors = {}
    for col in range(len(us)):
        for u in us:
            if u in colors:
                continue

            not_ok = len(list(
                filter(
                    lambda v: (v in colors) and (colors[v] == col), 
                    adj[u]
                ))
            )
            if not_ok:
                continue
            colors[u] = col

    return colors



def print_colors(colors):
    print(max([colors[k] for k in colors.keys()]) + 1)
    for u in sorted(list(colors.keys())):
        print(u, colors[u], sep=':')



if __name__ == '__main__':
    adj = read_input()
    colors = color_graph(adj, ordering="degree")
    print_colors(colors)
