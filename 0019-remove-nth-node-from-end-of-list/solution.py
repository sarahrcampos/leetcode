# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mapList = {}
        curr = head
        i = 0
        while curr:
            mapList[i] = curr
            curr = curr.next
            i += 1
        
        length = len(mapList)  
        i = length-n      
        if i == 0:
            return head.next
        
        mapList[i-1].next = mapList[i+1] if i+1<length else None

        return head
