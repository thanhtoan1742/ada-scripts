import numpy as np
from common import *


dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def read_input():
    with open('knight_tour.txt') as f:
        lines = f.read().strip().split('\n')

    n = int(lines[0])
    nums = lmap(int, ' '.join(lines[1:]).strip().split())
    board = np.array(nums).reshape((n, n))
    return board




def print_board(board):
    for row in board:
        for cell in row:
            print(
                '{0: <4}'.format(cell),
                end=''
            )
        print()
    print()


def try_next_move(board, x, y):
    n = len(board)
    # print(board[x, y])
    # print(x + 1, y + 1, board[x, y])
    # print_board(board)
    if board[x][y] == n*n:
        # print_board(board)
        print('aa')
        return

    for i in range(8):
        u = x + dx[i]
        v = y + dy[i]
        if u < 0 or u >= n or v < 0 or v >= n:
            continue
        if board[u][v] != 0:
            continue

        board[u][v] = board[x][y] + 1
        try_next_move(board, u, v)
        board[u][v] = 0



def resume_tour(board):
    n = len(board)
    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            if board[x][y] < board[i][j]:
                x = i
                y = j

    try_next_move(board, x, y)


if __name__ == '__main__':
    board = read_input()
    resume_tour(board)
