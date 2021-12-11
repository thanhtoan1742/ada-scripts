from copy import deepcopy
import numpy as np
from queue import PriorityQueue
from math import ceil, log2
from common import *

BLANK = '.'


class HTNode:
    def __init__(self, v=BLANK, f=0, l=None, r=None) -> None:
        self.f = f
        self.v = v
        self.l = l
        self.r = r

    def __lt__(self, other):
        return (self.f, self.v) < (other.f, other.v)

    def __str__(self):
        return f'({self.v}:{self.f})'


def make_huffman_tree(freq):
    q = PriorityQueue()
    for v, f in freq:
        q.put(HTNode(v, f))

    while q.qsize() > 1:
        x = q.get()
        y = q.get()
        t = HTNode(BLANK, x.f + y.f, x, y)
        q.put(t)

    return q.get()


def extract_huffman_tree(node, depth=0, code=''):
    res = {}
    if node.v != '' and node.v != BLANK:
        res[node.v] = code

    if node.l:
        t = extract_huffman_tree(node.l, depth + 1, code + '0')
        res.update(t)
    if node.r:
        t = extract_huffman_tree(node.r, depth + 1, code + '1')
        res.update(t)
    return res


def make_huffman_codes(freq):
    tree = make_huffman_tree(freq)
    return extract_huffman_tree(tree)


def make_normal_codes(freq):
    l = ceil(log2(len(freq)))
    codes = {}
    for i, (v, _) in enumerate(freq):
        codes[v] = lbin(i, l)
    return codes


def print_codes(codes):
    for k in codes:
        print(k, codes[k], sep=':')
    print()


def encode_size(freq, codes):
    return sum([len(codes[v])*f for v, f in freq])


def encode(text, codes) -> str:
    return ''.join([codes[ch] if ch in codes else '' for ch in text])


def make_frequency_table(text):
    count = {}
    for ch in text:
        if not ch in count:
            count[ch] = 0
        count[ch] += 1

    return [(k, count[k]) for k in count]



def read_frequency_table():
    with open('huffman_frequency_table.txt') as f:
        lines = f.read().strip().split('\n')

    v = lines[0].strip().split()
    f = lmap(int, lines[1].strip().split())
    return [(v[i], f[i]) for i in range(len(v))]



def read_text():
    with open('huffman_text.txt') as f:
        return f.read().strip()





if __name__ == '__main__':
    freq = read_frequency_table()
    text = read_text()
    huffman_codes = make_huffman_codes(freq)
    normal_codes = make_normal_codes(freq)

    # print_codes(huffman_codes)
    # print_codes(normal_codes)
    # freq = make_frequency_table(text)
    # huffman_codes = make_huffman_codes(freq)
    print(encode(text, huffman_codes))


