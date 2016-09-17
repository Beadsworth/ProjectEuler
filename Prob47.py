from EulerHelpers import find_prime_factors

num = 1
num_unique = 4
consec_num = 0
num_list = []

while consec_num < num_unique:

    num_factors = find_prime_factors(num)
    distinct_factors = set(num_factors)
    if len(distinct_factors) == num_unique:
        consec_num += 1
        num_list.append(num)
    else:
        consec_num = 0
        num_list = []

    num += 1

print(num_list)
