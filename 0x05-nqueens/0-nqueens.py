#!/usr/bin/python3
"""placement of N non-attacking queens on an N×N chessboard."""
import sys


def n_from_argv():
    """Get the value of N from command-line"""
    if len(sys.argv) != 2:
        return 0, "Usage: nqueens N"
    try:
        N = int(sys.argv[1])
    except ValueError:
        return 0, "N must be a number"
    if N < 4:
        return N, "N must be at least 4"
    return N, None


def attacable(place, queen):
    """Check if a place is attacable by a queen"""
    xdiff = abs(place[0] - queen[0])
    ydiff = abs(place[1] - queen[1])
    return xdiff == ydiff or xdiff == 0 or ydiff == 0


def solve(N, available):
    """Solve the nqueens problem recursively"""
    if N == 0:
        return [[]]
    if len(available) < N:
        return []

    solutions = []

    for queen in available:
        avail = [p for p in available if not attacable(p, queen)]
        result = solve(N - 1, avail)
        for row in result:
            if any([point in sol for point in row for sol in solutions]):
                continue
            row.insert(0, queen)
            solutions.append(row)

    return solutions


def nqueens(N):
    """get every possible solution to place
    N non-attacking queens on an NxN chessboard
    """
    board = [[i, j] for i in range(N) for j in range(N)]
    return solve(N, board)


if __name__ == "__main__":
    N, err = n_from_argv()
    if err:
        print(err)
        exit(1)
    for solution in nqueens(N):
        print(solution)
