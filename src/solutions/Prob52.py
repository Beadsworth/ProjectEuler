import src.EulerHelpers as Euler
import math
import tqdm
import collections


def digit_counts(number):
    counts_dict = collections.defaultdict(int)
    for digit in Euler.num_2_list(number):
        counts_dict[digit] += 1

    return counts_dict


def has_same_digits(a, b):
    return digit_counts(a) == digit_counts(b)


def search_magnitude(magnitude, threshold):
    first_digit_max = 10//threshold
    search_start = 10 ** (magnitude - 1)
    search_stop = (first_digit_max + 1) * (10 ** (magnitude - 1))

    for number in tqdm.tqdm(range(search_start, search_stop)):
        count = 1 + sum(1 for i in range(2, threshold + 1) if has_same_digits(number, number * i))
        if count >= threshold:
            return number

    return None


if __name__ == '__main__':
    for mag in range(6, 10 + 1):
        print('magnitude: {}'.format(mag))
        result = search_magnitude(magnitude=mag, threshold=6)
        if result:
            print(result)
            break
