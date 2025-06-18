class Node:
    def __init__(self, val, next = None, previous = None):
        self.val = val
        self.next = next
        self.previous = previous

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.tail = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.previous = self.current
        self.current.next = newNode
        self.tail = self.current = newNode

    def back(self, steps: int) -> str:
        i = 0
        while self.current != self.head:
            if i == steps:
                break
            self.current = self.current.previous
            i += 1
        return self.current.val
        

    def forward(self, steps: int) -> str:
        i = 0
        while self.current != self.tail:
            if i == steps:
                break
            self.current = self.current.next
            i += 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
