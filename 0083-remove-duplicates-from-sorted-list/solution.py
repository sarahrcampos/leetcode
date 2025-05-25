# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        while current:
            next = current.next
            while next and next.val == current.val:
                next = next.next
            current.next = next
            current = current.next
        return head
# 1 -> 1 -> 2
#current = 1 [0]
#next = 1 [1]
#next = 2
#current.next = 2

