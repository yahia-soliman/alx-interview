#!/usr/bin/python3
"""placement of N non-attacking queens on an N×N chessboard."""
import sys


def n_from_argv():
    """Get the value of N from command-line"""
    if len(sys.orig_argv) != 3:
        return 0, "Usage: nqueens N"
    try:
        N = int(sys.orig_argv[2])
    except ValueError:
        return 0, "N must be a number"
    if N < 4:
        return N, "N must be at least 4"
    return N, None


def attacable(place, queenplace):
    """Check if a place is attacable by a queen"""
    xdiff = abs(place[0] - queenplace[0])
    ydiff = abs(place[1] - queenplace[1])
    return xdiff == ydiff or xdiff == 0 or ydiff == 0


def nqueens(N):
    """get every possible solution to place
    N non-attacking queens on an NxN chessboard
    """
    solutions = []
    board = {(i, j) for i in range(N) for j in range(N)}
    for place in board:
        queens = {place}
        for p in board:
            if any([attacable(p, queen) for queen in queens]):
                continue
            queens.add(p)
        if len(queens) == N:
            solutions.append(queens)

    return solutions


if __name__ == "__main__":
    N, err = n_from_argv()
    if err:
        print(err)
        exit(1)
    for solution in nqueens(N):
        print(solution)
