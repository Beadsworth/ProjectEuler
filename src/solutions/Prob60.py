"""
4-prime list = [3, 7, 109, 673]
4-prime answer = 792

build list of primes
find next prime
compare that prime to every prime already in the list
when 4 pairs are found, you are done
if prime doesn't match any, more on to next iteration
"""
from src.EulerHelpers import prime_gen_2, is_prime
from typing import List


def concats_are_prime(a: int, b: int) -> bool:
    """returns True if both concatenations are prime"""

    concat_1 = int(str(a) + str(b))
    concat_2 = int(str(b) + str(a))
    result = is_prime(concat_1) and is_prime(concat_2)

    return result


def concat_list_is_prime(prime_list: List[int]) -> bool:
    """Check if all possible pairs satisfy the prime condition.  Assumes prime_list is sorted"""

    for index, a in enumerate(prime_list):
        for b in prime_list[index+1:]:
            pair_is_good = concats_are_prime(a, b)

            # if one pair fails the test, the whole list fails
            if not pair_is_good:
                return False
            # print(f'prime_1: {a: >4}, prime_2: {b: >4}')
        return True


def check_prime_position(required_primes: int, prime_list: List[int], current_prime: int) -> List[int]:
    """return list of primes if prime has required_primes matches before it"""

    matches_needed = required_primes - 1
    matches = 0
    paired_primes = []
    for prime in prime_list:
        if concats_are_prime(a=prime, b=current_prime):
            paired_primes.append(prime)
            matches += 1

            # short-circuit condition
            if matches == matches_needed:
                break

    final_result = paired_primes + [current_prime, ]
    # call again with prime_list = final_result[:-1] and current_prime = final_result[-2]
    # then prime_list = final_result[:-2] and current_prime = final_result[-3]
    # etc
    return final_result


def find_pair_list(required_primes: int) -> List[int]:

    prime_list = []
    # skip 2
    for prime in prime_gen_2(start=2, stop=673):
        print(f'\rprime: {prime: >6}', end='')
        matching_primes = check_prime_position(required_primes=required_primes, prime_list=prime_list, current_prime=prime)
        if len(matching_primes) >= required_primes:
            return matching_primes

        prime_list.append(prime)



if __name__ == '__main__':
    print('starting script...')



    # test_primes = [3, 7, 109, 673]
    # test_primes = [3, 7, 109]

    # test = concat_list_is_prime(prime_list=test_primes)
    # answer = find_pair_list(required_primes=4)
    my_prime_list = list(prime_gen_2(start=3, stop=96))
    answer = check_prime_position(required_primes=4, prime_list=my_prime_list, current_prime=97)

    print(f'\ranswer: {answer}, sum:{sum(answer)}')

    print('done!')
