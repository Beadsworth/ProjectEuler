from EulerHelpers import is_prime, find_primes, find_perms, num_2_list, list_2_num, find_n_to_m_primes


def is_trunc_prime(prime):
    num_list = num_2_list(prime)
    digits = len(num_list)
    for i in range(1, digits):
        temp1 = list_2_num(num_list[i:])
        temp2 = list_2_num(num_list[:digits - i])

        if is_prime(temp1) and is_prime(temp2):
            pass
        else:
            return False

    return True


def purge(input_list):
    output_list = []
    for item in input_list:
        temp = num_2_list(item)
        if 0 in temp or 4 in temp or 6 in temp or 8 in temp or temp[0] == 1 or temp[len(temp)-1] == 1 or temp[0] == 9\
                or temp[len(temp)-1] == 9:
            pass
        else:
            if temp.count(2) < 2 and temp.count(5) < 2:
                output_list.append(item)

    return output_list


upper_limit = 1000000


prime_list = find_primes(upper_limit)
# only consider primes above 7
prime_list = prime_list[4:]
purged_list = purge(prime_list)
trunc_list = []

for item in purged_list:
    if is_trunc_prime(item):
        trunc_list.append(item)

print(trunc_list)
print('Sum = ' + str(sum(trunc_list)))



