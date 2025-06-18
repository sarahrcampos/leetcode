# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #hashmap approach
        map = {}
        fast, slow, i, j = head, head, 0, 0
        maximum = -1
        while fast:
            map[i] = slow.val
            fast = fast.next.next
            slow = slow.next
            i += 1
            j += 2
        while slow:
            maximum = max(maximum, slow.val + map[j-1-i])
            slow = slow.next
            i += 1
        return maximum
        

        
