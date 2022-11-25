import math
import os


def get_path(relative_path):
    """get absolute_path relative to top-level "crypto" folder"""
    dirname = os.path.dirname(__file__)

    higher_path = dirname
    for i in range(1):
        higher_path = os.path.split(higher_path)[0]

    file_path = os.path.join(higher_path, relative_path)
    return file_path


def is_prime(number):

    try:
        integer = int(number)
    except (TypeError, ValueError) as e:
        raise TypeError('Number not integer!  Cannot determine if prime.')

    if integer <= 1:
        raise TypeError('Number not above 1!  Cannot determine if prime.')

    if integer == 2:
        return True

    if integer % 2 == 0:  # if even
        return False

    upper_limit = int(math.sqrt(integer)) + 1  # need + 1 for 4, and just to be safe

    for potential_factor in range(3, upper_limit, 2):
        if integer % potential_factor == 0:
            return False  # factor found, not prime, escape this

    return True


def find_factors(number):

    if number == 0:
        raise TypeError('Cannot factor zero!')
    if number % 1 != 0 or number < 1:
        raise TypeError('Positive ints only!')
    if number == 1:
        return [1]

    factor_list = [1, ]

    sq_rt = int(math.sqrt(number))

    for potential_factor in range(2, sq_rt + 1):
        if number % potential_factor == 0:  # if it's a factor...
            comp_factor = number // potential_factor
            factor_list.append(potential_factor)
            if comp_factor not in factor_list:
                factor_list.append(comp_factor)

    factor_list.append(number)  # number -> add itself as factor
    factor_list.sort()
    return factor_list


def find_prime_factors(number):

    prime_factor_list = []
    factor_list = find_factors(number)

    for factor in factor_list:
        if factor == 1:
            continue
        if is_prime(factor):
            prime_factor_list.append(factor)

    return prime_factor_list


def get_prime_factorization(n):

    prime_factors = find_prime_factors(n)

    result = {}

    for prime in prime_factors:

        quotient = n
        count = 0
        while quotient % prime == 0:
            count += 1
            quotient = quotient // prime

        result[prime] = count

    return result


def get_prime_factorization_pool(n):

    prime_factorization = get_prime_factorization(n)

    factors = []
    for prime_factor, count in prime_factorization.items():
        factors = factors + [prime_factor for i in range(count)]

    return factors


def sequence_product(sequence):

    product = 1
    for n in sequence:
        product = product * n

    return product


def get_all_factorization_pool(n):

    prime_factor_pool = get_prime_factorization_pool(n)
    found_factors = []

    for partition in set_partition(prime_factor_pool):
        factors = sorted([sequence_product(sequence) for sequence in partition])

        # trivial case, need 1 * n added
        if len(factors) == 1:
            factors = factors + [1]

        if factors not in found_factors:
            found_factors.append(factors)
            yield factors


def get_all_factorization(n):

    all_factor_pool = get_all_factorization_pool(n)
    factorization_combos = []

    for factorization in all_factor_pool:
        factor_dict = {}
        for factor in factorization:
            # update factor dictionary
            if factor not in factor_dict:
                factor_dict[factor] = 1
            else:
                factor_dict[factor] += 1

        factorization_combos.append(factor_dict)

    return factorization_combos


def find_next_prime(start):
    """Finds and returns next prime from start.  If start is prime, start is returned"""

    if start <= 2:
        return 2

    potential_prime = int(start)

    if potential_prime % 2 == 0:  # if even, add one (even cannot be prime anyway)
        potential_prime += 1

    while True:
        if is_prime(potential_prime):
            return potential_prime
        else:
            potential_prime += 2


def find_prev_prime(start):
    """Finds and returns prev prime from start.  If start is prime, start is returned"""

    if start <= 2:
        return 2

    potential_prime = int(start)

    if potential_prime % 2 == 0:  # if even, subtract one (even cannot be prime anyway)
        potential_prime -= 1

    while potential_prime > 1:
        if is_prime(potential_prime):
            return potential_prime
        else:
            potential_prime -= 2

    return 2  # if you get to this point, you have reached two and cannot go lower


def prime_gen(start, end=None):
    """prime number generator.  Finds next prime from start, then iterates until no more primes less than end"""

    if end is None:  # makes argument behavior similar to range()
        start, end = 2, start
        if end < 2:
            return

    # from here, both start and end were declared as parameters
    if end < start:
        raise TypeError('End is less than start')

    current_prime = find_next_prime(start)

    if current_prime > end:
        return

    if current_prime < 3:
        yield 2

    if current_prime <= 3:
        current_prime = 3

    # TODO: is this redundant?
    if current_prime > end:
        return

    # from here on, start/current prime is 3 or greater
    while True:
        yield current_prime
        current_prime = find_next_prime(current_prime+2)
        if current_prime > end:
            break


def fib_gen(nth_term):
    """fibonacci number generator.  Input is number of desired terms, up to and including the nth term.
    F(0) = 0, F(1) = 1, F(2) = 1."""

    if (type(nth_term) is not int) or (nth_term < 0):
        raise TypeError('Must be positive integer or zero!')

    terms_left = nth_term + 1
    prev_prev_num = 0
    prev_num = 1

    # yield first two terms
    yield 0
    terms_left -= 1
    if terms_left <= 0:
        return
    yield 1
    terms_left -= 1

    while terms_left > 0:

        curr_num = prev_num + prev_prev_num
        prev_prev_num = prev_num
        prev_num = curr_num
        yield curr_num
        terms_left -= 1


def find_nth_fib_term(n):

    fib = fib_gen(n)
    nth_term = next(fib)
    for i in range(n):
        nth_term = next(fib)

    return nth_term


def find_primes(up_to_num):
    """Returns list of primes up to and including the argument"""

    if up_to_num < 2:
        return []

    prime_list = []

    for prime in prime_gen(up_to_num):
        prime_list.append(prime)

    return prime_list


def find_first_n_primes(n):
    """Return list of the n smallest primes"""

    if ((n % 1) != 0) or (n < 0):
        raise TypeError('Must give natural number!')

    if n == 0:
        return []

    if n == 1:
        return [2, ]

    #  from this point on, n is at least 2
    prime_list = [2, ]
    curr_prime = 3

    for i in range(n-1):

        prime_list.append(curr_prime)
        prev_prime = curr_prime
        curr_prime = find_next_prime(prev_prime + 2)

    return prime_list


def find_n_to_m_primes(n, m):
    """Returns consecutive list of primes, from nth to mth prime"""

    if ((m % 1) != 0) or (m < n):
        raise TypeError('Bad range given')

    if n == 0:
        n = 1

    prime_list = find_first_n_primes(m)
    prime_list = prime_list[n-1:]

    return prime_list


def num_2_list(number):
    """Return list of digits, based off input number, negative numbers returned as positive list"""

    assert type(number) is int, 'Must be integer!'

    if number < 0:
        number *= -1

    return [int(c) for c in str(number)]


def list_2_num(num_list):
    """Complement to num_2_list()"""

    for item in num_list:
        assert type(item) is int, 'List of ints only!'

    assert len(num_list) > 0, 'List was empty!'

    return int(''.join(str(x) for x in num_list))


def scramble(progress, pool, result):
    """recursive function for combo, permutations.  Progress is result, pool is where combos come from.
      Returns Nothing.  Result is entered as parameter and altered!"""

    if len(pool) == 0:
        result.append(progress)
        return None

    for digit in range(len(pool)):
        new_progress = list(progress)  # copy for each recursive call
        new_pool = list(pool)  # copy for each recursive call

        new_num = pool[digit]
        new_progress.append(new_num)

        new_pool.pop(digit)
        scramble(new_progress, new_pool, result)

    return None


def find_perms(input_list):
    """Takes input list and returns all permutations of that list.  Input list not affected.
    Returns a list.  Inputs not necessarily ints.  No repetition (unless already repeated in input), all items used
    Length of result_list will be n factorial.  Recommend not go over len(input_list) == 10"""

    progress_list = []
    temp_list = list(input_list)
    result_list = []
    scramble(progress_list, temp_list, result_list)

    return result_list


def collatz_gen(starting_num):
    """Iterate through Collatz sequence.  First term will be the input parameter"""

    if (type(starting_num) is not int) or (starting_num < 1):
        raise TypeError('Must be positive integer above 1')

    current_term = starting_num

    yield current_term

    while current_term > 1:

        if current_term % 2 == 0:  # if even
            current_term = current_term // 2
            yield current_term

        else:  # if odd
            current_term = 3*current_term + 1
            yield current_term


def find_nth_triangle_num(n):

    return (n * (n + 1))//2


def find_n_triangle_nums(n):
    """return list of triangle numbers, up to nth term"""

    if (type(n) is not int) or (n < 1):
        raise TypeError('Must be positive integer above 1')

    tri_list = [1]

    for i in range(2, n+1):

        tri_list.append(find_nth_triangle_num(i))

    return tri_list


def set_partition(collection):
    """recursively find partitions of a set"""

    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in set_partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n+1:]
        # put `first` in its own subset
        yield [[first]] + smaller


def partition_into_m_parts(n, m):
    """generate sequences of length m where sum = n"""

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


def is_palindrome(number):
    num_list = num_2_list(number)
    num_digits = len(num_list)
    for i in range(num_digits // 2):
        if num_list[i] != num_list[num_digits - 1 - i]:
            return False

    return True
