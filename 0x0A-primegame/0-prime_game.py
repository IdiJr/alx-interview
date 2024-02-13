#!/usr/bin/python3
"""Prime game winner determination"""


def is_prime(num):
    primes = [True] * (num + 1)
    primes[0] = primes[1] = False

    for x in range(2, int(num ** 0.5) + 1):
        if primes[x]:
            for y in range(x ** 2, num + 1, x):
                primes[y] = False
    return primes


def get_primes(n):
    primes = []
    for i, is_prime_flag in enumerate(is_prime(n)):
        if is_prime_flag:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Prime game winner determination"""
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    # generate a list of prime number based on the max numbers in num
    n = max(nums)
    primes = is_prime(n)
    for n in nums:
        # Count the number of prime numbers in the set
        count = sum(primes[2:n + 1])
        # If the count is even, Ben wins, otherwise Maria wins
        ben_wins += count % 2 == 0
        maria_wins += count % 2 == 1

    if maria_wins == ben_wins:
        return None

    return 'Maria' if maria_wins > ben_wins else 'Ben'
