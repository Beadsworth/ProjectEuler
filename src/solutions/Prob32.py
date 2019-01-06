import src.EulerHelpers as Euler
import math
import itertools


def get_pan_digital_products(k):

    solutions = []

    # digits to select for pan_digital numbers
    digit_pool = [i for i in range(1, k + 1)]

    # iterate over first partition position
    # for first factor of length 1 to one third of k
    for i in range(1, k//3 + 1):

        a_len = i
        # find all permutations of first number
        for a_perm in itertools.permutations(digit_pool, a_len):

            # reduce the pool of digits available
            reduced_pool = [digit for digit in digit_pool if digit not in a_perm]

            # iterate over second partition position
            # 2nd partition must come after first
            for j in range(i + 1, (k - 1) + 1):
                b_len = j - i
                c_len = k - a_len - b_len

                # if factor lengths are our of order, continue to next 2nd partition position iteration
                if not a_len <= b_len <= c_len:
                    continue

                # find all permutations of second factor
                for b_perm in itertools.permutations(reduced_pool, b_len):

                    # reduce pool once again
                    final_pool = [digit for digit in reduced_pool if digit not in b_perm]

                    # find all permutations of the product
                    for c_perm in itertools.permutations(final_pool, c_len):

                        # calculate a, b, c
                        a = Euler.list_2_num(a_perm)
                        b = Euler.list_2_num(b_perm)
                        c = Euler.list_2_num(c_perm)

                        # print progress
                        # print([a_perm] + [b_perm] + [c_perm])

                        # if a match is found, add it to solution list (if unique)
                        if a * b == c:
                            solutions.append((a, b, c))

    return solutions


if __name__ == '__main__':

    solutions = get_pan_digital_products(9)

    unique_products = set()
    for solution in solutions:
        a, b, c, = solution
        unique_products.add(c)
        print("{a} * {b} = {c}".format(a=a, b=b, c=c))

    print("answer = ", sum(unique_products))
