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


if __name__ == "__main__":
    N, err = n_from_argv()
    if err:
        print(err)
        exit(1)
