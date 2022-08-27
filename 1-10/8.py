import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}{os.sep}8.txt", "r") as f:
    string = f.read()

array = [string[index : index + 13] for index in range(len(string) - 12)]
prod_array = [math.prod([int(x) for x in string]) for string in array]
print(sorted(prod_array)[-1])
