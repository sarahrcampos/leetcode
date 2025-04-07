class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        SIZE = len(nums)
        left, right = 0, 0
        window = set()
        while right <= min(k, SIZE-1):
            if nums[right] in window:
                return True
            window.add(nums[right])
            right += 1
        print(window)
        while right < SIZE:
            window.remove(nums[left])
            if nums[right] in window:
                return True
            window.add(nums[right])
            left, right = left + 1, right + 1
        return False
        
        
        
        
