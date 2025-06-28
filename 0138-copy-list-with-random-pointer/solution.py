"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#can we have cycles in this linked list?

#                              o
# 7 -> 13 -> 11 -> 10 -> 1 -> null

#dummy
# 0 -> 7 -> 13 -> 11 -> 10 -> 1 -> null
#                             c

#map
#o7: n7
#o13: n13
#o11: n11
#o10: n10
#o1: n1
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        map = {}
        
        original, current = head, dummy
        while original:
            newNode = Node(original.val)
            current.next = newNode
            map[original] = newNode #mapping original to the new node
            original = original.next 
            current = current.next

        current.next = None

        original = head
        while original:
            map[original].random = map[original.random] if original.random else None
            original = original.next
        
        return dummy.next


#                               o                              
# 7 -> 13 -> 11 -> 10 -> 1 -> null

#       dummy
#       0 -> 7 -> 13 -> 11 -> 10 -> 1 -> null
#random     null  n7     n1   n11   n7

#map
#o7: n7
#o13: n13
#o11: n11
#o10: n10
#o1: n1
