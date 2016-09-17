import math, copy


def is_prime(number):

    if (number % 1) is not 0:
        raise TypeError('Number not integer!  Cannot determine if prime.')

    if number <= 1:
        raise TypeError('Number not above 1!  Cannot determine if prime.')

    upper_limit = int(math.sqrt(number)) + 1  # need + 1 for 4, and just to be safe

    for potential_factor in range(2, upper_limit):
        if number % potential_factor is 0:
            return False  # factor found, not prime, escape this

    return True


def find_factors(number):

    factor_list = [1, ]
    for potential_factor in range(2, number):
        if potential_factor > (number / 2):
            break
        if number % potential_factor is 0:  # if it's a factor...
            if potential_factor in factor_list:  # if you find duplicate, you're already done
                return factor_list
            else:
                factor_list.append(potential_factor)
                comp_factor = number // potential_factor
                if comp_factor not in factor_list:
                    factor_list.append(comp_factor)  # add complementary factor

    factor_list.append(number)
    factor_list.sort()
    return factor_list


def find_prime_factors(number):

    prime_factor_list = []
    factor_list = find_factors(number)

    for factor in factor_list:
        if factor is 1:
            continue
        if is_prime(factor):
            prime_factor_list.append(factor)

    return prime_factor_list


def find_primes(up_to_num):
    """Returns list of primes up to and including the argument"""

    if up_to_num < 2:
        return []

    prime_list = [2, ]
    current_num = 3

    while current_num <= up_to_num:

        if is_prime(current_num):
            prime_list.append(current_num)

        current_num += 2
        # print(current_num / up_to_num)

    return prime_list


def find_first_n_primes(n):
    """Return list of the n smallest primes, slowly"""

    if ((n % 1) is not 0) or (n < 0):
        raise TypeError('Must give natural number!')

    if n is 0:
        return []

    if n is 1:
        return [2, ]

    #  from this point on, n is at least 2
    prime_list = []
    current_prime_count = 1
    current_num = 3

    while current_prime_count < n:

        prime_list = find_primes(current_num)
        current_prime_count = len(prime_list)
        current_num += 2

    return prime_list


def find_n_to_m_primes(n, m):
    """Returns consecutive list of primes, from nth to mth prime"""

    if ((m % 1) is not 0) or (m < n):
        raise TypeError('Bad range given')

    if n is 0:
        n = 1

    prime_list = find_first_n_primes(m)
    prime_list = prime_list[n-1:]

    return prime_list


def num_2_list(number):
    """Return list of digits, based off input number, negative numbers returned as positive list"""

    if type(number) is not int:
        raise TypeError('Must be integer!')

    if number is 0:
        return [0, ]

    if number < 0:
        number *= -1

    max_order = 1
    num_check = 0

    while num_check != number:
        max_order *= 10
        num_check = number % max_order

    num_list = []
    current_number = 1
    previous_order = 1
    current_order = 10

    while previous_order < max_order:

        current_number = ((number % current_order) - (number % previous_order)) // previous_order
        num_list.append(current_number)
        previous_order = current_order
        current_order *= 10

    result_list = list(reversed(num_list))
    return result_list


def list_2_num(num_list):
    """Complement to num_2_list()"""

    new_num_list = list(num_list)

    for item in new_num_list:
        if type(item) is not int:
            raise TypeError('List of Ints only!')

    if len(new_num_list) is 0:
        raise TypeError('List was empty!')

    temp_list = new_num_list

    digits = len(new_num_list)
    for i in range(digits):
        temp_list[digits -1 - i] *= 10 ** i

    return sum(temp_list)


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
