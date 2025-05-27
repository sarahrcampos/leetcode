class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        minimum, current = len(blocks), 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                current += 1
            if r - l + 1 == k:
                minimum = min(minimum, current)
                current -= 1 if blocks[l] == "W" else 0
                l += 1
        
        return minimum
            
