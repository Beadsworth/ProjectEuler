from EulerHelpers import fib_gen

fib = fib_gen(1000000)

current_term = 0
current_index = -1

while current_term < 10**(1000-1):

    current_index += 1
    current_term = next(fib)

print('Index: ' + str(current_index))
