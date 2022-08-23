def sum_multiples(limit, number):
    p = limit // number
    return number * p * (p + 1) // 2


print(sum_multiples(999, 3) + sum_multiples(999, 5) - sum_multiples(999, 15))
