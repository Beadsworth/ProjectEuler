from EulerHelpers import find_factors


def divisible_by_factors(number, factor_list):

    for factor in factor_list:
        if (number % factor) is not 0:
            return False

    return True


def reduce_factor_list(factor_list):
    factor_pile = []
    new_list = []
    for factor in reversed(factor_list):
        if factor in factor_pile:
            continue
        else:
            new_list.append(factor)
        temp_list = find_factors(factor)
        for item in temp_list:
            if item not in factor_pile:
                factor_pile.append(item)
            else:
                pass

    return new_list

top_of_range = 20
current_num = top_of_range
temp_list = range(1, top_of_range+1)
reduced_list = reduce_factor_list(temp_list)


while divisible_by_factors(current_num, reduced_list) is False:

    current_num += 10
#     print(current_num)

print(current_num)

#reduced_list = reduce_factor_list(range(1,21))
#print(reduced_list)