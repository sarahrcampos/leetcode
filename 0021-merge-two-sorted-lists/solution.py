# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previous = None
        first = list1
        second = list2
        while second:
            if first and second.val > first.val:
                previous = first
                first = first.next
                continue
            if previous:
                previous.next = second
            else:
                list1 = second
            if not first:
                first = second
                break
            elif second.val <= first.val:
                temp = second.next
                second.next = first
                previous = second
                second = temp
                
        return list1
            
            
        
