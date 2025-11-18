#memoization
#de quantas formas A PARTIR DA SOMA ATUAL eu consigo formar o 4
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [0] * (target+1) #-> [0,0,0,0,0]
        cache[-1] = 1
        nums.sort()

        for i in range(target-1, -1, -1):
            for num in nums:
                if i + num > target:
                    break
                cache[i] += cache[i + num]
        return cache[0]
                


        # #memoization:
        # def combine(currSum):
        #     if currSum in cache:
        #         return cache[currSum]
        #     if currSum == target:
        #         return 1
        #     if currSum > target:
        #         return 0
            
        #     count = 0
        #     for num in nums:
        #         count += combine(currSum + num)
            
        #     cache[currSum] = count
        #     return count
        
        # return combine(0)
