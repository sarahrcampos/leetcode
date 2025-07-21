class Node:
    def __init__(self, key, val=-1, next=None, prev=None):
        self.key = key
        self.value = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = None

    def remove(self, node):
        next = node.next
        if node.prev: node.prev.next = node.next
        if node.next: node.next.prev = node.prev
        if node == self.head:
            self.head = next
            
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if node != self.tail:
            self.remove(node)
            self.append(node)
            
        return node.value
    
    def append(self, node):
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def put(self, key: int, value: int) -> None:
        newNode = Node(key) if key not in self.cache else self.cache[key]
        newNode.value = value
        if not self.head:
            self.head = self.tail = newNode
        elif newNode != self.tail: #Otherwise, add the key-value pair to the cache
            if key in self.cache: #Update the value of the key if the key exists
                self.remove(newNode)
            self.append(newNode)
        self.cache[key] = newNode

        #If the number of keys exceeds the capacity from this operation, evict the least recently used key
        if len(self.cache) > self.capacity:
            newHead = self.head.next if self.head.next else newNode
            newHead.prev = None
            del self.cache[self.head.key]
            self.head = newHead
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
