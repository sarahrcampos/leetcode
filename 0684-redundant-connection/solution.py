class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [1] * (n + 1)
    
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for a, b in edges:
            if not uf.union(a,b):
                return [a,b]
        
