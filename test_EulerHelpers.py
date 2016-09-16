import unittest, math

from EulerHelpers import is_prime, find_factors, find_prime_factors, find_primes, find_first_n_primes, \
    num_2_list, list_2_num, find_perms


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

    def test_find_factors(self):

        for number in range(1,1000):
            factor_list = find_factors(number)

            for factor in factor_list:
                self.assertTrue((number % factor) is 0)

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
            self.assertRaises(TypeError, num_2_list, bad)

    def test_list_2_num(self):

        for i in range(1000):
            self.assertEqual(i, list_2_num(num_2_list(i)))

        self.assertRaises(TypeError, list_2_num, [])
        self.assertRaises(TypeError, list_2_num, [0.2, 0.6, 1.3])
        self.assertRaises(TypeError, list_2_num, ['h', 'e', 'llo'])

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


if __name__ == '__main__':
    unittest.main()
