class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        maximum, current = 0, 0
        left, right = 0, 0
        for i in range(len(grumpy)):
            if not grumpy[i]:
                current += customers[i]        
        while right < len(grumpy):
            if grumpy[right]:
                current += customers[right]
            if right - left == minutes-1:
                maximum = max(maximum, current)
                current -= grumpy[left] * customers[left]
                left += 1
            right += 1        
        return maximum
        
