from common import *


def read_input():
    with open('set_cover.txt') as f:
        lines = f.read().strip().split('\n')
    X = set(split_strip(lines[0], ','))
    F = lmap(lambda line: set(split_strip(line, ',')), lines[1:])
    return X, F


def greedy(X, F):
    cover = []
    U = X
    while True:
        old_size = len(U)

        best = 0
        for i in range(1, len(F)):
            if len(U.intersection(F[i])) > len(U.intersection(F[best])):
                best = i
        U.difference_update(F[best])

        if len(U) == old_size:
            break

        cover.append(best)

    return cover


if __name__ == '__main__':
    X, F = read_input()
    greedy_cover = greedy(X, F)
    print(greedy_cover)
