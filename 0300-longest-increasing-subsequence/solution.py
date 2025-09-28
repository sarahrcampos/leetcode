#nums = [10,9,2,5,3,7,101,5]
#         l             r
#LIS = [-inf, 2, 3, 7, 101]

#DP + Binary Search -> Time: O(nlogn) Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [float("-inf")]

        for num in nums:
            if num > LIS[-1]:
                LIS.append(num)
            else:
                l, r = 0, len(LIS) - 1
                while l < r:
                    m = (l+r)//2
                    if num > LIS[m]:
                        l = m + 1
                    else:
                        r = m
                LIS[r] = num

        return len(LIS) - 1
        
