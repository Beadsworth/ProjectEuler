import src.EulerHelpers as Euler
import math
import tqdm


class Checker:

    def __init__(self, digit_list, set_num):
        """digit list determines which digits are replaced.  Last digit should always be False"""
        assert digit_list[-1] is False, "last digit cannot be replaced"

        u = 10 - set_num
        self.digit_list = digit_list
        fixed_digit_list = self.digit_list[:-1]
        replacement_indices = [i for i, x in enumerate(digit_list) if x]
        non_replacement_indices = [i for i, x in enumerate(fixed_digit_list) if not x]
        x = len(non_replacement_indices)

        potential_list = []
        if x > 0:
            for i in range(10**x):
                y = ['?' for i in range(len(self.digit_list)-1)]
                format_str = '{:0'+str(x)+'d}'
                new_nums = [int(c) for c in format_str.format(i)]
                for k, num in enumerate(new_nums):
                    y[non_replacement_indices[k]] = str(num)

                for last_digit in (1, 3, 7, 9):
                    new_y = y + [str(last_digit)]
                    # print(new_y)
                    # potential_list.append(new_y)

                    # check this combo
                    # by now, the pattern has been assembled
                    # only u number of failures allowed
                    if new_y == ['5', '6', '?', '?', '3']:
                        print("here")
                    q = 0
                    pass_list = []
                    for k in range(10):
                        if q > u:
                            break
                        new_z = new_y.copy()
                        for m in replacement_indices:

                            new_z[m] = str(k)
                        new_num = int(''.join(new_z))
                        if new_num > 10**(len(digit_list)-1) and Euler.is_prime(new_num):
                            pass_list.append(new_num)
                        else:
                            q += 1
                    if len(pass_list) >= set_num:
                        print(pass_list)

        # for v in potential_list:
        #     print(v)


if __name__ == '__main__':

    number_len = 6
    for i in tqdm.tqdm(range(1, 2**(number_len-1))):
        bin_repr = bin(i)[2:]
        repl_list = [False] * (number_len - 1 - len(bin_repr)) + [True if x == '1' else False for x in bin_repr] + [False]
        Checker(repl_list, set_num=8)
