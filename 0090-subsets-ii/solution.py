class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            #usar i
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            #não usar i nem seus irmãos gêmeos
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1 , curr)
        
        backtrack(0,[])
        return res
