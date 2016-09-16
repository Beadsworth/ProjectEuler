

upper_limit = 100
n_nat_numbers = list(range(1, upper_limit + 1))


def sum_square(n_list):
    temp_list = []
    for n in n_list:
        temp_list.append(n * n)

    return sum(temp_list)


def square_sum(n_list):
    temp = sum(n_list)
    return temp ** 2


def sum_square_diff(n_list):

    a = sum_square(n_list)
    b = square_sum(n_list)
    return b - a

answer = sum_square_diff(n_nat_numbers)
print(answer)