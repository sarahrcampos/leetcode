# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        map = {}
        a = headA
        while a:
            map[a] = True
            a = a.next
        b = headB
        while b:
            if b in map:
                return b
            b = b.next
        return None
        
