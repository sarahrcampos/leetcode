# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #check by levels of the tree (BFS) + two pointers

        queue = deque([root])
        while queue:
            #2 pointers -> check if it's a mirror
            l, r = 0, len(queue)-1
            while l<r:
                if queue[l] and queue[r] and queue[l].val != queue[r].val:
                    return False
                elif not queue[l] and queue[r]:
                    return False
                elif not queue[r] and queue[l]:
                    return False
                l, r = l+1, r-1
            for _ in range(len(queue)): #level
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        
        return True
