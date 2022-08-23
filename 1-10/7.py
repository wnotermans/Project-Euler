from math import sqrt

prime_list = []
num = 2
prime = True
while len(prime_list) != 10001:
    for div in range(2, int(sqrt(num)) + 1):
        prime = True
        if num % div == 0:
            prime = False
            break
    if prime:
        prime_list.append(num)
    num += 1
print(prime_list[-1])
