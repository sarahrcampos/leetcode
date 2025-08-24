# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root
        def dfs(node, curr):
            nonlocal res           
           # print(node, curr)
            if not node:
                return curr            
            i = 1 + dfs(node.left, curr)
            #print(i, k)
            if i == k:
                res = node
                return i            
            return dfs(node.right, i)
            
        dfs(root, 0)
        return res.val
