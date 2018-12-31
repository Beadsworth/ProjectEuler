import math
from EulerHelpers import num_2_list

number = 100
fact = math.factorial(number)
fact_sum = sum(num_2_list(fact))

print('The sum of all digits in ' + str(number) + '! is ' + str(fact_sum))