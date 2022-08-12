from math import sqrt


def prime_sieve(limit):
    """return list of primes < limit"""
    sieve = [True] * (limit // 2)
    for i in range(3, int(sqrt(limit)) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = [False] * ((limit - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, limit // 2) if sieve[i]]


def prime_factorisation(number):
    """returns dictionary in the form {factor_1: exponent,...}"""
    if is_prime(number):
        return {number: 1}
    out = {}
    small_primes = prime_sieve(1000)
    for divisor in small_primes:
        if not number % divisor:
            out[divisor] = 1
            number //= divisor
            while not number % divisor:
                out[divisor] += 1
                number //= divisor
    if number == 1:
        return out

    primes = prime_sieve(min(number // 25, 1000000))

    for index in range(len(primes)):
        if number == 1:
            return out
        while not number % primes[index]:
            if primes[index] in out:
                out[primes[index]] += 1
            else:
                out[primes[index]] = 1
            number //= primes[index]
        else:
            index += 1

    divisor = primes[-1]
    while number != 1:
        if is_prime(number):
            out[number] = 1
            return out
        if not number % divisor:
            if divisor in out:
                out[divisor] += 1
            else:
                out[divisor] = 1
            number //= divisor
        else:
            divisor += 2

    return out


def is_prime(number):
    """return True if number is prime"""
    if number == 2 or number == 3:
        return True
    if not number % 3 or not number % 2 or number == 1:
        return False
    for i in range(5, int(sqrt(number)) + 1, 6):
        if not number % i or not number % (i + 2):
            return False
    return True


def all_prime(prime_list):
    """returns True if all elements of iterable are prime"""
    for number in prime_list:
        if not is_prime(number):
            return False
    return True


def any_prime(prime_list):
    """returns True if any element of iterable is prime"""
    for number in prime_list:
        if is_prime(number):
            return True
    return False
