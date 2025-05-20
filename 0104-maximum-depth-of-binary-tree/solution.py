# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def dfs(node, currentSum):
            if not node:
                return currentSum
            left = dfs(node.left, 1 + currentSum)
            right = dfs(node.right, 1 + currentSum)
            return max(left, right)
        return dfs(root, 0)
            
        
