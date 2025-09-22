#9,9,9
#1,0,0,0
#carry = 1

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        carry = (digits[-1] + 1)//10
        digits[-1] = (digits[-1] + 1) % 10        
        for i in range(len(digits) - 2, -1, -1):
            temp = carry
            carry = (digits[i] + carry) // 10
            digits[i] = (digits[i] + temp) % 10            
        if carry:
            digits = [carry] + digits
        return digits
