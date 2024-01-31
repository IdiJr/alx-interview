#!/usr/bin/python3
"""
Coins Changing module
"""


def makeChange(coins, total):
    """Calculate the fewest number of coins
    needed to meet a given total amount.
    Args:
        coins ([list]): A list of coin values available.
        total ([number]): The target amount
    Return: The fewest number of coins needed to reach the total,
    or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, ncoins = (0, 0)
    copy_total = total
    length_coins = len(coins)

    while(i < length_coins and copy_total > 0):
        if (copy_total - coins[i]) >= 0:
            copy_total -= coins[i]
            ncoins += 1
        else:
            i += 1

    check = copy_total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins
