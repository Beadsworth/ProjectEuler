import src.EulerHelpers as Euler
import math
import itertools


def get_num_list(num):
    return list(sorted(str(num)))


def find_answer():
    primes = Euler.find_primes(10000)
    pool = [n for n in primes if len(str(n)) == 4]

    # generate prime combinations
    for i, i_num in enumerate(pool[:-2]):
        print(i)
        for j, j_num in enumerate(pool[i + 1:-1]):
            for k, k_num in enumerate(pool[j + i + 2:]):

                # if arithmetic sequence
                if k_num - j_num == j_num - i_num:

                    seq = i_num, j_num, k_num
                    i_list = get_num_list(i_num)
                    j_list = get_num_list(j_num)
                    k_list = get_num_list(k_num)

                    # if all are permutations:
                    if k_list == j_list and j_list == i_list:
                        num_str = ''.join([str(s) for s in seq])

                        # if not given solution, print and break
                        if num_str != '148748178147':
                            return num_str


if __name__ == '__main__':

    answer = find_answer()
    print("answer =", answer)



