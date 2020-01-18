import unittest, math, time

from EulerHelpers import is_prime, find_factors, find_prime_factors, find_primes, find_first_n_primes, \
    num_2_list, list_2_num, find_perms, prime_gen, fib_gen, find_nth_fib_term


class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sanity(self):
        pass

    master_prime_list = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
        107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
        227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
        349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
        613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
        751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
        887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,
    ]

    def test_is_prime(self):

        not_prime_list =[
            4, 6, 8, 21, 25, 666, 1000000
        ]

        err_list = [
            -1, 0, 1, 1.999999, -2, -5, 'hello'
        ]

        for number in self.master_prime_list:
            self.assertTrue(is_prime(number))

        for number in not_prime_list:
            self.assertFalse(is_prime(number))

        for number in err_list:
            self.assertRaises(TypeError, is_prime, number)

        mag_prime_list = [
            1000003,
            10000019,
            100000007,
            1000000007,
            10000000019,
            100000000003,
            1000000000039,
            10000000000037,
            100000000000031
        ]

        for num in mag_prime_list:
            start = time.time()
            is_prime(num)
            stop = time.time()
            diff = stop - start
            print(str(num) + ' is_prime() calculated in ', end='')
            print('{:.2e}'.format(diff), end='')
            print(' seconds.')

    def test_find_factors(self):

        for number in range(1,1000):
            factor_list = find_factors(number)

            for factor in factor_list:
                self.assertTrue((number % factor) is 0)

        for prime in self.master_prime_list:
            result = find_factors(prime)
            self.assertTrue(len(result) is 2)

        large_num_list = [
            1000000,
            10000000,
            100000000,
            1000000000,
            10000000000,
            100000000000,
            1000000000000,
            10000000000000,
            100000000000000
        ]

        for num in large_num_list:
            start = time.time()
            find_factors(num)
            stop = time.time()
            diff = stop - start
            print(str(num) + ' find_factors() calculated in ', end='')
            print('{:.2e}'.format(diff), end='')
            print(' seconds.')

    def test_find_prime_factors(self):

        self.assertEqual(find_prime_factors(1000000), [2, 5])
        self.assertEqual(find_prime_factors(13195), [5, 7, 13, 29])

    def test_find_primes(self):

        self.assertEqual(find_primes(997), self.master_prime_list)
        self.assertEqual(find_primes(998), self.master_prime_list)
        self.assertEqual(find_primes(999), self.master_prime_list)
        self.assertEqual(find_primes(1000), self.master_prime_list)

        self.assertNotEqual(find_primes(996), self.master_prime_list)

    def test_find_first_n_primes(self):

        for i in range(50):
            sub_list = self.master_prime_list[:i]
            n_list = find_first_n_primes(i)
            self.assertEqual(sub_list, n_list)

    def test_num_2_list(self):

        good_list = [
            [0, [0]],
            [1, [1]],
            [2, [2]],
            [123, [1, 2, 3]],
            [13579, [1, 3, 5, 7, 9]],
            [9999999999, [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]],
            [-9876543210, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
            [314159265358979323, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3]],
            [10 ** 20, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
            [10101, [1, 0, 1, 0, 1]]
            ]

        for good in good_list:
            self.assertEqual(num_2_list(good[0]), good[1])

        bad_list = [0.1, 99.6, 2/3, 'hello']

        for bad in bad_list:
            self.assertRaises(AssertionError, num_2_list, bad)

    def test_list_2_num(self):

        for i in range(1000):
            self.assertEqual(i, list_2_num(num_2_list(i)))

        self.assertRaises(AssertionError, list_2_num, [])
        self.assertRaises(AssertionError, list_2_num, [0.2, 0.6, 1.3])
        self.assertRaises(AssertionError, list_2_num, ['h', 'e', 'llo'])

        list1 = [1, 2, 3, 4, 5]
        list2 = list(list1)
        list_2_num(list1)
        self.assertEqual(list1, list2)  # make sure list is not altered

    def test_find_perms(self):

        upper = 9
        for i in range(1, upper):

            check_list = list(range(1, i+1))
            input_list = list(range(1, i+1))
            result = find_perms(input_list)

            self.assertEqual(check_list, input_list)  # make sure no changes were made to input list
            self.assertEqual(len(result), math.factorial(i))

    def test_prime_gen(self):

        start = 0
        stop = 10

        for prime in prime_gen(stop):
            print(prime)

        prime_max = max(self.master_prime_list)
        gen_primes = prime_gen(prime_max)

        for prime in self.master_prime_list:
            self.assertEqual(prime, next(gen_primes))

        a = prime_gen(0)
        a_len = len(list(a))
        b = prime_gen(1)
        b_len = len(list(b))
        c = prime_gen(2)
        c_len = len(list(c))

        self.assertTrue(a_len == 0)
        self.assertTrue(b_len == 0)
        self.assertTrue(c_len == 1)

    def test_fib(self):

        fib_seq = [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
            10946,
            17711,
            28657,
            46368,
            75025,
            121393,
            196418,
            317811,
            514229,
            832040,
            1346269,
            2178309,
            3524578,
            5702887,
            9227465,
            14930352,
            24157817,
            39088169,
            63245986,
            102334155,
            165580141,
            267914296,
            433494437,
            701408733,
            1134903170,
            1836311903,
            2971215073,
            4807526976,
            7778742049,
            12586269025,
            20365011074,
            32951280099,
            53316291173,
            86267571272,
            139583862445,
            225851433717,
            365435296162,
            591286729879,
            956722026041,
            1548008755920,
            2504730781961,
            4052739537881,
            6557470319842,
            10610209857723,
            17167680177565,
            27777890035288,
            44945570212853,
            72723460248141,
            117669030460994,
            190392490709135,
            308061521170129,
            498454011879264,
            806515533049393,
            1304969544928657,
            2111485077978050,
            3416454622906707,
            5527939700884757,
            8944394323791464,
            14472334024676221,
            23416728348467685,
            37889062373143906,
            61305790721611591,
            99194853094755497,
            160500643816367088,
            259695496911122585,
            420196140727489673,
            679891637638612258,
            1100087778366101931,
            1779979416004714189,
            2880067194370816120,
            4660046610375530309,
            7540113804746346429,
            12200160415121876738,
            19740274219868223167,
            31940434634990099905,
            51680708854858323072,
            83621143489848422977,
            135301852344706746049,
            218922995834555169026,
        ]

        generated_fib = fib_gen(99)
        for number in fib_seq:
            self.assertEqual(number, next(generated_fib))

        for index, number in enumerate(fib_seq):
            self.assertEqual(number, find_nth_fib_term(index))


if __name__ == '__main__':
    unittest.main()
