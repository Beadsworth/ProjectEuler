import src.EulerHelpers as Euler
import tqdm


class PalCheck:

    def __init__(self, number: int):
        self.number = number

    @property
    def binary_str(self):
        """the binary string representation of the number"""
        return f'{self.number:b}'

    @property
    def is_palindrome(self):
        """is the original number a palindrome?"""
        return Euler.is_palindrome(self.number)

    @property
    def is_binary_palindrome(self) -> bool:
        """is the binary representation a palindrome?"""
        int_convert = int(self.binary_str)
        bin_is_palindrome = Euler.is_palindrome(int_convert)
        return bin_is_palindrome

    @property
    def is_dual_palindrome(self):
        """does the number satisfy both palindrome conditions?"""
        return self.is_palindrome and self.is_binary_palindrome


if __name__ == '__main__':

    dual_pal_list = []
    # all numbers less than one-million
    # only odd numbers can be binary palindromes
    for number in tqdm.tqdm(range(1, 1_000_000, 2)):
        checker = PalCheck(number)
        if checker.is_dual_palindrome:
            dual_pal_list.append(checker.number)

    result = sum(dual_pal_list)
    print(f'result: {result}')
