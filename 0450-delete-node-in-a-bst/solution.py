# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSuccessor(self, node):
        curr = node.right
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            successor = self.getSuccessor(root)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        
        return root
        



