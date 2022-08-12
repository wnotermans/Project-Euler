def sum_divisors(limit, divisor):
    p = limit // divisor
    return divisor * p * (p + 1) // 2


print(sum_divisors(999, 3) + sum_divisors(999, 5) - sum_divisors(999, 15))
