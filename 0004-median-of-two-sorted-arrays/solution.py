class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1) - 1
        length = len(nums1) + len(nums2)
        half = length // 2
        while True:
            m1 = (l+r)//2
            m2 = half - m1 - 2

            left1 = nums1[m1] if m1 >= 0 else float("-inf")
            left2 = nums2[m2] if m2 >= 0 else float("-inf")
            right1 = nums1[m1 + 1] if m1+1 < len(nums1) else float("inf")
            right2 = nums2[m2 + 1] if m2+1 < len(nums2) else float("inf")

            if left1 <= right2 and left2 <= right1:
                if length % 2:
                    return min(right1, right2)
                else:
                    return (min(right1, right2) + max(left1, left2))/2
            elif left1 > right2:
                r = m1 - 1
            elif left2 > right1:
                l = m1 + 1
                
        
