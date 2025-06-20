#undirected graph
#edges = list [a,b]
#succProb = weights of the edges => cannot be negative
#acyclic (besides <->)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            graph[a].append((-succProb[i], b)) 
            graph[b].append((-succProb[i], a))
        
        heap = [(-1, start_node)]
        visited = set()
        while heap:
            weight, node = heapq.heappop(heap)
            if node == end_node:
                return -weight
            visited.add(node)
            for weight2, node2 in graph[node]:
                if node2 not in visited:
                    heapq.heappush(heap, (-1 * (weight * weight2), node2)) #lets add them negative to use dijkstra

        
        return 0
