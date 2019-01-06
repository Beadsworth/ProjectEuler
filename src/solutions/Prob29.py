import src.EulerHelpers as Euler
import math


if __name__ == '__main__':
    top_a = 100
    top_b = 100

    products = set()
    for a in range(2, top_a + 1):
        for b in range(2, top_b + 1):
            products.add(a ** b)

    print("answer = ", len(products))
