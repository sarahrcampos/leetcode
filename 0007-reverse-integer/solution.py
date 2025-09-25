class Solution:
    def reverse(self, x: int) -> int:
        limit = 2**33
        mask = 0x100000000
#the easiest way
        strX = str(x)
        reverseX = strX[::-1]
        if x < 0:
            reverseX = "-" + reverseX[0:-1]
        reverseX = int(reverseX)
        return reverseX if  -(1 << 31) <= reverseX <= (1 << 31) - 1 else 0

