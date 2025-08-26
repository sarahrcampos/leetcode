class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            # se já permutamos todos
            if start == len(nums):
                res.append(nums[:])  # faz cópia da permutação atual
                return

            for i in range(start, len(nums)):
                # troca o elemento atual com o candidato
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # desfaz a troca (backtracking)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res

