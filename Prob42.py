import csv
from EulerHelpers import find_n_triangle_nums

tri_list = find_n_triangle_nums(100)
word_list = []

f = open('p042_words.txt', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        word_list = row
finally:
    f.close()


def convert_word(current_word):
    temp_sum = 0
    for letter in current_word:
        temp_sum += (ord(letter) - 64)

    return temp_sum


def is_tri_word(current_word):

    word_sum = convert_word(current_word)
    if word_sum in tri_list:
        return True
    else:
        return False


tally = 0

for word in word_list:

    if is_tri_word(word):
        tally += 1

print(tally)






