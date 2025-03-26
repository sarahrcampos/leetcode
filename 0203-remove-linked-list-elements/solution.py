# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        previous = None
        current = head
        while current:
            if current.val != val:
                previous = current
            elif not previous:
                head = current.next
            else:
                previous.next = current.next
            current = current.next
        return head
        
