class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(cost):
                return 0
            
            one = dfs(i+1) + cost[i]
            two = dfs(i+2) + cost[i]
            cache[i] = min(one, two)
            return cache[i]
        dfs(0)
        return min(cache[0], cache[1])

