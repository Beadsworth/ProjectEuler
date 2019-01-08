import src.EulerHelpers as Euler
import math


class Cell:

    def __init__(self, level, index, value):
        self.level = level
        self.index = index
        self.value = value
        self.path_value = 0
        self.max_level = 0

    @property
    def child_coords(self):

        left_coords = None
        right_coords = None

        if self.level < self.max_level:

            level = self.level + 1

            left_index = self.index
            right_index = self.index + 1

            left_coords = level, left_index
            right_coords = level, right_index

        return left_coords, right_coords


class Pyramid:

    def __init__(self, pyr_str):
        self.levels = []
        for level, line in enumerate(pyr_str.strip().split('\n')):

            cells_values = line.strip().split()
            cells = [Cell(level=level, index=i, value=int(value))
                     for i, value in enumerate(cells_values)]
            self.levels.append(cells)

        for level in self.levels:
            for cell in level:
                cell.max_level = self.level_count - 1

    @property
    def level_count(self):
        return len(self.levels)

    def iterate_over(self):
        for level in reversed(self.levels):
            for cell in level:
                left_coord, right_coord = cell.child_coords

                # at bottom of pyramid
                if left_coord is None:
                    cell.path_value = cell.value

                else:
                    left_level, left_index = left_coord
                    right_level, right_index = right_coord

                    left_child_cell = self.levels[left_level][left_index]
                    right_child_cell = self.levels[right_level][right_index]

                    cell.path_value = cell.value + max(left_child_cell.path_value, right_child_cell.path_value)

        print("answer = ", self.levels[0][0].path_value)


    def print_pyramid(self):
        for level, cells in enumerate(self.levels):
            spaces = (len(self.levels) - level - 1)
            format_str = ''.join([' ' for i in range(3 * spaces)]) + '{:<4}' + ''.join([' {:<4}'
                                                                                        for i in range(len(cells) - 1)])
            cell_values = [cell.value for cell in cells]
            print(format_str.format(*cell_values))
            # for cell in level:
            #     print(cell.value)


if __name__ == '__main__':

    pyramid_str = \
        """
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
        """

    pyr = Pyramid(pyramid_str)
    pyr.print_pyramid()
    pyr.iterate_over()
