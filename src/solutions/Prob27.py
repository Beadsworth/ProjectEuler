import src.EulerHelpers as Euler


def quad(a, b, n):
    """quad form from problem"""

    return n**2 + a*n + b


def quad_is_prime(a, b, n):
    """return True/False on whether quad is prime (must be positive to be prime)"""
    return quad(a, b, n) > 1 and Euler.is_prime(quad(a, b, n))


def get_prime_pairs(pairs, n):
    """return list of good pairs"""
    prime_pairs = []
    for pair in pairs:
        a, b = pair
        if quad_is_prime(a, b, n):
            prime_pairs.append(pair)

    return prime_pairs


if __name__ == '__main__':

    # reduce number of pairs ot valid pairs only

    # to pass case n = 1, a must be odd
    a_list = [i for i in range(-999, 999, 2)]
    # to pass case n = 0, b must be prime
    b_list = [x for x in Euler.find_first_n_primes(1000) if x < 1000]

    valid_pairs = []
    for a in a_list:
        for b in b_list:
            # constraint for positive outcome, i.e. (n(n+a) + b) must be positive in n=1 case)
            if a > -1*b:
                valid_pairs.append((a, b))

    # iterate through n, eliminating bad pairs until only one pair remains
    remaining_pairs = valid_pairs
    pairs_left = len(remaining_pairs)
    n = -1
    while pairs_left > 1:
        n += 1
        remaining_pairs = get_prime_pairs(remaining_pairs, n)
        pairs_left = len(remaining_pairs)
        print(pairs_left)

    # print results
    final_pair = remaining_pairs[0]
    final_a, final_b = final_pair
    print("n:{n}, pair:{pair}".format(n=n, pair=final_pair))
    print("answer: {answer}".format(answer=final_a*final_b))
