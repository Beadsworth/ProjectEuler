from EulerHelpers import is_prime

prime_place_target = 10001
prime_place_num = 1
testing_num = 1

# count 2 automatically, start on 3 and count every other number
while prime_place_num < prime_place_target:
    print('Number of primes found so far: ' + str(prime_place_num))
    testing_num += 2

    if is_prime(testing_num):
        prime_place_num += 1


print(testing_num)