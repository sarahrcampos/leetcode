class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operators = {
            '+': lambda a,b : a+b,
            '-': lambda a,b : a-b,
            '*': lambda a,b : a*b,
            '/': lambda a,b : int(a/b)
        }
        for i in range(len(tokens)-1, -1, -1):
            token = tokens[i]
            if token in operators or (stack and stack[-1] in operators):
                stack.append(token)
                continue
            operandA = int(token)
            while stack and stack[-1] not in operators:
                operandB = int(stack.pop())
                operator = stack.pop()
                operandA = operators[operator](operandA, operandB)
            stack.append(operandA)
            
        return stack[0]


