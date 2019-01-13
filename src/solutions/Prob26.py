import src.EulerHelpers as Euler
import math
import decimal

decimal.getcontext().prec = 1000


def to_proper_fraction(numerator, denominator):
    whole = numerator // denominator
    remainder = numerator - denominator * whole
    return whole, remainder


def gen_remainders(numerator, denominator):

    whole, remainder = to_proper_fraction(numerator, denominator)
    current_numerator = remainder * 10
    current_deci = str(whole) + '.'
    yield remainder, current_deci

    while True:

        current_addition = ''

        # keep adding zeros until we can divide
        while current_numerator < denominator:
            current_numerator = current_numerator * 10

            # add zero to current_deci
            current_addition += '0'

        whole, remainder = to_proper_fraction(current_numerator, denominator)
        current_addition += str(whole)
        current_deci += current_addition
        yield remainder, current_addition

        if remainder == 0:
            return
        else:
            current_numerator = remainder * 10


def get_repetition(numerator, denominator):

    remainders = []
    additions = []

    first_index = 0

    for index, (remainder, addition) in enumerate(gen_remainders(numerator, denominator)):
        additions.append(addition)

        # print(addition)
        if remainder == 0:
            first_index = index + 1
            break

        elif remainder in remainders:
            # index for first repeated digit
            first_index = remainders.index(remainder)
            break
        else:
            remainders.append(remainder)

    single_digits = additions[:first_index + 1]
    repeated_digits = additions[first_index + 1:]
    rep_len = len(repeated_digits)

    # TF include paranetheses
    para = 0
    if rep_len > 0:
        para = 1

    rep_str = ''.join(single_digits) + para*'(' + ''.join(repeated_digits) + para*')'
    progress_str = '{num:>1}/{dem:>3} -> {rep:<20} ({rep_len} repetitions)'\
        .format(num=numerator, dem=denominator, rep=rep_str, rep_len = rep_len)
    print(progress_str)

    return rep_len


if __name__ == '__main__':

    max_rep_count = 0
    max_divisor = 1
    for n in range(2, 999 + 1):
        rep_count = get_repetition(1, n)
        if rep_count > max_rep_count:
            max_rep_count = rep_count
            max_divisor = n

    print("\n1/{max_divisor} produces the most repetitions at {rep_count} repetitions"
          .format(rep_count=max_rep_count, max_divisor=max_divisor))


