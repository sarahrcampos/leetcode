# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        dummy = ListNode()
        while current:
            if current.next == dummy:
                return True
            temp = current.next
            current.next = dummy
            current = temp            
        return False
        
