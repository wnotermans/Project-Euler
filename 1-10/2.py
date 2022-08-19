fib_1, fib_2, _sum = 2, 8, 0
while fib_1 < 4000000:
    _sum += fib_1
    fib_1, fib_2 = fib_2, fib_1 + 4 * fib_2
print(_sum)
