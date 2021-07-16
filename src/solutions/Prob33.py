import src.EulerHelpers as Euler
import fractions
import math


class Check:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    @property
    def is_trivial(self) -> bool:
        return (self.numerator % 10 == 0) and (self.denominator % 10 == 0)

    @property
    def is_curious(self) -> bool:
        num_list = Euler.num_2_list(self.numerator)
        den_list = Euler.num_2_list(self.denominator)

        correction_count = 0

        for digit in num_list.copy():
            if digit in den_list:
                num_list.remove(digit)
                den_list.remove(digit)

                # log correction
                correction_count += 1

        # if no corrections made, there is no reduction
        if correction_count < 1:
            return False

        # switched order case, e.g. 12/21 -> empty/empty
        # fraction equals 1/1 -> not equal to original fraction that was less than 1
        if len(num_list) < 1:
            return False

        new_num = Euler.list_2_num(num_list)
        new_den = Euler.list_2_num(den_list)

        # prevent divide by zero in next step
        if new_num == 0 or new_den == 0:
            return False

        # test for fraction equivalency: old_num/new_num = old_den/new_den
        if self.numerator/new_num == self.denominator/new_den:
            return True
        else:
            return False

    @property
    def is_non_trivial_curious(self) -> bool:
        return self.is_curious and not self.is_trivial


if __name__ == '__main__':

    non_trivial_cases = []
    for den in range(10, 100):
        for num in range(10, den):
            check = Check(numerator=num, denominator=den)
            # print(f'{check}: {check.is_trivial}, {check.is_curious}, {check.is_non_trivial_curious}')

            if check.is_non_trivial_curious:
                non_trivial_cases.append(check)


    print([str(case) for case in non_trivial_cases])

    num_mult = den_mult = 1

    for case in non_trivial_cases:
        num_mult = num_mult * case.numerator
        den_mult = den_mult * case.denominator

    result = fractions.Fraction(num_mult, den_mult)
    print(result)
