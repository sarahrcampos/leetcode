# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(float("inf"))
        curr = dummy
        finished = set()
        
        while len(finished) < len(lists):
            smallest = -1
            for i in range(len(lists)):
                if i in finished:
                    continue
                if not lists[i]:
                    finished.add(i)
                    continue
                if smallest == -1 or lists[i].val < lists[smallest].val:
                    smallest = i

            if smallest != -1:
                curr.next = lists[smallest]
                lists[smallest] = lists[smallest].next       
                curr = curr.next

        curr.next = None
        return dummy.next
