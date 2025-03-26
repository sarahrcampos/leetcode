# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        if length < 2:
            return True
        previous, middle = head, head.next
        head.next = None
        for i in range(1, length//2):
            temp = middle
            middle = middle.next
            temp.next = previous
            previous = temp
        p1 = previous
        p2 = middle if length % 2 == 0 else middle.next
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        if p1 == None and p2 == None:
            return True
        return False
            

        
