import src.EulerHelpers as Euler
import math
import tqdm


def passes_goldbach(i, p, x):
    return i == p + 2 * (x**2)


def is_goldbach(i, primes):
    for p in reversed(primes):
        x_guess = math.sqrt((i - p) / 2)
        x_test_cases = [math.floor(x_guess), math.ceil(x_guess)]

        for x in x_test_cases:
            if passes_goldbach(i=i, p=p, x=x):
                return True

    return False


if __name__ == '__main__':
    primes = []
    composites = []
    for i in tqdm.tqdm(range(2, 10**5 + 1)):
        # if prime
        if Euler.is_prime(i):
            primes.append(i)
        # if composite
        else:
            composites.append(i)
            # if composite and odd
            if i % 2 == 1:
                if not is_goldbach(i, primes=primes):
                    print('{} is not an odd-composite Goldbach number'.format(i))
                    break




