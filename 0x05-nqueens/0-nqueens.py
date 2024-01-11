#!/usr/bin/python3
""" N queens puzzle solving module """
import sys


def is_safe(board, row, col, n):
    # Check if there is a queen in the same row on the left
    for i in range(col):
        if board[i] == row or \
           board[i] == row - (col - i) or \
           board[i] == row + (col - i):
            return False
    return True


def solveNQUtil(board, col, n, solutions):
    if col == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            solveNQUtil(board, col + 1, n, solutions)


def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []

    solveNQUtil(board, 0, n, solutions)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
