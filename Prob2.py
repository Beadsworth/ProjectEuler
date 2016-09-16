import math


def make_fib(max_number):
    fib_list = [1,2]
    add_1 = 1
    add_2 = 2
    sum_1_2 = add_1 + add_2

    while sum_1_2 <= max_number:
        fib_list.append(sum_1_2)
        add_1 = add_2
        add_2 = sum_1_2
        sum_1_2 = add_1 + add_2

    return fib_list


def make_even(number_list):
    even_list = []
    for number in number_list:
        if (number % 2) == 0:
            even_list.append(number)

    return even_list

max_number = 4000000
new_fib_list = make_fib(max_number)
new_fib_even = make_even(new_fib_list)

even_fib_sum = sum(new_fib_even)
print(even_fib_sum)

