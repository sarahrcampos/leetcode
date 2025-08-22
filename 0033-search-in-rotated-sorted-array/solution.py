class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2

            if nums[m] > target:
                if nums[m] <= nums[r]: #m está no right
                    r = m - 1
                else: #m está no left
                    if nums[l] <= target:
                        r = m - 1
                    else:
                        l = m + 1
            elif nums[m] < target:
                if nums[m] <= nums[r]: #m está no right
                    if nums[r] >= target:
                        l = m + 1
                    else:
                        r = m - 1
                else: #m está no left
                    l = m + 1
            else:
                return m

            

        return -1
