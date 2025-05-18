#using trie
#Time O(n*w)
class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Solution(object):
    def removeSubfolders(self, folder):
        res = []
        root = Node()

        for f in folder:
            current = root
            for c in f.split("/")[1:]:                
                if current.endOfWord:
                    break
                if c not in current.children:
                    current.children[c] = Node()
                current = current.children[c]
            current.endOfWord = True
        
        def dfs(current, path):
            if current.endOfWord:
                res.append(path)
                return
            for key, child in current.children.items():
                dfs(child, path + "/" + key)
        
        dfs(root, "")
        return res
        




        
        
