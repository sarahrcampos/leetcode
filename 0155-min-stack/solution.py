"""
Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

Example
-2, 0, -3
getMin = -3
-2,0
top = 0
getMin = -2

"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.stack.append([val, self.min])
        self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stack:
            return None
        popped = self.stack.pop()
        self.min = popped[1]
        return popped[0]

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
