class Solution(object):
    def minEatingSpeed(self, piles, h):
        MAX = max(piles)
        left, right = 1, MAX
        k = MAX
        while left <= right:
            s = 0
            middle = (left+right)//2
            for bananas in piles:
                s = s + bananas//middle
                if bananas%middle != 0:
                    s = s + 1
            print("for: ", middle, middle, s)
            if s > h:
                left = middle + 1
            else:
                if middle < k: k = middle
                right = middle - 1
            print("while: ",left, right, k)                
        return k
        
