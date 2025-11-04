# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def transform(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            sibling = node.right if node.left else None
            node.right = node.left if node.left else node.right
            node.left = None
            lastNode = transform(node.right)
            lastNode.right = sibling
            if sibling:
                lastNode = transform(sibling)
            return lastNode
        transform(root)
            
            
