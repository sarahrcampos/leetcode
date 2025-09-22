#n = 10
#x = -2

#2^3 = 2*2*2
#2^-3 = ((2/2)/2)/2

# -3 = powNegative(-1)/powNegative(-2)
# -1: 2
# -2: 2/2

#2^-4 = ((((2/2)/2)/2)/2)/2

#x = 2, n = -2
# -2 = powNegative(-1)/powNegative(-1)
#-1: 2

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        cache = {}
        def powPositive(n):
            if n in cache:
                return cache[n]
            if n == 0:
                return 1
            if n == 1 or n == -1:
                return x
            half = int(n/2)
            cache[n] = (powPositive(half) * powPositive(n - half))
            return cache[n]
        
        return powPositive(n) if n >= 0 else 1/powPositive(-n)
