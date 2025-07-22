# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        while True:
            #print(lists)
            minimum, node, index = float("inf"), None, -1
            for i in range(len(lists)):
                if not lists[i]: 
                    continue
                if lists[i].val < minimum:
                    minimum = lists[i].val
                    node = lists[i]
                    index = i
            if index == -1:
                break
            result.next = node
            result = node
            lists[index] = node.next
        return dummy.next
