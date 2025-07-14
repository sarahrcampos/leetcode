# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = []
        while head:
            binary.append(head.val)
            head = head.next
        
        result = 0
        n = len(binary)
        for i in range(n-1, -1, -1):
            result += binary[i] * 2**(n-1-i)
        return result

