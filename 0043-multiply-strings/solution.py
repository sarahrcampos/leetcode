#123
#456x
#------
#  738
# 6150
#49200
#-----
#56088


#123
#x4
#----
#492

#multiplica, vai um, multiplica, soma o vai um, (...)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        count = 0
        if num1 < num2:
            num1, num2 = num2, num1
        pow = 0
        for i in range(len(num2)-1,-1,-1): #multiplicar cada dígito de num2 por cada um dos dígitos de num1
            carry = 0
            res = deque()            
            for j in range(len(num1)-1, -1, -1):
                multiply = int(num1[j]) * int(num2[i]) + carry
                res.appendleft(str(multiply % 10))
                carry = multiply // 10
            if carry: res.appendleft(str(carry))
            #print(int("".join(res))*(10**pow))
            count = count + int("".join(res))*(10**pow)
            pow += 1
        return str(count)


