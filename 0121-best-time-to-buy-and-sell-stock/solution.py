class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy, sell = sell, sell + 1
            else:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
        return profit
        
