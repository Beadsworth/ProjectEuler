import math


def is_py_trip(a, b):
    c = math.sqrt(a**2 + b**2)
    return c % 1 == 0

upper_limit = 500

for i in range(1, upper_limit):
    for j in range(i, upper_limit):
        if is_py_trip(i, j):
            k = math.sqrt(i**2 + j**2)
            # print(i+j+k)
            if i + j + k == 1000:
                print(int(i*j*k))