import src.EulerHelpers as Euler
import math
import tqdm
import collections


class Relationships:

    def __init__(self, file_path):
        with open(Euler.get_path(file_path), mode='r') as file:
            txt = file.read().strip()

        logins = [int(x) for x in txt.split('\n')]
        unique_logins = sorted(set(logins))

        self.passcode = []
        self.relationships = []
        for login in unique_logins:
            digits = Euler.num_2_list(login)
            a = digits[:2]
            b = digits[1:]
            for x in (a, b):
                if x not in self.relationships:
                    self.relationships.append(x)

        # create a list of digits to ignore
        self.ignore_list = list(range(10))
        self.valid_list = []
        for relationship in self.relationships:
            for digit in relationship:
                if digit in self.ignore_list:
                    self.ignore_list.remove(digit)
                    self.valid_list.append(digit)

    def iterate(self):
        while len(self.filtered_relationships) > 0:
            # print(self.filtered_relationships)
            dig_res = self.digit_results(self.filtered_relationships)
            first_digit = dig_res[0][0]
            self.ignore_list.append(first_digit)
            self.valid_list.remove(first_digit)
            self.passcode.append(first_digit)

        # add remaining number
        self.passcode += self.valid_list
        print('passcode = {}'.format(Euler.list_2_num(self.passcode)))

    def digit_results(self, test_relationships):
        index_counts = {i: collections.defaultdict(int) for i in range(10)}
        for relationship in test_relationships:
            for i, digits in enumerate(relationship):
                index_counts[digits][i] += 1

        digit_results = [(key, value[1]) for key, value in index_counts.items() if key not in self.ignore_list]
        # sorted_digit_results = sorted(digit_results, key=lambda x: x[1] * 100 + x[2] * 10 + x[3], reverse=True)
        return sorted(digit_results, key=lambda x: x[-1])

    @property
    def filtered_relationships(self):
        new_relationships = []
        for relationship in self.relationships:
            if relationship[0] not in self.ignore_list and relationship[1] not in self.ignore_list:
                new_relationships.append(relationship)

        return new_relationships


if __name__ == '__main__':
    my_path = r'src/misc/p079_keylog.txt'
    Relationships(my_path).iterate()
