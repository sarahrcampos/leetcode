from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()
        

    def push(self, x):
        self.queue.append(x)
        

    def pop(self):
        if self.empty():
            return None
        for i in range (0, len(self.queue) - 1):
            element = self.queue.popleft()
            self.push(element)
        return self.queue.popleft()
        

    def top(self):
        if self.empty():
            return None
        element = self.pop()
        self.push(element)
        return element

    def empty(self):
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
