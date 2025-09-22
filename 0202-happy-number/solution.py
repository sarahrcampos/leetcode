class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            count = 0
            while n > 0:                
                count += (n%10)**2
                n = n//10
            n = count            
        return True

