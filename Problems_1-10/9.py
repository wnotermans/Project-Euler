from math import sqrt


for a in range(1, 500):
    for b in range(a, 1000 - a):
        c = sqrt(a**2 + b**2)
        if not c % 1 and a + b + c == 1000:
            print(int(a * b * c))
            exit()
