# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        newNodes = [None] * n
        for i, node in enumerate(nodes):
            newNodes[(i+k)%n] = node
        for i in range(1, n):
            newNodes[i-1].next = newNodes[i]
        newNodes[-1].next = None
        return newNodes[0]        
