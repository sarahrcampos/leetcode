class Solution(object):
    def minimumRecolors(self, blocks, k):
        left, right, recolors = 0, 0, 0
        min_recolors = k
        while right < len(blocks):
            if blocks[right] == "W":
                recolors += 1            
            if right - left + 1 == k:
                min_recolors = min(min_recolors, recolors)
                if blocks[left] == "W":
                    recolors -= 1
                left += 1
            
            right += 1
        return min_recolors
            
            
