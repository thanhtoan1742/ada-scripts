from common import *


def read_input():
    with open('ltp_scheduling.txt') as f:
        lines = f.read().strip().split('\n')
    m = int(lines[0])
    a = [(int(e), i + 1) for i, e in enumerate(lines[1].split())]
    return m, a


def ltp_schedule(m, a):
    a.sort(reverse=True)
    procs = [[] for _ in range(m)]

    for i, (u, idx) in enumerate(a):
        u = 0
        for v in range(1, m):
            tu = sum(map(lambda x: a[x][0], procs[u]))
            tv = sum(map(lambda x: a[x][0], procs[v]))
            if tv < tu:
                u = v

        procs[u].append(i)

    return procs


def print_procs(a, procs):
    end = 0
    for proc in procs:
        for i in proc:
            print(
                '{0: <3}'.format(a[i][1])*a[i][0],
                end=''
            )
        t = sum(map(lambda x: a[x][0], proc))
        end = max(end, t)
        print()
    print(end)



if __name__ == '__main__':
    m, a = read_input()
    procs = ltp_schedule(m, a)
    print_procs(a, procs)


