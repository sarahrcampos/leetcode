"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':        
        if not head:
            return None
        mapNodes = {}
        dummy = Node(0)
        
        newHead = dummy
        curr = head
        while curr:
            newHead.next = Node(curr.val)
            newHead = newHead.next
            mapNodes[curr] = newHead
            curr = curr.next
            
        curr = head
        while curr:
            mapNodes[curr].random = mapNodes[curr.random] if curr.random in mapNodes else None
            curr = curr.next

        return dummy.next
        
