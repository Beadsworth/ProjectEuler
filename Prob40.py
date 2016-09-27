from EulerHelpers import num_2_list

upper_limit = 200000  # found empirically
irrational = []

for i in range(1, upper_limit + 1):
    temp = num_2_list(i)
    irrational.extend(temp)


def d(n):

    return irrational[n-1]

# print(len(irrational))
print('Answer: ' + str(d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)))
