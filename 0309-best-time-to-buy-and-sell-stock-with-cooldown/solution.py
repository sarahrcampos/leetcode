class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(action, i, curr):
            if i >= len(prices):
                return 0

            if (action, i, curr) not in memo:
                buy = dfs("buy", i+1, prices[i]) if action != "buy" else 0
                sell = (prices[i] - curr + dfs("cooldown",i+2, 0)) if action == "buy" else 0
                skip = dfs(action, i+1, curr)
                memo[(action, i, curr)] = max(buy, sell, skip)

            return memo[(action, i, curr)]
        
        return dfs("cooldown",0,0)

            
