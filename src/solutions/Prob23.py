import src.EulerHelpers as Euler


def is_abundant(integer):
    factors = Euler.find_factors(integer)
    proper_factors = factors[:-1]
    return sum(proper_factors) > integer


def is_sum_of_two_from_list(term_list, n):

    print(n)
    term_list_fixed = [x for x in term_list if x < n]
    for i, term_1 in enumerate(term_list_fixed):
        scrap = n - term_1
        if scrap in term_list_fixed[i:]:
            return True

    return False


if __name__ == '__main__':

    abundant_numbers = [n for n in range(12, 28123+1) if is_abundant(n)]
    non_abundant_sums = [x for x in range(1, 28123+1) if not is_sum_of_two_from_list(abundant_numbers, x)]
    print("sum:", sum(non_abundant_sums))
