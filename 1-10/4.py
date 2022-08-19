def palindrome(number):
    return str(number)[::-1] == str(number)


_max = 0
for i in range(1000, 100, -1):
    for j in range(i, 100, -1):
        if i * j <= _max:
            continue
        if palindrome(i * j):
            _max = i * j
print(_max)
