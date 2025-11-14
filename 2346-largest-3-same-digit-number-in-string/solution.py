#num -> inteiro grande
#good = tem tamanho 3 e só tem 1 dígito
#sliding window?
#retornar o MAIOR good number
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = 0
        strLargest = ""
        l = 0
        for r in range(len(num)):
            while l < r and num[r] != num[l]:
                l += 1
            
            if (r - l + 1) == 3:
                number = int(num[l:r+1])
                if number >= largest:
                    largest = number
                    strLargest = num[l:r+1]
                l += 1
        
        return strLargest
