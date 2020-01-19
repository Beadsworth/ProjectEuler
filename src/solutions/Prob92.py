import src.EulerHelpers as Euler
import math
import tqdm

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89


class Solver:

    def __init__(self, upper_limit):
        self.solution_dict = {}
        self.upper_limit = upper_limit

        for i in tqdm.tqdm(range(1, self.upper_limit)):
            # print(i, end=' → ')
            self.solution_dict[i] = self.converges_to_89(i)

    @staticmethod
    def square_sum(number):
        digit_list = Euler.num_2_list(number)
        return sum(x**2 for x in digit_list)

    def converges_to_89(self, number):
        t = number
        while True:
            t = self.square_sum(t)
            # print(t, end=' → ')
            if t == 1:
                # print(False)
                return False
            elif t == 89:
                # print(True)
                return True
            elif t < number:
                # print(self.solution_dict[t])
                return self.solution_dict[t]

    @property
    def convergence_count(self):
        return sum(1 for n, conv_to_89 in self.solution_dict.items() if conv_to_89)


if __name__ == '__main__':

    s = Solver(upper_limit=10**7)
    print("answer = ", s.convergence_count)
