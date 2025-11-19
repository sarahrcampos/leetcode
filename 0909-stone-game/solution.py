#apenas duas opções: do começo ou do fim

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if l == r:
                return piles[l]
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            
            start = dfs(l + 1, r)
            end = dfs(l, r - 1)

            cache[(l,r)] = max(piles[l] - start, piles[r] - end)
            return cache[(l,r)]
        
        return dfs(0, len(piles) - 1) > 0
