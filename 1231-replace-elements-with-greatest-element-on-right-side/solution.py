class Solution(object):
    def replaceElements(self, arr):
        SIZE = len(arr)
        res = [-1] * SIZE
        for i in range(SIZE-2, -1, -1):
            res[i] = arr[i+1] if arr[i+1] >= res[i+1] else res[i+1]
        return res
        
