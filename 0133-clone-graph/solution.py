"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapOld2New = {}
        def dfs(old):
            if not old:
                return None
            if old in mapOld2New:
                return mapOld2New[old]
            mapOld2New[old] = Node(old.val)
            for neighbor in old.neighbors:
                mapOld2New[old].neighbors.append(dfs(neighbor))          
            return mapOld2New[old]


        return dfs(node)
