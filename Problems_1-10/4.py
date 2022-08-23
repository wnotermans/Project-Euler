def palindrome(number):
    return str(number)[::-1] == str(number)


_max = 0
i = 999
while i >= 100:
    if i % 11 == 0:
        j = 999
        dj = 1
    else:
        j = 990
        dj = 11
    while j >= i:
        if i * j <= _max:
            break
        if palindrome(i * j):
            _max = i * j
        j -= dj
    i -= 1
print(_max)
