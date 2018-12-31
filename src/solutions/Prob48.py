last_10 = 10000000000
upper_limit = 1000
temp_sum = 0

for i in range(1, upper_limit + 1):
    temp_sum += i ** i

print('Answer: ' + str(temp_sum % last_10))