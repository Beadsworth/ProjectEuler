import src.EulerHelpers as Euler
import math
import csv
import Prob18 as p18

def get_pyramid_str():

    with open(r'p067_triangle.txt', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        pyr_str = ''
        for row in csv_reader:
            row_str = ' '.join(row)
            pyr_str += '\n' + row_str

        return pyr_str.strip()


if __name__ == '__main__':

    pyramid_str = get_pyramid_str()

    pyr = p18.Pyramid(pyramid_str)
    pyr.print_pyramid()
    pyr.iterate_over()
