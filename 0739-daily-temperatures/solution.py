class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        
        return output

#[73,74,75,71,69,72,76,73]
# i = 7
#stack  [6, 7]
#output [1, 1, 4, 2, 1, 1, 0, 0]
