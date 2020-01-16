import src.EulerHelpers as Euler
import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def diff_vector(m, n):
        """vector that points from m to n"""
        m_x, m_y = m
        n_x, n_y = n

        return n_x - m_x, n_y - m_y

    def distance(self, m, n):
        """return distance between m and n"""
        x, y = self.diff_vector(m, n)
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def tri_side_lengths(self, a, b, c):
        return {
            'ab': self.distance(a, b),
            'bc': self.distance(b, c),
            'ca': self.distance(c, a)
        }

    @property
    def side_lengths(self):
        return self.side_lengths(self.a, self.b, self.c)

    def tri_area(self, a, b, c):
        tri_lengths = self.tri_side_lengths(a, b, c)
        l, m, n = tri_lengths['ab'], tri_lengths['bc'], tri_lengths['ca']
        # calculate the semi-perimeter
        s = (l + m + n) / 2
        # calculate the area
        area = (s * (s - l) * (s - m) * (s - n)) ** 0.5
        return area

    @property
    def area(self):
        return self.tri_area(self.a, self.b, self.c)

    def diff_areas(self, p):
        triangles = (p, a, b), (p, b, c), (p, c, a)
        areas = (self.tri_area(*triangle) for triangle in triangles)
        return sum(areas)

    def point_is_within(self, p):
        """Compare areas to see if p is within.  Use rounding to be sure."""
        t_area = self.area
        p_area = self.diff_areas(p)
        # print('t_area: {}, p_area: {}'.format(t_area, p_area))
        print(p_area - t_area)
        return round(p_area, 3) <= round(t_area, 3)


if __name__ == '__main__':

    triangles_path = r'src/misc/p102_triangles.txt'
    p = (0, 0)

    count = 0
    with open(Euler.get_path(triangles_path)) as file:
        for line in file:
            nums = [int(x.strip()) for x in line.split(',')]
            a, b, c = tuple(nums[0:2]), tuple(nums[2:4]), tuple(nums[4:])
            tri = Triangle(a, b, c)
            if tri.point_is_within(p):
                count += 1
    print('Number of triangles that contain the origin: {}/1000'.format(count))
