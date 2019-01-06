import src.EulerHelpers as Euler
import csv


class ExpPair:

    def __init__(self, base, exp):
        self.base = int(base)
        self.exp = int(exp)

    # too slow
    # divide each exp by 100000 to speed up
    @property
    def result(self):
        return self.base ** (self.exp/100000)


if __name__ == '__main__':

    exp_pairs = []
    with open(r'p099_base_exp.txt', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            base, exp = row
            exp_pairs.append(ExpPair(base, exp))

    bases = [exp_pair.base for exp_pair in exp_pairs]
    # factors = [Euler.find_factors(base) for base in bases]

    results = [(i+1, exp_pair.result) for i, exp_pair in enumerate(exp_pairs)]
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    for x in sorted_results:
        print(x)
