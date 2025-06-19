# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s1, s2, f = head, head.next, head.next
        head.next = None
        while f and f.next:
            f = f.next.next
            temp = s2.next
            s2.next = s1
            s1 = s2
            s2 = temp
        #if not f -> odd -> end with s1 =>  s2 -> s1
        #if f -> even -> end with s2 => s1 -> s2
        if not s2:
            return head
        t1, t2 = s1.next, s2.next
        if not f:
            s2.next, s1.next = s1, None
            s1 = t1
            t1 = s1.next
        else:
            s2.next = None
        
        while s1:
            s1.next = s2
            s2 = t2
            if t2:
                temp = t2.next
                t2.next = s1
                t2 = temp
            s1 = t1
            if t1:
                t1 = t1.next
            
        
        return head
