import src.EulerHelpers as euler


def sum_of_digits(integer):
    return sum(euler.num_2_list(integer))


def sum_of_digits_of_power_of_2(power):
    return sum_of_digits(2**power)


def print_power_answer(power):
    answer = sum_of_digits_of_power_of_2(power)
    print("sum of digits of 2 to the power of {power} = {answer}".format(power=power, answer=answer))


if __name__ == '__main__':
    print_power_answer(15)
    print_power_answer(1000)
