import src.EulerHelpers as Euler
import math
import itertools


if __name__ == '__main__':

    pool = list(range(10))

    count = 0
    for x in itertools.permutations(pool, 10):
        print(count)
        # print(x)
        count += 1

        if count >= 1000000:
            print(Euler.list_2_num(x))
            break
