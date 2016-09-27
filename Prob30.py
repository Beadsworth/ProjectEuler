from EulerHelpers import num_2_list

power = 5
upper_limit = 1000000
answer_list = []


def check_pow(number):

    num_list = num_2_list(number)
    power_list = [digit ** power for digit in num_list]
    power_sum = sum(power_list)
    if power_sum == number:
        return True
    else:
        return False

for i in range(2, upper_limit):
    if check_pow(i):
        answer_list.append(i)

print('Answer list: ' + str(answer_list))
print('Answer: ' + str(sum(answer_list)))
