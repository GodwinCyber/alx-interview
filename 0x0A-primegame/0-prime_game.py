#!/usr/bin/python3
"""Module Interview"""


def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up to n
        using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """Determine who the winner is after x rounds."""
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    for n in nums:
        # Game simulation for a single round
        primes_set = set(primes)
        primes_set = {p for p in primes_set if p <= n}
        current_player = "Maria"

        while primes_set:
            # Maria always picks the smallest prime
            prime_to_remove = min(primes_set)
            multiples = set(range(prime_to_remove, n + 1, prime_to_remove))
            primes_set -= multiples  # Remove prime and all its multiples

            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"

        if current_player == "Maria":
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
