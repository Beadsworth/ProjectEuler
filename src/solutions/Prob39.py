import src.EulerHelpers as Euler
import math


def is_solution(triangle_sides):
    a, b, c = sorted(triangle_sides)
    # print(a, b, c)

    if a ** 2 + b ** 2 == c ** 2:
        return True


if __name__ == '__main__':

    solution_counts = {}
    for p in range(3, 1000 + 1):
        print(p)

        solution_count = 0
        for triple in Euler.partition_into_m_parts(p, 3):
            if is_solution(triple):
                solution_count += 1

        solution_counts[p] = solution_count

    max_count = 0
    max_p = 0
    for p, count in solution_counts.items():
        if count > max_count:
            max_count = count
            max_p = p

    print("answer: p={p}, count={count}".format(p=max_p, count=max_count))
