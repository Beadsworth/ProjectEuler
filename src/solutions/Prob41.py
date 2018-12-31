import copy
from EulerHelpers import find_n_to_m_primes, num_2_list, is_prime, find_perms, list_2_num

pan_ranges = [

    [123456789, 987654321],
    [12345678 ,  87654321],
    [1234567  ,   7654321],
    [123456   ,    654321],
    [12345    ,     54321],
    [1234     ,      4321],
    [123      ,       321],
    [12       ,        21],

]


def is_pandigital(number):

    # digit_count = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    digit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if number <= 0:
        return False
    if number == 1:
        return True

    if number > 987654321:
        return False

    digit_list = num_2_list(number)
    num_of_digits = len(digit_list)
    digit_count = digit_count[:num_of_digits]

    for digit in digit_list:
        digit_count[digit - 1] += 1

    for digit in digit_count:
        if digit != 1:
            return False

    return True


# nothing above this line is actually used to solve problem


# use permutations to generate list of pandigital numbers

pan_input = num_2_list(1234567)

pan_list = find_perms(pan_input)

# reverse order and find primes
for pan in reversed(pan_list):
    # pan is list -> convert to number
    fixed_pan = list_2_num(pan)
    if is_prime(fixed_pan):
        print(fixed_pan)
        print(is_pandigital(fixed_pan))
        break


