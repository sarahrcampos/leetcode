class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        n -= 2
        while n >= 0:
            temp = first
            first += second
            second = temp
            n-=1
        return first
        

            

