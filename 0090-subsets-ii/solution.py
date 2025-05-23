# for each i we have two decisions: use i or not
# []           [1]
#[]  [2]    [1] [1,2]
#[] [2] -> oh no we got a duplicate
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort() #O(nlogn)
        result = []
        def backtrack(i, combination):
            if i >= len(nums):
                result.append(combination[::])
                return
            
            #use i
            combination.append(nums[i])
            backtrack(i+1, combination)

            #do not use i
            current = combination.pop()
            #or it's cousins
            while i < len(nums) and nums[i] == current:
                i += 1
            backtrack(i, combination)

        backtrack(0, [])
        return result
        
