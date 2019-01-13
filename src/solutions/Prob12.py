import src.EulerHelpers as Euler
import math


def solve():
    n = 0
    while True:
        n += 1
        print(n)  # debug
        tri_number = Euler.find_nth_triangle_num(n)
        tri_factors = Euler.find_factors(tri_number)
        # print(tri_factors)

        if len(tri_factors) >= 500:
            print("answer =", tri_number)
            return


if __name__ == '__main__':

    solve()
