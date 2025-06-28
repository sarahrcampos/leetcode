# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        sz, i = 0, 0
        map = {}
        current = head
        while current:
            map[i] = current
            current = current.next
            sz += 1
            i += 1
        if sz - n == 0:
            return head.next
        
        map[sz-n-1].next = map[sz-n].next

        return head
