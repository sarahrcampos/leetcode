# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow, fast = slow.next, fast.next.next
        if not prev:
            return head
        prev.next = None
        r, slow.next = slow.next, None
        while r:
            temp, r = r, r.next
            temp.next = slow
            slow = temp

        l, r = head, slow
        while l and r:
            tempL, tempR = l, r
            l, r = l.next, r.next
            tempL.next = tempR
            tempR.next = l if l else r
        
        return head
        
            
        
