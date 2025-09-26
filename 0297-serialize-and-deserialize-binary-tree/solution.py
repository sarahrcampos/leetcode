# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
#using preorder!
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "#"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        return preorder(root)
    # 12##34##5##

    def deserialize(self, data):
        tree = data.split(",")
        root = TreeNode(0)
        i = 0
        def preorder(curr):
            nonlocal i
            if i >= len(tree) or tree[i] == "#":
                return None
            curr.val = tree[i]
            i += 1
            curr.left = preorder(TreeNode(0))            
            i += 1
            curr.right = preorder(TreeNode(0))
            return curr
        return preorder(root)
#         i
# 12##34##5##
#                   1
#         2                     3
#    None    None       4               5
#                   None    None    None    None

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
