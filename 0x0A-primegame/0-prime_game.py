#!/usr/bin/python3
"""Given a set of consecutive integers starting from 1 up to and including n

Maria and Ben are playing a game:
    they take turns choosing a prime number (less than n)
    removing that number and its multiples from the set
    The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """determine who the most winner

    x: is the number of rounds
    nums: is an array of n

    Returns: Name of the winner (Maria or Ben) or None
    """
    mariaWins = x / 2
    for i in range(x):
        mariaWins -= playMaria(nums[i])

    if mariaWins == x / 2:
        return None

    return "Maria" if mariaWins > x / 2 else "Ben"


def playMaria(n):
    """Play a round of the game

    n: positive number
    """
    won = False
    integers = set(range(1, n + 1))
    for prime in primeGenerator(n):
        won = not won
        for i in list(integers):
            if i % prime == 0:
                integers.remove(i)
    return won


def primeGenerator(maxValue):
    primes = set()
    for n in range(2, maxValue):
        for prime in primes:
            if n % prime == 0:
                break
        else:
            primes.add(n)
            yield n
