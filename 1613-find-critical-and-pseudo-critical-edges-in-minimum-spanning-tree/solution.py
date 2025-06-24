class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        temp = []
        for i in range(len(edges)):
            a, b, w = edges[i]
            temp.append((w, a, b, i))
        edges = temp
        edges.sort()

        uf = UnionFind(n)
        total = 0
        for w, a, b, i in edges:
            if uf.union(a, b):
                total += w
        
        critical, pseudocritical = [], []
        for i in range(len(edges)):
            uf = UnionFind(n)
            current = 0
            for j in range(len(edges)):
                if i != j:
                    if uf.union(edges[j][1], edges[j][2]):
                        current += edges[j][0]
            if current > total or max(uf.rank) < n:
                critical.append(edges[i][3])
                continue
            current = edges[i][0]
            uf = UnionFind(n)
            uf.union(edges[i][1], edges[i][2])
            for j in range(len(edges)):
                if uf.union(edges[j][1], edges[j][2]):
                    current += edges[j][0]
            if current == total:
                pseudocritical.append(edges[i][3])
        
        return [critical, pseudocritical]
                    

            
                

        

