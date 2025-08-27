class Solution:
    #monotonic decreasing queue
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        l = 0
        for r in range(len(nums)):
            while queue and nums[r] > queue[-1]:
                queue.pop()    
            queue.append(nums[r])
            if r - l + 1 == k:
                res.append(queue[0])
                if queue[0] == nums[l]:
                    queue.popleft()
                l += 1           
        
        return res

