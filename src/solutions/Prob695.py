import src.EulerHelpers as Euler
import math
import random
import tqdm
import datetime


class Point:

    @staticmethod
    def unit_square_point():
        x, y = random.random(), random.random()
        return x, y

    def __init__(self, name):
        self.name = name
        self.x, self.y = self.unit_square_point()


class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return 'Rectangle {}-{}'.format(self.p1.name, self.p2.name)

    @property
    def area(self):
        w = abs(self.p1.x - self.p2.x)
        h = abs(self.p1.y - self.p2.y)
        return w * h


class Scenario:

    def __init__(self):
        self.points = {}
        for letter in ('a', 'b', 'c'):
            self.points[letter] = Point(name=letter)

        self.rectangles = {
            'ab': Rectangle(self.points['a'], self.points['b']),
            'bc': Rectangle(self.points['b'], self.points['c']),
            'ca': Rectangle(self.points['c'], self.points['a'])
        }

    @property
    def middle_rectangle(self):
        rectangles = [rect for rect in self.rectangles.values()]
        middle_rect = sorted(rectangles, key=lambda r: r.area)[1]
        return middle_rect

    @property
    def middle_rectangle_area(self):
        return self.middle_rectangle.area


if __name__ == '__main__':
    print("start time: {}".format(datetime.datetime.now().strftime('%H:%M:%S')))
    # progress = []
    sum_of_outcomes = 0

    for i in range(1, 10**10 + 1):
        sum_of_outcomes += Scenario().middle_rectangle_area
        mean = 1.0 * sum_of_outcomes / i

        if i % 10**6 == 0:
            # progress.append((i, mean))
            print('{:0.10f}'.format(round(mean, 10)))
