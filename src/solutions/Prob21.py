from EulerHelpers import find_factors


def d(n):

    factors = find_factors(n)
    factors = factors[:len(factors) - 1]
    return sum(factors)


def find_amicable(stop):

    ama_list = []

    print('Completion: 0%', end='')
    for i in range(1, stop):
        print('.', end='', flush=True)
        if i % 100 == 0:
            print('')
            print('Completion: ', end='')
            print("{0:.0f}%".format(i / stop * 100), end='')
        for j in range(i + 1, stop):
            d1 = d(i)
            d2 = d(j)
            if (d1 == j) and (d2 == i):
                ama_list.append(d1)
                ama_list.append(d2)

    return ama_list

answer = find_amicable(10000)
print(answer)
print('Answer: ' +str(sum(answer)))