# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # reverse the nodes of the list k at a time
    #If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        prev, curr = None, head
        start = None
        last = head

        while last:
            i = 0
            oldStart = start
            start = last = curr
            while i < k and last:
                i += 1
                last = last.next
            if i < k and not last:
                break
            while curr != last:    
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp            

            if not start.next:
                head = prev
            start.next = last  
            if oldStart:
                oldStart.next = prev
            prev = start     

        
        return head
