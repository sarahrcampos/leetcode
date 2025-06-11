# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                    return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        queue = deque()
        queue.append(root)
        while queue:
            current = queue.popleft()
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
            if current.val == subRoot.val and isSameTree(current, subRoot):
                return True
        return False

