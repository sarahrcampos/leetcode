# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        resultList = ListNode()
        resultList.val = -101
        p = resultList
        while head:
            temp = head.next
            if head.val != p.val:
                head.next = None
                p.next = head                
                p = p.next
            head = temp
        return resultList.next
        
