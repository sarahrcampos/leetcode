# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def traverse(root, array):
            if not root:
                return
            traverse(root.left, array)
            traverse(root.right, array)
            array.append(root.val)
        traverse(root, result)
        return result


            



