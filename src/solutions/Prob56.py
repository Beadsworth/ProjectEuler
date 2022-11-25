"""
cycle through all a**b where a, b [2, 100]
only 99^2 number to check
sum the digits of each number, find the max of such sums
"""

import src.EulerHelpers as eh

def get_digit_sum(number: int) -> int:
    """return sum of all digits in number"""
    digits = eh.num_2_list(number=number)
    result = sum(digits)

    return result

def is_pow(n: int) -> bool:
    """returns true if number can be expressed in the form a**b"""
    factorizations = eh.get_all_factorization(n)
    pow_factorizations = [fac for fac in factorizations if len(fac.keys()) == 1]
    result = len(pow_factorizations) > 0

    return result

if __name__ == '__main__':
    print('starting script...')
    print('')

    max_digit_sum = 1
    for a in range(2, 100+1):
        for b in range(2, 100+1):

            # progress
            print(f'\rprogress: {a}, {b}', end='')

            num = a**b
            digit_sum = get_digit_sum(num)
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum

    answer = max_digit_sum
    print(f'\nmax sum : {answer}')

    print('done!')
