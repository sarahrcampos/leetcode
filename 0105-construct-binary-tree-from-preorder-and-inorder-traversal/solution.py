# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder: root - left - right
        #inorder: left - root - right
        root = TreeNode(preorder[0])
        map = {n:i for i,n in enumerate(inorder)}

        def dfs(current, newNode):
            if not current:
                return TreeNode(newNode)
            if map[newNode] < map[current.val]:
                current.left = dfs(current.left, newNode)
            else:
                current.right = dfs(current.right, newNode)
            return current
        for i in range(1, len(preorder)):
            node = preorder[i]
            dfs(root, node)
        
        return root


            
