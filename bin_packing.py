from common import *


def read_input():
    with open('bin_packing.txt') as f:
        lines = f.read().strip().split('\n')
    m = int(lines[0])
    a = [(int(e), i + 1) for i, e in enumerate(lines[1].split())]
    return m, a



def bin_pack(m, a, policy="first", decreasing=False):
    if decreasing:
        a.sort(key=lambda x: (-x[0], x[1]))

    bins = []
    bin_weights = []
    for weight, idx in a:
        i = -1
        for j in range(len(bins)):
            if bin_weights[j] + weight > m:
                continue

            if policy == "first":
                i = j
                break

            if policy == "best" and (i == -1 or bin_weights[j] + weight > bin_weights[i] + weight):
                i = j

        if i == -1:
            bins.append([])
            bin_weights.append(0)
            i = len(bins) - 1

        bins[i].append(idx)
        bin_weights[i] += weight

    return bins

def print_bins(bins):
    for bin in bins: 
        print(bin)
    print()


if __name__ == '__main__':
    m, a = read_input()
    bins = bin_pack(m, a, policy="first")
    print_bins(bins)
    bins = bin_pack(m, a, policy="best")
    print_bins(bins)
    bins = bin_pack(m, a, policy="first", decreasing=True)
    print_bins(bins)
    bins = bin_pack(m, a, policy="best", decreasing=True)
    print_bins(bins)
