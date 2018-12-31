from EulerHelpers import is_prime, find_primes, find_perms, num_2_list, list_2_num, find_n_to_m_primes


def rot(num):
    num_list = num_2_list(num)
    num_list.append(num_list[0])
    num_list = num_list[1:]
    rot_num = list_2_num(num_list)
    return rot_num


def purge(input_list):
    output_list = []
    for item in input_list:
        temp = num_2_list(item)
        if 0 in temp or 2 in temp or 4 in temp or 5 in temp or 6 in temp or 8 in temp:
            pass
        else:
            output_list.append(item)

    return output_list


def circular_check(num, input_list, output_list):

    # determine number of rotations needed
    digits = len(num_2_list(num))
    temp = num

    for i in range(digits - 1):
        temp = rot(temp)
        if temp not in input_list:
            return

    output_list.append(num)


upper_limit = 1000000

circ_list = []
prime_list = find_primes(upper_limit)
# given: 13 circ primes under 100.  Reduce list to consider only numbers 100+, add 13 to answer at end
prime_list = prime_list[25:]
purged_list = purge(prime_list)


for item in purged_list:
    circular_check(item, purged_list, circ_list)
    print(prime_list.index(item)/len(purged_list))

print(circ_list)
print('Circular primes under ' + str(upper_limit) + ' is: ' + str(13+len(circ_list)))


