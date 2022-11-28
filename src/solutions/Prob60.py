"""
4-prime list = [3, 7, 109, 673]
4-prime answer = 792

build dictionary of primes
{prime: list of concat pairs including self}
when latest key has at least 3 matches, verify all matches have other matches in their own key
might be possible that you get more than the required number of matches
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


def check_prime_position(prime_list: List[int], current_prime: int) -> List[int]:
    """return list of primes if prime has required_primes matches before it"""

    paired_primes = []
    for prime in prime_list:
        if concats_are_prime(a=prime, b=current_prime):
            paired_primes.append(prime)

    final_result = paired_primes
    # call again with prime_list = final_result[:-1] and current_prime = final_result[-2]
    # then prime_list = final_result[:-2] and current_prime = final_result[-3]
    # etc
    return final_result


def find_pair_list(required_primes: int) -> List[int]:

    prime_matches = {}
    prime_list = []
    # skip 2
    for prime in prime_gen_2(start=3, stop=673):
        # print progress
        print(f'\rprime: {prime: >6}', end='')

        # for the current prime, find all possible matches
        matching_primes = check_prime_position(prime_list=prime_list, current_prime=prime)
        prime_list.append(prime)
        if matching_primes:
            prime_matches[prime] = matching_primes


            print(prime_matches)

            # backwards iteration through list
            # need at least required_primes number of matches
            match_count = 1
            reversed_prime_matches = list(reversed(matching_primes))
            for i, prime_match in enumerate(reversed_prime_matches):
                # key must exist and value must contain all lower numbers
                if prime_match in prime_matches:
                    smaller_list = list(reversed_prime_matches)[i+1:]
                    smaller_count = [x for x in smaller_list if x in prime_matches]
                    if smaller_count == len(list(reversed_prime_matches)):
                        match_count += 1
                        if match_count >= required_primes:
                            return prime_list[-1]

            # end condition
            if len(matching_primes) >= required_primes+2:
                return prime


if __name__ == '__main__':
    print('starting script...')



    # test_primes = [3, 7, 109, 673]
    # test_primes = [3, 7, 109]

    # test = concat_list_is_prime(prime_list=test_primes)
    # answer = find_pair_list(required_primes=4)
    # my_prime_list = list(prime_gen_2(start=3, stop=673))
    answer = find_pair_list(4)

    # print(check_prime_position(prime_list=my_prime_list, current_prime=673))

    print(f'\ranswer: {answer}')

    print('done!')
