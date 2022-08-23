from math import sqrt

prime_list = [2]
num = 3
prime = True
while len(prime_list) != 10001:
    for div in range(3, int(sqrt(num)) + 1, 2):
        prime = True
        if num % div == 0:
            prime = False
            break
    if prime:
        prime_list.append(num)
    num += 2
print(prime_list[-1])
