# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def dfs(node):
            if not node or (not node.left and not node.right):
                return node
            temp = dfs(node.right)
            node.right = dfs(node.left)
            node.left = temp
            return node
        dfs(root)
        return root
        
