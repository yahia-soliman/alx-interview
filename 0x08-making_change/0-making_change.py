#!/usr/bin/python3
"""Module for figuring out the fewest number of coins
"""


def makeChange(coins, total):
    """fewest number from `coins` to meet the `total` amount
    """
    if total <= 0:
        return 0
    n = 0
    for coin in sorted(coins, reverse=True):
        while coin <= total:
            total -= coin
            n += 1
    return n if total == 0 else -1
