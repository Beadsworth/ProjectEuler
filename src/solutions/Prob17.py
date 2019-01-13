import src.EulerHelpers as Euler
import math


single_digits = \
    {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

teens = \
    {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }

double_digits = \
    {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }


def remove_spaces_and_hyphens(num_str):

    fixed_str = num_str
    # remove spaces
    fixed_str = ''.join(fixed_str.split())
    # remove hyphens
    fixed_str = ''.join(fixed_str.split('-'))

    return fixed_str


def get_last_two_digits(num):

    num_str = ''

    # 1 - 9
    if num <= 9:
        num_str = single_digits[num]

    # 10 - 19
    elif num <= 19:
        num_str = teens[num]

    # 20 - 99
    else:
        ones = num % 10
        tens = num - ones

        num_str = double_digits[tens]

        if ones > 0:
            num_str += '-' + single_digits[ones]

    return num_str


def get_num_str(num):


    num_str = ''

    # 0
    if num == 0:
        num_str = 'zero'

    # 1000
    if num == 1000:
        num_str = 'one thousand'

    else:

        last_two_digits = num % 100
        last_two_digits_str = get_last_two_digits(last_two_digits)
        hundreds = num - last_two_digits
        hundreds_digit = hundreds / 100

        if hundreds_digit > 0:
            num_str += single_digits[hundreds_digit] + ' hundred'
            if last_two_digits > 0:
                num_str += ' and '
        if last_two_digits > 0:
            num_str += last_two_digits_str

    return num_str


def count_letters(num):

    num_str = get_num_str(num)
    print(num_str)
    fixed_str = remove_spaces_and_hyphens(num_str)

    return len(fixed_str)


if __name__ == '__main__':

    # debug
    print(count_letters(342))  # should be 23
    print(count_letters(115))  # should be 20

    answer = sum(count_letters(i) for i in range(1, 1000 + 1))
    print("answer =", answer)


