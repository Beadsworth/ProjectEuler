import src.EulerHelpers as Euler
import math
import itertools


def sequence_product(sequence):

    product = 1
    for n in sequence:
        product = product * n

    return product


def is_product_sum_sequence(sequence):
    # sequence can have repetitions
    seq_sum = sum(sequence)
    seq_prod = sequence_product(sequence)

    return seq_sum == seq_prod


def mps_lower_limit(k):
    """for a given k, return lower limit minimum-product-sum (mps)"""
    return int(math.ceil(k**(k/(k-1))))


def guaranteed_solution_seq(k):
    """guaranteed solution for a given k"""
    return [1 for i in range(k - 2)] + [2] + [k]


def mps_upper_limit(k):
    """for a given k, return upper limit minimum-product-sum (mps)"""
    # return sum(guaranteed_solution_seq(k))
    return 2 * k


def gen_valid_seq(k):

    for x in itertools.combinations_with_replacement(range(1, k + 1), k):
        # guaranteed volume solution
        # to proceed any further means to increase the volume
        # but a solution has already been found with x[-2] = 2
        # so an optimal solution must have already occurred before this point

        # if x[-2] > 2:
        #     break

        yield x


def gen_product_sum_seqs(k):

    for seq in gen_valid_seq(k):
        if is_product_sum_sequence(seq):
            yield seq


def indicies_of_last_occurance(sequence):

    indicies = []
    last_index = len(sequence) - 1
    for i, number in enumerate(sequence):
        if i == last_index:
            continue
        elif sequence[i] != sequence[i + 1] and sequence[i] != 0:
            indicies.append(i)

    indicies = indicies + [last_index]
    return indicies


def coef_level(i, sequence, results):

    indicies = indicies_of_last_occurance(sequence)
    print(len(indicies))

    if i >= len(sequence) - 2:
        # stop
        return

    else:
        for index in indicies:
            new_seq = sequence.copy()
            new_seq[i] -= 1
            new_seq[index] += 1
            results.append(new_seq)
            coef_level(i + 1, new_seq, results)


def coef_level_wrapper(level):
    initial = [1 for i in range(level)]
    results = [initial, ]

    coef_level(i=0, sequence=initial, results=results)

    # unique lists only
    number_strings = [''.join(str(x) for x in seq) for seq in results]
    unique_number_strings = set(number_strings)
    seqs = [[int(c) for c in number_string] for number_string in unique_number_strings]
    return seqs


def k_coefs_helper(k):
    max_mps = mps_upper_limit(k)
    initial_mps = k + 2
    levels = max_mps - initial_mps + 1

    coef_seqs = []
    for level in range(2, levels + 2):
        print("level: ", level)
        prepend = [0 for i in range(levels - level + 1)]
        level_results = [prepend + coefs for coefs in coef_level_wrapper(level)]
        for level_result in level_results:
            coef_seqs.append(level_result)

    return coef_seqs


def k_coefs(k):

    k_coefs = k_coefs_helper(k)

    for seq in k_coefs:
        for i, coef in enumerate(seq):
            seq[i] += 1

    # sorteded_k_coefs = sorted(k_coefs, key=lambda x: Euler.list_2_num(x))
    return k_coefs


def get_min_mps(k):

    # each term must be between 1 and K
    # i -> index
    mps_min = mps_lower_limit(k)
    mps_max = mps_upper_limit(k)

    for seq in gen_valid_seq(k):
        if mps_min < sum(seq) < mps_max:
            pass


def n_count_max(k, n):
    """
    return max number of occurrences of n in the sequence for k.
    note: r is known to be at most 2 * k.  If all numbers in sequence are n, then r = n ** k
    therefor, n ** k <= 2 * k
    """
    return int(math.floor(math.log(2 * k, n)))


def k_pool(k):
    """
    find pool of number that can be in k's sequence.
    note: only numbers less than k can occur, and each number has a max # of occurences.
    """

    pool = [1 for i in range(k-2)]
    for n in range(2, k + 1):
        pool_add = [n for i in range(n_count_max(k, n))]
        pool = pool + pool_add

    return sorted(pool)


def r_pool(k, r):

    r_factors = Euler.find_factors(r)
    pool = [n for n in k_pool(k) if n in r_factors]
    return pool


def k_pool_count_dict(k):

    dict = {}
    pool = k_pool(k)
    for n in range(1, k + 1):
        n_count = sum(1 for i in pool if i == n)
        dict[n] = n_count

    return dict


def k_temp_wrapper(k):

    result = []
    pool_count_dict = k_pool_count_dict(k)
    k_temp(k, 0, pool_count_dict, result)
    return result


def k_temp(k, level, pool_count_dict, result):

    for n in range(1, k + 1):

        if level >= k:
            result.append(pool_count_dict)
            return

        else:
            new_dict = pool_count_dict.copy()
            new_dict[n] -= 1

            if new_dict[n] < 0:
                # skip iteration
                continue

            else:
                k_temp(k, level + 1, new_dict, result)


def parts_algo(n, m):

        if not n >= m >= 2:
            raise RuntimeError("must have n >= m >= 2")

        # H1
        # add initial zero so a can follow math convention
        a = [0] + [n - m + 1] + [1 for i in range(m - 1)] + [-1]

        while True:
            # H2
            yield a[1:-1]

            while a[2] < a[1] - 1:
                # H3
                a[1] -= 1
                a[2] += 1
                yield a[1:-1]

            # H4
            j = 3
            s = a[1] + a[2] - 1

            while a[j] >= a[1] - 1:
                s = s + a[j]
                j += 1

            # H5
            if j > m:
                # you are done
                return

            x = a[j] + 1
            a[j] = x
            j = j - 1

            # H6
            while j > 1:
                a[j] = x
                s = s - x
                j = j - 1

            a[1] = s


def k_check(k):

    # r cannot be prime
    non_primes = [r for r in range(k, 2 * k + 1) if not Euler.is_prime(r)]

    for r in non_primes:
        # print(r)

        gen = parts_algo(r, k)
        for sequence in gen:
            # print(sequence)
            if sequence_product(sequence) > 2 * k:
                break
            # print(sequence)
            if is_product_sum_sequence(sequence):
                return r


def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n+1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def r_combos(r):
    """from prime factorization"""
    pool = Euler.get_prime_factorization_pool(r)

    combos = []
    for n, p in enumerate(partition(pool), 1):
        digits = sorted((sequence_product(c) for c in p))
        # print(n, digits)
        if digits not in combos:
            combos.append(digits)

    return combos


def find_r_for_k(k, r_combo_dict):

    # test all r
    for r in range(k, 2 * k + 1):

        # for factorization in r_combos(r):
        for factorization in r_combo_dict[r]:
            if len(factorization) > k:
                continue
            else:
                missing = k - len(factorization)
                fixed = [1 for i in range(missing)] + factorization

                if is_product_sum_sequence(fixed):
                    return r


def check_non_unique_n(n):

    for t in range(1, 2 * r + 1):
        pass


# def k_temp_2(k):
#
#     initial = [1 for i in range(k)]
#
#     # start at end
#     for index in reversed(range(k)):
#         n_max =
#         for i in range(1, k + 1):
#             initial[-1] = i
#                 if exceeded, change index:
#                     # break out to change index
#                     break


if __name__ == '__main__':
    # test_seq = [1, 1, 1, 1, 2, 6]
    # print("{seq}: {tf}".format(seq=test_seq, tf=is_product_sum_sequence(test_seq)))

    # for k in range(12000, 12000 + 1):
    #     seq = [1 for i in range(k - 2)] + [2] + [k]
    #     tf = is_product_sum_sequence(seq)
    #
    #     print("k: {k}, is solution: {tf}, seq: {seq}".format(k=k, tf=tf, seq=seq))

    # k_temp(100)
    # for k in range(10):
    #     print(str(k) + ": ", len(k_pool(k)))

    # for i in range(10000, 12000):
        # print(i)


    # pool = Euler.get_prime_factorization_pool(12000)
    # print(pool)
    # # what you are taking out of n
    # for combo in itertools.combinations(pool, 5):
    #     print(combo)


    # k = 12000
    # for r in range(k, 2*k+1):
    #     factors = Euler.find_factors(r)
    #     gen = itertools.combinations_with_replacement(len(factors), k)
    #     for g in gen:
    #         print(sum(g))

    # print(len(r_pool(12000, 12000)))

    top_k = 12000

    r_factorizations = {}
    for r in range(2, 2 * top_k + 1):
        print("r = ", r)
        r_factorizations[r] = r_combos(r)

    r_k = {}
    for k in range(2, top_k + 1):
        print("k = ", k)
        r_k[k] = find_r_for_k(k=k, r_combo_dict=r_factorizations)

    #     k_r[k] = k_check(k)
    #     print(k)
    #
    answer = sum(set(r_k.values()))
    print("answer = ", answer)

    # k_check(10000)
    # k = 5
    # gen = parts_algo(8, k)
    # for g in gen:
    #     # if sequence_product(g) == 2 * k:
    #     print(g)

    print("done")
