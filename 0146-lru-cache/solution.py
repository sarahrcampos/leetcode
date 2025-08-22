class Node:
    def __init__(self, val=0, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.tail = None
        self.mapList = {}

    def get(self, key: int) -> int:
        if key not in self.mapList:
            return -1
        
        node = self.mapList[key]
        if node == self.tail:
            return node.val
        
        self.moveNodeToTail(node)

        return node.val
    

    def moveNodeToTail(self, node):
        if node == self.tail:
            return
        if node == self.head:
            self.head = self.head.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = None
        node.prev = self.tail   
        if self.tail:     
            self.tail.next = node
        self.tail = node


    def put(self, key: int, value: int) -> None:
        node = self.mapList[key] if key in self.mapList else Node(key=key)
        node.val = value
        self.mapList[key] = node

        self.moveNodeToTail(node)
        if not self.head:
            self.head = node  

        if len(self.mapList) > self.capacity: #evict the least recently used key
            del self.mapList[self.head.key]
            self.head = self.head.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
