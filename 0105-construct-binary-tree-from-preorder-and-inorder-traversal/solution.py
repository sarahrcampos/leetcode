# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #inorder = left root right
    #preorder = root left right

#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7]

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None            
        root = TreeNode(preorder[0])
        inOrderIndex = inorder.index(root.val)
        
        root.left = self.buildTree(
            preorder[1 : inOrderIndex + 1],
            inorder[ : inOrderIndex]        
        )

        root.right = self.buildTree(
            preorder[inOrderIndex + 1 : ],
            inorder[inOrderIndex + 1 : ]
        )
        return root

