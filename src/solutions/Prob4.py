from EulerHelpers import num_2_list

# find palindromes in made of product of two 3-digit numbers
# product must be in range 100 * 100 -> 999 * 999
# first, find all palindromes within that range


def is_palindrome(number):
    num_list = num_2_list(number)
    num_digits = len(num_list)
    for i in range(num_digits // 2):
        if num_list[i] != num_list[num_digits - 1 - i]:
            return False

    return True


def gen_pal_list(min, max):

    pal_list = []
    for number in range(min, max + 1):
        if is_palindrome(number):
            pal_list.append(number)

    return pal_list


def find_proper_factors(number, min, max):
    proper_factor_list = []
    for factor in range(min, max +1):
        comp_factor = number // factor
        if (number % factor == 0) and (comp_factor >= min) and (comp_factor <= max):
            proper_factor_list.append(sorted([factor, comp_factor]))

    return proper_factor_list

start = 100
stop = 999

pal_list = gen_pal_list(start*start, stop*stop)
proper_pal_list = []

for pal in pal_list:
    temp_factors = find_proper_factors(pal, start, stop)
    temp_list = [pal, temp_factors]
    if len(temp_factors) != 0:
        proper_pal_list.append(pal)


#for item in proper_pal_list:
#    print('Pal: ' + str(item[0]) + '\n' + 'Factors: ' + str(item[1]))

print('Biggest palindrome: ' + str(max(proper_pal_list)))