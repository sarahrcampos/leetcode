class Solution(object):
    #O(n)
    def numOfSubarrays(self, arr, k, threshold):
        TARGET = threshold * k
        total, count = 0, 0
        left, right = 0,0

        while right < len(arr):
            total += arr[right]
            if right - left == k-1:
                if total >= TARGET:
                    count += 1
                total -= arr[left]
                left += 1
            right += 1

        return count
        
