import math
from EulerHelpers import find_prime_factors


number = 600851475143


prime_factor_list = find_prime_factors(number)
max_prime_factor = max(prime_factor_list)

print(max_prime_factor)
