#!/usr/bin/python3
"""Calculation of minimum operations in a situation
you have a file containing one letter X
the only operations you can do to this file is "Copy All", "Paste"

given a number `n` what is the minimum number of operations
needed to have `n` X in the file
"""


def minOperations(n):
    """get the minimum number of operations"""
    return sum(primeFactors(n))


def primeFactors(n):
    """Get a list of all prime factors for a number"""
    factors = []
    if n < 2:
        return factors
    for prime in primeGenerator():
        while n % prime == 0:
            n /= prime
            factors.append(prime)
        if n == 1:
            break
    return factors


def primeGenerator():
    """prime numbers generator"""
    n = 2
    primes = []
    while True:
        for prime in primes:
            if n % prime == 0:
                break
        else:
            yield n
            primes.append(n)
        n += 1
