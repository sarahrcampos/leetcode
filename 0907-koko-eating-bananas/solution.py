class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)                
        minimum = right
        while left <= right:
            middle = (right+left)//2
            hours = 0
            for pile in piles:
                hours += (pile // middle) + (1 if pile % middle else 0)
            if hours <= h:
                right = middle - 1
                minimum = min(minimum, middle)
            else:
                left = middle + 1            

        return minimum





#k = bananas/hora
#if piles[i] < k -> piles[i] = 0
#return k so she can eat all the bananas within h hours

#piles = [3,6,7,11], h = 8
#pra comer 1 pilha por hora -> 11 -> sobra 4 horas
#
