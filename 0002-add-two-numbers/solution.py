# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        result = dummy
        while l1 or l2:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = total // 10
            node = ListNode(total%10)
            result.next = node
            result = node
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            result.next = ListNode(carry)
        return dummy.next

        
