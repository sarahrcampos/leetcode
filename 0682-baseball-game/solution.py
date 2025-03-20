class Solution(object):
    def calPoints(self, operations):
        stack = []
        sum = 0

        for operation in operations:
            if operation == "C":
                sum -= stack.pop()
                continue
            if operation == "+":
                stack.append(stack[-1] + stack[-2])                                
            elif operation == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))
            sum  += stack[-1]
        return sum

            
        
