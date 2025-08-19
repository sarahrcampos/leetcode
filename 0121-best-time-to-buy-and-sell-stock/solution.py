class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            maximum = max(maximum, prices[right] - prices[left])
        return maximum
