def palindrome(number):
    num = str(number)
    while len(num) > 1:
        if num[0] == num[-1]:
            num = num[1:-1]
        else:
            return False
    return True


out = []
for i in range(100, 1000):
    for j in range(i, 1000):
        if palindrome(i * j):
            out.append(i * j)
print(sorted(out)[-1])
