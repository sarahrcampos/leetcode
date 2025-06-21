class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                distance = abs(xi-xj) + abs(yi - yj)
                graph[i].append((distance,j))
                graph[j].append((distance,i))
        heap = [(0, 0, 0)]
        visited = set()
        total = 0
        while heap:
            distance, source, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            total += distance
            for weight, neighbor in graph[node]:
                heapq.heappush(heap, (weight, node, neighbor))
        return total
