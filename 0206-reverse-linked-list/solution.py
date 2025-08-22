# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #iteratively:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     newHead = None
    #     while head:
    #         temp = head
    #         head = head.next
    #         temp.next = newHead
    #         newHead = temp

    #     return newHead


    #recursively
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.newHead = None
        def reverse(head, prev):          
            if not head:
                return prev
            temp = head.next
            head.next = prev
            return reverse(temp, head)        
        
        return reverse(head, None)
