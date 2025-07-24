class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += (2**i) * (0 if n & 2**31 == 0 else 1)
            n = n << 1
        return res
