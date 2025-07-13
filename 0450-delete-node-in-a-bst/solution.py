# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValue(node):
            while node and node.left:
                node = node.left
            return node.val
        
        def remove(node, key):
            if not node:
                return node
            if key > node.val:
                node.right = remove(node.right, key)
            elif key < node.val:
                node.left = remove(node.left, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                node.val = minValue(node.right)
                node.right = remove(node.right, node.val)

            return node
        
        return remove(root, key)
