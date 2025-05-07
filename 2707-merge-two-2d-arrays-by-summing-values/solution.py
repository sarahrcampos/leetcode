class Solution(object):
    #Time: O(n)
    #Space: O(n)
    def mergeArrays(self, nums1, nums2):
        p1, p2 = 0, 0
        SIZE_1, SIZE_2 = len(nums1), len(nums2)
        result = []
        while p1 < SIZE_1 and p2 < SIZE_2:
            if nums1[p1][0] == nums2[p2][0]:
                result.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1, p2 = p1 + 1, p2 + 1
            elif nums1[p1][0] < nums2[p2][0]:
                result.append([nums1[p1][0], nums1[p1][1]])
                p1 += 1
            else:
                result.append([nums2[p2][0], nums2[p2][1]])
                p2 += 1
        while p1 < SIZE_1:
            result.append([nums1[p1][0], nums1[p1][1]])
            p1 += 1
        while p2 < SIZE_2:
            result.append([nums2[p2][0], nums2[p2][1]])
            p2 += 1
        return result
        
