# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb: #não preciso verificar se pa e pb são not null, porque se ambos forem null é pq as listas são diferentes
        #tipo, se elas não tiverem interseção, elas vão se encontrar no null (next da folha)
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

# A -> a1 -> a2 -> c1 -> c2 -> c3
# B -> b1 -> b2 -> b3 -> c1 -> c2 -> c3
#no total, são 11 nós
#11 = 5 + 6 = 6 + 5
#portanto, se eu percorrer a1 inteiro (5 nós) e voltar p/ headB e percorrer tudo (6) vou acabar no 11
#e se eu percorrer b inteiro (6 nós) e voltar p/ headA e percorrer tudo (5) vou acabar no 11 tbm
