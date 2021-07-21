import src.EulerHelpers as Euler
import math
import tqdm
from typing import List


def change(amount: int, coins: List[int]) -> int:
    t_coins = sorted(coins)

    dp = [0 for i in range(0, amount + 1)]
    dp[0] = 1

    for coin in t_coins:
        for amt in range(coin, amount + 1):
            dp[amt] += dp[amt - coin]

    return dp[-1]

if __name__ == '__main__':
    # facts
    my_amount = 200
    my_coins = [1, 2, 5, 10, 20, 50, 100, 200]
    answer = change(amount=my_amount, coins=my_coins)

    print(f'answer: {answer}')
