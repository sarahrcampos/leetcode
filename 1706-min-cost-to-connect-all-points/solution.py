class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(len(points))
        minHeap = []
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                minHeap.append([abs(xi-xj)+abs(yi-yj), i, j])
        heapq.heapify(minHeap)
        res = 0
        while minHeap:
            distance, point1, point2 = heapq.heappop(minHeap)            
            if uf.union(point1, point2):
                res += distance
        
        return res

