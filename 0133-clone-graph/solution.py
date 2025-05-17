"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        visited = {}

        def dfs(current):
            if not current:
                return None
            if current.val in visited:
                return visited[current.val]

            newNode = Node(current.val)
            visited[current.val] = newNode
            for n in current.neighbors:
                newNode.neighbors.append(dfs(n))
            return newNode
        
        return dfs(node)

        
        
