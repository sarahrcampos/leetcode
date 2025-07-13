# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def createArray(node):
            if not node:
                return
            createArray(node.left)
            res.append(node.val)
            createArray(node.right)
        
        createArray(root)
        return res[k-1]
