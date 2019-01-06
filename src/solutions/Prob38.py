import src.EulerHelpers as Euler
import math
import itertools


def get_concat_products():

    good_products = []

    # for each n
    for n in range(2, 9 + 1):
        seq = [x for x in range(1, n + 1)]

        # for each integer
        i = 0
        result_len = 0
        while result_len <= 9:
            i += 1

            products = [i * s for s in seq]
            result = ''.join([str(product) for product in products])
            result_len = len(result)
            if result_len == 9 and len(set(result)) == 9 and '0' not in result:
                print(i, seq, result)
                good_products.append(int(result))

    return good_products


if __name__ == '__main__':

    results = get_concat_products()
    print("answer = ", sorted(results, reverse=True)[0])
