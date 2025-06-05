class Solution:
    #Time: O(n²)
    #Space: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for i in range(len(nums)):
            if count[nums[i]] == 0:
                continue
            count[nums[i]] -= 1
            localCount = count.copy()
            for j in range(len(nums)):
                if i == j or localCount[nums[j]] <= 0:
                    continue
                localCount[nums[j]] -= 1
                target = -(nums[i] + nums[j])
                if target in localCount and localCount[target] > 0:
                    localCount[target] = 0
                    res.append([nums[i], nums[j], target])
            count[nums[i]] = 0
        return res


