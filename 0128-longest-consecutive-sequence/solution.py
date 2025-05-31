class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        while nums_set:
            total = 0
            queue = deque()
            queue.append(nums_set.pop())
            while queue:
                current = queue.popleft()
                total += 1
                if current-1 in nums_set:
                    queue.append(current-1)
                    nums_set.remove(current-1)
                if current+1 in nums_set:
                    queue.append(current+1)
                    nums_set.remove(current+1)
            max_length = max(max_length, total)

        return max_length
