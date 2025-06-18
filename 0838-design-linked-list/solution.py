class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        if not self.head or index < 0:
            return -1
        current, i = self.head, 0
        while current:
            if i == index:
                break
            i += 1
            current = current.next
        if not current or i != index:
            return -1
        return current.val
        
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.tail:
            self.tail = self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        current, i, previous = self.head, 0, None
        while current:
            if i == index:
                break
            i += 1
            previous = current
            current = current.next
        if i != index:
            return
        newNode = Node(val)
        if not previous:
            self.addAtHead(val)
        elif not current:
            previous.next = newNode
            self.tail = newNode
        else:
            newNode.next = current
            previous.next = newNode



    def deleteAtIndex(self, index: int) -> None:
        if not self.head or index < 0:
            return
        current, i, previous = self.head, 0, None
        while current:
            if i == index:
                break
            i += 1
            previous = current
            current = current.next
        if not current or i != index:
            return
        
        if not previous:
            self.head = self.head.next
        else:
            previous.next = current.next
        
        if not current.next:
            self.tail = previous


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
