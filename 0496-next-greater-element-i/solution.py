class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        #O(n.m)
        for i in range(0, len(nums1)):
            greater, after = -1, False
            for n2 in nums2:
                if(n2 == nums1[i]):
                    after = True
                elif after and n2 > nums1[i]:
                    greater = n2
                    break
            nums1[i] = greater
        return nums1

        
