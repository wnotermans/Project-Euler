fib_1, fib_2, _sum = 1, 1, 0
while fib_1 < 4000000:
    if fib_1 % 2 == 0:
        _sum += fib_1
    fib_1, fib_2 = fib_1 + fib_2, fib_1
print(_sum)
