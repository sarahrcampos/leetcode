class Solution:
    def reverseBits(self, n: int) -> int:
        power = 0
        res = 0
        cur = n
        while power < 32:
            res += (cur%2) * 2**(31-power)
            power += 1
            cur = cur // 2
        return res
