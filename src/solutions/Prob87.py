import src.EulerHelpers as Euler
import math


if __name__ == '__main__':

    # generate list of primes
    upper_limit = 50000000
    prime_limit = int(math.ceil(math.sqrt(upper_limit)))
    primes = Euler.find_primes(up_to_num=prime_limit)

    squares = [x ** 2 for x in primes if x ** 2 < upper_limit]
    cubes = [x ** 3 for x in primes if x ** 3 < upper_limit]
    fourths = [x ** 4 for x in primes if x ** 4 < upper_limit]

    print(len(squares)*len(cubes)*len(fourths))
    print(squares)
    print(cubes)
    print(fourths)

    power_triples = set()
    for square in squares:
        for cube in cubes:
            for fourth in fourths:
                print(square, cube, fourth)
                triple_sum = square + cube + fourth
                if triple_sum < upper_limit:
                    power_triples.add(triple_sum)

    print("answer:", len(power_triples))
