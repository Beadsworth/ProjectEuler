import math

natural_numbers_100 = range(1,1000)


def is_mult_3_or_5(number):
    if (number % 3 == 0) or (number % 5 == 0):
        return True
    else:
        return False


def find_all_mults(number_list):
    mult_list = []
    for number in number_list:
        if is_mult_3_or_5(number):
            mult_list.append(number)

    return mult_list

mult_list = find_all_mults(natural_numbers_100)
sum = sum(mult_list)
print(sum)
