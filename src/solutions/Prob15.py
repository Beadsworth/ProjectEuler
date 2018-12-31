# start at top-left corner -- position (x, y); move to bottom-right corner -- position (0, 0)
# x -> x-1 means moving right, y -> y-1 means moving down


def move(x1, y1, x2, y2, routes):  # pass routes by reference, change value

    """find unique paths from (x1, y1) to (x2, y2)"""

    # print('(' + str(x) + ', ' + str(y) + ')')
    if x1 == x2 or y1 == y2:  # count how many times this is true -> number of unique routes
        routes += 1
        return routes

    if x1 > x2:
        routes = move(x1 - 1, y1, x2, y2, routes)

    if y1 >= y2:
        routes = move(x1, y1 - 1, x2, y2, routes)

    return routes


def travel(x1, y1, x2, y2):
    return move(x1, y1, x2, y2, 0)


def find_paths(grid_side_len):

    return travel(grid_side_len, grid_side_len, 0, 0)


def print_grid(side_length):

    for i in reversed(range(side_length + 1)):
        for j in reversed(range(side_length + 1)):
            print('{0: >5}'.format(str(travel(i, j, 0, 0))), end='')
        print('')


#print(find_paths(4))

side = 5
print_grid(side)

"""This code does not find the answer for grid 20X20.  However, it was discovered that moves required at each location\
mimics Pascal's triangle.  For an n x n grid, number of paths equals n*2 choose n"""