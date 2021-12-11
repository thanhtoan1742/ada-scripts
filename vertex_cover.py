def read_input():
    with open('vertex_cover.txt') as f:
        lines = f.read().strip().split('\n')

    adj = {}
    for line in lines:
        u, vs = [e.strip() for e in line.split(':')]
        adj[u] = [e.strip() for e in vs.split()]
    return adj


def approx_vertex_cover(adj):
    e = {(u, v) for u in adj for v in adj[u]}
    cover = set()
    while len(e):
        u, v = e.pop()
        t = {(x, y) for x, y in e if x == u or x == v or y == u or y == v}
        e.difference_update(t)
        print(u, v)
        print(e)
        print(t)
        print()
        cover.add(u)
        cover.add(v)

    return cover


if __name__ == '__main__':
    adj = read_input()
    approx_cover = approx_vertex_cover(adj)
    print(sorted(list(approx_cover)))

