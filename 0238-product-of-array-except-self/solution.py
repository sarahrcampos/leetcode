class Solution:
    #Space: O(1)
    #Time: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        #prefix
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        #suffix
        nums.append(nums[n-1])
        for i in range(n-1, 0, -1):
            nums[i] = nums[i-1] * nums[i+1]
       
        #result
        for i in range(n-2, -1, -1):
            res[i] = res[i] * nums[i+2]

        return res
        




#1 - brute force - O(n²)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(nums)):
    #         product = 1
    #         for j in range(len(nums)):
    #             if i == j: continue
    #             product *= nums[j]
    #         res.append(product)
        
    #     return res

#2 - prefix and suffix arrays
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix, suffix = [1]*len(nums), [1]*len(nums)
    #     for i in range(1,len(nums)):
    #         prefix[i] = prefix[i-1] * nums[i-1]
    #     for i in range(len(nums)-2, -1,-1):
    #         suffix[i] = nums[i+1] * suffix[i+1]
    #     #nums = [1,2,3,4]
    #     #prefix = [1, 1, 2, 6]
    #     #suffix = [24, 12, 4, 1]

    #     res = []
    #     for i in range(len(nums)):
    #         res.append(prefix[i] * suffix[i])
    #     return res
