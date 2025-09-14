class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, amount):
            if amount == 0:
                return 1
            if i >= len(coins) or amount < 0:
                return 0

            if (i, amount) not in cache:
                cache[(i,amount)] = dfs(i, amount - coins[i]) + dfs(i+1, amount)
            return cache[(i, amount)]
        
        return dfs(0, amount)
            

