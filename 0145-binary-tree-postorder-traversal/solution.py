# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        processed = set()
        stack = [root]
        res = []
        while stack:
            if not root:
                break
            root = stack.pop()
            if root in processed:
                res.append(root.val)
                continue
            
            stack.append(root)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            processed.add(root)

        return res
            
            

