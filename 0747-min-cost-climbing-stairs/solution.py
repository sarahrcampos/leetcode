class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first, second = cost[n-2], cost[n-1]
        for i in range(n-3, -1, -1):
            temp = first
            first = cost[i] + min(first, second)
            second = temp
        return min(first, second)
