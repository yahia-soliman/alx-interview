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


def nqueens(N):
    """Get every possible solution to place
    N non-attacking queens on an NxN chessboard
    """
    cols = []
    neg_diag = set()
    pos_diag = set()
    solutions = []

    def place_queen(row=0):
        """Place queens recursively on an NxN chessboard"""
        if row == N:
            # There are already N queens placed (a solution)
            return solutions.append(cols.copy())
        for col in range(N):
            add = row + col
            sub = row - col
            # if not under attack by any placed queen
            if not (col in cols or add in pos_diag or sub in neg_diag):
                # place it in this [row, col]
                cols.append(col)
                pos_diag.add(add)
                neg_diag.add(sub)
                # place another one in next row
                place_queen(row + 1)
                # take the queen off-board to use it in the next valid column
                cols.pop()
                pos_diag.remove(add)
                neg_diag.remove(sub)

    place_queen()
    return solutions


if __name__ == "__main__":
    N, err = n_from_argv()
    if err:
        print(err)
        exit(1)
    for sol in nqueens(N):
        print([[x, y] for x, y in enumerate(sol)])
