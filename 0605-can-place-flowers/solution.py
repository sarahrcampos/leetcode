class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        aux = [0] + flowerbed + [0]
        for i in range (1, len(aux)-1):
            if (aux[i] == 0 and
                aux[i-1] == 0 and
                aux[i+1] == 0):
                aux[i] = 1
                count += 1
        print(count)
        return count >= n
        
