# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, leftLimit, rightLimit):
            if not node:
                return True
            if node.val <= leftLimit or node.val >= rightLimit:
                return False
            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.right.val <= node.val:
                return False
            
            return (validate(node.left, leftLimit, node.val) and
                    validate(node.right, node.val, rightLimit))
        
        return validate(root, float("-inf"), float("inf"))
            
