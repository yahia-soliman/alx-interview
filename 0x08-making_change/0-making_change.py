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
        divisible = total // coin
        if divisible:
            n += divisible
            total %= coin
    return n if total == 0 else -1
