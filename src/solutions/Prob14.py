from EulerHelpers import collatz_gen

upper_limit = 1000000
max_length = 0
max_start = 0

for i in range(1, upper_limit + 1):

    # if even and under half of upper limit, skip (i * 2 will have a length at of at least one more term)
    if i % 2 == 0 and i <= upper_limit // 2:
        continue

    seq = collatz_gen(i)
    seq_len = sum(1 for x in seq)

    if seq_len > max_length:
        max_length = seq_len
        max_start = i

print('Consider all starting numbers under ' + str(upper_limit) + '...')
print('The longest Collatz sequence starts on ' + str(max_start) + ' and has length of ' + str(max_length))

