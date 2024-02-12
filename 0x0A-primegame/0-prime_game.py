#!/usr/bin/python3
"""Prime game winner determination"""


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Prime game winner determination"""
    maria_wins = 0
    ben_wins = 0
    for x in nums:
        primes = get_primes(x)
        # Count the number of prime numbers in the set
        prime_count = len(primes)
        # If the count is even, Ben wins, otherwise Maria wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
