#coins = [1,2,5], amount = 11
#minCoins 0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 1, 6: 2, 7: 2, 8: 3, 9: 3, 10: 2, 11: 3

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        minCoins = [float("inf")] * (amount + 1)
        minCoins[0] = 0
        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0 and num - coin <= amount:
                    minCoins[num] = min(minCoins[num], minCoins[num - coin] + 1)
        #print(minCoins)
        return minCoins[amount] if minCoins[amount] != float("inf") else -1
