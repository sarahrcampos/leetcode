class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        #minimum time - dijkstra
        #to reach ALL the nodes - maximum from the shortest hashmap
        shortest = {}
        heap = [(0, k)] #k is the start point
        while heap:
            weight, node = heapq.heappop(heap)
            if node in shortest:
                continue
            shortest[node] = weight
            for weight_neighbor, neighbor in graph[node]:
                if neighbor not in shortest:
                    heapq.heappush(heap, (weight + weight_neighbor, neighbor))
        return -1 if len(shortest) != n else max(shortest.values())
