#!/usr/bin/python3
"""
Determine the winner of each round of the prime game.
"""


def isWinner(x_rounds, n_values):
    """
    To determine the winner of
    each round of the prime game
    """
    if x_rounds < 1 or not n_values:
        return None

    maria_wins, ben_wins = 0, 0

    max_n = max(n_values)
    primes = [True for _ in range(1, max_n + 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, max_n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x_rounds), n_values):
        primes_count = len(list(filter(lambda prime: prime, primes[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1

    if maria_wins == ben_wins:
        return None

    return 'Maria' if maria_wins > ben_wins else 'Ben'
