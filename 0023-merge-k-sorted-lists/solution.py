# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #merge two lists
    def merge(self, list1, list2):
        dummy = ListNode()
        curr = dummy        
        while list1 and list2:            
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1: curr.next = list1
        if list2: curr.next = list2
        return dummy.next

    #merge the lists in pairs
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists) - 1, 2):
                temp.append(self.merge(lists[i], lists[i+1]))
            if len(lists) % 2:
                temp.append(lists[len(lists) - 1])                    
            lists = temp
        return lists[0]
