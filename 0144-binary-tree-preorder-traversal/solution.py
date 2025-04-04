# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root
        while True:
            if not current and not stack:
                break
            if not current and stack:
                current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            current = current.left
        return result
