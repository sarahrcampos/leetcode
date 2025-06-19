# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #invert list approach
        maximum = -1
        s, f, n = head, head.next, head.next
        head.next = None
        while f and f.next:
            f = f.next.next
            temp = n.next
            n.next = s
            s = n
            n = temp
        
        while s:
            maximum = max(maximum, s.val + n.val)
            s, n = s.next, n.next
        
        return maximum
        
        
        

        
