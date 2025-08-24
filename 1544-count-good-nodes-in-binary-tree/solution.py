# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maximum):
            if not node:
                return 0
            count = 1 if maximum <= node.val else 0
            return count + dfs(node.left, max(maximum, node.val)) + dfs(node.right, max(maximum, node.val))
        
        return dfs(root, root.val)
