class Solution(object):
    def arrangeCoins(self, n):
        row = 0
        while n >= 0:
            row += 1
            n -= row     
        return row - 1
        
