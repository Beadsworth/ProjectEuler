import src.EulerHelpers as Euler
import math
import string


def get_names(file_path):

    with open(file_path) as file:
        txt = file.read()

    names_list = sorted(name.split('\"')[1].upper() for name in txt.split(','))

    return names_list


def name_count(name):

    count = 0
    for letter in name:
        letter_value = string.ascii_uppercase.index(letter) + 1
        count += letter_value

    return count


if __name__ == '__main__':

    names_file_path = r'/home/jmb/PycharmProjects/ProjectEuler/src/solutions/p022_names.txt'
    names = get_names(names_file_path)
    counts = [(i+1) * name_count(name) for i, name in enumerate(names)]

    answer = sum(counts)
    print("answer =", answer)