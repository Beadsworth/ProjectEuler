import src.EulerHelpers as Euler
import math


def find_dia_sum(side):
    """
    for box of size side x side, find sum of diagonals
    side must be odd
    """

    assert side % 2 == 1, "side must be odd"

    # closed form solution
    r = (side - 1) / 2
    return int((16 * (r ** 3) + 30 * (r ** 2) + 26 * r + 3) / 3)


if __name__ == '__main__':
    print(find_dia_sum(1001))
