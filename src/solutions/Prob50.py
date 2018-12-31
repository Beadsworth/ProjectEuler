from EulerHelpers import find_n_to_m_primes, find_first_n_primes, is_prime, find_primes


def find_consec_sum_primes(up_to_n, reduction_factor):
    """Returns list containing list of [sum, num_consec_primes]"""

    temp_list = []
    prime_list = find_primes((1/reduction_factor)*up_to_n)
    len_prime_list = len(prime_list)

    i = 0
    j = reduction_factor
    last_sum = 0

    while last_sum < up_to_n:
        if i >= len_prime_list:
            break
        while last_sum < up_to_n:
            if j >= len_prime_list:
                break
            new_prime_list = prime_list[i: j]
            last_sum = sum(new_prime_list)
            len_last_sum = len(new_prime_list)
            if last_sum > up_to_n:
                last_sum = 0
                break
            if [last_sum, len_last_sum] not in temp_list:
                temp_list.append([last_sum, len_last_sum])

            j += 1

        i += 1
        j = i + reduction_factor
        print(i)

    return temp_list


def reduce_to_prime_sums(list_list):
    reduced_list = []
    for item in list_list:
        if is_prime(item[0]):
            reduced_list.append(item)

    return reduced_list


def find_longest(reduced_list):
    longest_len = 0
    longest_prime = 2

    for item in reduced_list:
        if (item[1] >= longest_len) and (item[0] > longest_prime):
            longest_len = item[1]
            longest_prime = item[0]

    print('Length is: ' + str(longest_len))
    return longest_prime

reduce = 200
upper_limit = 1000000

temp_list1 = find_consec_sum_primes(upper_limit, reduce)
temp_list2 = reduce_to_prime_sums(temp_list1)
answer = find_longest(temp_list2)

#print(temp_list1)
#print(temp_list2)

print('Answer is: '+str(answer))
#print(is_prime(answer))
