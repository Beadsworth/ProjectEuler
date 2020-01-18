import src.EulerHelpers as Euler
import math
import tqdm


def reversed_number(number):
    return Euler.list_2_num(reversed(Euler.num_2_list(number)))


def lychrel_sum(number):
    return number + reversed_number(number)


def is_lychrel(number):

    temp = number
    for j in range(50):
        temp = lychrel_sum(temp)
        if Euler.is_palindrome(temp):
            return False

    # no palindrome found
    else:
        return True


if __name__ == '__main__':

    upper_limit = 10000
    # upper_limit = 10000

    check_list = list(range(1, upper_limit+1))

    lychrel_list = []
    for i in tqdm.tqdm(check_list):

        if is_lychrel(i):
            lychrel_list.append(i)

    print(len(lychrel_list))
