#nums tem n objetos
#podem ser red = 0, white = 1 or blue = 2
#ordenar in-place
#objetos da mesma cor sejam adjacentes
#ordem = red, white, blue

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = [0, 0, 0]
        for num in nums:
            bucket[num] += 1
        
        j = 0
        for i in range(3):
            for _ in range(bucket[i]):
                nums[j] = i
                j += 1                
        
